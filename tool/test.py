

row ,col = list(map(int,input().split()))
# col ,row = list(map(int,input().split()))

# print(row, col)
mat = []

def dfs(pos,ret,visted=None,):
    rr,cc = pos
    if visted is None:
        visted = {pos: True}
    else:
        visted[pos] = True
    if mat[pos[0]][pos[1]] == '3':
        ret.append(pos)
    for rc in [(rr-1,cc-1),(rr-1,cc),(rr-1,cc+1),(rr,cc+1),(rr+1,cc+1),(rr+1,cc),(rr+1,cc-1),(rr,cc-1)]:
        _r,_c =rc
        if 0<=_r <row and 0<=_c<col and rc != pos:
                if mat[_r][_c] != "1" and not visted.get((_r, _c), False):
                    dfs((_r, _c), ret,visted, )

for line in range(row):
    mat.append(input().split())

# print(mat)
ret_ = []
count = 0
for r in range(row):
    for c in range(col):
        if mat[r][c] == "2":
            tmp_ret = []
            dfs((r,c),tmp_ret,visted=None)
            ret_.append(tmp_ret)
            count += 1
            if count == 2:
                break
    if count == 2:
        break

ret1= ret_[0]
ret2= ret_[1]

ret_cout = 0
for item in ret1:
    if item in ret2:
        ret_cout += 1

print(ret_cout)



"""
2 2
2 2
3 0


4 4
2 1 0 3
0 1 2 1
0 3 0 0
0 0 0 0

4 4
2 1 2 3
0 1 0 0
0 1 0 0
3 1 0 0



4 5
2 1 0 3 0
0 1 2 1 0
0 3 0 0 0
0 0 0 0 3
"""