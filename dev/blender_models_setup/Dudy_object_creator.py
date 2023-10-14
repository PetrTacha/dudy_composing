import bpy
from bpy.types import Panel, Operator

# Define the Panel class
class DUDYToolPanel(Panel):
    bl_label = "DUDY Tool"
    bl_idname = "PT_DUDYToolPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'DUDY Tool'

    def draw(self, context):
        layout = self.layout

        # Input fields for X and Y scale
        layout.label(text="Scale (it will be divided by 100):")
        layout.label(text="Try to be near 300x300px.")
        layout.prop(context.scene, "custom_scale_x")
        layout.prop(context.scene, "custom_scale_y")

        # Button to create the plane
        layout.operator("object.create_plane")

# Define the Operator class to create the plane
class CreatePlaneOperator(Operator):
    bl_label = "Create Plane"
    bl_idname = "object.create_plane"

    def execute(self, context):
        # Clear existing objects and data
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type='MESH')
        bpy.ops.object.delete()

        # Get the custom X and Y scale values
        scale_x = context.scene.custom_scale_x
        scale_y = context.scene.custom_scale_y

        # Create a new plane object
        bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=(0, 0, 0))
        plane = bpy.context.object

        # Scale the plane
        plane.scale.x = scale_x /100
        plane.scale.y = scale_y /100

        return {'FINISHED'}

# Register the classes
def register():
    bpy.utils.register_class(DUDYToolPanel)
    bpy.utils.register_class(CreatePlaneOperator)
    bpy.types.Scene.custom_scale_x = bpy.props.FloatProperty(name="X Scale", default=1)
    bpy.types.Scene.custom_scale_y = bpy.props.FloatProperty(name="Y Scale", default=1)

def unregister():
    bpy.utils.unregister_class(DUDYToolPanel)
    bpy.utils.unregister_class(CreatePlaneOperator)
    del bpy.types.Scene.custom_scale_x
    del bpy.types.Scene.custom_scale_y

if __name__ == "__main__":
    register()