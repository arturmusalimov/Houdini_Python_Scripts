import hou

from PySide2 import QtWidgets

# Main window always in foreground 
def getHoudiniMainWindow():
    return hou.qt.mainWindow()

class RenameTool(QtWidgets.QDialog): 
    def __init__(self, nodes, parent=getHoudiniMainWindow()):     
        super(RenameTool, self).__init__(hou.qt.mainWindow())
        self.nodes = nodes
        self.storeNodeNames()
        self.configure_dialog()
        self.widgets()
        self.layouts()
        self.connections()

    # Title and size of main winodw
    def configure_dialog(self):
        self.setWindowTitle("Live node renamer")
        self.setMinimumWidth(480)
        self.setMinimumHeight(340)

    # Declaring windgets
    def widgets(self): 
        self.search = QtWidgets.QLineEdit()
        self.search.setPlaceholderText("Search")

        self.replace = QtWidgets.QLineEdit()
        self.replace.setPlaceholderText("Replace")

        self.sep = hou.qt.Separator()

        self.prefix = QtWidgets.QLineEdit()
        self.suffix = QtWidgets.QLineEdit()

        self.resetButton = QtWidgets.QPushButton("Reset")

        self.okButton = QtWidgets.QPushButton("Rename")
        self.cancelButton = QtWidgets.QPushButton("Cancel")

    # Building layout with widgets    
    def layouts(self): 
        self.mainLayout = QtWidgets.QVBoxLayout(self)

        self.mainLayout.addWidget(self.search)
        self.mainLayout.addWidget(self.replace)
        
        self.mainLayout.addWidget(self.sep)

        self.optionsLaysout = QtWidgets.QFormLayout()
        self.optionsLaysout.addRow("Prefix", self.prefix)
        self.optionsLaysout.addRow("Suffix", self.suffix)

        self.mainLayout.addLayout(self.optionsLaysout)
        self.mainLayout.addWidget(self.sep)

        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.addWidget(self.okButton)
        self.buttonLayout.addWidget(self.resetButton)
        self.buttonLayout.addWidget(self.cancelButton)

        self.mainLayout.addLayout(self.buttonLayout)

    def storeNodeNames(self):
        self.nodeNames = {}
        for node in self.nodes:
            self.nodeNames[node] = node.name()
    
    def restoreNames(self):
        for node in self.nodes:
            node.setName(self.nodeNames[node])
        self.close()

    def rename(self):
        searchText = self.search.text().replace(" ", "_")
        replaceText = self.replace.text().replace(" ", "_")
        prefixText = self.prefix.text().replace(" ", "_")
        suffixText = self.suffix.text().replace(" ", "_")

        for node in self.nodes: 
            originalName = self.nodeNames[node]

            if searchText in originalName and searchText and replaceText:
                modifiedName = originalName.replace(searchText, replaceText)
            else: 
                modifiedName = originalName

            modifiedName = prefixText + modifiedName + suffixText
            node.setName(modifiedName, unique_name=True)

    def resetSelectedName(self):
        for node in self.nodes:
            node.setName(node.type().name(), unique_name=True)

    def connections(self):
        self.cancelButton.clicked.connect(self.restoreNames)
        self.cancelButton.clicked.connect(self.close)
        self.okButton.clicked.connect(self.close)
        self.resetButton.clicked.connect(self.resetSelectedName)

        self.search.textChanged.connect(self.rename)
        self.replace.textChanged.connect(self.rename)
        self.prefix.textChanged.connect(self.rename)
        self.suffix.textChanged.connect(self.rename)
    

