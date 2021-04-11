#矩阵形式存储

class Graph:

    def __init__(self,vertex_num):
        self.vertexNum = vertex_num
        self.edgeNum=0
        self.weight=[[0 for __ in range(self.vertexNum)] for _ in range(self.vertexNum)]


    def insert_edge(self,v1,v2,weight=1,is_direct=True):
        """
        插入边操作
        :param v1: 第一个点
        :param v2: 第二个点
        :param weight: 权重
        :param is_direct: 是否有向
        :return:
        """
        # 邻接矩阵存储
        self.weight[v1][v2]=weight

    # 深度遍历
    def dfs(self,vertex, visted=None):
        if visted is None:
            visted={}
        visted[vertex]=True
        print(vertex)
        for v in range(self.vertexNum):
            if self.weight[vertex][v]==1 and not visted.get(v,False):
                self.dfs(v,visted)

    # 广度优先
    def bfs(self,vertex):
        queue=list()
        visted=dict()
        visted[vertex] = True
        print(vertex)
        queue.append(vertex)
        while len(queue)!=0:
            v = queue.pop(0)
            for _ in range(self.vertexNum):
                if self.weight[v][_] == 1 and not visted.get(_, False):
                    visted[_]=True
                    print(_)
                    queue.append(_)
if __name__ == '__main__':
    g=Graph(4)
    g.insert_edge(0,1)
    g.insert_edge(1,2)
    g.insert_edge(0,3)
    print(g.weight)
    g.dfs(0)  # 0 1 2 3
    print()
    g.bfs(0) # 0 1 3 2