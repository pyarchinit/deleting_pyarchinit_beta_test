# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyarchinit_Periodo_fase_ui.ui'
#
# Created: Mon Jan 28 23:13:23 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogPeriodoFase(object):
    def setupUi(self, DialogPeriodoFase):
        DialogPeriodoFase.setObjectName(_fromUtf8("DialogPeriodoFase"))
        DialogPeriodoFase.resize(624, 595)
        DialogPeriodoFase.setMinimumSize(QtCore.QSize(540, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/iconSite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogPeriodoFase.setWindowIcon(icon)
        self.gridLayout_9 = QtGui.QGridLayout(DialogPeriodoFase)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_29 = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_2.addWidget(self.label_29, 0, 0, 1, 1)
        self.pushButton_connect = QtGui.QPushButton(DialogPeriodoFase)
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))
        self.gridLayout_2.addWidget(self.pushButton_connect, 0, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_first_rec = QtGui.QPushButton(DialogPeriodoFase)
        self.pushButton_first_rec.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/5_leftArrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_first_rec.setIcon(icon1)
        self.pushButton_first_rec.setObjectName(_fromUtf8("pushButton_first_rec"))
        self.gridLayout.addWidget(self.pushButton_first_rec, 0, 0, 1, 1)
        self.pushButton_prev_rec = QtGui.QPushButton(DialogPeriodoFase)
        self.pushButton_prev_rec.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/4_leftArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_prev_rec.setIcon(icon2)
        self.pushButton_prev_rec.setObjectName(_fromUtf8("pushButton_prev_rec"))
        self.gridLayout.addWidget(self.pushButton_prev_rec, 0, 1, 1, 2)
        self.pushButton_next_rec = QtGui.QPushButton(DialogPeriodoFase)
        self.pushButton_next_rec.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/6_rightArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_next_rec.setIcon(icon3)
        self.pushButton_next_rec.setObjectName(_fromUtf8("pushButton_next_rec"))
        self.gridLayout.addWidget(self.pushButton_next_rec, 0, 4, 1, 1)
        self.pushButton_last_rec = QtGui.QPushButton(DialogPeriodoFase)
        self.pushButton_last_rec.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/7_rightArrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_last_rec.setIcon(icon4)
        self.pushButton_last_rec.setObjectName(_fromUtf8("pushButton_last_rec"))
        self.gridLayout.addWidget(self.pushButton_last_rec, 0, 5, 1, 1)
        self.pushButton_new_rec = QtGui.QPushButton(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_rec.setFont(font)
        self.pushButton_new_rec.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/newrec.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_rec.setIcon(icon5)
        self.pushButton_new_rec.setObjectName(_fromUtf8("pushButton_new_rec"))
        self.gridLayout.addWidget(self.pushButton_new_rec, 0, 6, 1, 1)
        self.pushButton_save = QtGui.QPushButton(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/b_save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon6)
        self.pushButton_save.setAutoDefault(False)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.gridLayout.addWidget(self.pushButton_save, 0, 7, 1, 1)
        self.pushButton_delete = QtGui.QPushButton(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon7)
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.gridLayout.addWidget(self.pushButton_delete, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(70, 30, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.pushButton_new_search = QtGui.QPushButton(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_search.setFont(font)
        self.pushButton_new_search.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/new_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_search.setIcon(icon8)
        self.pushButton_new_search.setObjectName(_fromUtf8("pushButton_new_search"))
        self.gridLayout.addWidget(self.pushButton_new_search, 1, 4, 1, 1)
        self.pushButton_search_go = QtGui.QPushButton(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_search_go.setFont(font)
        self.pushButton_search_go.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search_go.setIcon(icon9)
        self.pushButton_search_go.setObjectName(_fromUtf8("pushButton_search_go"))
        self.gridLayout.addWidget(self.pushButton_search_go, 1, 5, 1, 1)
        self.pushButton_sort = QtGui.QPushButton(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_sort.setFont(font)
        self.pushButton_sort.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/sort.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sort.setIcon(icon10)
        self.pushButton_sort.setObjectName(_fromUtf8("pushButton_sort"))
        self.gridLayout.addWidget(self.pushButton_sort, 1, 6, 1, 1)
        self.pushButton_view_all = QtGui.QPushButton(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_view_all.setFont(font)
        self.pushButton_view_all.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/view_all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_view_all.setIcon(icon11)
        self.pushButton_view_all.setObjectName(_fromUtf8("pushButton_view_all"))
        self.gridLayout.addWidget(self.pushButton_view_all, 1, 7, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.line_6 = QtGui.QFrame(DialogPeriodoFase)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout.addWidget(self.line_6)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_42 = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_42.setFont(font)
        self.label_42.setAutoFillBackground(True)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_5.addWidget(self.label_42, 0, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_43 = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_43.setFont(font)
        self.label_43.setMargin(0)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_4.addWidget(self.label_43, 0, 1, 1, 1)
        self.label_status = QtGui.QLabel(DialogPeriodoFase)
        self.label_status.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_status.setFont(font)
        self.label_status.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_status.setMouseTracking(False)
        self.label_status.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_status.setFrameShape(QtGui.QFrame.Box)
        self.label_status.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_status.setText(_fromUtf8(""))
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setMargin(0)
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.gridLayout_4.addWidget(self.label_status, 1, 0, 1, 1)
        self.label_sort = QtGui.QLabel(DialogPeriodoFase)
        self.label_sort.setMinimumSize(QtCore.QSize(40, 0))
        self.label_sort.setSizeIncrement(QtCore.QSize(40, 0))
        self.label_sort.setBaseSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_sort.setFont(font)
        self.label_sort.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_sort.setMouseTracking(False)
        self.label_sort.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_sort.setFrameShape(QtGui.QFrame.Box)
        self.label_sort.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_sort.setText(_fromUtf8(""))
        self.label_sort.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sort.setMargin(0)
        self.label_sort.setObjectName(_fromUtf8("label_sort"))
        self.gridLayout_4.addWidget(self.label_sort, 1, 1, 1, 1)
        self.label_34 = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_34.setFont(font)
        self.label_34.setMargin(0)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_4.addWidget(self.label_34, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_27 = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setMargin(0)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_3.addWidget(self.label_27, 0, 0, 1, 1)
        self.label_rec_corrente = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft Sans Serif"))
        font.setPointSize(12)
        self.label_rec_corrente.setFont(font)
        self.label_rec_corrente.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_rec_corrente.setMouseTracking(False)
        self.label_rec_corrente.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_rec_corrente.setFrameShape(QtGui.QFrame.Box)
        self.label_rec_corrente.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_rec_corrente.setObjectName(_fromUtf8("label_rec_corrente"))
        self.gridLayout_3.addWidget(self.label_rec_corrente, 0, 1, 1, 1)
        self.label_28 = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_28.setFont(font)
        self.label_28.setMargin(0)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)
        self.label_rec_tot = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft Sans Serif"))
        font.setPointSize(12)
        self.label_rec_tot.setFont(font)
        self.label_rec_tot.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_rec_tot.setMouseTracking(False)
        self.label_rec_tot.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_rec_tot.setFrameShape(QtGui.QFrame.Box)
        self.label_rec_tot.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_rec_tot.setObjectName(_fromUtf8("label_rec_tot"))
        self.gridLayout_3.addWidget(self.label_rec_tot, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_8 = QtGui.QFrame(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.line_8.setFont(font)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.verticalLayout.addWidget(self.line_8)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.comboBox_sito = QtGui.QComboBox(DialogPeriodoFase)
        self.comboBox_sito.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_sito.setFont(font)
        self.comboBox_sito.setMouseTracking(True)
        self.comboBox_sito.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.comboBox_sito.setEditable(True)
        self.comboBox_sito.setMaxVisibleItems(99999)
        self.comboBox_sito.setMaxCount(2147483647)
        self.comboBox_sito.setFrame(False)
        self.comboBox_sito.setObjectName(_fromUtf8("comboBox_sito"))
        self.comboBox_sito.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_sito, 0, 0, 3, 8)
        self.label = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_7.addWidget(self.label, 3, 0, 1, 1)
        self.comboBox_periodo = QtGui.QComboBox(DialogPeriodoFase)
        self.comboBox_periodo.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_periodo.setFont(font)
        self.comboBox_periodo.setAutoFillBackground(False)
        self.comboBox_periodo.setEditable(True)
        self.comboBox_periodo.setMaxVisibleItems(15)
        self.comboBox_periodo.setMaxCount(15)
        self.comboBox_periodo.setObjectName(_fromUtf8("comboBox_periodo"))
        self.comboBox_periodo.addItem(_fromUtf8(""))
        self.comboBox_periodo.addItem(_fromUtf8(""))
        self.comboBox_periodo.addItem(_fromUtf8(""))
        self.comboBox_periodo.addItem(_fromUtf8(""))
        self.comboBox_periodo.addItem(_fromUtf8(""))
        self.comboBox_periodo.addItem(_fromUtf8(""))
        self.comboBox_periodo.addItem(_fromUtf8(""))
        self.comboBox_periodo.addItem(_fromUtf8(""))
        self.comboBox_periodo.addItem(_fromUtf8(""))
        self.comboBox_periodo.addItem(_fromUtf8(""))
        self.comboBox_periodo.addItem(_fromUtf8(""))
        self.comboBox_periodo.addItem(_fromUtf8(""))
        self.comboBox_periodo.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_periodo, 4, 0, 1, 1)
        self.comboBox_fase = QtGui.QComboBox(DialogPeriodoFase)
        self.comboBox_fase.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_fase.setFont(font)
        self.comboBox_fase.setEditable(True)
        self.comboBox_fase.setObjectName(_fromUtf8("comboBox_fase"))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.comboBox_fase.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_fase, 4, 1, 1, 1)
        self.label_8 = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_7.addWidget(self.label_8, 5, 1, 1, 1)
        self.label_7 = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_7.addWidget(self.label_7, 5, 0, 1, 1)
        self.lineEdit_codice_periodo = QtGui.QLineEdit(DialogPeriodoFase)
        self.lineEdit_codice_periodo.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lineEdit_codice_periodo.setObjectName(_fromUtf8("lineEdit_codice_periodo"))
        self.gridLayout_7.addWidget(self.lineEdit_codice_periodo, 4, 4, 1, 1)
        self.label_2 = QtGui.QLabel(DialogPeriodoFase)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_7.addWidget(self.label_2, 4, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 4, 7, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(100, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 4, 6, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 4, 2, 1, 1)
        self.pushButton_show_periodo = QtGui.QPushButton(DialogPeriodoFase)
        self.pushButton_show_periodo.setObjectName(_fromUtf8("pushButton_show_periodo"))
        self.gridLayout_7.addWidget(self.pushButton_show_periodo, 5, 4, 1, 1)
        self.pushButton_pdf_exp = QtGui.QPushButton(DialogPeriodoFase)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pdf-icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_pdf_exp.setIcon(icon12)
        self.pushButton_pdf_exp.setObjectName(_fromUtf8("pushButton_pdf_exp"))
        self.gridLayout_7.addWidget(self.pushButton_pdf_exp, 3, 7, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_6 = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_6.addWidget(self.label_6, 3, 0, 1, 2)
        self.line_10 = QtGui.QFrame(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.line_10.setFont(font)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.gridLayout_6.addWidget(self.line_10, 4, 0, 2, 4)
        self.label_38 = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_38.setFont(font)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout_6.addWidget(self.label_38, 9, 0, 1, 1)
        self.lineEdit_cron_iniz = QtGui.QLineEdit(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_cron_iniz.setFont(font)
        self.lineEdit_cron_iniz.setObjectName(_fromUtf8("lineEdit_cron_iniz"))
        self.gridLayout_6.addWidget(self.lineEdit_cron_iniz, 10, 0, 1, 1)
        self.label_37 = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_37.setFont(font)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout_6.addWidget(self.label_37, 11, 0, 1, 1)
        self.label_14 = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_6.addWidget(self.label_14, 11, 1, 1, 1)
        self.textEdit_descrizione_per = QtGui.QTextEdit(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_descrizione_per.setFont(font)
        self.textEdit_descrizione_per.setObjectName(_fromUtf8("textEdit_descrizione_per"))
        self.gridLayout_6.addWidget(self.textEdit_descrizione_per, 2, 0, 1, 4)
        self.lineEdit_cron_fin = QtGui.QLineEdit(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_cron_fin.setFont(font)
        self.lineEdit_cron_fin.setObjectName(_fromUtf8("lineEdit_cron_fin"))
        self.gridLayout_6.addWidget(self.lineEdit_cron_fin, 10, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(38, 19, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 10, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 10, 3, 1, 1)
        self.label_13 = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.lineEdit_per_estesa = QtGui.QLineEdit(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_per_estesa.setFont(font)
        self.lineEdit_per_estesa.setText(_fromUtf8(""))
        self.lineEdit_per_estesa.setObjectName(_fromUtf8("lineEdit_per_estesa"))
        self.gridLayout_8.addWidget(self.lineEdit_per_estesa, 0, 0, 1, 2)
        self.label_25 = QtGui.QLabel(DialogPeriodoFase)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_8.addWidget(self.label_25, 1, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(418, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem7, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_8)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_9.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(DialogPeriodoFase)
        QtCore.QMetaObject.connectSlotsByName(DialogPeriodoFase)

    def retranslateUi(self, DialogPeriodoFase):
        DialogPeriodoFase.setWindowTitle(QtGui.QApplication.translate("DialogPeriodoFase", "pyArchInit Gestione Scavi - Periodizzazione di scavo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("DialogPeriodoFase", "DBMS Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_connect.setText(QtGui.QApplication.translate("DialogPeriodoFase", "Reload DB", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_first_rec.setToolTip(QtGui.QApplication.translate("DialogPeriodoFase", "First rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_prev_rec.setToolTip(QtGui.QApplication.translate("DialogPeriodoFase", "Prev rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_next_rec.setToolTip(QtGui.QApplication.translate("DialogPeriodoFase", "Next rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_last_rec.setToolTip(QtGui.QApplication.translate("DialogPeriodoFase", "Last rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_rec.setToolTip(QtGui.QApplication.translate("DialogPeriodoFase", "New record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setToolTip(QtGui.QApplication.translate("DialogPeriodoFase", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_delete.setToolTip(QtGui.QApplication.translate("DialogPeriodoFase", "Delete record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_search.setToolTip(QtGui.QApplication.translate("DialogPeriodoFase", "new search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_search_go.setToolTip(QtGui.QApplication.translate("DialogPeriodoFase", "search !!!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_sort.setToolTip(QtGui.QApplication.translate("DialogPeriodoFase", "Order by", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view_all.setToolTip(QtGui.QApplication.translate("DialogPeriodoFase", "View alls records", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("DialogPeriodoFase", "DB Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("DialogPeriodoFase", "Ordinamento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("DialogPeriodoFase", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("DialogPeriodoFase", "record n.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rec_corrente.setText(QtGui.QApplication.translate("DialogPeriodoFase", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("DialogPeriodoFase", "record tot.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rec_tot.setText(QtGui.QApplication.translate("DialogPeriodoFase", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sito.setItemText(0, QtGui.QApplication.translate("DialogPeriodoFase", "Inserisci un valore", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogPeriodoFase", "Sito", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(0, QtGui.QApplication.translate("DialogPeriodoFase", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(1, QtGui.QApplication.translate("DialogPeriodoFase", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(2, QtGui.QApplication.translate("DialogPeriodoFase", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(3, QtGui.QApplication.translate("DialogPeriodoFase", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(4, QtGui.QApplication.translate("DialogPeriodoFase", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(5, QtGui.QApplication.translate("DialogPeriodoFase", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(6, QtGui.QApplication.translate("DialogPeriodoFase", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(7, QtGui.QApplication.translate("DialogPeriodoFase", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(8, QtGui.QApplication.translate("DialogPeriodoFase", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(9, QtGui.QApplication.translate("DialogPeriodoFase", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(10, QtGui.QApplication.translate("DialogPeriodoFase", "11", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(11, QtGui.QApplication.translate("DialogPeriodoFase", "13", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(12, QtGui.QApplication.translate("DialogPeriodoFase", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(0, QtGui.QApplication.translate("DialogPeriodoFase", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(1, QtGui.QApplication.translate("DialogPeriodoFase", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(2, QtGui.QApplication.translate("DialogPeriodoFase", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(3, QtGui.QApplication.translate("DialogPeriodoFase", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(4, QtGui.QApplication.translate("DialogPeriodoFase", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(5, QtGui.QApplication.translate("DialogPeriodoFase", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(6, QtGui.QApplication.translate("DialogPeriodoFase", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(7, QtGui.QApplication.translate("DialogPeriodoFase", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(8, QtGui.QApplication.translate("DialogPeriodoFase", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(9, QtGui.QApplication.translate("DialogPeriodoFase", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(10, QtGui.QApplication.translate("DialogPeriodoFase", "11", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(11, QtGui.QApplication.translate("DialogPeriodoFase", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(12, QtGui.QApplication.translate("DialogPeriodoFase", "13", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(13, QtGui.QApplication.translate("DialogPeriodoFase", "14", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(14, QtGui.QApplication.translate("DialogPeriodoFase", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("DialogPeriodoFase", "Fase", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DialogPeriodoFase", "Periodo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogPeriodoFase", "Codice periodo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_show_periodo.setText(QtGui.QApplication.translate("DialogPeriodoFase", "Visualizza il periodo sul GIS", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_pdf_exp.setText(QtGui.QApplication.translate("DialogPeriodoFase", "PDF EXP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DialogPeriodoFase", "Descrizione ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setText(QtGui.QApplication.translate("DialogPeriodoFase", "Cronologia ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_cron_iniz.setText(QtGui.QApplication.translate("DialogPeriodoFase", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("DialogPeriodoFase", "Iniziale ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("DialogPeriodoFase", "Finale ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_cron_fin.setText(QtGui.QApplication.translate("DialogPeriodoFase", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("DialogPeriodoFase", "Dati descrittivi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("DialogPeriodoFase", "Estesa letterale ", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc