import hou

selected_nodes = hou.selectedNodes()

for node in selected_nodes:
        
        geo = node.geometry()
        bounding_box = geo.boundingBox()
        min_y_local = bounding_box.minvec().y()
        world_pos_y = node.parm('ty').eval()
        translate_y = world_pos_y - min_y_local
        node.parm('ty').set(translate_y)

