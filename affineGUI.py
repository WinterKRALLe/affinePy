import sys, string
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton
from PyQt5 import uic


Ui_MainWindow, QtBaseClass = uic.loadUiType("affineGUI.ui")


class MyApp(QMainWindow, Ui_MainWindow):

    def zasifruj(self):
        from affine import normalizeText
        try:
            a = int(self.klicA.text())
            b = int(self.klicB.text())
        except:
            err = "Potřebuji klíče"
            self.error.setText(err)
        text = self.inputZasifrovat.text()
        text = normalizeText(text)
        s = ""
        for i in text:
            if (i == " "):
                s += "XMEZERAX"
                continue
            alphabet = string.ascii_lowercase
            ot = alphabet.find(i)
            X = (a * ot + b) % 26
            s += string.ascii_uppercase[X]
        self.outputZasifrovat.setText(s)


    def desifruj(self):
        try:
            a = int(self.klicA.text())
            b = int(self.klicB.text())
        except:
            err = "Potřebuji klíče"
            self.error.setText(err)
        s = ""
        letter = self.inputDesifrovat.text()
        letter = str.lower(letter)
        letter = letter.replace("xmezerax", " ")
        for h in letter:
            if h == " ":
                s += " "
                continue
            alphabet = string.ascii_lowercase
            ot = alphabet.find(h)
            try:
                pozice = (pow(a, -1, 26)*(ot-b)) % 26
                s += string.ascii_uppercase[pozice]
            except:
                err = "Inverzní prvek neexistuje, nepoužívejte sudá čísla"
                self.error.setText(err)
        if self.puvodniText.isChecked() == True:
            self.outputDesifrovat.setText(s)
        else:
            from textwrap import wrap
            s = "".join(s.split())
            s = wrap(s, 5)
            s = " ".join(s)
            self.outputDesifrovat.setText(s)


    def __init__(self):

        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.puvodniText.setChecked(True)

        self.zasifrovat.clicked.connect(self.zasifruj)
        self.desifrovat.clicked.connect(self.desifruj)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
