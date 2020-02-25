def find_k(list,k):
    if k<=100:#k较小时采用递归定义，复杂度k*n
        if k==1:
            return max(list) 
        else:
            list.remove(max(list))
            return find_k(list,k-1)
    else:#k较大时，先排序再取，复杂度由排序算法决定
        sorted(list)
        return list[-k]