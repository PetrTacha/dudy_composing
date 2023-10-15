## Dudy composing

Builds are in parent directory, assets are only required if the testing `config.json` is used.

| Command                 | Description          |
|-------------------------|----------------------|
| Install for development | `npm install`        |
| Build for production    | `npm run build-prod` |
| Build for development   | `npm run build`      |


## How to make new model
In folder blender_models_setup are 3 files, the .blend and .blend1 files is blender file with example of new model.
The process is as follows:
1. open Blender
2. remove everything from scene
3. create plane mesh with width and height near 3.00x3.00 (check the resolution of the image, teh plane must have the same resolution)
4. add material, in shader remove BSDF, create new node Image texture.
5. link the image texture (with selected picture) to the Material output Surface.
6. in edit mode, use knife to cut out the shape + remove vertices.
7. export as .glb file
8. in export deselect: Transform (+Y Up), and animation

For faster creating, the folder contain blender script Dudy_object_creator.py. 
The script make tool menu, with 2 inputs X and Y, where you can add size of the png picture and button create plane, which create plane mesh from the given inputs (the inputs are divided by 100). 
