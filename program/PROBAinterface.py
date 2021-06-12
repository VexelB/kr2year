from PyQt5.QtWidgets import QApplication, QFrame, QGroupBox, QRadioButton, QListWidget, QLabel,\
                            QListWidgetItem, QPushButton, QListView, QAction, QMainWindow, qApp,\
                            QWidget, QGridLayout, QTableWidget, QTabWidget, QVBoxLayout, QSpinBox,\
                            QLineEdit, QHBoxLayout, QVBoxLayout, QButtonGroup, QPlainTextEdit
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage

class Ui_MainWindow(object):

    def menu(self, MainWindow):

        MainWindow.setGeometry(50, 50, 800, 600)  # расположение окна (x, y) = (50, 50) от левого верхнего угла,
                                                  # 800 - ширина, 600 - высота
        MainWindow.setFixedWidth(800)  # ограничение на изменение ширины окна
        MainWindow.setFixedHeight(600)  # ограничение на изменение высоты окна

        # меню
        self.list = QListWidget(MainWindow)  # создание экземпляра List
        self.list.setGeometry(10, 10, 180, 570)  # расположение List
        self.list.setFixedWidth(180)  # фиксированная ширина List
        self.list.setSortingEnabled(False)  # отключение сортировки

        # List of Widgets - MENU
        self.itemMultMatrix = QListWidgetItem()  # создание экземпляра строки в List
        self.list.addItem(self.itemMultMatrix)  # добавление экземпляра строки в List
        self.itemMultMatrix.setText("Умножение матриц")  # заполнение текстом

        self.Gauss = QListWidgetItem()  # создание экземпляра строки в List
        self.list.addItem(self.Gauss)  # добавление экземпляра строки в List
        self.Gauss.setText("Метод Гаусса")  # заполнение текстом

        self.transpMatrix = QListWidgetItem()  # создание экземпляра строки в List
        self.list.addItem(self.transpMatrix)  # добавление экземпляра строки в List
        self.transpMatrix.setText("Транспонирование матриц")  # заполнение текстом

        self.Factor = QListWidgetItem()  # создание экземпляра строки в List
        self.list.addItem(self.Factor)  # добавление экземпляра строки в List
        self.Factor.setText("Треугольная факторизация")  # заполнение текстом

    def setupUi(self, MainWindow):

        self.mainWidget = QWidget(MainWindow)  # общий виджет
        self.mainWidget.setGeometry(200, 10, 590, 570)  # расположение основного виджета

        ui = self.mainWidget  # переменная для сокращения записи

        # Шрифт
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        # создание в основной части заголовка страницы
        ui.labelName = QLabel(ui)
        ui.labelName.setGeometry(220, 10, 191, 20)
        ui.labelName.setText("Умножение матриц")
        ui.labelName.setFont(font)

        # создание подчеркивания названия темы
        ui.line = QFrame(ui)
        ui.line.setGeometry(10, 30, 571, 20)
        ui.line.setFrameShape(QFrame.HLine)  # форма подчеркивания - без этого параметра не будет отображаться
        ui.line.setFrameShadow(QFrame.Sunken)  # тень подчеркивания

        # форма ввода
        ui.formInput = QGroupBox(ui)
        ui.formInput.setGeometry(30, 50, 120, 80)
        ui.formInput.setTitle("Форма ввода")
        ui.formInput.btnRadioCell = QRadioButton(ui.formInput)
        ui.formInput.btnRadioCell.setGeometry(10, 20, 82, 17)
        ui.formInput.btnRadioCell.setText("Ячейки")
        ui.formInput.btnRadioCell.setChecked(True)
        ui.formInput.btnRadioCell.setObjectName("RadioCell")
        ui.formInput.btnRadioBox = QRadioButton(ui.formInput)
        ui.formInput.btnRadioBox.setGeometry(10, 50, 82, 17)
        ui.formInput.btnRadioBox.setText("Окно")
        ui.formInput.btnRadioBox.setObjectName("RadioBox")

        # объединение радио-кнопок в группы
        ui.formInput.group = QButtonGroup(ui.formInput)
        ui.formInput.group.addButton(ui.formInput.btnRadioBox)
        ui.formInput.group.addButton(ui.formInput.btnRadioCell)

        # размерность матрицы
        self.mainWidget.dimension = QGroupBox(self.mainWidget)
        self.mainWidget.dimension.setGeometry(185, 50, 211, 80)
        self.mainWidget.dimension.setTitle("Размерность матриц")
        self.mainWidget.dimension.labelA = QLabel(self.mainWidget.dimension)
        self.mainWidget.dimension.labelA.setGeometry(10, 20, 91, 16)
        self.mainWidget.dimension.labelA.setText("Матрица A:")
        ui.dimension.labelB = QLabel(ui.dimension)
        ui.dimension.labelB.setGeometry(10, 50, 91, 16)
        ui.dimension.labelB.setText("Матрица B:")
        ui.dimension.spinBoxA1 = QSpinBox(ui.dimension)
        self.mainWidget.dimension.spinBoxA1.setMinimum(1)
        self.mainWidget.dimension.spinBoxA1.setMaximum(6)
        ui.dimension.spinBoxA1.setGeometry(90, 20, 42, 22)
        ui.dimension.spinBoxA2 = QSpinBox(ui.dimension)
        self.mainWidget.dimension.spinBoxA2.setMinimum(1)
        self.mainWidget.dimension.spinBoxA2.setMaximum(6)
        ui.dimension.spinBoxA2.setGeometry(150, 20, 42, 22)
        ui.dimension.spinBoxB1 = QSpinBox(ui.dimension)
        self.mainWidget.dimension.spinBoxB1.setMinimum(1)
        self.mainWidget.dimension.spinBoxB1.setMaximum(6)
        ui.dimension.spinBoxB1.setGeometry(90, 50, 42, 22)
        ui.dimension.spinBoxB2 = QSpinBox(ui.dimension)
        self.mainWidget.dimension.spinBoxB2.setMinimum(1)
        self.mainWidget.dimension.spinBoxB2.setMaximum(6)
        ui.dimension.spinBoxB2.setGeometry(150, 50, 42, 22)
        ui.dimension.labelX1 = QLabel(ui.dimension)
        ui.dimension.labelX1.setGeometry(140, 20, 16, 16)
        ui.dimension.labelX1.setText("x")
        ui.dimension.labelX2 = QLabel(ui.dimension)
        ui.dimension.labelX2.setGeometry(140, 50, 16, 16)
        ui.dimension.labelX2.setText("x")

        # матрица А
        ui.matrixA = QGroupBox(ui)
        ui.matrixA.setGeometry(30, 150, 261, 171)
        ui.matrixA.setTitle("Матрица А")
        self.mainWidget.matrixA.wid = QWidget(self.mainWidget.matrixA)
        self.mainWidget.matrixA.wid.setGeometry(5, 10, 251, 156)
        grid = QGridLayout(self.mainWidget.matrixA.wid)
        self.mainWidget.matrixA.wid.setLayout(grid)
        # self.mainWidget.matrixA.wid.WinInput = QPlainTextEdit(self.mainWidget.matrixA.wid)
        # grid.addWidget(self.mainWidget.matrixA.wid.WinInput)

        # матрица В
        ui.matrixB = QGroupBox(ui)
        ui.matrixB.setGeometry(30, 340, 261, 171)
        ui.matrixB.setTitle("Матрица B")
        self.mainWidget.matrixB.wid = QWidget(self.mainWidget.matrixB)
        self.mainWidget.matrixB.wid.setGeometry(5, 10, 251, 156)
        grid = QGridLayout(self.mainWidget.matrixB.wid)
        self.mainWidget.matrixB.wid.setLayout(grid)

        # заметки
        ui.notes = QGroupBox(ui)
        ui.notes.setGeometry(310, 150, 261, 80)
        ui.notes.setTitle("Заметки")

        # ui.notes.label = QLabel(ui.notes)
        # ui.notes.label.setGeometry(5, 10, 251, 65)
        # ui.pixmap = QPixmap("src/NotesMult.png")
        # ui.notes.label.setPixmap(ui.pixmap)

        ui.notes.button = QPushButton(ui.notes)
        ui.notes.button.setIconSize(QSize(150, 60))
        ui.notes.button.setGeometry(10, 20, 240, 50)
        ui.notes.button.setIcon(QIcon(QPixmap("src/NotesMult.png")))
        ui.notes.button.setEnabled(False)

        # кнопка
        ui.btnResult = QPushButton(ui)
        ui.btnResult.setGeometry(400, 260, 75, 23)
        ui.btnResult.setText("Результат")
        ui.btnResult2 = QPushButton(ui)
        ui.btnResult2.setGeometry(400, 260, 75, 23)
        ui.btnResult2.setText("Результат")
        ui.btnResult2.hide()

        # матрица С
        ui.matrixC = QGroupBox(ui)
        ui.matrixC.setGeometry(310, 320, 261, 191)
        ui.matrixC.setTitle("Матрица C")
        self.mainWidget.matrixC.wid = QWidget(self.mainWidget.matrixC)
        self.mainWidget.matrixC.wid.setGeometry(5, 10, 251, 176)
        grid = QGridLayout(self.mainWidget.matrixC.wid)
        self.mainWidget.matrixC.wid.setLayout(grid)

    def setupUiG(self, MainWindow):

        self.widget = QWidget(MainWindow)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(200, 10, 590, 570))
        self.widget.setAutoFillBackground(False)
        self.widget.setObjectName("widget")

        ui = self.widget

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        # создание в основной части заголовка страницы
        self.widget.label = QLabel(ui)
        self.widget.label.setGeometry(220, 10, 191, 20)
        self.widget.label.setText("Метод Гаусса")
        self.widget.label.setFont(font)

        self.line = QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(10, 30, 571, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")

        ui.dimension = QGroupBox(self.widget)
        ui.dimension.setGeometry(185, 50, 200, 80)
        ui.dimension.spinBoxA1 = QSpinBox(ui.dimension)
        ui.dimension.spinBoxA1.setMinimum(1)
        ui.dimension.spinBoxA1.setMaximum(6)
        ui.dimension.spinBoxA1.setGeometry(150, 20, 42, 22)
        ui.dimension.spinBoxA2 = QSpinBox(ui.dimension)
        ui.dimension.spinBoxA2.setMinimum(1)
        ui.dimension.spinBoxA2.setMaximum(6)
        ui.dimension.spinBoxA2.setGeometry(150, 50, 42, 22)

        ui.matrixA = QGroupBox(ui)
        ui.matrixA.setGeometry(30, 150, 441, 351)
        ui.matrixA.setTitle("Система")
        self.widget.matrixA.wid = QWidget(self.widget.matrixA)
        self.widget.matrixA.wid.setGeometry(5, 10, 431, 336)
        grid = QGridLayout(self.widget.matrixA.wid)
        self.widget.matrixA.wid.setLayout(grid)

        ui.matrixC = QGroupBox(ui)
        ui.matrixC.setGeometry(490, 150, 80, 319)
        ui.matrixC.setTitle("Результат")
        self.widget.matrixC.wid = QWidget(self.widget.matrixC)
        self.widget.matrixC.wid.setGeometry(5, 10, 70, 304)
        grid = QGridLayout(self.widget.matrixC.wid)
        self.widget.matrixC.wid.setLayout(grid)

        # форма ввода
        ui.formInput = QGroupBox(ui)
        ui.formInput.setGeometry(30, 50, 120, 80)
        ui.formInput.setTitle("Форма ввода")
        ui.formInput.btnRadioCell = QRadioButton(ui.formInput)
        ui.formInput.btnRadioCell.setGeometry(10, 20, 82, 17)
        ui.formInput.btnRadioCell.setText("Ячейки")
        ui.formInput.btnRadioCell.setChecked(True)
        ui.formInput.btnRadioCell.setObjectName("RadioCell")
        ui.formInput.btnRadioBox = QRadioButton(ui.formInput)
        ui.formInput.btnRadioBox.setGeometry(10, 50, 82, 17)
        ui.formInput.btnRadioBox.setText("Окно")
        ui.formInput.btnRadioBox.setObjectName("RadioBox")
        # объединение радио-кнопок в группы
        ui.formInput.group = QButtonGroup(ui.formInput)
        ui.formInput.group.addButton(ui.formInput.btnRadioBox)
        ui.formInput.group.addButton(ui.formInput.btnRadioCell)

        self.label_2 = QLabel(ui.dimension)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QLabel(ui.dimension)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 141, 16))
        self.label_4.setObjectName("label_4")
        ui.groupBox_5 = QGroupBox(self.widget)
        ui.groupBox_5.setGeometry(QtCore.QRect(420, 50, 150, 80))
        ui.groupBox_5.setObjectName("groupBox_5")
        ui.groupBox_5.button = QPushButton(ui.groupBox_5)
        ui.groupBox_5.button.setIconSize(QSize(120, 50))
        ui.groupBox_5.button.setGeometry(10, 20, 130, 50)
        ui.groupBox_5.button.setEnabled(False)
        ui.groupBox_5.button.setIcon(QIcon(QPixmap("src/NotesGauss.png")))
        ui.groupBox_5.button.setEnabled(False)

        ui.pushButton = QPushButton(self.widget)
        ui.pushButton.setGeometry(QtCore.QRect(490, 478, 80, 23))
        ui.pushButton.setObjectName("pushButton")

        ui.btnResult2 = QPushButton(ui)
        ui.btnResult2.setGeometry(490, 478, 80, 23)
        ui.btnResult2.setText("Решить")
        ui.btnResult2.hide()

        ui.dimension.setTitle("Размерность системы")
        self.label_2.setText("Кол-во строк:")
        self.label_4.setText("Кол-во неизвестных:")
        ui.groupBox_5.setTitle("Заметки")
        ui.pushButton.setText("Решить")

    def setupUi3(self, MainWindow):

        self.widget2 = QWidget(MainWindow)
        self.widget2.setEnabled(True)
        self.widget2.setGeometry(QtCore.QRect(200, 10, 590, 570))
        self.widget2.setAutoFillBackground(False)
        self.widget2.setObjectName("widget2")

        ui = self.widget2

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        # создание в основной части заголовка страницы
        self.widget2.label = QLabel(ui)
        self.widget2.label.setGeometry(150, 10, 590, 20)
        self.widget2.label.setText("Транспонирование матрицы")
        self.widget2.label.setFont(font)

        self.line = QFrame(self.widget2)
        self.line.setGeometry(QtCore.QRect(10, 30, 571, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")

        ui.dimension = QGroupBox(self.widget2)
        ui.dimension.setGeometry(185, 50, 200, 80)
        ui.dimension.spinBoxA1 = QSpinBox(ui.dimension)
        ui.dimension.spinBoxA1.setMinimum(1)
        ui.dimension.spinBoxA1.setMaximum(6)
        ui.dimension.spinBoxA1.setGeometry(150, 20, 42, 22)
        ui.dimension.spinBoxA2 = QSpinBox(ui.dimension)
        ui.dimension.spinBoxA2.setMinimum(1)
        ui.dimension.spinBoxA2.setMaximum(6)
        ui.dimension.spinBoxA2.setGeometry(150, 50, 42, 22)

        ui.matrixA = QGroupBox(ui)
        ui.matrixA.setGeometry(30, 150, 260, 300)
        ui.matrixA.setTitle("Исходная матрица")
        ui.matrixA.wid = QWidget(ui.matrixA)
        ui.matrixA.wid.setGeometry(5, 10, 250, 285)
        grid = QGridLayout(ui.matrixA.wid)
        ui.matrixA.wid.setLayout(grid)

        ui.matrixC = QGroupBox(ui)
        ui.matrixC.setGeometry(310, 150, 260, 300)
        ui.matrixC.setTitle("Транспонированная матрица")
        self.widget2.matrixC.wid = QWidget(self.widget2.matrixC)
        self.widget2.matrixC.wid.setGeometry(5, 10, 250, 285)
        grid = QGridLayout(self.widget2.matrixC.wid)
        self.widget2.matrixC.wid.setLayout(grid)

        # форма ввода
        ui.formInput = QGroupBox(ui)
        ui.formInput.setGeometry(30, 50, 120, 80)
        ui.formInput.setTitle("Форма ввода")
        ui.formInput.btnRadioCell = QRadioButton(ui.formInput)
        ui.formInput.btnRadioCell.setGeometry(10, 20, 82, 17)
        ui.formInput.btnRadioCell.setText("Ячейки")
        ui.formInput.btnRadioCell.setChecked(True)
        ui.formInput.btnRadioCell.setObjectName("RadioCell")
        ui.formInput.btnRadioBox = QRadioButton(ui.formInput)
        ui.formInput.btnRadioBox.setGeometry(10, 50, 82, 17)
        ui.formInput.btnRadioBox.setText("Окно")
        ui.formInput.btnRadioBox.setObjectName("RadioBox")

        # объединение радио-кнопок в группы
        ui.formInput.group = QButtonGroup(ui.formInput)
        ui.formInput.group.addButton(ui.formInput.btnRadioBox)
        ui.formInput.group.addButton(ui.formInput.btnRadioCell)

        self.label_2 = QLabel(ui.dimension)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QLabel(ui.dimension)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 141, 16))
        self.label_4.setObjectName("label_4")
        self.groupBox_5 = QGroupBox(self.widget2)
        self.groupBox_5.setGeometry(QtCore.QRect(420, 50, 150, 80))
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_5.button = QPushButton(self.groupBox_5)
        self.groupBox_5.button.setIconSize(QSize(120, 40))
        self.groupBox_5.button.setGeometry(10, 20, 130, 50)
        self.groupBox_5.button.setIcon(QIcon(QPixmap("src/NotesTransp.png")))
        self.groupBox_5.button.setEnabled(False)
        ui.pushButton = QPushButton(self.widget2)
        ui.pushButton.setGeometry(QtCore.QRect(30, 460, 540, 20))
        ui.pushButton.setObjectName("pushButton")

        ui.btnResult2 = QPushButton(ui)
        ui.btnResult2.setGeometry(30, 460, 540, 20)
        ui.btnResult2.setText("Транспонировать")
        ui.btnResult2.hide()

        ui.dimension.setTitle("Размерность матрицы")
        self.label_2.setText("Кол-во строк:")
        self.label_4.setText("Кол-во столбцов:")
        self.groupBox_5.setTitle("Заметки")
        ui.pushButton.setText("Транспонировать")

    def setupUiF(self, MainWindow):

        self.widget3 = QWidget(MainWindow)
        self.widget3.setEnabled(True)
        self.widget3.setGeometry(QtCore.QRect(200, 10, 590, 570))
        self.widget3.setAutoFillBackground(False)
        self.widget3.setObjectName("widget")

        ui = self.widget3

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        # создание в основной части заголовка страницы
        ui.label = QLabel(ui)
        ui.label.setGeometry(150, 10, 590, 20)
        ui.label.setText("Треугольная факторизация")
        ui.label.setFont(font)
        # self.widget.label.setText('mda')

        self.line = QFrame(self.widget3)
        self.line.setGeometry(QtCore.QRect(10, 30, 571, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")

        ui.dimension = QGroupBox(self.widget3)
        ui.dimension.setGeometry(185, 50, 200, 80)
        ui.dimension.spinBoxA1 = QSpinBox(ui.dimension)
        ui.dimension.spinBoxA1.setMinimum(1)
        ui.dimension.spinBoxA1.setMaximum(6)
        ui.dimension.spinBoxA1.setGeometry(150, 30, 42, 22)

        ui.matrixA = QGroupBox(ui)
        ui.matrixA.setGeometry(145, 140, 290, 190)
        ui.matrixA.setTitle("Система")
        ui.matrixA.wid = QWidget(self.widget3.matrixA)
        ui.matrixA.wid.setGeometry(5, 10, 280, 175)
        grid = QGridLayout(self.widget3.matrixA.wid)
        self.widget3.matrixA.wid.setLayout(grid)

        ui.options = QGroupBox(ui)
        ui.options.setGeometry(30, 140, 80, 190)
        ui.options.setTitle("Варианты")
        ui.options.v1 = QRadioButton(ui.options)
        ui.options.v1.setGeometry(10, 20, 100, 17)
        ui.options.v1.setIcon(QIcon('src/V1.png'))
        ui.options.v1.setIconSize(QSize(50, 20))
        # ui.options.v1.setText("Вариант 1")
        ui.options.v1.setChecked(True)
        ui.options.v1.setObjectName("v1")
        ui.options.v2 = QRadioButton(ui.options)
        ui.options.v2.setGeometry(10, 40, 100, 17)
        ui.options.v2.setIcon(QIcon('src/V2.png'))
        ui.options.v2.setIconSize(QSize(50, 20))
        ui.options.v2.setObjectName("v2")
        ui.options.v3 = QRadioButton(ui.options)
        ui.options.v3.setGeometry(10, 60, 100, 17)
        ui.options.v3.setIcon(QIcon('src/V3.png'))
        ui.options.v3.setIconSize(QSize(50, 20))
        ui.options.v3.setObjectName("v3")
        ui.options.v4 = QRadioButton(ui.options)
        ui.options.v4.setGeometry(10, 80, 100, 17)
        ui.options.v4.setIcon(QIcon('src/V4.png'))
        ui.options.v4.setIconSize(QSize(50, 20))
        ui.options.v4.setObjectName("v4")
        ui.options.v5 = QRadioButton(ui.options)
        ui.options.v5.setGeometry(10, 100, 100, 17)
        ui.options.v5.setIcon(QIcon('src/V5.png'))
        ui.options.v5.setIconSize(QSize(50, 20))
        ui.options.v5.setObjectName("v5")
        ui.options.v6 = QRadioButton(ui.options)
        ui.options.v6.setGeometry(10, 120, 100, 17)
        ui.options.v6.setIcon(QIcon('src/V6.png'))
        ui.options.v6.setIconSize(QSize(50, 20))
        ui.options.v6.setObjectName("v6")
        ui.options.v7 = QRadioButton(ui.options)
        ui.options.v7.setGeometry(10, 140, 100, 17)
        ui.options.v7.setIcon(QIcon('src/V7.png'))
        ui.options.v7.setIconSize(QSize(50, 20))
        ui.options.v7.setObjectName("v7")
        ui.options.v8 = QRadioButton(ui.options)
        ui.options.v8.setGeometry(10, 160, 100, 17)
        ui.options.v8.setIcon(QIcon('src/V8.png'))
        ui.options.v8.setIconSize(QSize(50, 20))
        ui.options.v8.setObjectName("v8")
        # объединение радио-кнопок в группы
        ui.options.group = QButtonGroup(ui.options)
        ui.options.group.addButton(ui.options.v1)
        ui.options.group.addButton(ui.options.v2)
        ui.options.group.addButton(ui.options.v3)
        ui.options.group.addButton(ui.options.v4)
        ui.options.group.addButton(ui.options.v5)
        ui.options.group.addButton(ui.options.v6)
        ui.options.group.addButton(ui.options.v7)
        ui.options.group.addButton(ui.options.v8)

        ui.matrixL = QGroupBox(ui)
        ui.matrixL.setGeometry(30, 370, 250, 200)
        ui.matrixL.setTitle("Левая матрица")
        ui.matrixL.wid = QWidget(self.widget3.matrixL)
        ui.matrixL.wid.setGeometry(5, 10, 240, 185)
        grid = QGridLayout(self.widget3.matrixL.wid)
        self.widget3.matrixL.wid.setLayout(grid)

        ui.matrixR = QGroupBox(ui)
        ui.matrixR.setGeometry(320, 370, 250, 200)
        ui.matrixR.setTitle("Правая матрица")
        ui.matrixR.wid = QWidget(self.widget3.matrixR)
        ui.matrixR.wid.setGeometry(5, 10, 240, 185)
        grid = QGridLayout(self.widget3.matrixR.wid)
        self.widget3.matrixR.wid.setLayout(grid)

        ui.matrixC = QGroupBox(ui)
        ui.matrixC.setGeometry(470, 140, 100, 190)
        ui.matrixC.setTitle("Результат")
        ui.matrixC.wid = QWidget(self.widget3.matrixC)
        ui.matrixC.wid.setGeometry(5, 10, 90, 175)
        grid = QGridLayout(self.widget3.matrixC.wid)
        ui.matrixC.wid.setLayout(grid)

        # форма ввода
        ui.formInput = QGroupBox(ui)
        ui.formInput.setGeometry(30, 50, 120, 80)
        ui.formInput.setTitle("Форма ввода")
        ui.formInput.btnRadioCell = QRadioButton(ui.formInput)
        ui.formInput.btnRadioCell.setGeometry(10, 20, 82, 17)
        ui.formInput.btnRadioCell.setText("Ячейки")
        ui.formInput.btnRadioCell.setChecked(True)
        ui.formInput.btnRadioCell.setObjectName("RadioCell")
        ui.formInput.btnRadioBox = QRadioButton(ui.formInput)
        ui.formInput.btnRadioBox.setGeometry(10, 50, 82, 17)
        ui.formInput.btnRadioBox.setText("Окно")
        ui.formInput.btnRadioBox.setObjectName("RadioBox")
        # объединение радио-кнопок в группы
        ui.formInput.group = QButtonGroup(ui.formInput)
        ui.formInput.group.addButton(ui.formInput.btnRadioBox)
        ui.formInput.group.addButton(ui.formInput.btnRadioCell)

        self.label_2 = QLabel(ui.dimension)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QLabel(ui.dimension)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 141, 16))
        self.label_4.setObjectName("label_4")
        self.groupBox_5 = QGroupBox(self.widget3)
        self.groupBox_5.setGeometry(QtCore.QRect(420, 50, 150, 80))
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_5.button = QPushButton(self.groupBox_5)
        self.groupBox_5.button.setIconSize(QSize(130, 50))
        self.groupBox_5.button.setGeometry(10, 20, 130, 50)
        self.groupBox_5.button.setIcon(QIcon(QPixmap("src/NotesFact.png")))
        self.groupBox_5.button.setEnabled(False)
        ui.pushButton = QPushButton(self.widget3)
        ui.pushButton.setGeometry(QtCore.QRect(30, 340, 540, 20))
        ui.pushButton.setObjectName("pushButton")

        ui.btnResult2 = QPushButton(ui)
        ui.btnResult2.setGeometry(30, 340, 540, 20)
        ui.btnResult2.setText("Решить")
        ui.btnResult2.hide()

        ui.dimension.setTitle("Размерность системы")
        self.label_2.setText("Кол-во строк:")
        self.label_4.setText("Кол-во неизвестных:")
        self.groupBox_5.setTitle("Заметки")
        ui.pushButton.setText("Решить")
