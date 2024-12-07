# Houdini Utility Scripts

This repository contains multiple tools aimed at improving workflows within Houdini. Each tool is organized in its own directory, with its own dedicated `README.md` providing instructions and requirements. The main purpose of this top-level documentation is to give an overview of the available scripts and their functions.

## Tools Overview

1. **Asset Versioning Tool**  
   A script that automates versioning of `.hip` files, incrementing file names and allowing rollback to previous versions.

2. **PBR Texture Swapping Tool**  
   A script for quickly cycling through folders containing PBR texture sets, streamlining the process of assigning new textures to a material node.

3. **Node Renaming Tool**  
   An interface that provides live, non-destructive renaming of selected nodes, with search/replace functionality and optional prefix/suffix application.

4. **Move to Zero Tool**  
   A script that adjusts selected nodes so their lowest bounding box point sits at world Y=0, simplifying object placement normalization.

5. **Custom PyPanel with Qt UI**  
   A tool with a PySide2-based UI that controls various couch parameters in Houdini. It relies on a `.ui` file and background imagery, and can be loaded as a PyPanel or custom parameter view.

## Directory Structure

The repository is structured into separate subdirectories, each containing:

- The Python script(s)
- A `README.md` with usage instructions, requirements, and configuration notes
- Additional files such as `.ui` files or images if required

Refer to the individual `README.md` files in each tool’s folder for detailed instructions on setup and operation.
