import os
import sys
import json
import shutil
import random
import re
from glob import glob
from docx import Document
from PyQt5 import QtWidgets, QtCore

# Constants
# JSON test definitions now in tests_json, sections as subfolders (or root "General")
tests_base = './tests_json'
results_file = 'results.json'

# Helpers
def ensure_base():
    os.makedirs(tests_base, exist_ok=True)

def load_sections():
    """
    Lista subcarpetas en tests_json como secciones.
    Si no hay subcarpetas pero existen JSON en root, devuelve ['General'].
    """
    ensure_base()
    secs = [d for d in os.listdir(tests_base)
            if os.path.isdir(os.path.join(tests_base, d))]
    if not secs:
        jsons = glob(os.path.join(tests_base, '*.json'))
        if jsons:
            secs = ['General']
    return secs

# Parser para JSON o .docx (fallback)
def parse_test(path):
    if path.lower().endswith('.json'):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    doc = Document(path)
    qlist, current = [], None
    for p in doc.paragraphs:
        t = p.text.strip()
        if not t: continue
        if re.match(r'.+\?$', t) and not re.match(r'^[ABCD][\.)]', t):
            if current: qlist.append(current)
            current = {'question': t, 'options': {}, 'answer': None}
            continue
        if current and re.match(r'^[ABCD][\.\)\-]\s+', t):
            label, text = t[0], re.sub(r'^[ABCD][\.\)\-]\s+', '', t)
            current['options'][label] = text
            continue
        if current and re.match(r'(?i)^respuesta[:]?[ \t]*[ABCD]', t):
            m = re.search(r'([ABCD])', t.upper())
            if m: current['answer'] = m.group(1)
            continue
    if current: qlist.append(current)
    if any(q.get('answer') is None for q in qlist):
        answers = [p.text.strip()[0] for p in doc.paragraphs
                if re.match(r'^[ABCD][\.\)\-]', p.text.strip())]
        if len(answers) >= len(qlist):
            for q,a in zip(qlist, answers): q['answer'] = a
    return qlist

# Carga/Guarda resultados
def load_results():
    if os.path.exists(results_file):
        with open(results_file,'r',encoding='utf-8') as f:
            return json.load(f)
    return {'exams':[]}

def save_results(data):
    with open(results_file,'w',encoding='utf-8') as f:
        json.dump(data,f,indent=2,ensure_ascii=False)

# Diálogo de revisión con scroll y coloreado
def show_review(parent, answers):
    dlg = QtWidgets.QDialog(parent)
    dlg.setWindowTitle('Revisión del Test')
    dlg.resize(600, 400)
    lay = QtWidgets.QVBoxLayout(dlg)

    html = '<html><body>'
    for item in answers:
        q = item['question']
        corr_txt = item.get('correct_text', '–––')
        sel_txt = item.get('selected_text', 'Sin responder')

        # Para decidir el color, seguimos comparando las letras:
        corr_letter = item.get('correct_letter')
        sel_letter = item.get('selected_letter')
        color_sel = 'green' if sel_letter == corr_letter else 'red'

        html += f'<p><b>Pregunta:</b> {q}<br>'
        html += f'<span style="color:green"><b>Correcta:</b> {corr_txt}</span><br>'
        html += f'<span style="color:{color_sel}"><b>Tu respuesta:</b> {sel_txt}</span></p><hr>'
    html += '</body></html>'

    te = QtWidgets.QTextEdit()
    te.setReadOnly(True)
    te.setHtml(html)
    lay.addWidget(te)

    btn = QtWidgets.QPushButton('Cerrar')
    btn.clicked.connect(dlg.accept)
    lay.addWidget(btn)

    dlg.exec_()


# GUI principal
class TestApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Generador de Tests')
        self.resize(800,600)
        self.results = load_results()
        self._init_ui()

    def _init_ui(self):
        tabs = QtWidgets.QTabWidget()
        tabs.addTab(self._tests_tab(),'Tests')
        tabs.addTab(self._stats_tab(),'Estadísticas')
        self.setCentralWidget(tabs)

    def _tests_tab(self):
        w = QtWidgets.QWidget(); layout = QtWidgets.QVBoxLayout()
        hl = QtWidgets.QHBoxLayout()
        self.section_cb = QtWidgets.QComboBox(); hl.addWidget(self.section_cb)
        self.test_cb = QtWidgets.QComboBox(); hl.addWidget(self.test_cb)
        btn_load = QtWidgets.QPushButton('Hacer Test'); btn_load.clicked.connect(self.start_lesson)
        hl.addWidget(btn_load)
        layout.addLayout(hl)
        hl2 = QtWidgets.QHBoxLayout()
        btn_rand = QtWidgets.QPushButton('Examen 20 aleatorias'); btn_rand.clicked.connect(self.start_random)
        hl2.addWidget(btn_rand)
        btn_add_sec = QtWidgets.QPushButton('Nueva Sección'); btn_add_sec.clicked.connect(self.add_section)
        hl2.addWidget(btn_add_sec)
        btn_add_test = QtWidgets.QPushButton('Añadir Test'); btn_add_test.clicked.connect(self.add_test)
        hl2.addWidget(btn_add_test)
        layout.addLayout(hl2)
        self._refresh_sections()
        w.setLayout(layout)
        return w

    def _stats_tab(self):
        w = QtWidgets.QWidget(); layout = QtWidgets.QVBoxLayout()
        self.stats_txt = QtWidgets.QTextEdit(); self.stats_txt.setReadOnly(True)
        layout.addWidget(self.stats_txt)
        btn = QtWidgets.QPushButton('Actualizar'); btn.clicked.connect(self.show_stats)
        layout.addWidget(btn)
        w.setLayout(layout)
        return w

    def _refresh_sections(self):
        secs = load_sections()
        self.section_cb.blockSignals(True)
        self.section_cb.clear(); self.section_cb.addItems(secs)
        self.section_cb.blockSignals(False)
        self._refresh_tests()
        self.section_cb.currentIndexChanged.connect(self._refresh_tests)

    def _refresh_tests(self):
        sec = self.section_cb.currentText()
        if sec=='General': pattern = os.path.join(tests_base,'*.json')
        else: pattern = os.path.join(tests_base,sec,'*.json')
        files = [os.path.basename(f) for f in glob(pattern)]
        self.test_cb.clear(); self.test_cb.addItems(files)

    def add_section(self):
        name,ok = QtWidgets.QInputDialog.getText(self,'Nueva Sección','Nombre:')
        if ok and name:
            sec = name.replace(' ','_')
            os.makedirs(os.path.join(tests_base,sec),exist_ok=True)
            self._refresh_sections()

    def add_test(self):
        sec = self.section_cb.currentText()
        src,_ = QtWidgets.QFileDialog.getOpenFileName(self,'Seleccionar .json','','JSON files (*.json)')
        if src and src.lower().endswith('.json'):
            if sec=='General': dst = os.path.join(tests_base,os.path.basename(src))
            else: dst = os.path.join(tests_base,sec,os.path.basename(src))
            shutil.copy(src,dst); self._refresh_tests()

    def start_lesson(self):
        sec = self.section_cb.currentText(); test = self.test_cb.currentText()
        if not test:
            QtWidgets.QMessageBox.warning(self,'Error','No hay tests en la sección seleccionada.')
            return
        path = (os.path.join(tests_base,test) if sec=='General'
                else os.path.join(tests_base,sec,test))
        qs = parse_test(path)
        if not qs:
            QtWidgets.QMessageBox.warning(self,'Error',f'No se encontraron preguntas en {test}.')
            return
        self._conduct(qs,'lesson',sec,test)

    def start_random(self):
        all_q=[]
        for sec in load_sections():
            pattern = (os.path.join(tests_base,'*.json') if sec=='General'
                    else os.path.join(tests_base,sec,'*.json'))
            for f in glob(pattern):
                for q in parse_test(f): q['section']=sec; all_q.append(q)
        if not all_q:
            QtWidgets.QMessageBox.warning(self,'Error','No hay preguntas disponibles.')
            return
        sel = random.sample(all_q,min(20,len(all_q)))
        self._conduct(sel,'random20',None,None)

    def _conduct(self,questions,typ,sec,test):
        dlg = QuestionDialog(questions,self)
        if dlg.exec_():
            ans = dlg.user_answers
            score = sum(1 for a in ans if a.get('selected_letter') == a.get('correct_letter'))
            self.results['exams'].append({'type':typ,'section':sec,'test':test,
                                        'score':score,'total':len(ans)})
            save_results(self.results)
            QtWidgets.QMessageBox.information(self,'Resultados',f'Puntuación: {score}/{len(ans)}')
            self.show_stats()
            show_review(self,ans)

    def show_stats(self):
        by_sec={}; total_c=total_q=0
        for e in self.results['exams']:
            key=e.get('section','General'); by_sec.setdefault(key,[]).append(e)
            total_c+=e['score']; total_q+=e['total']
        text=f'Total: {total_c}/{total_q}\n'
        for s,exs in by_sec.items():
            text+=f"Sección '{s}': {sum(e['score'] for e in exs)}/{sum(e['total'] for e in exs)}\n"
        self.stats_txt.setText(text)

class QuestionDialog(QtWidgets.QDialog):
    def __init__(self,questions,parent=None):
        super().__init__(parent)
        self.questions=questions; self.user_answers=[]; self.idx=0
        self.setWindowTitle('Examen')
        self.layout=QtWidgets.QVBoxLayout(); self.setLayout(self.layout)
        self.lbl=QtWidgets.QLabel(); self.lbl.setWordWrap(True)
        self.layout.addWidget(self.lbl)
        self.opt_group=QtWidgets.QGroupBox('Opciones')
        self.opt_layout=QtWidgets.QVBoxLayout(); self.opt_group.setLayout(self.opt_layout)
        self.layout.addWidget(self.opt_group)
        self.radio_group=QtWidgets.QButtonGroup(self); self.radio_group.setExclusive(True)
        self.btn_next=QtWidgets.QPushButton('Siguiente'); self.btn_next.clicked.connect(self.next_q)
        self.layout.addWidget(self.btn_next)
        self._show_question()

    def _show_question(self):
        q=self.questions[self.idx]; self.lbl.setText(q['question'])
        for i in reversed(range(self.opt_layout.count())):
            w=self.opt_layout.itemAt(i).widget(); self.radio_group.removeButton(w)
            self.opt_layout.removeWidget(w); w.deleteLater()
        for key,txt in sorted(q['options'].items()):
            rb=QtWidgets.QRadioButton(f"{key}. {txt}")
            rb.setAutoExclusive(False); rb.setChecked(False)
            self.radio_group.addButton(rb); self.opt_layout.addWidget(rb)
        for b in self.radio_group.buttons():
            b.toggled.connect(lambda checked,btn=b: btn.setAutoExclusive(True) if checked else None)
        if self.idx==len(self.questions)-1:
            self.btn_next.setText('Terminar')

    def next_q(self):
        sel_letter = None
        # Buscamos la letra marcada
        for b in self.radio_group.buttons():
            if b.isChecked():
                sel_letter = b.text()[0]  # “A”, “B”, “C” o “D”

        # Obtenemos la letra correcta tal como estaba
        corr_letter = self.questions[self.idx]['answer']

        # SACAMOS EL TEXTO (string) correspondiente a cada letra
        sel_text = None
        if sel_letter:
            sel_text = self.questions[self.idx]['options'].get(sel_letter, None)

        corr_text = self.questions[self.idx]['options'].get(corr_letter, None)

        # Ahora guardamos en user_answers no sólo letra, sino texto completo
        self.user_answers.append({
            'question': self.questions[self.idx]['question'],
            'selected_letter': sel_letter,
            'selected_text': sel_text,
            'correct_letter': corr_letter,
            'correct_text': corr_text
        })

        self.idx += 1
        if self.idx < len(self.questions):
            self._show_question()
        else:
            self.accept()

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    win=TestApp(); win.show(); sys.exit(app.exec_())

# End of file
