import hou
import os
import PySide2 as ps

class TextureAssigner:
    # Initialize
    def __init__(self, root_path):
        self.root_path = root_path
        self.current_index = 0
        self.subfolders = []
        
        # Get all subfolders in the root directory to loop through later
        for f in os.scandir(root_path):
            if f.is_dir():
                self.subfolders.append(f.path)
         

    # Return the path of the current folder based on current_index
    def get_current_folder(self):
        if self.current_index >= len(self.subfolders):
            self.current_index = 0  
        elif self.current_index < 0:
            self.current_index = len(self.subfolders) - 1
        return self.subfolders[self.current_index]

    # Apply textures from the current folder to the material parameters
    def apply_textures(self, material):
        path = self.get_current_folder()
        print("Applying textures from: " + path)
        files = os.listdir(path)

        for image in files:
            if "diff" in image:
                hou.parm('/stage/materiallibrary1/PBR_SKin/base_color_image/file').set(path + "/" + image)
            if "nor" in image:
                hou.parm('/stage/materiallibrary1/PBR_SKin/normal_image/file').set(path + "/" + image)
            if "rough" in image:
                hou.parm('/stage/materiallibrary1/PBR_SKin/spec_rough_image/file').set(path + "/" + image)
            if "disp" in image:
                hou.parm('/stage/materiallibrary1/PBR_SKin/displacement_image/file').set(path + "/" + image)

    def move_to_next_folder(self):
        self.current_index += 1
        if self.current_index >= len(self.subfolders):
            self.current_index = 0  

    def move_to_previous_folder(self):
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.subfolders) - 1 

def getHoudiniMainWindow():
    return hou.qt.mainWindow()

# Set GUI window properties
class CreateWindow(ps.QtWidgets.QDialog):
    def __init__(self, parent=getHoudiniMainWindow()):
        super(CreateWindow, self).__init__(parent)

        self.setWindowTitle("Texture Loop Assign")
        self.setMinimumSize(300, 120)

        self.textureAssigner = None  
        self.createWidgets() 
        self.createLayouts()  
        self.createConnections() 

    def createWidgets(self):
        self.texturePathLineEdit = ps.QtWidgets.QLineEdit()  
        self.texturePathButton = hou.qt.FileChooserButton() 
        self.nextFolderButton = ps.QtWidgets.QPushButton("Next Material")  
        self.previousFolderButton = ps.QtWidgets.QPushButton("Previous Material")  

        self.texturePathButton.setFileChooserTitle("Select Root Directory")
        self.texturePathButton.setFileChooserMode(hou.fileChooserMode.Read)
        self.texturePathButton.setFileChooserFilter(hou.fileType.Directory)

    def createLayouts(self):
        directoryPathLayout = ps.QtWidgets.QHBoxLayout()
        directoryPathLayout.addWidget(self.texturePathLineEdit)
        directoryPathLayout.addWidget(self.texturePathButton)

        buttonLayout = ps.QtWidgets.QHBoxLayout()
        buttonLayout.addWidget(self.previousFolderButton)
        buttonLayout.addWidget(self.nextFolderButton)

        formLayout = ps.QtWidgets.QFormLayout()
        formLayout.addRow("Path to Root Folder: ", directoryPathLayout)
        formLayout.addRow(buttonLayout)

        mainLayout = ps.QtWidgets.QVBoxLayout(self)
        mainLayout.addLayout(formLayout)

    # Connect user actions (button clicks) to the corresponding methods
    def createConnections(self):
        self.texturePathButton.fileSelected.connect(self.setTexturePathLineEditText)
        self.nextFolderButton.clicked.connect(self.moveToNextFolder)
        self.previousFolderButton.clicked.connect(self.moveToPreviousFolder)

    # Set the text of the line edit to the selected file path
    def setTexturePathLineEditText(self, file_path):    
        self.texturePathLineEdit.setText(file_path)
        self.textureAssigner = TextureAssigner(file_path)  

    # Move to the next folder and apply textures
    def moveToNextFolder(self):        
        if not self.textureAssigner:
            print("No root folder selected.")
            return
        self.textureAssigner.move_to_next_folder()
        self.assignTextures()

    # Move to the previous folder and apply textures
    def moveToPreviousFolder(self):
        if not self.textureAssigner:
            print("No root folder selected.")
            return
        self.textureAssigner.move_to_previous_folder()
        self.assignTextures()

    # Apply textures from the current folder to the selected material in Houdini
    def assignTextures(self):
        if not self.textureAssigner:
            print("No root folder selected.")
            return
        material = hou.selectedNodes()[0] 
        self.textureAssigner.apply_textures(material)

try:
    CreateWindow.close()
    CreateWindow.deleteLater()
except:
    pass
CreateWindow = CreateWindow()
CreateWindow.show()