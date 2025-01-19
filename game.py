import numpy as np

def playgame():
    grid = [[0,0,4,0,5,0,0,0,0],
            [9,0,0,7,3,4,6,0,0],
            [0,0,3,0,2,1,0,4,9],
            [0,3,5,0,9,0,4,8,0],
            [0,9,0,0,0,0,0,3,0],
            [0,7,6,0,1,0,9,2,0],
            [3,1,0,9,7,0,2,0,0],
            [0,0,9,1,8,2,0,0,3],
            [0,0,0,0,6,0,1,0,0]]
    condition = False
    print(np.matrix(grid))
    
    while condition == False:
        print("enter number between 1 and 9 to be input")
        num = input()
        print("which row should number be entered")
        print("1,2,3,4,5,6,7,8,or 9")
        row = input()
        print("which column would you like to put it")
        print("1,2,3,4,5,6,7,8,or 9")
        column = input()
        if (int(num) < 10 and int(row) < 10 and int(column) < 10 and int(num) > 0 and int(row) > 0 and int(column) > 0):
            if (grid[int(row)-1][int(column)-1] == grid[0][2] 
            or grid[int(row)-1][int(column)-1] == grid[0][4] 
            or grid[int(row)-1][int(column)-1] == grid[1][0] 
            or grid[int(row)-1][int(column)-1] == grid[1][3] 
            or grid[int(row)-1][int(column)-1] == grid[1][4] 
            or grid[int(row)-1][int(column)-1] == grid[1][5] 
            or grid[int(row)-1][int(column)-1] == grid[1][6] 
            or grid[int(row)-1][int(column)-1] == grid[2][2] 
            or grid[int(row)-1][int(column)-1] == grid[2][4] 
            or grid[int(row)-1][int(column)-1] == grid[2][5] 
            or grid[int(row)-1][int(column)-1] == grid[2][7] 
            or grid[int(row)-1][int(column)-1] == grid[2][8]
            or grid[int(row)-1][int(column)-1] == grid[3][1]
            or grid[int(row)-1][int(column)-1] == grid[3][2]
            or grid[int(row)-1][int(column)-1] == grid[3][4]
            or grid[int(row)-1][int(column)-1] == grid[3][6]
            or grid[int(row)-1][int(column)-1] == grid[3][7]
            or grid[int(row)-1][int(column)-1] == grid[4][1]
            or grid[int(row)-1][int(column)-1] == grid[4][7]
            or grid[int(row)-1][int(column)-1] == grid[5][1]
            or grid[int(row)-1][int(column)-1] == grid[5][2]
            or grid[int(row)-1][int(column)-1] == grid[5][4]
            or grid[int(row)-1][int(column)-1] == grid[5][6]
            or grid[int(row)-1][int(column)-1] == grid[5][7]
            or grid[int(row)-1][int(column)-1] == grid[6][0]
            or grid[int(row)-1][int(column)-1] == grid[6][1]
            or grid[int(row)-1][int(column)-1] == grid[6][3]
            or grid[int(row)-1][int(column)-1] == grid[6][4]
            or grid[int(row)-1][int(column)-1] == grid[6][6]
            or grid[int(row)-1][int(column)-1] == grid[7][2]
            or grid[int(row)-1][int(column)-1] == grid[7][3]
            or grid[int(row)-1][int(column)-1] == grid[7][4]
            or grid[int(row)-1][int(column)-1] == grid[7][5]
            or grid[int(row)-1][int(column)-1] == grid[7][8]
            or grid[int(row)-1][int(column)-1] == grid[8][4]
            or grid[int(row)-1][int(column)-1] == grid[8][6]):
                print("error")
                print("Dont try and change given figures... CHEATER >:(")
                pass
            else:
                grid[int(row)-1].pop(int(column)-1)
                grid[int(row)-1].insert(int(column)-1,int(num))
                row1 = sum(grid[0])
                row2 = sum(grid[1])
                row3 = sum(grid[2])
                row4 = sum(grid[3])
                row5 = sum(grid[4])
                row6 = sum(grid[5])
                row7 = sum(grid[6])
                row8 = sum(grid[7])
                row9 = sum(grid[8])
                clmn1 = grid[0][0]+grid[1][0]+grid[2][0]+grid[3][0]+grid[4][0]+grid[5][0]+grid[6][0]+grid[7][0]+grid[8][0]
                clmn2 = grid[0][1]+grid[1][1]+grid[2][1]+grid[3][1]+grid[4][1]+grid[5][1]+grid[6][1]+grid[7][1]+grid[8][1]
                clmn3 = grid[0][2]+grid[1][2]+grid[2][2]+grid[3][2]+grid[4][2]+grid[5][2]+grid[6][2]+grid[7][2]+grid[8][2]
                clmn4 = grid[0][3]+grid[1][3]+grid[2][3]+grid[3][3]+grid[4][3]+grid[5][3]+grid[6][3]+grid[7][3]+grid[8][3]
                clmn5 = grid[0][4]+grid[1][4]+grid[2][4]+grid[3][4]+grid[4][4]+grid[5][4]+grid[6][4]+grid[7][4]+grid[8][4]
                clmn6 = grid[0][5]+grid[1][5]+grid[2][5]+grid[3][5]+grid[4][5]+grid[5][5]+grid[6][5]+grid[7][5]+grid[8][5]
                clmn7 = grid[0][6]+grid[1][6]+grid[2][6]+grid[3][6]+grid[4][6]+grid[5][6]+grid[6][6]+grid[7][6]+grid[8][6]
                clmn8 = grid[0][7]+grid[1][7]+grid[2][7]+grid[3][7]+grid[4][7]+grid[5][7]+grid[6][7]+grid[7][7]+grid[8][7]
                clmn9 = grid[0][8]+grid[1][8]+grid[2][8]+grid[3][8]+grid[4][8]+grid[5][8]+grid[6][8]+grid[7][8]+grid[8][8]
                if (row1 == 45 and row2 == 45 and row3 == 45 and row4 == 45 and row5 == 45 and row6 == 45 and row7 == 45 and row8 == 45 and row9 == 45 and clmn1 == 45 and clmn2 == 45 and clmn3 == 45 and clmn4 == 45 and clmn5 == 45 and clmn6 == 45 and clmn7 == 45 and clmn8 == 45 and clmn9 == 45 ):
                    condition = True
                    print(" WINNER WINNER")
                    print("CHICKEN DINNER")
                    print("   \(*^*)/")
                print(np.matrix(grid))
        else:
            print("error")
            print("STOP CHEATING!!!!")
            pass


