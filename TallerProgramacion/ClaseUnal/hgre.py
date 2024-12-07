import random
T = [[0 for j in range(8)] for i in range(8)]
ii = [2, 2, 1, 1, -1, -1, -2, -2]
jj = [-1, 1, -2, 2, 2, -2, -1, 1]
n = 8
i0 = 7
j0 = 0
k = 1
T[i0][j0] = k
print(f"\n .. posición inicial: ({i0}, {j0}) = {T[i0][j0]}\n")
ix = i0
jy = j0

while k < n*n:
    adj_counts = []
    for i in range(8):
        ix = i0 + ii[i]
        jy = j0 + jj[i]
        if 0 <= ix < 8 and 0 <= jy < 8:
            if T[ix][jy] == 0:
                adj_count = 0
                for j in range(8):
                    ni = ix + ii[j]
                    nj = jy + jj[j]
                    if 0 <= ni < 8 and 0 <= nj < 8:
                        if T[ni][nj] == 0:
                            adj_count += 1
                adj_counts.append((adj_count, i))
    if adj_counts:
        adj_counts.sort()
        count, i = adj_counts[0]
        ix = i0 + ii[i]
        jy = j0 + jj[i]
        k += 1
        T[ix][jy] = k
        i0 = ix
        j0 = jy
    else:
        break

print("    0  1  2  3  4  5  6  7\n")
for i in range(n):
    print(f"{i} * ", end="")
    for j in range(n):
        if T[i][j] < 10 and T[i][j] > 0:
            print(f" 0{T[i][j]} ", end="")
        elif T[i][j] == 0:
            print(" .. ", end="")
        else:
            print(f" {T[i][j]} ", end="")
    print("")

print(f"\nk: {k} de {n*n} posibles")