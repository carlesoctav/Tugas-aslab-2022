from numpy import zeros

n=5
movement=[[1,0],[0,1],[-1,0],[0,-1]]
mat_0=zeros((n,n))
mat_0[0,0]=1
print(mat_0)
counter=2
i=0
row_pointer=0
column_pointer=0
mov=movement[i%4]
while counter<=n**2:

    if(row_pointer+mov[0]>=n or row_pointer+mov[0]<0 or column_pointer+mov[1]>=n or column_pointer+mov[1]<0 or mat_0[row_pointer+mov[0]][column_pointer+mov[1]]!=0):
        i+=1
        mov=movement[i%4]
        continue

    row_pointer+=mov[0]
    column_pointer+=mov[1]
    mat_0[row_pointer, column_pointer]=counter
    counter+=1
    print(mat_0)

