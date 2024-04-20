# Cassandre, 20210863
# Viviane Binet, 20244728

import sys


def read_problem(input_file):
    """Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier,
    faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
    d'autres librairies.
    Functions to read/write in files. you can modify them, do some parsing,
    add a return value, but don't use other librairies"""
    # lecture du fichier/file reading
    file = open(input_file, "r")
    rows, cols = map(int, file.readline().strip().split())  # get rows and cols
    matrix = [list(map(int, list(line.strip()))) for line in file if line.strip()]  # get matrix
    file.close()
    return rows, cols, matrix

#Notes du cours BFS
def BreadthFirstSearch(row, col, Matrix, visited, rows, cols):
    queue = [(row, col)]  # init queue xith i, j
    count = 0
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # down, left, up, right
    while queue:
        row, col = queue.pop(0)

        if not visited[row][col]:
            visited[row][col] = True
            count += 1
            # queue unvisited connected neighbors
            for dirRow, dirCol in directions:
                next_row, next_col = row + dirRow, col + dirCol
                if (0 <= next_row < rows) and (0 <= next_col < cols) and (Matrix[next_row][next_col] == 1) and not visited[next_row][next_col]:
                    queue.append((next_row, next_col))  
    
    return count

def largest_well(rows, cols, Matrix):
    visited = [[False] * cols for _ in range(rows)]  # Set all to unvisited
    result = 0
    for i in range(rows):
        for j in range(cols):
            if Matrix[i][j] == 1 and not visited[i][j]:  # If water and not visited
                result = max(result, BreadthFirstSearch(i, j, Matrix, visited, rows, cols))  # Max between previous result and BFS
    return result


def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()


def main(args):
    """Fonction main/Main function"""
    input_file = args[0]
    output_file = args[1]

    rows, cols, matrix = read_problem(input_file)
    answer = largest_well(rows, cols, matrix)

    # answering
    write(output_file, str(answer))

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])