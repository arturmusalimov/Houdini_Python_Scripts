# PBR Texture Swapping Tool for Houdini

This script allows rapid cycling through directories of PBR texture sets and automatically applies them to a selected material node in Houdini. It reduces manual re-linking of textures, streamlining the look development process.

## Features

- **Automated Texture Assignment:**  
  Assigns base color (diffuse), normal, roughness, and displacement textures based on filename patterns.
  
- **Directory Cycling:**  
  Quickly navigate through multiple subfolders of texture sets using Next/Previous controls.

## Requirements

- Houdini
- Python environment with `hou` module (Houdini’s Python)
- `PySide2` (included in recent Houdini versions)

## Pre-Setup

All textures should contain identifying substrings:
- `diff` for base color maps
- `nor` for normal maps
- `rough` for roughness maps
- `disp` for displacement maps

Adjust your filenames before use.

## Usage

1. Place the script in a location accessible to Houdini (e.g., `pythonX.Xlibs`).
2. Run the script and select the root directory containing subfolders of PBR textures.
3. Select the material node to be updated.
4. Use **Next Material** or **Previous Material** to cycle through texture sets.

**Example Directory Structure:**

- `RootFolder/`
  - `MaterialSet01/`
    - `tree_diff.jpg`
    - `tree_nor.jpg`
    - `tree_rough.jpg`
    - `tree_disp.jpg`
  - `MaterialSet02/`
    - `rock_diff.png`
    - `rock_nor.png`
    - `rock_rough.png`
    - `rock_disp.png`
  - `MaterialSet03/`
    - `metal_diff.exr`
    - `metal_nor.exr`
    - `metal_rough.exr`
    - `metal_disp.exr`

The script will let you quickly switch among `MaterialSet01`, `MaterialSet02`, and `MaterialSet03`.

## License

This script is provided as-is. Feel free to modify and adjust it to fit your pipeline and naming conventions.






