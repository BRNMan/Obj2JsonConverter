import sys
import json

inputFile = "yanma.obj"
outputFile = "test.json"

vertexPositions =[]
vertexNormals = []
vertexTextureCoords = []
textureCoordIndices = []
normalIndices = []
indices = []

f = open(inputFile, "r")
for line in f:
	if(line[0] == '#'):
		continue
	splitLine = line.split(' ')
	if(splitLine[0] == 'v'):
		vertexPositions.append(float(splitLine[1]))
		vertexPositions.append(float(splitLine[2]))
		vertexPositions.append(float(splitLine[3]))
	elif(splitLine[0] == 'vt'):
		vertexTextureCoords.append(float(splitLine[1]))
		vertexTextureCoords.append(float(splitLine[2]))
	elif(splitLine[0] == 'vn'):
		vertexNormals.append(float(splitLine[1]))
		vertexNormals.append(float(splitLine[2]))
		vertexNormals.append(float(splitLine[3]))
	elif(splitLine[0] == 'f'):
		# Indexed starting at 1
		indices.append(int(splitLine[1].split('/')[0])-1)
		indices.append(int(splitLine[2].split('/')[0])-1)
		indices.append(int(splitLine[3].split('/')[0])-1)
		textureCoordIndices.append(int(splitLine[1].split('/')[1])-1)
		textureCoordIndices.append(int(splitLine[2].split('/')[1])-1)
		textureCoordIndices.append(int(splitLine[3].split('/')[1])-1)
		normalIndices.append(int(splitLine[1].split('/')[2])-1)
		normalIndices.append(int(splitLine[2].split('/')[2])-1)
		normalIndices.append(int(splitLine[3].split('/')[2])-1)

f.close()

#Now map each texture coord and normal to a vertex using the mappings from the faces.
sortedTextureCoords = [0.0]*int(2*len(vertexPositions)/3)
for i in range(0, len(indices)):
	texCoordIndex = textureCoordIndices[i]
	vertexIndex = indices[i]
	sortedTextureCoords[vertexIndex*2] = vertexTextureCoords[texCoordIndex*2]
	sortedTextureCoords[vertexIndex*2+1] = vertexTextureCoords[texCoordIndex*2+1]

sortedNormals = [0.0]*int(2*len(vertexPositions)/3)
for i in range(0, len(indices)):
	normalIndex = normalIndices[i]
	vertexIndex = indices[i]
	sortedNormals[vertexIndex*2] = vertexTextureCoords[normalIndex*2]
	sortedNormals[vertexIndex*2+1] = vertexTextureCoords[normalIndex*2+1]


x = {
	"vertexPositions" : vertexPositions,
	"vertexTextureCoords" : sortedTextureCoords,
	"vertexNormals" : sortedNormals,
	"indices" : indices,
}

f = open(outputFile, "w")
f.write(json.dumps(x))
f.close()
