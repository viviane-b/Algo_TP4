#Nom, matricule
#Nom, matricule

import sys
import time
#Fonction pour lire le fichier d'input. Vous ne deviez pas avoir besoin de la modifier.
#Retourne la liste des noms d'étudiants (students) et la liste des paires qui ne peuvent
#doivent pas être mis dans le même groupe (pairs)
#
#Function to read the input file. You shouldn't have to modify it.
#Returns the list of student names (students) and the list of pairs of students that
#shouldn't be put in the same group (pairs)
def read(fileName):
    # lecture du fichier
    fileIn = open(fileName,"r")
    linesIn = fileIn.readlines()
    fileIn.close()

    nbStudents = int(linesIn[0])
    students = []
    if(nbStudents != 0):
        students = [s.strip() for s in linesIn[1:nbStudents+1]]
    nbPairs = int(linesIn[nbStudents+1])
    pairs = []
    if(nbPairs != 0):
        pairs = [s.strip().split() for s in linesIn[nbStudents+2:nbStudents+nbPairs+2]]

    return students, pairs


#Fonction qui écrit dans le fichier d'output. 
#le paramètre content est un string
#
#Function that writes in the output file.
#The content parameter is a string
def write(fileName, content):
    Outputfile = open(fileName, "w")
    Outputfile.write(content)
    Outputfile.close()

#Fonction principale à compléter.
#students : liste des noms des étudiants
#pairs : liste des paires d'étudiants à ne pas grouper ensemble
#        chaque paire est sous format de liste [x, y]
#Valeur de retour : string contenant la réponse. Si c'est impossible, retourner "impossible"
#                   Sinon, retourner en un string les deux lignes représentant les
#                   les deux groupes d'étudants (les étudiants sont séparés par des
#                   espaces et les deux lignes séparées par un \n)
#
#Function to complete
#students : list of student names
#pairs : list of pairs of students that shouldn't be grouped together.
#        each pair is given as a list [x, y]
#Return value : string with the output. If it is impossible, return "impossible".
#               otherwise, return in a single string both ouput lines that contain
#               two groups (students are separated by spaces and the two lines by a \n)

def DFS(graph, vertex, color):

    stack = [(vertex, 0)] # init stack
    color[vertex] = 0  # color w/ 0
    while stack:
        v, current = stack.pop()
        next = 1 - current # next coloring
        for desc in graph[v]['descendants']:
            if desc not in color:  # not visited
                color[desc] = next
                stack.append((desc, next))
            elif color[desc] != next:
                return False  # not 2 colorable
    return True

def createGroups(students, pairs):
    # create graph: key is the vertex, values are neighboors of the vertex (unwanted pair)
    global graph
    graph = {}
    for student in students:
        graph[student]={'descendants': [], 'precedent':[], 'discovered':0 }

    for pair in pairs:
        graph[pair[0]]['descendants'].append(pair[1])
        graph[pair[1]]['descendants'].append(pair[0])

    color = {}
    for student in students:
        if student not in color:
            if not DFS(graph, student, color):
                output = "impossible"
                return output
    if color == {}: #nothing or the same
        output =  "impossible"  
        return output     
    
    col1 = [s for s in color if color[s] == 0]
    col2 = [s for s in color if color[s] == 1]
    
    output = '\n'.join([' '.join(col1) +'\n'+ ' '.join(col2)]) #concated color groups
    return output

#Normalement, vous ne devriez pas avoir à modifier
#Normaly, you shouldn't need to modify
def main(args):
    input_file = args[0]
    output_file = args[1]
    students, pairs = read(input_file)
    start_time = time.time()
    output = createGroups(students, pairs)
    print("Time: ", time.time() - start_time)
    #print("recieved output", output)
    write(output_file, output)
            

#Ne pas changer
#Don't change
if __name__ == '__main__':
    main(sys.argv[1:])