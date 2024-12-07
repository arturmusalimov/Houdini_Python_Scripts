import hou
import os
import PySide2 as ps

class VersioningTool:
    def __init__(self, root_path, asset_name):
        self.root_path = root_path
        self.asset_name = asset_name
        self.asset_versions = self.get_existing_versions()

    # Check the root directory for existing versions
    def get_existing_versions(self):
        asset_versions = []
        for f in os.listdir(self.root_path):
            if f.startswith(self.asset_name) and f.endswith(".hip"):            
                asset_versions.append(f)
        return sorted(asset_versions)

    # Find the next version number based on the highest current version
    def get_next_version(self):
        if not self.asset_versions:
            return 1                                                            
        latest_version = self.asset_versions[-1]
        version_num = int(latest_version.split("_v")[-1].split(".")[0])         
        return version_num + 1  
    
    # New versioned file based on the next available version number
    def save_new_version(self):    
        next_version = self.get_next_version()
        new_version_name = f"{self.asset_name}_v{next_version:02d}.hip"
        new_version_path = os.path.join(self.root_path, new_version_name)
    
        print(f"Saving new version: {new_version_path}")
        hou.hipFile.save(new_version_path)                                      
        self.asset_versions.append(new_version_name)                           

    # Load to a previous version
    def rollback_version(self, version_number):
        version_name = f"{self.asset_name}_v{version_number:02d}.hip"
        if version_name in self.asset_versions:
            version_path = os.path.join(self.root_path, version_name)
            print("Rolling back to: " + version_path)
            hou.hipFile.load(version_path)                                      
        else:
            print("Version " + version_number + " not found.")
    
# Creating GUI 
class CreateVersioningWindow(ps.QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CreateVersioningWindow, self).__init__(parent)
        self.setWindowTitle("Asset Versioning Tool")
        self.setMinimumSize(400, 150)

        self.versioning_tool = None

        self.createWidgets()
        self.createLayouts()
        self.createConnections()

        last_directory = self.load_last_directory()
        self.rootPathLineEdit.setText(last_directory)

    def createWidgets(self):

        self.rootPathLineEdit = ps.QtWidgets.QLineEdit()
        self.rootPathButton = ps.QtWidgets.QPushButton("Select Root Directory")
        
        # Input asset name
        self.assetNameLineEdit = ps.QtWidgets.QLineEdit()
        
        # Buttons for save, refresh and load
        self.saveVersionButton = ps.QtWidgets.QPushButton("Save New Version")
        self.rollbackButton = ps.QtWidgets.QPushButton("Load Version")
        self.refreshObjectButton = ps.QtWidgets.QPushButton("Refresh Selection")

    def createLayouts(self):
        # Layout for the root path selection
        rootPathLayout = ps.QtWidgets.QHBoxLayout()
        rootPathLayout.addWidget(self.rootPathLineEdit)
        rootPathLayout.addWidget(self.rootPathButton)

        # Layout for the asset name input and version buttons
        assetLayout = ps.QtWidgets.QHBoxLayout()
        assetLayout.addWidget(self.assetNameLineEdit)
        assetLayout.addWidget(self.refreshObjectButton)

        buttonLayout = ps.QtWidgets.QHBoxLayout()
        buttonLayout.addWidget(self.saveVersionButton)
        buttonLayout.addWidget(self.rollbackButton)

        # Main layout
        mainLayout = ps.QtWidgets.QVBoxLayout(self)
        mainLayout.addLayout(rootPathLayout)
        mainLayout.addLayout(assetLayout)
        mainLayout.addLayout(buttonLayout)

    def save_last_directory(self, path):
        # Store the path in hou.session
        hou.session.last_directory = path

    def load_last_directory(self):
        # Check if the last_directory exists in hou.session
        return getattr(hou.session, 'last_directory', '')   


    def createConnections(self):
        # Connect the root path button to the file chooser
        self.rootPathButton.clicked.connect(self.selectRootPath)
        # Connect the buttons to their respective functions
        self.saveVersionButton.clicked.connect(self.saveNewVersion)
        self.rollbackButton.clicked.connect(self.rollbackVersion)
        self.refreshObjectButton.clicked.connect(self.select_first_selected_object)

    def selectRootPath(self):
        root_path = ps.QtWidgets.QFileDialog.getExistingDirectory(self, "Select Root Directory")
        if root_path:
            self.rootPathLineEdit.setText(root_path)
            self.save_last_directory(root_path)  # Save the root directory in hou.session

    def saveNewVersion(self):

        self.select_first_selected_object()

        # Save a new version of the asset
        root_path = self.rootPathLineEdit.text()
        asset_name = self.assetNameLineEdit.text()
        if not self.versioning_tool:
            self.versioning_tool = VersioningTool(root_path, asset_name)
        self.versioning_tool.save_new_version()

    def rollbackVersion(self):
        # Roll back to a previous version (prompt for version number)
        root_path = self.rootPathLineEdit.text()
        asset_name = self.assetNameLineEdit.text()
        version_number, ok = ps.QtWidgets.QInputDialog.getInt(self, "Rollback Version", "Enter version number to rollback:")
        if ok:
            if not self.versioning_tool:
                self.versioning_tool = VersioningTool(root_path, asset_name)
            self.versioning_tool.rollback_version(version_number)

    def select_first_selected_object(self):
        # Get the list of selected nodes in Houdini
        selected_nodes = hou.selectedNodes()

        # If there are selected nodes, use the first one
        if selected_nodes:
            first_selected_node = selected_nodes[0]  # Get the first selected node
            self.assetNameLineEdit.setText(first_selected_node.name())  # Set the node's name in the line edit
        else:
            self.assetNameLineEdit.setText('') # Clear the field if no object is selected


# Example to run the dialog
try:
    CreateVersioningWindow.close()
    CreateVersioningWindow.deleteLater()
except:
    pass

CreateVersioningWindow = CreateVersioningWindow()
CreateVersioningWindow.show()