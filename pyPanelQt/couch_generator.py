import hou
import os
from PySide2 import QtWidgets
from PySide2 import QtUiTools
from PySide2 import QtGui
from PySide2.QtCore import Qt

script_path = os.path.dirname(__file__)
print(script_path)

class CouchGenerator(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super(CouchGenerator, self).__init__(parent)
        print("Run Couch Generator")

        # UI Loader
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(script_path + "/couch_generator.ui")

        # Find and Set Image Widget
        self.image = self.ui.findChild(QtWidgets.QLabel, "image")
        self.image.setPixmap(script_path + "/couch2.jpg")

        self.width_slider = self.ui.findChild(QtWidgets.QSlider, "width_slider")
        self.side_height_slider = self.ui.findChild(QtWidgets.QSlider, "side_hight_slider")
        self.feet_height_slider = self.ui.findChild(QtWidgets.QSlider, "feet_height_slider")
        self.back_height_slider = self.ui.findChild(QtWidgets.QSlider, "back_height")
        self.back_depth_slider = self.ui.findChild(QtWidgets.QSlider, "back_depth")
        self.side_width_slider = self.ui.findChild(QtWidgets.QSlider, "side_width")
        self.back_cusion_height_slider = self.ui.findChild(QtWidgets.QSlider, "back_cusion_height")

        # Set slider ranges for float representation
        self.width_slider.setMinimum(200)
        self.width_slider.setMaximum(1000)  
        self.width_slider.setSingleStep(1)
    
        self.side_height_slider.setMinimum(0)
        self.side_height_slider.setMaximum(200)  
        self.side_height_slider.setSingleStep(1)

        self.feet_height_slider.setMinimum(0)
        self.feet_height_slider.setMaximum(200)  
        self.feet_height_slider.setSingleStep(1)

        self.back_height_slider.setMinimum(0)
        self.back_height_slider.setMaximum(200)  
        self.back_height_slider.setSingleStep(1)

        self.back_depth_slider.setMinimum(0)
        self.back_depth_slider.setMaximum(200)  
        self.back_depth_slider.setSingleStep(1)
        
        self.side_width_slider.setMinimum(0)
        self.side_width_slider.setMaximum(200)  
        self.side_width_slider.setSingleStep(1)
        
        self.back_cusion_height_slider.setMinimum(0)
        self.back_cusion_height_slider.setMaximum(200)  
        self.back_cusion_height_slider.setSingleStep(1)

        # Connections
        self.width_slider.valueChanged.connect(lambda: self.mod_attribute("width", self.width_slider.value() / 100.0))
        self.side_height_slider.valueChanged.connect(lambda: self.mod_attribute("side_height", self.side_height_slider.value() / 100))
        self.feet_height_slider.valueChanged.connect(lambda: self.mod_attribute("feet_height", self.feet_height_slider.value() / 100))
        self.back_height_slider.valueChanged.connect(lambda: self.mod_attribute("back_height", self.back_height_slider.value() / 100))
        self.back_depth_slider.valueChanged.connect(lambda: self.mod_attribute("back_depth", self.back_depth_slider.value() / 100))
        self.side_width_slider.valueChanged.connect(lambda: self.mod_attribute("side_width", self.side_width_slider.value() / 100))
        self.back_cusion_height_slider.valueChanged.connect(lambda: self.mod_attribute("back_cusion_height", self.back_cusion_height_slider.value() / 100))


        # Layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.ui)
        self.setLayout(self.layout)

    def mod_attribute(self, attr, value):
        print("Value: ", value)
        print("Attribute: ", attr)

        if attr == "width":
            hou.parm('/obj/couch/couch_generator/newparameter4').set(value)
        if attr == "side_height":
            hou.parm('/obj/couch/couch_generator/newparameter3').set(value)
        if attr == "feet_height":
            hou.parm('/obj/couch/couch_generator/height').set(value)
        if attr == "back_height":
            hou.parm('/obj/couch/couch_generator/newparameter2').set(value)
        if attr == "back_depth":
            hou.parm('/obj/couch/couch_generator/dist2').set(value)
        if attr == "side_width":
            hou.parm('/obj/couch/couch_generator/dist3').set(value)
        if attr == "back_cusion_height":
            hou.parm('/obj/couch/couch_generator/newparameter').set(value)
