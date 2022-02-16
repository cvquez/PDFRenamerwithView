# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window-en.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(935, 548)
        Window.setAutoFillBackground(False)
        Window.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Window)
        self.gridLayout.setObjectName("gridLayout")
        self.fileDirectoryLabel = QtWidgets.QLabel(Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileDirectoryLabel.sizePolicy().hasHeightForWidth())
        self.fileDirectoryLabel.setSizePolicy(sizePolicy)
        self.fileDirectoryLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.fileDirectoryLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        self.fileDirectoryLabel.setObjectName("fileDirectoryLabel")
        self.gridLayout.addWidget(self.fileDirectoryLabel, 0, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(74, 38, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 2, 1)
        self.splitter_2 = QtWidgets.QSplitter(Window)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.DateLabel = QtWidgets.QLabel(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DateLabel.sizePolicy().hasHeightForWidth())
        self.DateLabel.setSizePolicy(sizePolicy)
        self.DateLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.DateLabel.setMaximumSize(QtCore.QSize(210, 15))
        self.DateLabel.setObjectName("DateLabel")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.DateHorizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.DateHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.DateHorizontalLayout.setObjectName("DateHorizontalLayout")
        self.DateInput = QtWidgets.QDateEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DateInput.sizePolicy().hasHeightForWidth())
        self.DateInput.setSizePolicy(sizePolicy)
        self.DateInput.setMinimumSize(QtCore.QSize(210, 30))
        self.DateInput.setMaximumSize(QtCore.QSize(210, 30))
        self.DateInput.setCalendarPopup(True)
        self.DateInput.setDate(QtCore.QDate(2021, 1, 2))
        self.DateInput.setObjectName("DateInput")
        self.DateHorizontalLayout.addWidget(self.DateInput)
        self.DateCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.DateCheckBox.setText("")
        self.DateCheckBox.setChecked(True)
        self.DateCheckBox.setObjectName("DateCheckBox")
        self.DateHorizontalLayout.addWidget(self.DateCheckBox)
        self.IdLabel = QtWidgets.QLabel(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IdLabel.sizePolicy().hasHeightForWidth())
        self.IdLabel.setSizePolicy(sizePolicy)
        self.IdLabel.setMaximumSize(QtCore.QSize(210, 15))
        self.IdLabel.setObjectName("IdLabel")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.IdHorizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.IdHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.IdHorizontalLayout.setObjectName("IdHorizontalLayout")
        self.IdInput = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IdInput.sizePolicy().hasHeightForWidth())
        self.IdInput.setSizePolicy(sizePolicy)
        self.IdInput.setMinimumSize(QtCore.QSize(210, 30))
        self.IdInput.setMaximumSize(QtCore.QSize(210, 30))
        self.IdInput.setText("12345")
        self.IdInput.setObjectName("IdInput")
        self.IdHorizontalLayout.addWidget(self.IdInput)
        self.IdCheckBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.IdCheckBox.setText("")
        self.IdCheckBox.setChecked(True)
        self.IdCheckBox.setObjectName("IdCheckBox")
        self.IdHorizontalLayout.addWidget(self.IdCheckBox)
        self.TypeLabel = QtWidgets.QLabel(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TypeLabel.sizePolicy().hasHeightForWidth())
        self.TypeLabel.setSizePolicy(sizePolicy)
        self.TypeLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.TypeLabel.setMaximumSize(QtCore.QSize(210, 15))
        self.TypeLabel.setObjectName("TypeLabel")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.TypeHorizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.TypeHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.TypeHorizontalLayout.setObjectName("TypeHorizontalLayout")
        self.TypeLIst = QtWidgets.QListWidget(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TypeLIst.sizePolicy().hasHeightForWidth())
        self.TypeLIst.setSizePolicy(sizePolicy)
        self.TypeLIst.setMinimumSize(QtCore.QSize(210, 150))
        self.TypeLIst.setMaximumSize(QtCore.QSize(210, 150))
        self.TypeLIst.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.TypeLIst.setObjectName("TypeLIst")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.TypeLIst.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.TypeLIst.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.TypeLIst.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.TypeLIst.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.TypeLIst.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.TypeLIst.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.TypeLIst.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.TypeLIst.addItem(item)
        self.TypeHorizontalLayout.addWidget(self.TypeLIst)
        self.TypeCheckBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.TypeCheckBox.setText("")
        self.TypeCheckBox.setChecked(True)
        self.TypeCheckBox.setObjectName("TypeCheckBox")
        self.TypeHorizontalLayout.addWidget(self.TypeCheckBox)
        self.newNameInput = QtWidgets.QLineEdit(self.splitter_2)
        self.newNameInput.setMinimumSize(QtCore.QSize(250, 30))
        self.newNameInput.setMaximumSize(QtCore.QSize(250, 30))
        self.newNameInput.setObjectName("newNameInput")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.renameButton = QtWidgets.QPushButton(self.splitter)
        self.renameButton.setMinimumSize(QtCore.QSize(100, 30))
        self.renameButton.setMaximumSize(QtCore.QSize(100, 30))
        self.renameButton.setObjectName("renameButton")
        self.nextButton = QtWidgets.QPushButton(self.splitter)
        self.nextButton.setMinimumSize(QtCore.QSize(100, 30))
        self.nextButton.setMaximumSize(QtCore.QSize(100, 30))
        self.nextButton.setObjectName("nextButton")
        self.gridLayout.addWidget(self.splitter_2, 1, 0, 2, 1)
        self.fileDirectoryInput = QtWidgets.QLineEdit(Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileDirectoryInput.sizePolicy().hasHeightForWidth())
        self.fileDirectoryInput.setSizePolicy(sizePolicy)
        self.fileDirectoryInput.setMinimumSize(QtCore.QSize(400, 30))
        self.fileDirectoryInput.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fileDirectoryInput.setReadOnly(True)
        self.fileDirectoryInput.setObjectName("fileDirectoryInput")
        self.gridLayout.addWidget(self.fileDirectoryInput, 1, 1, 1, 1)
        self.loadFilesButton = QtWidgets.QPushButton(Window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadFilesButton.sizePolicy().hasHeightForWidth())
        self.loadFilesButton.setSizePolicy(sizePolicy)
        self.loadFilesButton.setMinimumSize(QtCore.QSize(100, 30))
        self.loadFilesButton.setMaximumSize(QtCore.QSize(100, 30))
        self.loadFilesButton.setObjectName("loadFilesButton")
        self.gridLayout.addWidget(self.loadFilesButton, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fileNameCount = QtWidgets.QLabel(Window)
        self.fileNameCount.setMinimumSize(QtCore.QSize(0, 15))
        self.fileNameCount.setMaximumSize(QtCore.QSize(16777215, 15))
        self.fileNameCount.setObjectName("fileNameCount")
        self.verticalLayout.addWidget(self.fileNameCount)
        self.pdfViewer = QtWebEngineWidgets.QWebEngineView(Window)
        self.pdfViewer.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.pdfViewer.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        self.pdfViewer.setMinimumSize(QtCore.QSize(560, 0))
        self.pdfViewer.setStyleSheet("background-color: rgb(0, 146, 82);")
        self.pdfViewer.setUrl(QtCore.QUrl("about:blank"))
        self.pdfViewer.setObjectName("pdfViewer")
        self.verticalLayout.addWidget(self.pdfViewer)
        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 2, 3)
        spacerItem1 = QtWidgets.QSpacerItem(234, 145, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)

        self.retranslateUi(Window)
        self.TypeLIst.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "PdfRenamerWithView"))
        self.fileDirectoryLabel.setText(_translate("Window", "Path:"))
        self.DateLabel.setText(_translate("Window", "Date (yyyyMMdd):"))
        self.DateInput.setDisplayFormat(_translate("Window", "yyyyMMdd"))
        self.IdLabel.setText(_translate("Window", "ID (ID_xxxx):"))
        self.TypeLabel.setText(_translate("Window", "Extra option:"))
        self.TypeLIst.setSortingEnabled(True)
        __sortingEnabled = self.TypeLIst.isSortingEnabled()
        self.TypeLIst.setSortingEnabled(False)
        item = self.TypeLIst.item(0)
        item.setText(_translate("Window", "CONTRACT"))
        item = self.TypeLIst.item(1)
        item.setText(_translate("Window", "DIPLOMA"))
        item = self.TypeLIst.item(2)
        item.setText(_translate("Window", "FORM"))
        item = self.TypeLIst.item(3)
        item.setText(_translate("Window", "PASSPORT"))
        item = self.TypeLIst.item(4)
        item.setText(_translate("Window", "REPORT"))
        item = self.TypeLIst.item(5)
        item.setText(_translate("Window", "RESUME"))
        item = self.TypeLIst.item(6)
        item.setText(_translate("Window", "TICKET"))
        item = self.TypeLIst.item(7)
        item.setText(_translate("Window", "WARRANT"))
        self.TypeLIst.setSortingEnabled(__sortingEnabled)
        self.newNameInput.setPlaceholderText(_translate("Window", "File new name"))
        self.renameButton.setText(_translate("Window", "Rename"))
        self.nextButton.setText(_translate("Window", "Next"))
        self.loadFilesButton.setText(_translate("Window", "Select"))
        self.fileNameCount.setText(_translate("Window", "PDF: *file_name.pdf*.  0 left."))