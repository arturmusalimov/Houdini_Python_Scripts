# Move to Zero Tool for Houdini

This script adjusts the selected nodes' positions so that their lowest bounding box point aligns with the world origin (Y=0). It simplifies the process of quickly normalizing object placement in your scene.

## Features

- **Automatic Alignment:**  
  Moves the selected nodes so their minimum bounding box coordinate on the Y-axis sits at zero.
  
- **Batch Processing:**  
  Works on all currently selected nodes at once.

## Requirements

- Houdini
- Python environment with `hou` module (Houdini’s Python)

## Usage

1. **Select Nodes:**  
   Select one or more nodes whose position you want to reset.
   
2. **Run the Script:**  
   Execute the script in the Python shell or integrate it as a shelf tool.  
   The selected nodes are automatically adjusted so that their geometry's lowest point sits at Y=0.

## Notes

- This tool only affects the Y-position of nodes.
- Useful for quickly normalizing assets before placement or instancing.
