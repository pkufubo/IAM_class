def find_k(list,k):
    list1=list.copy()
    if k<=100:#k较小时采用递归定义，复杂度k*n
        if k==1:
            return max(list1) 
        else:
            list1.remove(max(list1))
            return find_k(list1,k-1)
    else:#k较大时，先排序再取，复杂度由排序算法决定
        sorted(list)
        return list[-k]
		
def find_se(list):
    start=[]
    end=[]
    for i in range(len(list)):
        if list[i]!=0:
            if i==0 or list[i-1]==0:
                start.append(i)
            if i==len(list)-1:
                end.append(i)
        else:
            if i==len(list)-1 or list[i-1]!=0:
                end.append(i-1)
    return(start,end)
	
def main(list,k):
    start,end=find_se(list) 
    period=[end[i]-start[i]+1 for i in range(len(start))]#降水事件时间长度
    pre=[sum(list[start[i]:end[i]+1]) for i in range(len(start))]#降水事件的总降雨量
    f_event=[period[i]*pre[i] for i in range(len(start))]#计算f_event
    #print(f_event)
    #print(k)
    return find_k(f_event,k)

data=[1,0,0,1,2,0,4,0,3,5,6,0,0,0,0,1,0,5]
print(main(data,2))