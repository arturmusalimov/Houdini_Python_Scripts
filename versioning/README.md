# Asset Versioning Tool for Houdini

This is a simple Python script that helps you manage asset versions in Houdini. It automates version naming and makes it easy to quickly save new versions, roll back to older ones, and keep track of your work.

## Features

- **Automatic Versioning:** Automatically increments and saves a new `.hip` file each time you create a new version.
- **Rollback Capability:** Easily load a previous version by specifying the version number.
- **Asset Name Detection:** Quickly set the asset name by selecting an object in the scene.
- **Simple GUI:** A straightforward PySide2-based UI for selecting a directory, setting the asset name, and managing versions.

## Requirements

- Houdini
- Python environment with `hou` module (available in Houdini’s Python environment)
- `PySide2` (included with recent versions of Houdini)

## Installation

1. **Place the Script:**  
   Copy the script into your `houdini/python3.7libs` directory (or your current Houdini’s `pythonX.Xlibs` directory).
   
2. **Run the Tool:**  
   Open Houdini and run the script in the Python shell, or integrate it into a shelf tool.

## Usage

1. **Open the Dialog:**  
   When you run the script, a UI window will appear.
   
2. **Set Root Directory:**  
   Choose or enter the root directory where you want versions to be stored.
   
3. **Set Asset Name:**  
   Select an object in your scene and press **Refresh Selection** to set the asset name automatically, or type it manually.
   
4. **Save a New Version:**  
   Click **Save New Version**. A new `.hip` file with the next version number will be created.
   
5. **Rollback to a Previous Version:**  
   Click **Load Version** and enter the version number you want to load. The scene will switch to that version.

## Example

- Suppose your root directory is `C:/Projects/Assets` and your asset name is `tree`.  
- The tool will create files like `tree_v01.hip`, `tree_v02.hip`, and so on.  
- Loading version 2 will revert your scene to `tree_v02.hip`.

## Notes

- The tool remembers the last directory used in the current session.
- Ensure your selected node or entered asset name matches the naming convention you want for your versions.
- Always double-check the version number before rolling back to avoid losing recent changes.

## License

This script is provided as-is. Feel free to modify, share, or integrate it into your workflows.