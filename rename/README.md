# Node Renaming Tool for Houdini

This script provides a live, non-destructive node renaming interface for Houdini. It allows dynamic search-and-replace operations on selected node names, as well as applying prefixes and suffixes. Changes are reflected immediately, simplifying iterative naming workflows.

## Features

- **Search and Replace:**  
  Dynamically rename node names based on a user-defined search string and its replacement.
  
- **Prefix and Suffix Addition:**  
  Automatically add prefix and suffix strings to existing node names.
  
- **Live Updates:**  
  Names update as soon as values change, eliminating the need for repeated manual edits.

## Requirements

- Houdini
- Python environment with `hou` module (Houdini’s Python)
- `PySide2` (included in recent Houdini versions)

## Usage

1. **Select Nodes:**  
   Select the nodes in your network that you want to rename.

2. **Run the Script:**  
   Execute the script within Houdini’s Python environment or create a shelf tool to launch it.

3. **Set Search and Replace Parameters:**  
   Enter the text to be searched and replaced. Use the prefix/suffix fields to prepend or append text to existing names.

4. **Resetting or Canceling Changes:**  
   Click **Reset** to revert selected nodes to their default type-based names. Click **Cancel** to restore their original names and close the window.

## Notes

- Spaces are automatically converted to underscores.
- All changes are applied in real-time. If you need to discard changes, use the **Cancel** button before closing the tool.

## License

This script is provided as-is. Feel free to modify and adjust it to fit your pipeline and naming conventions.