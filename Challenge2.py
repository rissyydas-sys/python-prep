class Spiral_Matrix:
    def __init__(self,size):
        self.top_row = 0
        self.bottom_row = size-1
        self.left_column = 0
        self.right_column = size-1
        self.size = size

    def clockwise_spiralmatrix(self):
        num = 1
        matrix = [[0]*self.size for rows in range(self.size)]

        while self.left_column <= self.right_column and self.top_row <= self.bottom_row:

            for top in range(self.left_column,self.right_column+1):
                matrix[self.top_row][top] = num
                num+=1
            self.top_row+=1

            for right in range(self.top_row,self.bottom_row+1):
                matrix[right][self.right_column] = num
                num+=1
            self.right_column-=1

            for bottom in range(self.right_column,self.left_column-1,-1):
                matrix[self.bottom_row][bottom] = num
                num+=1
            self.bottom_row-=1
             
            for left in range(self.bottom_row,self.top_row-1,-1):
                matrix[left][self.left_column] = num
                num+=1
            self.left_column+=1
        width = len(str(self.size*self.size))
        for rows in matrix:
            print(" ".join(f"{x:>{width}}" for x in rows))

    def anticlockwise_spiralmatrix(self):
        num = 1
        matrix = [[0]*self.size for rows in range(self.size)]

        while self.left_column <= self.right_column and self.top_row <= self.bottom_row:

            for left in range(self.top_row,self.bottom_row+1):
                matrix[left][self.left_column] = num
                num+=1
            self.left_column+=1

            for bottom in range(self.left_column,self.right_column+1):
                matrix[self.bottom_row][bottom] = num
                num+=1
            self.bottom_row-=1

            for right in range(self.bottom_row,self.top_row-1,-1):
                matrix[right][self.right_column] = num
                num+=1
            self.right_column-=1

            for top in range(self.right_column,self.left_column-1,-1):
                matrix[self.top_row][top] = num
                num+=1
            self.top_row+=1
        width = len(str(self.size*self.size))
        for rows in matrix:
            print(" ".join(f"{x:>{width}}" for x in rows))

while True:
    try:
        size = int(input("Enter the size of matrix:"))
        choice = int(input("Choose 1. Clockwise 2. Anti-Clockwise 3.Exit:"))
        if choice == 1:
            spiral_clockwise = Spiral_Matrix(size)
            spiral_clockwise.clockwise_spiralmatrix()
        elif choice == 2:
            spiral_counterclockwise = Spiral_Matrix(size)
            spiral_counterclockwise.anticlockwise_spiralmatrix()
        elif choice == 3:
            print("Program Exits!!!")
            break
    except:
        print("Invalid value entered, Please enter correctly")
    else:
        continue