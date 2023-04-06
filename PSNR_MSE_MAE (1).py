import math
import numpy as np
def Calculate_The_Matrix(X,Y):
    Z = []
    for i in range(len(X)):
        row = []
        for j in range(len(X[i])):
            elm = X[i][j] - Y[i][j]
            if elm < 0:
                row.append(elm*-1)
            elif elm >= 0:
                row.append(elm)         
        Z.append(row)
    return Z

def MAE(matrix):
    row = len(matrix)
    colum = len(matrix[0])
    SUM = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            SUM += matrix[i][j]
    mae = (1/(row*colum))*SUM
    if mae < 0:
        return mae*-1
    elif mae >= 0:
        return mae

def MSE(matrix):
    row = len(matrix)
    colum = len(matrix[0])
    SUM = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            SUM =SUM + (matrix[i][j]**2)
    return (1/(row*colum))*SUM

def PSNR(matrix):
    B = 1
    for i in range(len(matrix)):
        B  = B * 2
    L = B - 1 
    if MSE(matrix) == 0:
        return "infinity"
    else :
        return "PSNR = {0} dB".format(10*math.log10((L*L)/MSE(matrix)))

if __name__ == '__main__':
    X = np.array([[1,8,6, 6 ],
                  [6,3,11,8 ],
                  [8,8,9, 10],
                  [9,10,10,7]])
    Y = np.array([[2,8,8, 7 ],
                  [6,3,12,8 ],
                  [5,4,9, 1 ],
                  [15,9,11,9]])
    Z = (X - Y)
    #OR
    Z = Calculate_The_Matrix(X,Y)
    
    
print(PSNR(Z))
print(MSE(Z))
