import os
import json
import re
from glob import glob
from docx import Document

# Carpeta donde están tus .docx
INPUT_DIR = './tests'
# Carpeta donde volcar los .json
OUTPUT_DIR = './tests_json'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def parse_test(path):
    doc = Document(path)
    preguntas = []
    actual = None

    for p in doc.paragraphs:
        t = p.text.strip()
        if not t:
            continue
        # nueva pregunta: termina en ?
        if re.match(r'.+\?$', t) and not re.match(r'^[ABCD][\.\)\-]', t):
            if actual:
                preguntas.append(actual)
            actual = {'question': t, 'options': {}, 'answer': None}
        # opción A.-D.
        elif actual and re.match(r'^[ABCD][\.\)\-]\s+', t):
            clave = t[0]
            texto = re.sub(r'^[ABCD][\.\)\-]\s+', '', t)
            actual['options'][clave] = texto
        # respuesta inline
        elif actual and re.match(r'(?i)^respuesta[:]? \s*[ABCD]', t):
            m = re.search(r'([ABCD])', t.upper())
            if m:
                actual['answer'] = m.group(1)
    if actual:
        preguntas.append(actual)
    return preguntas

def convert_all():
    for section in os.listdir(INPUT_DIR):
        sec_path = os.path.join(INPUT_DIR, section)
        if not os.path.isdir(sec_path): continue
        for docx in glob(os.path.join(sec_path, '*.docx')):
            qlist = parse_test(docx)
            name = os.path.splitext(os.path.basename(docx))[0] + '.json'
            out_path = os.path.join(OUTPUT_DIR, section + '__' + name)
            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(qlist, f, indent=2, ensure_ascii=False)
            print(f'→ {docx}  →  {out_path}')

if __name__ == '__main__':
    convert_all()
