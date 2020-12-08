# Obj2JsonConverter
Simple utility to convert an obj file to a JSON file for webgl use using one texture.

## Installation
Use this with python3, and change the inputFile and outputFile to whatever files you need.

## Usage
First, export your obj file using blender. This program will not recognize different materials so either bake your materials into one texture or just use a model without materials. Run the program, and you should get a json file as output with vertices, their indices, and normals and texture coordinates for each vertex. Import the file into your webgl program, and extract each of the following fields:
	"vertexPositions"
	"vertexTextureCoords"
	"vertexNormals"
	"indices"
