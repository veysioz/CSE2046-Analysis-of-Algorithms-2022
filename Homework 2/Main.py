from os import walk
import re

class Vertex:
    def __init__(self, number):
        self.number = number
        self.color = None
        self.adjacents = []

vertices = []
colors = []
o_num = 1

def search_vertex(number):
    for vertex in vertices:
        if vertex.number == number: return vertex
    
    vertex = Vertex(number)
    vertices.append(vertex)
    return vertex

def colorize_vertices():
    for vertex in vertices:
        temp = [] # Stores colorized adjacents

        for adjacent in vertex.adjacents:
            if adjacent.color != None: temp.append(adjacent)
        
        for i in range(len(colors), len(temp) + 1): colors.append(i)

        col = None
        for color in colors:
            found = True
            
            for t in temp:
                if t.color == color: found = False

            if found:
                col = color
                break
            
        vertex.color = col

def print_output():
    global o_num
    name = 'output' + str(o_num) + '.txt'
    with open("output/" + name, "w") as f:
        used_colors = -1
        for vertex in vertices:
            if vertex.color > used_colors: used_colors = vertex.color

        print(used_colors + 1, file=f)
        
        for i in range(len(vertices)):
            for vertex in vertices:
                if str(i+1) == vertex.number:
                    if i+1 == len(vertices): print(vertex.color, end="", file=f)
                    else: print(vertex.color, end=" ", file=f)
                    break
        
    f.close()
    
    o_num = o_num + 1

    print(name + " is written to output folder.")

def main():
    files = []

    for (path, dir, name) in walk("input/"):
        files.extend(name)
        break

    for n in files:
        if n[-1] == 't' and  n[-2] == 'x' and n[-3] == 't':
            with open('input/' + n) as file:
                lines = file.readlines()
        
            for line in lines:
                line = re.split(' |\n', line)
            
                if line[0] == 'e':
                    vertex = search_vertex(line[1])
                    vertex2 = search_vertex(line[2])

                    vertex.adjacents.append(vertex2)
                    vertex2.adjacents.append(vertex)
            
            file.close()
            
            colorize_vertices()

            print_output()

            vertices.clear()
            colors.clear()
    
if __name__ == "__main__":
    main()