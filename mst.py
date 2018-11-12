def prim(r_matrix):
    '''使用prim算法实现最小生成树，最后返回最小生成树的矩阵'''
    is_used = np.zeros((1,r_matrix.shape[1]))#节点是否用过，用过为1，没有用过为0
    binary_matrix = np.zeros((r_matrix.shape[1],r_matrix.shape[1]))#最小生成树中节点连接矩阵，1代表两个节点相连，0代表不相连
    first_v = np.random.randint(0,r_matrix.shape[1]) 
#    first_v = 0
    print(first_v)
    is_used[0][first_v] = 1
    r_matrix_copy = copy.deepcopy(r_matrix)
    for i in range(r_matrix_copy.shape[1]-1):
        t = r_matrix_copy[np.where(is_used[0])[0],:]
        min_index = np.where(t==np.min(t))#找出最小值所在的位置，【横坐标，纵坐标】
#        max_index = np.where(t==np.max(t))
        n_min = np.random.randint(0,min_index[0].shape[0])#随机选一个最小值，如果有多个相等的最小值的话，n_min代表选择第几个最小值
        next_v_row = np.where(is_used)[1][min_index[0][n_min]]
        next_v_col = min_index[1][n_min]
        binary_matrix[next_v_row][next_v_col]=1
        binary_matrix[next_v_col][next_v_row]=1
        for j in range(len(is_used[0])):
            if is_used[0][j]==1:
                r_matrix_copy[j][next_v_col]=1
                r_matrix_copy[next_v_col][j]=1
        is_used[0][next_v_col]=1  
#    kong = np.zeros((r_matrix.shape[0],r_matrix.shape[0]))
#    kong[np.where(rs)]=r_matrix[np.where(rs)]
#    final_r_matrix = kong
#    return final_r_matrix #返回最终带有权重的最小生成树
    return binary_matrix#二值矩阵，不带有权重
