import sys
import os
from random import randint, choice
from math import gcd
from itertools import cycle
import hashlib
import typing
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog, QMessageBox
import MainDesign
import RSADesignEnc
import RSADesignDec
import EGSADesignEnc
import EGSADesignDec
import DSADesignEnc
import DSADesignDec
import GOSTDesignEnc
import GOSTDesignDec
import ModeRSADesign
import ModeEGSADesign
import ModeDSADesign
import ModeGOSTDesign

class MainApp(QtWidgets.QMainWindow, MainDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.window1 = ModeRSAWindow()
        self.window2 = ModeEGSAWindow()
        self.window3 = ModeDSAWindow()
        self.window4 = ModeGOSTWindow()
        self.btnEnc1.clicked.connect(lambda checked: self.toggle_window(self.window1))
        self.btnEnc2.clicked.connect(lambda checked: self.toggle_window(self.window2))
        self.btnEnc3.clicked.connect(lambda checked: self.toggle_window(self.window3))
        self.btnEnc4.clicked.connect(lambda checked: self.toggle_window(self.window4))
    
    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()

class ModeRSAWindow(QtWidgets.QWidget, ModeRSADesign.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mode1 = RSAWindowEnc()
        self.mode2 = RSAWindowDec()
        self.btnEncryptMode.clicked.connect(lambda checked: self.toggle_mode(self.mode1))
        self.btnDecryptMode.clicked.connect(lambda checked: self.toggle_mode(self.mode2))
    
    def toggle_mode(self, mode):
        if mode.isVisible():
            mode.hide()
        else:
            mode.show()

class ModeEGSAWindow(QtWidgets.QWidget, ModeEGSADesign.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mode1 = EGSAWindowEnc()
        self.mode2 = EGSAWindowDec()
        self.btnEncryptMode.clicked.connect(lambda checked: self.toggle_mode(self.mode1))
        self.btnDecryptMode.clicked.connect(lambda checked: self.toggle_mode(self.mode2))
    
    def toggle_mode(self, mode):
        if mode.isVisible():
            mode.hide()
        else:
            mode.show()

class ModeDSAWindow(QtWidgets.QWidget, ModeDSADesign.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mode1 = DSAWindowEnc()
        self.mode2 = DSAWindowDec()
        self.btnEncryptMode.clicked.connect(lambda checked: self.toggle_mode(self.mode1))
        self.btnDecryptMode.clicked.connect(lambda checked: self.toggle_mode(self.mode2))
    
    def toggle_mode(self, mode):
        if mode.isVisible():
            mode.hide()
        else:
            mode.show()
                        
class ModeGOSTWindow(QtWidgets.QWidget, ModeGOSTDesign.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mode1 = GOSTWindowEnc()
        self.mode2 = GOSTWindowDec()
        self.btnEncryptMode.clicked.connect(lambda checked: self.toggle_mode(self.mode1))
        self.btnDecryptMode.clicked.connect(lambda checked: self.toggle_mode(self.mode2))
    
    def toggle_mode(self, mode):
        if mode.isVisible():
            mode.hide()
        else:
            mode.show()

class RSAWindowEnc(QtWidgets.QWidget, RSADesignEnc.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.click = False
        self.btnPQ.clicked.connect(self.calc_pq)
        self.btnSave.clicked.connect(self.save_num)
        self.btnE.clicked.connect(self.select_e)
        self.btnSel.clicked.connect(self.open_file)
        self.btnEnc.clicked.connect(self.save_file)
        self.btnSaveEDS.clicked.connect(self.save_eds)
    
    def calc_pq(self):
        if (self.click == False):
            self.rand_p = self.isPrime()
            self.rand_q = self.isPrime()
            self.labelP2.setText(str(self.rand_p))
            self.labelQ2.setText(str(self.rand_q))

            self.n = self.rand_p * self.rand_q
            self.len_n = len(str(self.n)) - 1
            self.labelN2.setText(str(self.n))

            self.fn = (self.rand_p - 1) * (self.rand_q - 1)
            self.labelFN2.setText(str(self.fn))

            self.e = randint(2, self.fn)
            while gcd(self.e, self.fn) != 1:
                self.e = randint(2, self.fn)
            self.labelE2.setText(str(self.e))

            self.d = randint(2, self.n - 1)
            while ((self.e * self.d) % self.fn) != 1:
                self.d = randint(2, self.n - 1)
            self.labelD2.setText(str(self.d))

            self.click = True
        else:
            again = QMessageBox.question(self, 'Question', "Вы хотите начать заново?")
            if again == QMessageBox.StandardButton.Yes:
                self.rand_p = self.isPrime()
                self.rand_q = self.isPrime()
                self.labelP2.setText(str(self.rand_p))
                self.labelQ2.setText(str(self.rand_q))

                self.n = self.rand_p * self.rand_q
                self.len_n = len(str(self.n)) - 1
                self.labelN2.setText(str(self.n))

                self.fn = (self.rand_p - 1) * (self.rand_q - 1)
                self.labelFN2.setText(str(self.fn))

                self.e = randint(2, self.fn)
                while gcd(self.e, self.fn) != 1:
                    self.e = randint(2, self.fn)
                self.labelE2.setText(str(self.e))

                self.d = randint(2, self.n - 1)
                while ((self.e * self.d) % self.fn) != 1:
                    self.d = randint(2, self.n - 1)
                self.labelD2.setText(str(self.d))

                self.click = True

    def isPrime(self):
        n = 699
        a = [i for i in range(n+1)]
        a[1] = 0
        i = 2
        while i <= n:
            if a[i] != 0:
                j = i + i
                while j <= n:
                    a[j] = 0
                    j = j + i
            i = i + 1
        a = [i for i in a if a[i] >= 2]
        a_rand = choice(a)
        return a_rand
    
    def save_num(self):
        try:
            lines_num = [str(self.rand_p), str(self.rand_q), str(self.n), str(self.fn), str(self.e)]
            save_number, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
            if save_number:
                with open(save_number, 'w+') as num_file:
                    for line in lines_num:
                        num_file.write(line + '\n')
                QMessageBox.information(self, 'Information', 'Числа сохранены')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначала необходимо создать числа')
    
    def select_e(self):
        dialog_e, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if dialog_e:
            with open(dialog_e, 'r') as file_e:
                self.AnotherE = int(file_e.read())
            self.labelAnotherE2.setText(str(self.AnotherE))
    
    def open_file(self):
        dialog, _ = QFileDialog.getOpenFileName(self, "Open FIle", ".", "Text Files (*.txt);;All Files (*)")
        if dialog:
            with open(dialog, 'r') as file:
                self.crypt_text = file.read()
            self.crypt_text = int(hashlib.sha256(self.crypt_text.encode('utf-8')).hexdigest(), 16) % 10**self.len_n
            with open(dialog, 'r') as byte_file:
                self.byte_text = byte_file.read()
            self.labelHash2.setText(str(self.crypt_text))

            self.c = (self.crypt_text ** self.AnotherE) % self.n
            self.labelC2.setText(str(self.c))
    
    def save_file(self):
        try:
            self.encrypt = self.encrypt_file()
            save_dialog, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
            if save_dialog:
                with open(save_dialog, 'w+') as save_file:
                    save_file.write(self.encrypt)
                QMessageBox.information(self, 'Information', 'Информация зашифрована')
            self.eds = (self.crypt_text ** self.d) % self.n
            self.labelEDS2.setText(str(self.eds))
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначало нужно выбрать файл и получить все числа')
    
    def encrypt_file(self):
        return "".join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(self.byte_text, cycle(str(self.crypt_text))))
    
    def save_eds(self):
        try:
            lines_eds = [str(self.c), str(self.eds)]
            eds_dialog, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
            if eds_dialog:
                with open(eds_dialog, 'w+') as eds_file:
                    for line in lines_eds:
                        eds_file.write(line + '\n')
                QMessageBox.information(self, 'Information', 'ЭЦП сохранено')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначало нужно получить ЭЦП')

class RSAWindowDec(QtWidgets.QWidget, RSADesignDec.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnLoadNum.clicked.connect(self.open_num)
        self.btnSelE.clicked.connect(self.save_e)
        self.btnSelEnc.clicked.connect(self.sel_file)
        self.btnSelEDS.clicked.connect(self.sel_eds)
        self.btnDec.clicked.connect(self.decrypt)
    
    def open_num(self):
        dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if dialog:
            with open(dialog, 'r') as file:
                self.lines = file.readlines()
            self.p = int(self.lines[0])
            self.q = int(self.lines[1])
            self.n = int(self.lines[2])
            self.fn = int(self.lines[3])
            self.AnotherE = int(self.lines[4])
            self.e = self.sel_e()
            self.d = self.sel_d()
            self.labelP2.setText(str(self.p))
            self.labelQ2.setText(str(self.q))
            self.labelN2.setText(str(self.n))
            self.labelFN2.setText(str(self.fn))
            self.labelE2.setText(str(self.e))
            self.labelD2.setText(str(self.d))
            self.labelAnotherE2.setText(str(self.AnotherE))
    
    def sel_e(self):
        self.e = randint(2, self.fn)
        while gcd(self.e, self.fn) != 1:
            self.e = randint(2, self.fn)
        return self.e
    
    def sel_d(self):
        self.d = randint(2, self.n - 1)
        while ((self.e * self.d) % self.fn) != 1:
            self.d = randint(2, self.n - 1)
        return self.d
    
    def save_e(self):
        try:
            save_dialog, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
            if save_dialog:
                with open(save_dialog, 'w+') as save_e:
                    save_e.write(str(self.e))
                QMessageBox.information(self, "Information", "Число e сохранено")
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначало нужно загрузить числа')
    
    def sel_file(self):
        file_dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if file_dialog:
            with open(file_dialog, 'r') as file:
                self.encrypt_text = file.read()
            QMessageBox.information(self, 'Information', 'Файл выбран')
    
    def sel_eds(self):
        eds_dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if eds_dialog:
            with open(eds_dialog, 'r') as eds_file:
                self.lines = eds_file.readlines()
            self.c = int(self.lines[0])
            self.eds = int(self.lines[1])
            self.labelC2.setText(str(self.c))
            self.labelEDS2.setText(str(self.eds))
    
    def decrypt(self):
        try:
            self.hash = (self.c ** self.d) % self.n
            self.check_eds = (self.eds ** self.AnotherE) % self.n
            if (self.hash == self.check_eds):
                self.crypt = self.hash
                QMessageBox.information(self, 'Information', 'Подпись подтверждена. Информация будет расшифрована')
                self.decrypts = self.decrypt_file()
                dec_dialog, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
                if dec_dialog:
                    with open(dec_dialog, 'w+') as dec_file:
                        dec_file.write(self.decrypts)
                    QMessageBox.information(self, 'Information', 'Информация расшифрована')
            else:
                QMessageBox.information(self, 'Information', 'Подпись не подтверждена. Информация не расшифрована')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначало нужно выбрать файл и получить все числа')
    
    def decrypt_file(self):
        return "".join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(self.encrypt_text, cycle(str(self.crypt))))
        
class EGSAWindowEnc(QtWidgets.QWidget, EGSADesignEnc.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.click = False
        self.btnStart.clicked.connect(self.calc_start)
        self.btnSave.clicked.connect(self.save_num)
        self.btnSelY.clicked.connect(self.sel_y)
        self.btnSel.clicked.connect(self.sel_file)
        self.btnEnc.clicked.connect(self.encrypt_file)
        self.btnSaveEDS.clicked.connect(self.save_eds)
    
    def calc_start(self):
        if (self.click == False):
            self.num_of_num = 699
            self.p = self.isPrime(self.num_of_num)
            self.g = self.isBothPrime(self.p)
            self.len_p = len(str(self.p)) - 1
            self.labelP2.setText(str(self.p))
            self.labelG2.setText(str(self.g))

            self.x_ = self.isPrime(self.p - 1)
            self.labelX2.setText(str(self.x_))
            self.y_ = (self.g ** self.x_) % self.p
            self.labelY2.setText(str(self.y_))
            self.click = True
        else:
            again = QMessageBox.question(self, 'Question', "Вы хотите начать заново?")
            if again == QMessageBox.StandardButton.Yes:
                self.num_of_num = 699
                self.p = self.isPrime(self.num_of_num)
                self.g = self.isBothPrime(self.p)
                self.len_p = len(str(self.p)) - 1
                self.labelP2.setText(str(self.p))
                self.labelG2.setText(str(self.g))

                self.x_ = self.isPrime(self.p - 1)
                self.labelX2.setText(str(self.x_))
                self.y_ = (self.g ** self.x_) % self.p
                self.labelY2.setText(str(self.y_))
                self.click = True
    
    def isPrime(self, n):
        a = [i for i in range(n+1)]
        a[1] = 0
        i = 2
        while i <= n:
            if a[i] != 0:
                j = i + i
                while j <= n:
                    a[j] = 0
                    j = j + i
            i = i + 1
        a = [i for i in a if a[i] >= 2]
        a_rand = choice(a)
        return a_rand
    
    def isBothPrime(self, mod):
        coprime_set = {num for num in range(1, mod) if gcd(num, mod) == 1}
        both_prime = [g for g in range(1, mod) if coprime_set == {pow(g, powers, mod) for powers in range(1, mod)}]
        g_prime = choice(both_prime)
        return g_prime
    
    def iscoprime(self, p):
        k = randint(1, p - 1)
        while gcd(p - 1, k) != 1:
            k = randint(1, p - 1)
        return k
    
    def save_num(self):
        try:
            lines_num = [str(self.p), str(self.g), str(self.y_)]
            save_number, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
            if save_number:
                with open(save_number, 'w+') as num_file:
                    for line in lines_num:
                        num_file.write(line + '\n')
                QMessageBox.information(self, 'Information', 'Числа сохранены')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначала необходимо создать числа')
    
    def sel_y(self):
        y_dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if y_dialog:
            with open(y_dialog, 'r') as y_file:
                self.AnotherY = int(y_file.read())
            self.labelAnotherY2.setText(str(self.AnotherY))
    
    def sel_file(self):
        dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if dialog:
            with open(dialog, 'r') as file:
                self.hash = file.read()
            self.hash = int(hashlib.sha256(self.hash.encode('utf-8')).hexdigest(), 16) % 10**self.len_p
            with open(dialog, 'r') as crypt_file:
                self.crypt_text = crypt_file.read()
            self.labelHash2.setText(str(self.hash))

            self.k = self.iscoprime(self.p)
            self.labelK2.setText(str(self.k))
            self.r = (self.g ** self.k) % self.p
            self.labelR2.setText(str(self.r))
    
    def encrypt_file(self):
        try:
            self.a = (self.g ** self.k) % self.p
            self.b = ((self.AnotherY ** self.k) * self.hash) % self.p
            self.encrypt = "".join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(self.crypt_text, cycle(str(self.hash))))
            save_dialog, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
            if save_dialog:
                with open(save_dialog, 'w+') as save_file:
                    save_file.write(self.encrypt)
                QMessageBox.information(self, 'Information', 'Информация зашифрована')
            self.mod = self.p - 1
            self.k_obr = pow(self.k, -1 , self.mod)
            self.s = ((self.hash - (self.x_ * self.r)) * self.k_obr) % (self.p - 1)
            self.labelEDS2.setText(str(self.r) + ', ' + str(self.s))
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначала нужно выбрать файл и получить все числа')
    
    def save_eds(self):
        try:
            lines_eds = [str(self.a), str(self.b), str(self.r), str(self.s)]
            eds_dialog, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
            if eds_dialog:
                with open(eds_dialog, 'w+') as eds_file:
                    for line in lines_eds:
                        eds_file.write(line + '\n')
                QMessageBox.information(self, 'Information', 'ЭЦП сохранено')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначало нужно получить ЭЦП')

            
class EGSAWindowDec(QtWidgets.QWidget, EGSADesignDec.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnLoad.clicked.connect(self.load_num)
        self.btnSaveY.clicked.connect(self.save_y)
        self.btnSel.clicked.connect(self.sel_file)
        self.btnSelEDS.clicked.connect(self.sel_eds)
        self.btnDec.clicked.connect(self.decrypt_file)
    
    def load_num(self):
        dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if dialog:
            with open(dialog, 'r') as file:
                self.lines = file.readlines()
            self.p = int(self.lines[0])
            self.g = int(self.lines[1])
            self.AnotherY = int(self.lines[2])
            self.labelP2.setText(str(self.p))
            self.labelG2.setText(str(self.g))
            self.labelAnotherY2.setText(str(self.AnotherY))
            self.len_p = len(str(self.p)) - 1

            self.x_ = self.isPrime(self.p - 1)
            self.labelX2.setText(str(self.x_))
            self.y_ = (self.g ** self.x_) % self.p
            self.labelY2.setText(str(self.y_))

    def isPrime(self, n):
        a = [i for i in range(n+1)]
        a[1] = 0
        i = 2
        while i <= n:
            if a[i] != 0:
                j = i + i
                while j <= n:
                    a[j] = 0
                    j = j + i
            i = i + 1
        a = [i for i in a if a[i] >= 2]
        a_rand = choice(a)
        return a_rand
    
    def save_y(self):
        try:
            y_dialog, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
            if y_dialog:
                with open(y_dialog, 'w+') as y_file:
                    y_file.write(str(self.y_))
                QMessageBox.information(self, 'Information', 'Число y сохранено')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначала необходимо загрузить числа')
    
    def sel_file(self):
        file_dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if file_dialog:
            with open(file_dialog, 'r') as file:
                self.encrypt_text = file.read()
            QMessageBox.information(self, 'Information', 'Файл выбран')

    def sel_eds(self):
        eds_dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if eds_dialog:
            with open(eds_dialog, 'r') as eds_file:
                self.lines_eds = eds_file.readlines()
            self.a = int(self.lines_eds[0])
            self.b = int(self.lines_eds[1])
            self.r = int(self.lines_eds[2])
            self.s = int(self.lines_eds[3])
            self.labelEDS2.setText(str(self.r) + ', ' + str(self.s))
    
    def decrypt_file(self):
        try:
            self.hash = (self.b * (self.a ** (self.p - 1 - self.x_))) % self.p
            self.check_eds1 = (self.g ** self.hash) % self.p
            self.check_eds2 = ((self.AnotherY ** self.r) * (self.r ** self.s)) % self.p
            if (self.check_eds1 == self.check_eds2):
                QMessageBox.information(self, 'Information', 'Подпись подтверждена. Информация будет расшифрована')
                self.decrypts = "".join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(self.encrypt_text, cycle(str(self.hash))))
                dec_dialog, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
                if dec_dialog:
                    with open(dec_dialog, 'w+') as dec_file:
                        dec_file.write(self.decrypts)
                    QMessageBox.information(self, 'Information', 'Информация расшифрована')
            else:
                QMessageBox.information(self, 'Information', 'Подпись не подтверждена. Информация не расшифрована')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначало нужно выбрать файл и получить все числа')


class DSAWindowEnc(QtWidgets.QWidget, DSADesignEnc.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.click = False
        self.btnStart.clicked.connect(self.calc_start)
        self.btnSave.clicked.connect(self.save_num)
        self.btnSel.clicked.connect(self.sel_file)
        self.btnEnc.clicked.connect(self.get_eds)
        self.btnSaveEDS.clicked.connect(self.save_eds)
    
    def calc_start(self):
        if (self.click == False):
            self.num_of_num_q = 699
            self.num_of_num_p = 9999
            self.prime = self.isPrimeDiv(self.num_of_num_q, self.num_of_num_p)
            self.q = self.prime[0]
            self.p = self.prime[1]
            self.g = self.isBothPrime(self.p, self.q)
            self.len_q = len(str(self.q)) - 1
            self.labelQ2.setText(str(self.q))
            self.labelP2.setText(str(self.p))
            self.labelG2.setText(str(self.g))

            self.x_ = randint(1, self.q)
            self.labelX2.setText(str(self.x_))
            self.y_ = (self.g ** self.x_) % self.p
            self.labelY2.setText(str(self.y_))
            self.click = True
        else:
            again = QMessageBox.question(self, 'Question', "Вы хотите начать заново?")
            if again == QMessageBox.StandardButton.Yes:
                self.num_of_num_q = 699
                self.num_of_num_p = 9999
                self.prime = self.isPrimeDiv(self.num_of_num_q, self.num_of_num_p)
                self.q = self.prime[0]
                self.p = self.prime[1]
                self.g = self.isBothPrime(self.p, self.q)
                self.len_q = len(str(self.q)) - 1
                self.labelQ2.setText(str(self.q))
                self.labelP2.setText(str(self.p))
                self.labelG2.setText(str(self.g))

                self.x_ = randint(1, self.q)
                self.labelX2.setText(str(self.x_))
                self.y_ = (self.g ** self.x_) % self.p
                self.labelY2.setText(str(self.y_))
                self.click = True
    
    def isPrimeDiv(self, num_q, num_p):
        q_arr = [i for i in range(num_q + 1)]
        q_arr[1] = 0
        i = 2
        while i <= num_q:
            if q_arr[i] != 0:
                j = i + i
                while j <= num_q:
                    q_arr[j] = 0
                    j = j + i
            i = i + 1
        q_arr = [i for i in q_arr if q_arr[i] >= 2]
        q = choice(q_arr)
        p_arr = [i for i in range(num_p + 1)]
        p_arr[1] = 0
        i = 2
        while i <= num_p:
            if p_arr[i] != 0:
                j = i + i
                while j <= num_p:
                    p_arr[j] = 0
                    j = j + i
            i = i + 1
        p_arr = [i for i in p_arr if p_arr[i] >= 2]
        p = choice(p_arr)
        while ((p - 1) % q != 0):
            p = choice(p_arr)
        return [q, p]
    
    def isBothPrime(self, p, q):
        g = 1
        while (g == 1):
            h = randint(1, p - 1)
            g = (h ** ((p - 1) // q)) % p
        return g
    
    def save_num(self):
        try:
            lines_num = [str(self.q), str(self.p), str(self.g), str(self.y_)]
            save_number, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
            if save_number:
                with open(save_number, 'w+') as num_file:
                    for line in lines_num:
                        num_file.write(line + '\n')
                QMessageBox.information(self, 'Information', 'Числа сохранены')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначала необходимо создать числа')
    
    def sel_file(self):
        dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if dialog:
            with open(dialog, 'r') as file:
                self.hash = file.read()
            self.hash = int(hashlib.sha256(self.hash.encode('utf-8')).hexdigest(), 16) % 10**self.len_q
            self.labelHash2.setText(str(self.hash))

            self.k = randint(1, self.q)
            self.labelK2.setText(str(self.k))
            self.r = ((self.g ** self.k) % self.p) % self.q
            self.labelR2.setText(str(self.r))
    
    def get_eds(self):
        try:
            self.k_obr = pow(self.k, -1 , self.q)
            self.s = ((self.hash + (self.x_ * self.r)) * self.k_obr) % self.q
            self.labelEDS2.setText(str(self.r) + ', ' + str(self.s))
            QMessageBox.information(self, 'Information', 'Подпись сформирована')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначала нужно выбрать файл и получить все числа')
    
    def save_eds(self):
        try:
            lines_eds = [str(self.r), str(self.s), str(self.hash)]
            eds_dialog, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
            if eds_dialog:
                with open(eds_dialog, 'w+') as eds_file:
                    for line in lines_eds:
                        eds_file.write(line + '\n')
                QMessageBox.information(self, 'Information', 'ЭЦП сохранено')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначало нужно получить ЭЦП')


class DSAWindowDec(QtWidgets.QWidget, DSADesignDec.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnLoad.clicked.connect(self.load_num)
        self.btnSel.clicked.connect(self.sel_file)
        self.btnSelEDS.clicked.connect(self.sel_eds)
        self.btnDec.clicked.connect(self.decrypt_file)
    
    def load_num(self):
        dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if dialog:
            with open(dialog, 'r') as file:
                self.lines = file.readlines()
            self.q = int(self.lines[0])
            self.p = int(self.lines[1])
            self.g = int(self.lines[2])
            self.AnotherY = int(self.lines[3])
            self.labelQ2.setText(str(self.q))
            self.labelP2.setText(str(self.p))
            self.labelG2.setText(str(self.g))
            self.labelAnotherY2.setText(str(self.AnotherY))
            self.len_p = len(str(self.p)) - 1

            self.x_ = randint(1, self.q)
            self.labelX2.setText(str(self.x_))
            self.y_ = (self.g ** self.x_) % self.p
            self.labelY2.setText(str(self.y_))
    
    def sel_file(self):
        file_dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if file_dialog:
            with open(file_dialog, 'r') as file:
                self.encrypt_text = file.read()
            QMessageBox.information(self, 'Information', 'Файл выбран')

    def sel_eds(self):
        eds_dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if eds_dialog:
            with open(eds_dialog, 'r') as eds_file:
                self.lines_eds = eds_file.readlines()
            self.r = int(self.lines_eds[0])
            self.s = int(self.lines_eds[1])
            self.hash = int(self.lines_eds[2])
            self.labelEDS2.setText(str(self.r) + ', ' + str(self.s))
    
    def decrypt_file(self):
        try:
            self.w = pow(self.s, -1 , self.q)
            self.u1 = (self.hash * self.w) % self.q
            self.u2 = (self.r * self.w) % self.q
            self.v = (((self.g ** self.u1) * (self.AnotherY ** self.u2)) % self.p) % self.q
            if (self.v == self.r):
                QMessageBox.information(self, 'Information', 'Подпись подтверждена')
            else:
                QMessageBox.information(self, 'Information', 'Подпись не подтверждена')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначало нужно выбрать файл и получить все числа')


class GOSTWindowEnc(QtWidgets.QWidget, GOSTDesignEnc.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.click = False
        self.btnStart.clicked.connect(self.calc_start)
        self.btnSave.clicked.connect(self.save_num)
        self.btnSel.clicked.connect(self.sel_file)
        self.btnEnc.clicked.connect(self.get_eds)
        self.btnSaveEDS.clicked.connect(self.save_eds)
    
    def calc_start(self):
        if (self.click == False):
            self.num_of_num_q = 699
            self.num_of_num_p = 9999
            self.prime = self.isPrimeDiv(self.num_of_num_q, self.num_of_num_p)
            self.q = self.prime[0]
            self.p = self.prime[1]
            self.g = self.isBothPrime(self.p, self.q)
            self.len_p = len(str(self.p)) - 1
            self.labelQ2.setText(str(self.q))
            self.labelP2.setText(str(self.p))
            self.labelG2.setText(str(self.g))

            self.x_ = randint(1, self.q)
            self.labelX2.setText(str(self.x_))
            self.y_ = (self.g ** self.x_) % self.p
            self.labelY2.setText(str(self.y_))
            self.click = True
        else:
            again = QMessageBox.question(self, 'Question', "Вы хотите начать заново?")
            if again == QMessageBox.StandardButton.Yes:
                self.num_of_num_q = 699
                self.num_of_num_p = 9999
                self.prime = self.isPrimeDiv(self.num_of_num_q, self.num_of_num_p)
                self.q = self.prime[0]
                self.p = self.prime[1]
                self.g = self.isBothPrime(self.p, self.q)
                self.len_p = len(str(self.p)) - 1
                self.labelQ2.setText(str(self.q))
                self.labelP2.setText(str(self.p))
                self.labelG2.setText(str(self.g))

                self.x_ = randint(1, self.q)
                self.labelX2.setText(str(self.x_))
                self.y_ = (self.g ** self.x_) % self.p
                self.labelY2.setText(str(self.y_))
                self.click = True
    
    def isPrimeDiv(self, num_q, num_p):
        q_arr = [i for i in range(num_q + 1)]
        q_arr[1] = 0
        i = 2
        while i <= num_q:
            if q_arr[i] != 0:
                j = i + i
                while j <= num_q:
                    q_arr[j] = 0
                    j = j + i
            i = i + 1
        q_arr = [i for i in q_arr if q_arr[i] >= 2]
        q = choice(q_arr)
        p_arr = [i for i in range(num_p + 1)]
        p_arr[1] = 0
        i = 2
        while i <= num_p:
            if p_arr[i] != 0:
                j = i + i
                while j <= num_p:
                    p_arr[j] = 0
                    j = j + i
            i = i + 1
        p_arr = [i for i in p_arr if p_arr[i] >= 2]
        p = choice(p_arr)
        while ((p - 1) % q != 0):
            p = choice(p_arr)
        return [q, p]
    
    def isBothPrime(self, p, q):
        g = 1
        while (g == 1):
            h = randint(1, p - 1)
            g = (h ** ((p - 1) // q)) % p
        return g
    
    def save_num(self):
        try:
            lines_num = [str(self.q), str(self.p), str(self.g), str(self.y_)]
            save_number, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
            if save_number:
                with open(save_number, 'w+') as num_file:
                    for line in lines_num:
                        num_file.write(line + '\n')
                QMessageBox.information(self, 'Information', 'Числа сохранены')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначала необходимо создать числа')
    
    def sel_file(self):
        dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if dialog:
            with open(dialog, 'r') as file:
                self.hash = file.read()
            self.hash = int(hashlib.sha256(self.hash.encode('utf-8')).hexdigest(), 16) % 10**self.len_p
            self.labelHash2.setText(str(self.hash))

            self.k = randint(1, self.q)
            self.labelK2.setText(str(self.k))
            self.r = ((self.g ** self.k) % self.p) % self.q
            self.labelR2.setText(str(self.r))
    
    def get_eds(self):
        try:
            self.s = ((self.x_ * self.r) + (self.k * self.hash)) % self.q
            self.labelEDS2.setText(str(self.r) + ', ' + str(self.s))
            QMessageBox.information(self, 'Information', 'Подпись сформирована')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначала нужно выбрать файл и получить все числа')
    
    def save_eds(self):
        try:
            lines_eds = [str(self.r), str(self.s), str(self.hash)]
            eds_dialog, _ = QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt);;All Files (*)")
            if eds_dialog:
                with open(eds_dialog, 'w+') as eds_file:
                    for line in lines_eds:
                        eds_file.write(line + '\n')
                QMessageBox.information(self, 'Information', 'ЭЦП сохранено')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначало нужно получить ЭЦП')

class GOSTWindowDec(QtWidgets.QWidget, GOSTDesignDec.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnLoad.clicked.connect(self.load_num)
        self.btnSel.clicked.connect(self.sel_file)
        self.btnSelEDS.clicked.connect(self.sel_eds)
        self.btnDec.clicked.connect(self.decrypt_file)
    
    def load_num(self):
        dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if dialog:
            with open(dialog, 'r') as file:
                self.lines = file.readlines()
            self.q = int(self.lines[0])
            self.p = int(self.lines[1])
            self.g = int(self.lines[2])
            self.AnotherY = int(self.lines[3])
            self.labelQ2.setText(str(self.q))
            self.labelP2.setText(str(self.p))
            self.labelG2.setText(str(self.g))
            self.labelAnotherY2.setText(str(self.AnotherY))
            self.len_p = len(str(self.p)) - 1

            self.x_ = randint(1, self.q)
            self.labelX2.setText(str(self.x_))
            self.y_ = (self.g ** self.x_) % self.p
            self.labelY2.setText(str(self.y_))
    
    def sel_file(self):
        file_dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if file_dialog:
            with open(file_dialog, 'r') as file:
                self.encrypt_text = file.read()
            QMessageBox.information(self, 'Information', 'Файл выбран')

    def sel_eds(self):
        eds_dialog, _ = QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        if eds_dialog:
            with open(eds_dialog, 'r') as eds_file:
                self.lines_eds = eds_file.readlines()
            self.r = int(self.lines_eds[0])
            self.s = int(self.lines_eds[1])
            self.hash = int(self.lines_eds[2])
            self.labelEDS2.setText(str(self.r) + ', ' + str(self.s))
    
    def decrypt_file(self):
        try:
            self.w = (self.hash ** (self.q - 2)) % self.q
            self.u1 = (self.s * self.w) % self.q
            self.u2 = ((self.q - self.r) * self.w) % self.q
            self.v = (((self.g ** self.u1) * (self.AnotherY ** self.u2)) % self.p) % self.q
            if (self.v == self.r):
                QMessageBox.information(self, 'Information', 'Подпись подтверждена')
            else:
                QMessageBox.information(self, 'Information', 'Подпись не подтверждена')
        except AttributeError:
            QMessageBox.information(self, 'Information', 'Сначало нужно выбрать файл и получить все числа')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()