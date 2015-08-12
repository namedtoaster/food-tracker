# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Sun Aug  9 02:11:53 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, QtXml
from update import update_food_list
from PyQt4.QtGui import QListView

program_title = "Food"

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        QtGui.QWidget.__init__(self)

        """Create the QListWidget based on the data pulled from the XML file"""
        self.xmlList = XmlList()
        
        self.xmlList.setFixedWidth(300)
        self.xmlList.setSortingEnabled(True)
        self.xmlList.sortItems()
        
        self.setCentralWidget(self.xmlList)
        
        self.statusBar().showMessage("Ready")
        #self.setupUi(self)
        self.resize(700, 700)

    def update(self):
        update_food_list()

    def open(self):
        """Eventually change to dialog box; for now, we'll always be using
        the same file"""

        filename = 'xml/food_list.xml'

        """An unecessary check now, but once the user has the ability to open
        a file, must check if a file has been selected. If not, return to the
        main program

        if not filename:
            return
        """
        
        in_file = QtCore.QFile('xml/food_list.xml')
        """If the file fails to open, flash warning message"""
        if not in_file.open(QtCore.QIODevice.ReadOnly):
            QtGui.QMessageBox.warning(self, program_title,
                                      "cannot read file %s:\n%s." % (filename,
                                                                     in_file.errorString()))
            return

        if self.xmlList.read(in_file):
            print ""
                
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(772, 690)
        self.centralwidget = QtGui.QWidget(MainWindow)
        #self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidget = XmlList(self.centralwidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.headerItem().setText(0, _fromUtf8("1"))
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuNew = QtGui.QMenu(self.menuFile)
        self.menuNew.setObjectName(_fromUtf8("menuNew"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionNew_Cookbook = QtGui.QAction(MainWindow)
        self.actionNew_Cookbook.setObjectName(_fromUtf8("actionNew_Cookbook"))
        self.actionNew_Recipe = QtGui.QAction(MainWindow)
        self.actionNew_Recipe.setObjectName(_fromUtf8("actionNew_Recipe"))
        self.actionNew_Food_Item = QtGui.QAction(MainWindow)
        self.actionNew_Food_Item.setObjectName(_fromUtf8("actionNew_Food_Item"))
        self.actionModify_Cookbook = QtGui.QAction(MainWindow)
        self.actionModify_Cookbook.setObjectName(_fromUtf8("actionModify_Cookbook"))
        self.actionModify_Recipe = QtGui.QAction(MainWindow)
        self.actionModify_Recipe.setObjectName(_fromUtf8("actionModify_Recipe"))
        self.actionModify_Food_Item = QtGui.QAction(MainWindow)
        self.actionModify_Food_Item.setObjectName(_fromUtf8("actionModify_Food_Item"))
        self.menuNew.addAction(self.actionNew_Cookbook)
        self.menuNew.addAction(self.actionNew_Recipe)
        self.menuNew.addAction(self.actionNew_Food_Item)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionModify_Cookbook)
        self.menuEdit.addAction(self.actionModify_Recipe)
        self.menuEdit.addAction(self.actionModify_Food_Item)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Food Tracker", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuNew.setTitle(_translate("MainWindow", "New...", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionNew_Cookbook.setText(_translate("MainWindow", "New Cookbook...", None))
        self.actionNew_Recipe.setText(_translate("MainWindow", "New Recipe...", None))
        self.actionNew_Food_Item.setText(_translate("MainWindow", "New Food Item...", None))
        self.actionModify_Cookbook.setText(_translate("MainWindow", "Modify Cookbook...", None))
        self.actionModify_Recipe.setText(_translate("MainWindow", "Modify Recipe...", None))
        self.actionModify_Food_Item.setText(_translate("MainWindow", "Modify Food Item...", None))


class XmlList(QtGui.QListWidget):
    def __init__(self, parent=None):
        super(XmlList, self).__init__(parent)

        self.domDocument = QtXml.QDomDocument()
        self.domElementForItem = {}

    def read(self, device):
        ok, errorStr, errorLine, errorColumn = self.domDocument.setContent(device)
        if not ok:
            QtGui.QMessageBox.information(self.window(), program_title,
                                          "Parse error at line %d, column %d:\n%s" % (errorLine, errorColumn, errorStr))
            return False

        root = self.domDocument.documentElement()
        self.clear()

        child = root.firstChildElement('item')
        
        while not child.isNull():
            """The next parsed element will always be an item, i.e. another food item
            in the XML file. Each respective child will not pass in a parent because
            aside from the list parent, there is no parent. The list tag only serves
            as a container for all the items."""
            self.parseItemElement(child)
            """Once the current food item has been processed, move onto the next food
            item and parse it's children. It is important to note that all children
            of each food item will be parsed in the parseItemElement function."""
            child = child.nextSiblingElement('item')
            
    def parseItemElement(self, element, parentItem=None):
        """Calling createItem will set the current object, whether it is a food item or
        a child of the food item, as a QListWidgetItem. The only time that a parent is
        passed into the parseItemElement function is when parsing children of the food
        item type."""
        item = self.createItem(element, parentItem)
        
        """The only time we care about the name of any of these elements is when parsing
        food item children. And since the highest level node is the food item, it's name
        will never be processed. It doesn't have a name anyway other than what it's child
        element 'name' reports."""
        name = element.firstChildElement('name').text()

        if not name:
            name = "Food"
        
        item.setText(name)
        
        child = element.firstChildElement()
        
        while not child.isNull():
            if child.tagName() == 'item':
                self.parseItemElement(child, item)
            if child.tagName() == 'id':
                """Set the attributes to the parent with ID being an attribute..."""
                self.domElementForItem[id(item)] = [str(child.text()), element]
            elif child.tagName() == 'name':
                """Since the name for the food item is already set, there is no
                need to go any further"""
                return
            child = child.nextSiblingElement()
        
    def createItem(self, element, parentItem=None):
        item = QtGui.QListWidgetItem()

        if parentItem is not None:
            item = QtGui.QListWidgetItem(parentItem)
        else:
            item = QtGui.QListWidgetItem(self)
        
        self.domElementForItem[id(item)] = [element]

        return item
        
if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    ex.open()
    sys.exit(app.exec_())
    
