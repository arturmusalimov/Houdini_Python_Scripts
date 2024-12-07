# PBR Texture Swapping Tool for Houdini

This Python script helps you quickly swap out sets of PBR materials in Houdini. It’s designed to speed up browsing through large collections of textures, letting you easily cycle through different material sets and instantly apply them to a chosen material node in your scene.

## What This Script Does

- **Automates Material Swapping:**  
  Cycle through folders that contain sets of textures (diffuse, normal, roughness, displacement) with simple Next/Previous buttons.
  
- **Quick Previewing:**  
  Quickly test different texture sets without manually re-linking every file.

- **Faster Workflow:**  
  Switch from one PBR material to another in seconds, helping you find the perfect look faster.

## Why It’s Good

- **Time-Saving:**  
  No more manually browsing through file dialogs or manually setting texture paths.
  
- **Easy Iteration:**  
  Quickly see how different texture sets look without stopping your workflow.
  
- **Simple UI Integration:**  
  The provided user interface makes it easy to choose a root directory and flip through subfolders.

## Important Pre-Work

You need to ensure that your texture files are named in a way the script can recognize them. For example, the script looks for these keywords in file names:  
- `"diff"` for base color (diffuse) textures  
- `"nor"` for normal maps  
- `"rough"` for roughness maps  
- `"disp"` for displacement maps

Before you run the script, rename your textures so they include these keywords. For example:  
- `myTexture_diff.png`  
- `myTexture_nor.png`  
- `myTexture_rough.png`  
- `myTexture_disp.png`

If the files follow this naming convention, the script will automatically link them to the correct material parameters.

## How to Use

1. **Place the Script:**  
   Put the script in a location where Houdini can access it (e.g., your Houdini `pythonX.Xlibs` folder).

2. **Open in Houdini:**  
   Launch Houdini and run the script in the Python shell, or make a shelf tool to load it.

3. **Set Root Directory:**  
   In the pop-up window, choose the root folder containing all the subfolders of PBR textures.

4. **Select a Material Node:**  
   In the network view, select the material node you want to test textures on.

5. **Cycle Through Textures:**  
   Use the **Next Material** and **Previous Material** buttons to move through the list of subfolders. The script will instantly update the selected material node with the textures from the chosen folder.

## Example Structure

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






