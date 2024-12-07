# Custom PyPanel with Qt UI for Houdini

This script provides a custom PySide2-based UI for adjusting couch parameters in Houdini. It uses sliders for dimension and property control, references an external `.ui` file for layout, and displays background images for visual context. The panel can be integrated as a PyPanel or embedded as a custom parameter view within Houdini.

## Features

- **Slider-Based Parameter Control:**  
  Allows direct manipulation of various couch attributes (width, side height, feet height, back height, back depth, side width, and back cushion height) via sliders.
  
- **UI File Integration:**  
  Loads the interface layout from an external `.ui` file, keeping the code organized and maintainable.
  
- **Background Imagery:**  
  Uses background images as visual references to provide context while adjusting parameters.

- **Parameter Linking:**  
  Updates corresponding parameters on the specified node (`/obj/couch/couch_generator/...`) in real-time as slider values change.

## Requirements

- Houdini
- Python environment with `hou` module (Houdini’s Python)
- `PySide2` (included in recent Houdini versions)
- `couch_generator.ui` file in the same directory as the script
- Supporting images (e.g. `couch2.jpg`) in the same directory

## Usage

1. **Setup:**  
   Place the `.ui` file and the image files in the same directory as the script.
   
2. **Load in Houdini:**  
   - Integrate the script as a PyPanel in the Windows > PyPanels menu, or  
   - Add it as a custom parameter view.

3. **Adjusting Parameters:**  
   Use the sliders to modify couch attributes. The associated node parameters will update instantly, allowing for immediate visual feedback.

4. **Customization:**  
   The `.ui` file and background images can be replaced or modified to fit different asset requirements.

## Notes

- Ensure that the node path (`/obj/couch/couch_generator`) and parameter names match the ones expected by the script.
- The value ranges and increments are set in code. Adjust them if needed.

## License

This script is provided as-is. Feel free to modify and adjust it to fit your pipeline and naming conventions.
