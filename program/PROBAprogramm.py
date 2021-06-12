import sys
from PROBAinterface import *
from PyQt5.QtWidgets import QApplication, QFrame, QGroupBox, QRadioButton, QListWidget, QLabel,\
                            QListWidgetItem, QPushButton, QListView, QAction, QMainWindow, qApp,\
                            QWidget, QGridLayout, QTableWidget, QTabWidget, QVBoxLayout, QSpinBox, QLineEdit,\
                            QPlainTextEdit, QMessageBox
from defs import *
from defsFact import *
from PyQt5.QtGui import QImage

class MyWin(QMainWindow):

    # выбор пункта меню
    def choose(self):
        if self.ui.itemMultMatrix.isSelected():  # isSelected() возвращает True/False
            try:
                try:
                    self.ui.mainWidget.hide()
                except:
                    pass
                self.ui.mainWidget.show()  # показ только что загруженного виджета
                self.ui.widget.hide()
                self.ui.widget2.hide()
                self.ui.widget3.hide()
            except:
                pass

        if self.ui.transpMatrix.isSelected():
            try:
                try:
                    self.ui.widget2.hide()
                except:
                    pass
                self.ui.mainWidget.hide()
                self.ui.widget.hide()
                self.ui.widget3.hide()
                self.ui.widget2.show()
            except:
                pass

        if self.ui.Gauss.isSelected():
            try:
                try:
                    self.ui.widget.hide()
                except:
                    pass
                self.ui.mainWidget.hide()
                self.ui.widget2.hide()
                self.ui.widget3.hide()
                self.ui.widget.show()
            except:
                pass

        if self.ui.Factor.isSelected():  # isSelected() возвращает True/False
            try:
                try:
                    self.ui.widget3.hide()
                except:
                    pass
                self.ui.mainWidget.hide()
                self.ui.widget2.hide()
                self.ui.widget.hide()
                self.ui.widget3.show()
            except:
                pass

    def changeEditAF(self):
        nameEdit = self.sender().objectName()  # передавалась ячейка ввода,
                                                # у которой название было "ij" в зависимости от позиции
        # получение расположения ячейки
        i = int(nameEdit[0])
        j = int(nameEdit[1])
        try:
            a = self.sender().text()
            a = float(a)
            self.mtrxA[i][j] = a  # добавление в матрицу А, введенного в ячейку числа
        except:
            pass

    def inputMatrixAF(self):
        self.ui.widget3.matrixA.wid.hide()  # скрываем виджет с матрицей
        self.ui.widget3.matrixA.wid.deleteLater()  # удаляем виджет с матрицей
        self.ui.widget3.matrixA.wid = QWidget(self.ui.widget3.matrixA)  # создаем новый виджет
        self.ui.widget3.matrixA.wid.setGeometry(5, 10, 280, 175)
        grid = QGridLayout(self.ui.widget3.matrixA.wid)  # макет нового виджета
        A1 = int(self.ui.widget3.dimension.spinBoxA1.value())  # считываем значение спинбоксов
        A2 = A1 + 1
        positions = [(i, j) for i in range(A1) for j in range(A2)]
        self.linesA = [[None for j in range(A2)] for i in range(A1)]  # матрица, в которой хранятся создаваемые ячейки
        self.mtrxA1 = []
        self.mtrxL1 = []
        try:
            self.mtrxA1 = self.mtrxA
            self.mtrxL1 = self.mtrxL
            self.mtrxR1 = self.mtrxR
        except Exception as e:
            pass
        self.mtrxA = [[0 for j in range(A2)] for i in range(A1)]  # матрица
        self.mtrxL = [[0 for j in range(A1)] for i in range(A1)]
        self.mtrxR = [[0 for j in range(A1)] for i in range(A1)]
        try:
            for i in range(len(self.mtrxA1)):
                for j in range(len(self.mtrxA1[0])):
                    self.mtrxA[i][j] = self.mtrxA1[i][j]

            for i in range(len(self.mtrxA1)):
                for j in range(len(self.mtrxA1)):
                    self.mtrxL[i][j] = self.mtrxL1[i][j]
                    self.mtrxR[i][j] = self.mtrxR1[i][j]
        except:
            try:
                for i in range(len(self.mtrxA)):
                    for j in range(len(self.mtrxA[0])):
                        self.mtrxA[i][j] = self.mtrxA1[i][j]
                for i in range(len(self.mtrxA)):
                    for j in range(len(self.mtrxA)):
                        self.mtrxL[i][j] = self.mtrxL1[i][j]
                        self.mtrxR[i][j] = self.mtrxR1[i][j]
            except Exception as e:
                pass
        for position in positions:
            (i, j) = position
            self.ui.widget3.matrixA.wid.line = QLineEdit(self.ui.widget3.matrixA.wid)  # создание ячейки
            self.linesA[i][j] = self.ui.widget3.matrixA.wid.line  # запоминаем созданную ячейку

            #  присваиваем имя созданной ячейки в формате Строка+столбец позиции
            self.ui.widget3.matrixA.wid.line.setObjectName(str(i) + str(j))
            nameFunc = self.linesA[i][j]
            self.ui.widget3.matrixA.wid.line.setText(str(self.mtrxA[i][j]))
            # на каждую созданную ячейку навешиваем событие "изменение"
            nameFunc.textChanged.connect(self.changeEditAF)

            grid.addWidget(self.ui.widget3.matrixA.wid.line, i, j)  # добавляем ячейку в макет
        self.ui.widget3.matrixA.wid.show()  # выводим матрицу из ячеек
        self.ui.widget3.matrixC.wid.hide()
        self.ui.widget3.matrixC.wid.deleteLater()
        self.ui.widget3.matrixC.wid = QWidget(self.ui.widget3.matrixC)  # создание нового виджета
        self.ui.widget3.matrixC.wid.setGeometry(5, 10, 90, 175)
        grid = QGridLayout(self.ui.widget3.matrixC.wid)
        for position in range(A2 - 1):
            self.ui.widget3.matrixC.wid.line = QLineEdit(self.ui.widget3.matrixC.wid)
            grid.addWidget(self.ui.widget3.matrixC.wid.line, position, 0)
            try:
                self.ui.widget3.matrixC.wid.line.setText(str(self.mtrxC[position]))
            except Exception as e:
                self.mtrxC = [0 for i in range(len(self.mtrxA[0]))]
                self.ui.widget3.matrixC.wid.line.setText(str(self.mtrxC[position]))
        self.ui.widget3.matrixC.wid.show()
        self.ui.widget3.matrixL.wid.hide()
        self.ui.widget3.matrixL.wid.deleteLater()
        self.ui.widget3.matrixL.wid = QWidget(self.ui.widget3.matrixL)
        self.ui.widget3.matrixL.wid.setGeometry(5, 10, 240, 185)
        grid = QGridLayout(self.ui.widget3.matrixL.wid)  # макет нового виджета
        A1 = int(self.ui.widget3.dimension.spinBoxA1.value())  # считываем значение спинбоксов
        A2 = A1 + 1
        self.linesL = [[None for j in range(A1)] for i in range(A1)]  # матрица, в которой хранятся создаваемые ячейки
        positions = [(i, j) for i in range(A1) for j in range(A1)]
        for position in positions:
            (i, j) = position
            self.ui.widget3.matrixL.wid.line = QLineEdit(self.ui.widget3.matrixL.wid)  # создание ячейки
            self.linesL[i][j] = self.ui.widget3.matrixL.wid.line  # запоминаем созданную ячейку

            #  присваиваем имя созданной ячейки в формате Строка+столбец позиции
            self.ui.widget3.matrixL.wid.line.setObjectName(str(i) + str(j))
            nameFunc = self.linesL[i][j]
            self.ui.widget3.matrixL.wid.line.setText(str(self.mtrxL[i][j]))
            # на каждую созданную ячейку навешиваем событие "изменение"
            # nameFunc.textChanged.connect(self.changeEditAG)
            grid.addWidget(self.ui.widget3.matrixL.wid.line, i, j)  # добавляем ячейку в макет
        self.ui.widget3.matrixL.wid.show()

        self.ui.widget3.matrixR.wid.hide()
        self.ui.widget3.matrixR.wid.deleteLater()
        self.ui.widget3.matrixR.wid = QWidget(self.ui.widget3.matrixR)
        self.ui.widget3.matrixR.wid.setGeometry(5, 10, 240, 185)
        grid = QGridLayout(self.ui.widget3.matrixR.wid)  # макет нового виджета
        A1 = int(self.ui.widget3.dimension.spinBoxA1.value())  # считываем значение спинбоксов
        A2 = A1 + 1
        self.linesR = [[None for j in range(A1)] for i in range(A1)]  # матрица, в которой хранятся создаваемые ячейки
        positions = [(i, j) for i in range(A1) for j in range(A1)]
        for position in positions:
            (i, j) = position
            self.ui.widget3.matrixR.wid.line = QLineEdit(self.ui.widget3.matrixR.wid)  # создание ячейки
            self.linesR[i][j] = self.ui.widget3.matrixR.wid.line  # запоминаем созданную ячейку

            #  присваиваем имя созданной ячейки в формате Строка+столбец позиции
            self.ui.widget3.matrixR.wid.line.setObjectName(str(i) + str(j))
            nameFunc = self.linesR[i][j]
            self.ui.widget3.matrixR.wid.line.setText(str(self.mtrxR[i][j]))
            # на каждую созданную ячейку навешиваем событие "изменение"
            # nameFunc.textChanged.connect(self.changeEditAG)
            grid.addWidget(self.ui.widget3.matrixR.wid.line, i, j)  # добавляем ячейку в макет
        self.ui.widget3.matrixR.wid.show()

    def resultMatrixCF(self, call=False):
        self.inputMatrixAF()
        self.mtrxC = []
        for i in range(len(self.mtrxA)):
            for j in range(len(self.mtrxA[0])):
                self.mtrxA[i][j] = float(self.mtrxA[i][j])
        mtrxa = []
        for i in range(len(self.mtrxA)):
            mtrxa.append([])
            for j in range(len(self.mtrxA[0])):
                mtrxa[i].append(self.mtrxA[i][j])
        try:
            if self.ui.widget3.options.v1.isChecked():
                self.mtrxL, self.mtrxR, self.mtrxC = factorV1(mtrxa)
            if self.ui.widget3.options.v2.isChecked():
                self.mtrxL, self.mtrxR, self.mtrxC = factorV2(mtrxa)
            if self.ui.widget3.options.v3.isChecked():
                self.mtrxL, self.mtrxR, self.mtrxC = factorV3(mtrxa)
            if self.ui.widget3.options.v4.isChecked():
                self.mtrxL, self.mtrxR, self.mtrxC = factorV4(mtrxa)
            if self.ui.widget3.options.v5.isChecked():
                self.mtrxL, self.mtrxR, self.mtrxC = factorV5(mtrxa)
            if self.ui.widget3.options.v6.isChecked():
                self.mtrxL, self.mtrxR, self.mtrxC = factorV6(mtrxa)
            if self.ui.widget3.options.v7.isChecked():
                self.mtrxL, self.mtrxR, self.mtrxC = factorV7(mtrxa)
            if self.ui.widget3.options.v8.isChecked():
                self.mtrxL, self.mtrxR, self.mtrxC = factorV8(mtrxa)
        except:
            if call == False:
                return QMessageBox.information(self, 'Zero deviding!', 'Zero deviding!', QMessageBox.Ok)
        self.ui.widget3.matrixC.wid.hide()
        self.ui.widget3.matrixC.wid.deleteLater()
        self.ui.widget3.matrixC.wid = QWidget(self.ui.widget3.matrixC)  # создание нового виджета
        self.ui.widget3.matrixC.wid.setGeometry(5, 10, 90, 175)
        grid = QGridLayout(self.ui.widget3.matrixC.wid)
        for position in range(len(self.mtrxC)):
            self.ui.widget3.matrixC.wid.line = QLineEdit(self.ui.widget3.matrixC.wid)
            [C] = self.mtrxC[position]
            self.ui.widget3.matrixC.wid.line.setText(str(C))
            grid.addWidget(self.ui.widget3.matrixC.wid.line, position, 0)
        self.ui.widget3.matrixC.wid.show()

        self.ui.widget3.matrixL.wid.hide()
        self.ui.widget3.matrixL.wid.deleteLater()
        self.ui.widget3.matrixL.wid = QWidget(self.ui.widget3.matrixL)
        self.ui.widget3.matrixL.wid.setGeometry(5, 10, 240, 185)
        grid = QGridLayout(self.ui.widget3.matrixL.wid)  # макет нового виджета
        A1 = int(self.ui.widget3.dimension.spinBoxA1.value())  # считываем значение спинбоксов
        A2 = A1 + 1
        self.linesL = [[None for j in range(A1)] for i in range(A1)]  # матрица, в которой хранятся создаваемые ячейки
        positions = [(i, j) for i in range(A1) for j in range(A1)]
        for position in positions:
            (i, j) = position
            self.ui.widget3.matrixL.wid.line = QLineEdit(self.ui.widget3.matrixL.wid)  # создание ячейки
            self.linesL[i][j] = self.ui.widget3.matrixL.wid.line  # запоминаем созданную ячейку

            #  присваиваем имя созданной ячейки в формате Строка+столбец позиции
            self.ui.widget3.matrixL.wid.line.setObjectName(str(i) + str(j))
            nameFunc = self.linesL[i][j]
            self.ui.widget3.matrixL.wid.line.setText(str(self.mtrxL[i][j]))
            # на каждую созданную ячейку навешиваем событие "изменение"
            # nameFunc.textChanged.connect(self.changeEditAG)
            grid.addWidget(self.ui.widget3.matrixL.wid.line, i, j)  # добавляем ячейку в макет
        self.ui.widget3.matrixL.wid.show()

        self.ui.widget3.matrixR.wid.hide()
        self.ui.widget3.matrixR.wid.deleteLater()
        self.ui.widget3.matrixR.wid = QWidget(self.ui.widget3.matrixR)
        self.ui.widget3.matrixR.wid.setGeometry(5, 10, 240, 185)
        grid = QGridLayout(self.ui.widget3.matrixR.wid)  # макет нового виджета
        A1 = int(self.ui.widget3.dimension.spinBoxA1.value())  # считываем значение спинбоксов
        A2 = A1 + 1
        self.linesR = [[None for j in range(A1)] for i in range(A1)]  # матрица, в которой хранятся создаваемые ячейки
        positions = [(i, j) for i in range(A1) for j in range(A1)]
        for position in positions:
            (i, j) = position
            self.ui.widget3.matrixR.wid.line = QLineEdit(self.ui.widget3.matrixR.wid)  # создание ячейки
            self.linesR[i][j] = self.ui.widget3.matrixR.wid.line  # запоминаем созданную ячейку

            #  присваиваем имя созданной ячейки в формате Строка+столбец позиции
            self.ui.widget3.matrixR.wid.line.setObjectName(str(i) + str(j))
            nameFunc = self.linesR[i][j]
            self.ui.widget3.matrixR.wid.line.setText(str(self.mtrxR[i][j]))
            # на каждую созданную ячейку навешиваем событие "изменение"
            # nameFunc.textChanged.connect(self.changeEditAG)
            grid.addWidget(self.ui.widget3.matrixR.wid.line, i, j)  # добавляем ячейку в макет
        self.ui.widget3.matrixR.wid.show()

    def printCF(self):
        self.ui.widget3.matrixC.wid.hide()
        self.ui.widget3.matrixC.wid.WinInputC.setPlainText('')
        strC = ""
        for i in range(len(self.result)):
            str2 = '{:.5f} '.format(float(self.result[i]))
            strC += str2
            self.ui.widget3.matrixC.wid.WinInputC.appendPlainText(strC)
            strC = ""
        self.ui.widget3.matrixC.wid.show()

        self.ui.widget3.matrixL.wid.hide()
        self.ui.widget3.matrixL.wid.WinInputL.setPlainText('')
        strC = ""
        for i in range(len(self.mtrxL)):
            for j in range(len(self.mtrxL)):
                str2 = '{:.5f} '.format(float(self.mtrxL[i][j]))
                strC += str2
            self.ui.widget3.matrixL.wid.WinInputL.appendPlainText(strC)
            strC = ""
        self.ui.widget3.matrixL.wid.show()

        self.ui.widget3.matrixR.wid.hide()
        self.ui.widget3.matrixR.wid.WinInputR.setPlainText('')
        strC = ""
        for i in range(len(self.mtrxR)):
            for j in range(len(self.mtrxR)):
                str2 = '{:.5f} '.format(float(self.mtrxR[i][j] + " "))
                strC += str2
            self.ui.widget3.matrixR.wid.WinInputR.appendPlainText(strC)
            strC = ""
        self.ui.widget3.matrixR.wid.show()

    def resultMatrixCCellF(self):
        strA = self.ui.widget3.matrixA.wid.WinInputA.toPlainText()  # считывание значений матрицы А
        # создание матрицы А
        b = strA.split('\n')
        c = []
        for i in b:
            if i == '':
                pass
            else:
                c += [i.split(' ')]
        self.mtrxACell = []
        for i in c:
            if len(i[0]) == 0:
                pass
            elif (i != ['']):
                s = []
                for p in i:
                    if p != '':
                        s += [p]
                self.mtrxACell += [s]

        # превращение элементов матриц А и В в числа
        for i in range(len(self.mtrxACell)):
            for j in range(len(self.mtrxACell[0])):
                self.mtrxACell[i][j] = float(self.mtrxACell[i][j])

        try:
            if self.ui.widget3.options.v1.isChecked():
                self.mtrxL, self.mtrxR, self.result = factorV1(self.mtrxACell)
            if self.ui.widget3.options.v2.isChecked():
                self.mtrxL, self.mtrxR, self.result = factorV2(self.mtrxACell)
            if self.ui.widget3.options.v3.isChecked():
                self.mtrxL, self.mtrxR, self.result = factorV3(self.mtrxACell)
            if self.ui.widget3.options.v4.isChecked():
                self.mtrxL, self.mtrxR, self.result = factorV4(self.mtrxACell)
            if self.ui.widget3.options.v5.isChecked():
                self.mtrxL, self.mtrxR, self.result = factorV5(self.mtrxACell)
            if self.ui.widget3.options.v6.isChecked():
                self.mtrxL, self.mtrxR, self.result = factorV6(self.mtrxACell)
            if self.ui.widget3.options.v7.isChecked():
                self.mtrxL, self.mtrxR, self.result = factorV7(self.mtrxACell)
            if self.ui.widget3.options.v8.isChecked():
                self.mtrxL, self.mtrxR, self.result = factorV8(self.mtrxACell)
        except Exception as e:
            return QMessageBox.information(self, 'Zero deviding!', 'Wrong SLAU!', QMessageBox.Ok)

        for i in range(len(self.result)):
            [C] = self.result[i]
            self.result[i] = str(C)

        for i in range(len(self.mtrxL)):
            for j in range(len(self.mtrxL)):
                self.mtrxL[i][j] = str(self.mtrxL[i][j])
        for i in range(len(self.mtrxR)):
            for j in range(len(self.mtrxR)):
                self.mtrxR[i][j] = str(self.mtrxR[i][j])

        self.printCF()

    def RadioBtnF(self):
        if self.ui.widget3.formInput.btnRadioBox.isChecked():
            self.ui.widget3.dimension.hide()

            # изменение ввода матрицы A
            self.ui.widget3.matrixA.wid.hide()  # скрываем виджет с матрицей
            self.ui.widget3.matrixA.wid.deleteLater()  # удаляем виджет с матрицей
            self.ui.widget3.matrixA.wid = QWidget(self.ui.widget3.matrixA)  # создаем новый виджет
            self.ui.widget3.matrixA.wid.setGeometry(5, 10, 280, 175)
            grid = QGridLayout(self.ui.widget3.matrixA.wid)
            self.ui.widget3.matrixA.wid.WinInputA = QPlainTextEdit(self.ui.widget3.matrixA.wid)
            # self.ui.mainWidget.matrixA.wid.WinInput.setPlainText("85469")
            grid.addWidget(self.ui.widget3.matrixA.wid.WinInputA)
            try:
                self.ui.widget3.matrixA.wid.WinInputA.setPlainText(self.textmatrix)
            except Exception as e:
                pass
            self.ui.widget3.matrixA.wid.show()

            self.ui.widget3.pushButton.hide()
            self.ui.widget3.btnResult2.show()

            self.ui.widget3.matrixC.wid.hide()
            self.ui.widget3.matrixC.wid.deleteLater()
            self.ui.widget3.matrixC.wid = QWidget(self.ui.widget3.matrixC)
            self.ui.widget3.matrixC.wid.setGeometry(5, 10, 90, 175)
            grid = QGridLayout(self.ui.widget3.matrixC.wid)
            self.ui.widget3.matrixC.wid.WinInputC = QPlainTextEdit(self.ui.widget3.matrixC.wid)
            grid.addWidget(self.ui.widget3.matrixC.wid.WinInputC)
            try:
                self.ui.widget3.matrixC.wid.WinInputC.setPlainText(self.textmatrixc)
            except Exception as e:
                pass
            self.ui.widget3.matrixC.wid.show()

            self.ui.widget3.matrixL.wid.hide()
            self.ui.widget3.matrixL.wid.deleteLater()
            self.ui.widget3.matrixL.wid = QWidget(self.ui.widget3.matrixL)
            self.ui.widget3.matrixL.wid.setGeometry(5, 10, 240, 185)
            grid = QGridLayout(self.ui.widget3.matrixL.wid)
            self.ui.widget3.matrixL.wid.WinInputL = QPlainTextEdit(self.ui.widget3.matrixL.wid)
            grid.addWidget(self.ui.widget3.matrixL.wid.WinInputL)
            try:
                self.ui.widget3.matrixL.wid.WinInputL.setPlainText(self.textmatrixl)
            except Exception as e:
                pass
            self.ui.widget3.matrixL.wid.show()

            self.ui.widget3.matrixR.wid.hide()
            self.ui.widget3.matrixR.wid.deleteLater()
            self.ui.widget3.matrixR.wid = QWidget(self.ui.widget3.matrixR)
            self.ui.widget3.matrixR.wid.setGeometry(5, 10, 240, 185)
            grid = QGridLayout(self.ui.widget3.matrixR.wid)
            self.ui.widget3.matrixR.wid.WinInputR = QPlainTextEdit(self.ui.widget3.matrixR.wid)
            grid.addWidget(self.ui.widget3.matrixR.wid.WinInputR)
            try:
                self.ui.widget3.matrixR.wid.WinInputR.setPlainText(self.textmatrixr)
            except Exception as e:
                pass
            self.ui.widget3.matrixR.wid.show()

        if self.ui.widget3.formInput.btnRadioCell.isChecked():
            try:
                self.textmatrix = self.ui.widget3.matrixA.wid.WinInputA.toPlainText()
                self.textmatrixr = self.ui.widget3.matrixR.wid.WinInputR.toPlainText()
                self.textmatrixl = self.ui.widget3.matrixL.wid.WinInputL.toPlainText()
                self.textmatrixc = self.ui.widget3.matrixC.wid.WinInputC.toPlainText()
            except Exception as e:
                pass

            self.ui.widget3.matrixA.wid.hide()
            # self.ui.widget.matrixB.wid.hide()
            self.ui.widget3.matrixC.wid.hide()
            self.ui.widget3.matrixL.wid.hide()
            self.ui.widget3.matrixR.wid.hide()
            self.inputMatrixAF()  # выводим матрицу из ячеек
            # try:
            #    self.resultMatrixCG(call = True)
            # except:
            #    pass
            self.ui.widget3.dimension.show()
            self.ui.widget3.btnResult2.hide()
            self.ui.widget3.pushButton.show()

    def changeEditAt(self):
        nameEdit = self.sender().objectName()  # передавалась ячейка ввода,
        # у которой название было "ij" в зависимости от позиции
        # получение расположения ячейки
        i = int(nameEdit[0])
        j = int(nameEdit[1])
        self.mtrxAt[i][j] = self.sender().text()  # добавление в матрицу А, введенного в ячейку числа

    def inputMatrixAt(self):
        self.ui.widget2.matrixA.wid.hide()  # скрываем виджет с матрицей
        self.ui.widget2.matrixA.wid.deleteLater()  # удаляем виджет с матрицей
        self.ui.widget2.matrixA.wid = QWidget(self.ui.widget2.matrixA)  # создаем новый виджет
        self.ui.widget2.matrixA.wid.setGeometry(5, 10, 250, 285)
        grid = QGridLayout(self.ui.widget2.matrixA.wid)  # макет нового виджета
        A1 = int(self.ui.widget2.dimension.spinBoxA1.value())  # считываем значение спинбоксов
        A2 = int(self.ui.widget2.dimension.spinBoxA2.value())
        # print(A1, A2)
        positions = [(i, j) for i in range(A1) for j in range(A2)]
        # print(positions)
        self.linesAt = [[None for j in range(A2)] for i in range(A1)]  # матрица, в которой хранятся создаваемые ячейки
        # self.mtrxAt = [[0 for j in range(A2)] for i in range(A1)]  # матрица

        self.mtrxA1 = []
        try:
            self.mtrxA1 = self.mtrxAt
        except Exception as e:
            pass
        self.mtrxAt = [[0 for j in range(A2)] for i in range(A1)]  # матрица
        try:
            for i in range(len(self.mtrxA1)):
                for j in range(len(self.mtrxA1[0])):
                    self.mtrxA[i][j] = self.mtrxA1[i][j]
        except:
            try:
                for i in range(len(self.mtrxAt)):
                    for j in range(len(self.mtrxAt[0])):
                        self.mtrxAt[i][j] = self.mtrxA1[i][j]
            except Exception as e:
                print(e)

        for position in positions:
            (i, j) = position
            self.ui.widget2.matrixA.wid.line = QLineEdit(self.ui.widget2.matrixA.wid)  # создание ячейки
            self.linesAt[i][j] = self.ui.widget2.matrixA.wid.line  # запоминаем созданную ячейку

            #  присваиваем имя созданной ячейки в формате Строка+столбец позиции
            self.ui.widget2.matrixA.wid.line.setObjectName(str(i) + str(j))
            nameFunc = self.linesAt[i][j]
            # на каждую созданную ячейку навешиваем событие "изменение"
            nameFunc.textChanged.connect(self.changeEditAt)
            grid.addWidget(self.ui.widget2.matrixA.wid.line, i, j)  # добавляем ячейку в макет
        # print(self.linesAt)
        # print(self.mtrxAt)
        # print(self.mtrxCt)
        self.ui.widget2.matrixA.wid.show()  # выводим матрицу из ячеек

    def resultMatrixCCellt(self):
        for i in range(len(self.mtrxAt)):
            for j in range(len(self.mtrxAt[0])):
                self.mtrxAt[i][j] = float(self.mtrxAt[i][j])
        # print(self.mtrxAt)
        self.mtrxCt = trans(self.mtrxAt)
        try:
            self.ui.widget2.matrixC.wid.hide()  # сокрытие виджета с матрицей ввода
            self.ui.widget2.matrixC.wid.deleteLater()  # удаление виджета с матрицей ввода
        except:
            pass
        self.ui.widget2.matrixC.wid = QWidget(self.ui.widget2.matrixC)  # создание нового виджета
        self.ui.widget2.matrixC.wid.setGeometry(5, 10, 250, 285)
        grid = QGridLayout(self.ui.widget2.matrixC.wid)  # добавление макета в новый виджет
        # вычисление размерности матрицы С
        C1 = int(len(self.mtrxAt))
        C2 = int(len(self.mtrxAt[0]))
        positions = [(i, j) for i in range(C2) for j in range(C1)]
        # self.linesC = [[None for j in range(C2)] for i in range(C1)]
        for position in positions:
            (i, j) = position
            self.ui.widget2.matrixC.wid.line = QLineEdit(self.ui.widget2.matrixC.wid)  # создание ячеек вывода
            self.ui.widget2.matrixC.wid.line.setText(str(self.mtrxCt[i][j]))  # заполнение созданных ячеек
            grid.addWidget(self.ui.widget2.matrixC.wid.line, i, j)  # расположение созданных ячеек
        self.ui.widget2.matrixC.wid.show()  # показ матрицы С

    def printCt(self):
        # self.ui.widget2.matrixC.wid.hide()
        # self.ui.widget2.matrixC.wid.WinInputC.setPlainText('')
        strC = ""
        for i in range(len(self.result)):
            for j in range(len(self.result[0])):
                str2 = '{:.5f} '.format(float(self.result[i][j]))
                strC += str2
            self.ui.widget2.matrixC.wid.WinInputC.appendPlainText(strC)
            strC = ""

    def resultMatrixCt(self):
        strA = self.ui.widget2.matrixA.wid.WinInputA.toPlainText()  # считывание значений матрицы А
        # создание матрицы А
        b = strA.split('\n')
        c = []
        for i in b:
            if i == '':
                pass
            else:
                c += [i.split(' ')]
        self.mtrxACellt = []
        # print(self.mtrxACell)
        for i in c:
            if len(i[0]) == 0:
                pass
            elif (i != ['']):
                s = []
                for p in i:
                    if p != '':
                        s += [p]
                self.mtrxACellt += [s]

        # strB = self.ui.mainWidget.matrixB.wid.WinInputB.toPlainText()
        # b = strB.split('\n')
        # c = []
        # for i in b:
        #     if i == '':
        #         pass
        #     else:
        #         c += [i.split(' ')]
        # self.mtrxBCell = []
        # for i in c:
        #     if len(i[0]) == 0:
        #         pass
        #     elif (i != ['']):
        #         s = []
        #         for p in i:
        #             if p != '':
        #                 s += [p]
        #         self.mtrxBCell += [s]

        # превращение элементов матриц А и В в числа
        for i in range(len(self.mtrxACellt)):
            for j in range(len(self.mtrxACellt[0])):
                self.mtrxACellt[i][j] = float(self.mtrxACellt[i][j])

        self.result = trans(self.mtrxACellt)

        for i in range(len(self.result)):
            for j in range(len(self.result[0])):
                self.result[i][j] = str(self.result[i][j])

        # print(self.result)
        self.printCt()

    def RadioBtnt(self):
        if self.ui.widget2.formInput.btnRadioBox.isChecked():
            self.ui.widget2.dimension.hide()

            # изменение ввода матрицы A
            self.ui.widget2.matrixA.wid.hide()  # скрываем виджет с матрицей
            self.ui.widget2.matrixA.wid.deleteLater()  # удаляем виджет с матрицей
            self.ui.widget2.matrixA.wid = QWidget(self.ui.widget2.matrixA)  # создаем новый виджет
            self.ui.widget2.matrixA.wid.setGeometry(5, 10, 250, 285)
            grid = QGridLayout(self.ui.widget2.matrixA.wid)
            self.ui.widget2.matrixA.wid.WinInputA = QPlainTextEdit(self.ui.widget2.matrixA.wid)
            # self.ui.mainWidget.matrixA.wid.WinInput.setPlainText("85469")
            grid.addWidget(self.ui.widget2.matrixA.wid.WinInputA)
            self.ui.widget2.matrixA.wid.show()

            self.ui.widget2.pushButton.hide()
            self.ui.widget2.btnResult2.show()

            self.ui.widget2.matrixC.wid.hide()
            self.ui.widget2.matrixC.wid.deleteLater()
            self.ui.widget2.matrixC.wid = QWidget(self.ui.widget2.matrixC)
            self.ui.widget2.matrixC.wid.setGeometry(5, 10, 250, 285)
            grid = QGridLayout(self.ui.widget2.matrixC.wid)
            self.ui.widget2.matrixC.wid.WinInputC = QPlainTextEdit(self.ui.widget2.matrixC.wid)
            grid.addWidget(self.ui.widget2.matrixC.wid.WinInputC)
            self.ui.widget2.matrixC.wid.show()

        if self.ui.widget2.formInput.btnRadioCell.isChecked():
            self.ui.widget2.matrixA.wid.hide()
            # self.ui.widget2.matrixB.wid.hide()
            self.ui.widget2.matrixC.wid.hide()
            self.ui.widget2.dimension.show()

            self.ui.widget2.btnResult2.hide()
            self.ui.widget2.pushButton.show()

    # функция для вычисления результирующей матрисы С
    def resultMatrixC(self):
        # преобразование элементов введенных матриц А и В в значения Int
        for i in range(len(self.mtrxA)):
            for j in range(len(self.mtrxA[0])):
                self.mtrxA[i][j] = float(self.mtrxA[i][j])
        for i in range(len(self.mtrxB)):
            for j in range(len(self.mtrxB[0])):
                self.mtrxB[i][j] = float(self.mtrxB[i][j])

        # перемножение матриц
        # дописать изменние вывода C, если значения int
        # mply импортирована из другого файла
        self.mtrxC = mply(self.mtrxA, self.mtrxB)
        try:
            self.ui.mainWidget.matrixC.wid.hide()  # сокрытие виджета с матрицей ввода
            self.ui.mainWidget.matrixC.wid.deleteLater()  # удаление виджета с матрицей ввода
        except:
            pass
        self.ui.mainWidget.matrixC.wid = QWidget(self.ui.mainWidget.matrixC)  # создание нового виджета
        self.ui.mainWidget.matrixC.wid.setGeometry(5, 10, 251, 176)
        grid = QGridLayout(self.ui.mainWidget.matrixC.wid)  # добавление макета в новый виджет
        # вычисление размерности матрицы С
        C1 = int(len(self.mtrxA))
        C2 = int(len(self.mtrxB[0]))
        positions = [(i, j) for i in range(C1) for j in range(C2)]
        # self.linesC = [[None for j in range(C2)] for i in range(C1)]
        for position in positions:
            (i, j) = position
            self.ui.mainWidget.matrixC.wid.line = QLineEdit(self.ui.mainWidget.matrixC.wid)  # создание ячеек вывода
            self.ui.mainWidget.matrixC.wid.line.setText(str(self.mtrxC[i][j]))  # заполнение созданных ячеек
            grid.addWidget(self.ui.mainWidget.matrixC.wid.line, i, j)  # расположение созданных ячеек
        self.ui.mainWidget.matrixC.wid.show()  # показ матрицы С

    # функция для записи ввода в матрицу а
    def changeEditAG(self):
        nameEdit = self.sender().objectName()  # передавалась ячейка ввода,
                                                # у которой название было "ij" в зависимости от позиции
        # получение расположения ячейки
        i = int(nameEdit[0])
        j = int(nameEdit[1])
        try:
            a = self.sender().text()
            a = float(a)
            self.mtrxA[i][j] = a  # добавление в матрицу А, введенного в ячейку числа
        except:
            pass
        #self.linesA[i][j].setFocus()

    def inputMatrixAG(self):
        self.ui.widget.matrixA.wid.hide()  # скрываем виджет с матрицей
        self.ui.widget.matrixA.wid.deleteLater()  # удаляем виджет с матрицей
        self.ui.widget.matrixA.wid = QWidget(self.ui.widget.matrixA)  # создаем новый виджет
        self.ui.widget.matrixA.wid.setGeometry(5, 10, 431, 336)
        grid = QGridLayout(self.ui.widget.matrixA.wid)  # макет нового виджета
        A1 = int(self.ui.widget.dimension.spinBoxA1.value())  # считываем значение спинбоксов
        A2 = A1 + 1
        positions = [(i, j) for i in range(A1) for j in range(A2)]
        self.linesA = [[None for j in range(A2)] for i in range(A1)]  # матрица, в которой хранятся создаваемые ячейки
        self.mtrxA1 = []
        try:
            self.mtrxA1 = self.mtrxA
        except Exception as e:
            pass
        self.mtrxA = [[0 for j in range(A2)] for i in range(A1)]  # матрица
        try:
            for i in range(len(self.mtrxA1)):
                for j in range(len(self.mtrxA1[0])):
                    self.mtrxA[i][j] = self.mtrxA1[i][j]
        except:
            try:
                for i in range(len(self.mtrxA)):
                    for j in range(len(self.mtrxA[0])):
                        self.mtrxA[i][j] = self.mtrxA1[i][j]
            except Exception as e:
                print(e)
        for position in positions:
            (i, j) = position
            self.ui.widget.matrixA.wid.line = QLineEdit(self.ui.widget.matrixA.wid)  # создание ячейки
            self.linesA[i][j] = self.ui.widget.matrixA.wid.line  # запоминаем созданную ячейку

            #  присваиваем имя созданной ячейки в формате Строка+столбец позиции
            self.ui.widget.matrixA.wid.line.setObjectName(str(i) + str(j))
            nameFunc = self.linesA[i][j]
            self.ui.widget.matrixA.wid.line.setText(str(self.mtrxA[i][j]))
            # на каждую созданную ячейку навешиваем событие "изменение"
            nameFunc.textChanged.connect(self.changeEditAG)
            grid.addWidget(self.ui.widget.matrixA.wid.line, i, j)  # добавляем ячейку в макет
        self.ui.widget.matrixA.wid.show()  # выводим матрицу из ячеек
        self.ui.widget.matrixC.wid.hide()
        self.ui.widget.matrixC.wid.deleteLater()
        self.ui.widget.matrixC.wid = QWidget(self.ui.widget.matrixC)  # создание нового виджета
        self.ui.widget.matrixC.wid.setGeometry(5, 10, 70, 304)
        grid = QGridLayout(self.ui.widget.matrixC.wid)
        for position in range(A2 - 1):
            self.ui.widget.matrixC.wid.line = QLineEdit(self.ui.widget.matrixC.wid)
            grid.addWidget(self.ui.widget.matrixC.wid.line, position, 0)
            try:
                self.ui.widget.matrixC.wid.line.setText(str(self.mtrxC[position]))
            except Exception as e:
                self.mtrxC = [0 for i in range(len(self.mtrxA[0]))]
                self.ui.widget.matrixC.wid.line.setText(str(self.mtrxC[position]))
        self.ui.widget.matrixC.wid.show()

    def resultMatrixCG(self, call = False):
        self.inputMatrixAG()
        self.mtrxC = []
        for i in range(len(self.mtrxA)):
            for j in range(len(self.mtrxA[0])):
                self.mtrxA[i][j] = float(self.mtrxA[i][j])
        mtrxa=[]
        for i in range(len(self.mtrxA)):
            mtrxa.append([])
            for j in range(len(self.mtrxA[0])):
                mtrxa[i].append(self.mtrxA[i][j])
        try:
            self.mtrxC = gauss(mtrxa)
        except:
            if call == False:
                return QMessageBox.information(self, 'Zero deviding!', 'Zero deviding!', QMessageBox.Ok)
        self.ui.widget.matrixC.wid.hide()
        self.ui.widget.matrixC.wid.deleteLater()
        self.ui.widget.matrixC.wid = QWidget(self.ui.widget.matrixC)  # создание нового виджета
        self.ui.widget.matrixC.wid.setGeometry(3, 5, 71, 311)
        grid = QGridLayout(self.ui.widget.matrixC.wid)
        for position in range(len(self.mtrxC)):
            self.ui.widget.matrixC.wid.line = QLineEdit(self.ui.widget.matrixC.wid)
            self.ui.widget.matrixC.wid.line.setText(str(self.mtrxC[position]))
            grid.addWidget(self.ui.widget.matrixC.wid.line, position, 0)
        self.ui.widget.matrixC.wid.show()


    def changeEditA(self):
        nameEdit = self.sender().objectName()  # передавалась ячейка ввода,
                                               # у которой название было "ij" в зависимости от позиции
        # получение расположения ячейки
        i = int(nameEdit[0])
        j = int(nameEdit[1])
        self.mtrxA[i][j] = self.sender().text()  # добавление в матрицу А, введенного в ячейку числа

    def inputMatrixA(self):
        self.ui.mainWidget.matrixA.wid.hide()  # скрываем виджет с матрицей
        self.ui.mainWidget.matrixA.wid.deleteLater()  # удаляем виджет с матрицей
        self.ui.mainWidget.matrixA.wid = QWidget(self.ui.mainWidget.matrixA)  # создаем новый виджет
        self.ui.mainWidget.matrixA.wid.setGeometry(5, 10, 251, 156)
        grid = QGridLayout(self.ui.mainWidget.matrixA.wid)  # макет нового виджета
        A1 = int(self.ui.mainWidget.dimension.spinBoxA1.value())  # считываем значение спинбоксов
        A2 = int(self.ui.mainWidget.dimension.spinBoxA2.value())
        positions = [(i, j) for i in range(A1) for j in range(A2)]
        self.linesA = [[None for j in range(A2)] for i in range(A1)]  # матрица, в которой хранятся создаваемые ячейки
        # self.mtrxA = [[0 for j in range(A2)] for i in range(A1)]  # матрица

        self.mtrxA1 = []
        try:
            self.mtrxA1 = self.mtrxA
        except Exception as e:
            pass
        self.mtrxA = [[0 for j in range(A2)] for i in range(A1)]  # матрица
        try:
            for i in range(len(self.mtrxA1)):
                for j in range(len(self.mtrxA1[0])):
                    self.mtrxA[i][j] = self.mtrxA1[i][j]
        except:
            try:
                for i in range(len(self.mtrxA)):
                    for j in range(len(self.mtrxA[0])):
                        self.mtrxA[i][j] = self.mtrxA1[i][j]
            except Exception as e:
                print(e)

        for position in positions:
            (i, j) = position
            self.ui.mainWidget.matrixA.wid.line = QLineEdit(self.ui.mainWidget.matrixA.wid)  # создание ячейки
            self.linesA[i][j] = self.ui.mainWidget.matrixA.wid.line  # запоминаем созданную ячейку

            #  присваиваем имя созданной ячейки в формате Строка+столбец позиции
            self.ui.mainWidget.matrixA.wid.line.setObjectName(str(i) + str(j))
            nameFunc = self.linesA[i][j]
            # на каждую созданную ячейку навешиваем событие "изменение"
            nameFunc.textChanged.connect(self.changeEditA)
            grid.addWidget(self.ui.mainWidget.matrixA.wid.line, i, j)  # добавляем ячейку в макет
        self.ui.mainWidget.matrixA.wid.show()  # выводим матрицу из ячеек

    # аналогично функциям для матрицы А
    def changeEditB(self):
        nameEdit = self.sender().objectName()
        i = int(nameEdit[0])
        j = int(nameEdit[1])
        self.mtrxB[i][j] = self.sender().text()

    def inputMatrixB(self):
        self.ui.mainWidget.matrixB.wid.hide()
        self.ui.mainWidget.matrixB.wid.deleteLater()
        self.ui.mainWidget.matrixB.wid = QWidget(self.ui.mainWidget.matrixB)
        self.ui.mainWidget.matrixB.wid.setGeometry(5, 10, 251, 156)
        grid = QGridLayout(self.ui.mainWidget.matrixB.wid)
        B1 = int(self.ui.mainWidget.dimension.spinBoxB1.value())
        B2 = int(self.ui.mainWidget.dimension.spinBoxB2.value())
        positions = [(i, j) for i in range(B1) for j in range(B2)]
        self.linesB = [[None for j in range(B2)] for i in range(B1)]
        # self.mtrxB = [[0 for j in range(B2)] for i in range(B1)]
        self.mtrxB1 = []
        try:
            self.mtrxB1 = self.mtrxB
        except Exception as e:
            pass
        self.mtrxB = [[0 for j in range(B2)] for i in range(B1)]  # матрица
        try:
            for i in range(len(self.mtrxB1)):
                for j in range(len(self.mtrxB1[0])):
                    self.mtrxA[i][j] = self.mtrxB1[i][j]
        except:
            try:
                for i in range(len(self.mtrxB)):
                    for j in range(len(self.mtrxB[0])):
                        self.mtrxA[i][j] = self.mtrxB1[i][j]
            except Exception as e:
                print(e)
        for position in positions:
            (i, j) = position
            self.ui.mainWidget.matrixB.wid.line = QLineEdit(self.ui.mainWidget.matrixB.wid)
            self.linesB[i][j] = self.ui.mainWidget.matrixB.wid.line
            # self.ui.mainWidget.matrixA.wid.line.setText("0")
            self.ui.mainWidget.matrixB.wid.line.setObjectName(str(i) + str(j))
            nameFunc = self.linesB[i][j]
            nameFunc.textChanged.connect(self.changeEditB)
            grid.addWidget(self.ui.mainWidget.matrixB.wid.line, i, j)
        self.ui.mainWidget.matrixB.wid.show()



    # Функция для вывода матрицы С, при выборе радио кнопки "окно"
    def printC(self):
        strC = ""
        for i in range(len(self.result)):
            for j in range(len(self.result[0])):
                str2 = '{:.5f} '.format(float(self.result[i][j]))
                strC += str2
            self.ui.mainWidget.matrixC.wid.WinInputC.appendPlainText(strC)
            strC = ""

    def printCG(self):
        self.ui.widget.matrixC.wid.hide()
        self.ui.widget.matrixC.wid.WinInputC.setPlainText('')
        strC = ""
        for i in range(len(self.result)):
            str2 = '{:.5f} '.format(float(self.result[i]))
            strC += str2
            self.ui.widget.matrixC.wid.WinInputC.appendPlainText(strC)
            strC = ""
        self.ui.widget.matrixC.wid.show()

    # Вычисление матрицы С, при выборе радио кнопки "окно"
    def resultMatrixCCell(self):
        strA = self.ui.mainWidget.matrixA.wid.WinInputA.toPlainText()  # считывание значений матрицы А
        # создание матрицы А
        b = strA.split('\n')
        c = []
        for i in b:
            if i == '':
                pass
            else:
                c += [i.split(' ')]
        self.mtrxACell = []
        for i in c:
            if len(i[0]) == 0:
                pass
            elif (i != ['']):
                s = []
                for p in i:
                    if p != '':
                        s += [p]
                self.mtrxACell += [s]

        strB = self.ui.mainWidget.matrixB.wid.WinInputB.toPlainText()
        b = strB.split('\n')
        c = []
        for i in b:
            if i == '':
                pass
            else:
                c += [i.split(' ')]
        self.mtrxBCell = []
        for i in c:
            if len(i[0]) == 0:
                pass
            elif (i != ['']):
                s = []
                for p in i:
                    if p != '':
                        s += [p]
                self.mtrxBCell += [s]

        # превращение элементов матриц А и В в числа
        for i in range(len(self.mtrxACell)):
            for j in range(len(self.mtrxACell[0])):
                self.mtrxACell[i][j] = float(self.mtrxACell[i][j])

        for i in range(len(self.mtrxBCell)):
            for j in range(len(self.mtrxBCell[0])):
                self.mtrxBCell[i][j] = float(self.mtrxBCell[i][j])

        self.result = mply(self.mtrxACell, self.mtrxBCell)

        for i in range(len(self.result)):
            for j in range(len(self.result[0])):
                self.result[i][j] = str(self.result[i][j])

        self.printC()

    def resultMatrixCCellG(self):
        strA = self.ui.widget.matrixA.wid.WinInputA.toPlainText()  # считывание значений матрицы А
        # создание матрицы А
        b = strA.split('\n')
        c = []
        for i in b:
            if i == '':
                pass
            else:
                c += [i.split(' ')]
        self.mtrxACell = []
        for i in c:
            if len(i[0]) == 0:
                pass
            elif (i != ['']):
                s = []
                for p in i:
                    if p != '':
                        s += [p]
                self.mtrxACell += [s]


        # превращение элементов матриц А и В в числа
        for i in range(len(self.mtrxACell)):
            for j in range(len(self.mtrxACell[0])):
                self.mtrxACell[i][j] = float(self.mtrxACell[i][j])

        self.result = gauss(self.mtrxACell)
        if self.result == 'zero!':
            return QMessageBox.information(self, 'Zero deviding!', 'Wrong SLAU!', QMessageBox.Ok)

        for i in range(len(self.result)):
            #for j in range(len(self.result[0])):
            self.result[i] = str(self.result[i])

        self.printCG()


    def RadioBtn(self):
        if self.ui.mainWidget.formInput.btnRadioBox.isChecked():
            self.ui.mainWidget.dimension.hide()

            # изменение ввода матрицы A
            self.ui.mainWidget.matrixA.wid.hide()  # скрываем виджет с матрицей
            self.ui.mainWidget.matrixA.wid.deleteLater()  # удаляем виджет с матрицей
            self.ui.mainWidget.matrixA.wid = QWidget(self.ui.mainWidget.matrixA)  # создаем новый виджет
            self.ui.mainWidget.matrixA.wid.setGeometry(5, 10, 251, 156)
            grid = QGridLayout(self.ui.mainWidget.matrixA.wid)
            self.ui.mainWidget.matrixA.wid.WinInputA = QPlainTextEdit(self.ui.mainWidget.matrixA.wid)
            # self.ui.mainWidget.matrixA.wid.WinInput.setPlainText("85469")
            grid.addWidget(self.ui.mainWidget.matrixA.wid.WinInputA)
            self.ui.mainWidget.matrixA.wid.show()

            # изменение ввода матрицы В
            self.ui.mainWidget.matrixB.wid.hide()
            self.ui.mainWidget.matrixB.wid.deleteLater()
            self.ui.mainWidget.matrixB.wid = QWidget(self.ui.mainWidget.matrixB)
            self.ui.mainWidget.matrixB.wid.setGeometry(5, 10, 251, 156)
            grid = QGridLayout(self.ui.mainWidget.matrixB.wid)
            self.ui.mainWidget.matrixB.wid.WinInputB = QPlainTextEdit(self.ui.mainWidget.matrixB.wid)
            grid.addWidget(self.ui.mainWidget.matrixB.wid.WinInputB)
            self.ui.mainWidget.matrixB.wid.show()

            self.ui.mainWidget.btnResult.hide()
            self.ui.mainWidget.btnResult2.show()

            self.ui.mainWidget.matrixC.wid.hide()
            self.ui.mainWidget.matrixC.wid.deleteLater()
            self.ui.mainWidget.matrixC.wid = QWidget(self.ui.mainWidget.matrixC)
            self.ui.mainWidget.matrixC.wid.setGeometry(5, 10, 251, 176)
            grid = QGridLayout(self.ui.mainWidget.matrixC.wid)
            self.ui.mainWidget.matrixC.wid.WinInputC = QPlainTextEdit(self.ui.mainWidget.matrixC.wid)
            grid.addWidget(self.ui.mainWidget.matrixC.wid.WinInputC)
            self.ui.mainWidget.matrixC.wid.show()


        if self.ui.mainWidget.formInput.btnRadioCell.isChecked():
            self.ui.mainWidget.matrixA.wid.hide()
            self.ui.mainWidget.matrixB.wid.hide()
            self.ui.mainWidget.matrixC.wid.hide()
            self.ui.mainWidget.dimension.show()
            self.ui.mainWidget.btnResult2.hide()
            self.ui.mainWidget.btnResult.show()

    def RadioBtnG(self):
        if self.ui.widget.formInput.btnRadioBox.isChecked():
            self.ui.widget.dimension.hide()

            # изменение ввода матрицы A
            self.ui.widget.matrixA.wid.hide()  # скрываем виджет с матрицей
            self.ui.widget.matrixA.wid.deleteLater()  # удаляем виджет с матрицей
            self.ui.widget.matrixA.wid = QWidget(self.ui.widget.matrixA)  # создаем новый виджет
            self.ui.widget.matrixA.wid.setGeometry(5, 10, 431, 336)
            grid = QGridLayout(self.ui.widget.matrixA.wid)
            self.ui.widget.matrixA.wid.WinInputA = QPlainTextEdit(self.ui.widget.matrixA.wid)
            # self.ui.mainWidget.matrixA.wid.WinInput.setPlainText("85469")
            grid.addWidget(self.ui.widget.matrixA.wid.WinInputA)
            try:
                self.ui.widget.matrixA.wid.WinInputA.setPlainText(self.textmatrix)
            except Exception as e:
                pass
            self.ui.widget.matrixA.wid.show()

            self.ui.widget.pushButton.hide()
            self.ui.widget.btnResult2.show()

            self.ui.widget.matrixC.wid.hide()
            self.ui.widget.matrixC.wid.deleteLater()
            self.ui.widget.matrixC.wid = QWidget(self.ui.widget.matrixC)
            self.ui.widget.matrixC.wid.setGeometry(5, 10, 70, 304)
            grid = QGridLayout(self.ui.widget.matrixC.wid)
            self.ui.widget.matrixC.wid.WinInputC = QPlainTextEdit(self.ui.widget.matrixC.wid)
            grid.addWidget(self.ui.widget.matrixC.wid.WinInputC)
            try:
                self.ui.widget.matrixC.wid.WinInputC.setPlainText(self.textmatrixc)
            except Exception as e:
                pass
            self.ui.widget.matrixC.wid.show()


        if self.ui.widget.formInput.btnRadioCell.isChecked():
            try:
                self.textmatrix = self.ui.widget.matrixA.wid.WinInputA.toPlainText()
                self.textmatrixc = self.ui.widget.matrixC.wid.WinInputC.toPlainText()
            except Exception as e:
                pass

            self.ui.widget.matrixA.wid.hide()
            #self.ui.widget.matrixB.wid.hide()
            self.ui.widget.matrixC.wid.hide()
            self.inputMatrixAG()  # выводим матрицу из ячеек
            #try:
            #    self.resultMatrixCG(call = True)
            #except:
            #    pass
            self.ui.widget.dimension.show()
            self.ui.widget.btnResult2.hide()
            self.ui.widget.pushButton.show()


    def downld(self):
        # навешиваем события на "изменение" спинбоксов
        self.ui.list.clicked.connect(self.choose)
        self.ui.mainWidget.dimension.spinBoxA1.valueChanged.connect(self.inputMatrixA)
        self.ui.mainWidget.dimension.spinBoxA2.valueChanged.connect(self.inputMatrixA)
        self.ui.mainWidget.dimension.spinBoxB1.valueChanged.connect(self.inputMatrixB)
        self.ui.mainWidget.dimension.spinBoxB2.valueChanged.connect(self.inputMatrixB)
        self.ui.widget.dimension.spinBoxA1.valueChanged.connect(self.inputMatrixAG)
        self.ui.widget.dimension.spinBoxA2.valueChanged.connect(self.inputMatrixAG)
        # навешиваем изменение на щелчок по кнопке "решить"
        self.ui.mainWidget.btnResult.clicked.connect(self.resultMatrixC)
        self.ui.widget.pushButton.clicked.connect(self.resultMatrixCG)
        # переход при выборе "окна"
        # все кнопки обязательно объединить в группу
        self.ui.mainWidget.formInput.group.buttonClicked.connect(self.RadioBtn)
        self.ui.mainWidget.btnResult2.clicked.connect(self.resultMatrixCCell)
        self.ui.widget.formInput.group.buttonClicked.connect(self.RadioBtnG)
        self.ui.widget.btnResult2.clicked.connect(self.resultMatrixCCellG)

        self.ui.widget2.dimension.spinBoxA1.valueChanged.connect(self.inputMatrixAt)
        self.ui.widget2.dimension.spinBoxA2.valueChanged.connect(self.inputMatrixAt)
        self.ui.widget2.pushButton.clicked.connect(self.resultMatrixCCellt)
        self.ui.widget2.formInput.group.buttonClicked.connect(self.RadioBtnt)
        self.ui.widget2.btnResult2.clicked.connect(self.resultMatrixCt)

        self.ui.widget3.dimension.spinBoxA1.valueChanged.connect(self.inputMatrixAF)
        self.ui.widget3.pushButton.clicked.connect(self.resultMatrixCF)
        self.ui.widget3.formInput.group.buttonClicked.connect(self.RadioBtnF)
        self.ui.widget3.btnResult2.clicked.connect(self.resultMatrixCCellF)
        self.inputMatrixAG()
        self.inputMatrixAF()
        self.inputMatrixA()
        self.inputMatrixB()
        self.inputMatrixAt()

    def __init__(self):
        super(MyWin, self).__init__()
        self.ui = Ui_MainWindow()  # загружаем класс с интерфейсами
        self.ui.menu(self)  # загружаем функцию с меню
        self.ui.setupUi(self)  # загружаем один из интерфейсов
        self.ui.setupUiG(self)
        self.ui.setupUi3(self)
        self.ui.setupUiF(self)
        self.ui.widget.hide()
        self.ui.widget2.hide()
        self.ui.widget3.hide()
        self.downld()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
