'''
初始化：由给定的 n 个权值 {ω1,ω2,⋯,ωn}{ω1,ω2,⋯,ωn}构造 n 棵只有一个根节点的二叉树，从而得到一个二叉树集合F={T1,T2,⋯,Tn}F={T1,T2,⋯,Tn}。
选取与合并：在FF中选取根节点的权值最小的两颗二叉树分别作为左右子树构造一棵新的二叉树（一般情况下将权值大的结点作为右子树。），这棵新二叉树的根节点的权值为其左、右子树根节点的权值之和。
删除与加入：在FF中删除作为左、右子树的两棵二叉树，并将新建立的二叉树加入到FF中。
重复上述两个步骤，当集合FF中只剩下一棵二叉树时，这棵二叉树便是哈夫曼树。




https://www.cnblogs.com/-citywall123/p/11297523.html
'''

import sys
import heapq


nums = [2, 3, 5, 1, 54, 23, 132]
heapq.heapify(nums) #把nums转化为最小堆.
print(nums)
print([heapq.heappop(nums) for _ in range(len(nums))])  # 每一次弹出最小的元素,直到nums为空了.

##########下面利用最小堆来进行哈夫曼树的建立.


class node():
    def __init__(self,name=None):
         self.left=None
         self.right=None
         self.name=name  #name用来存储节点名称.
#定义root节点就是tree本身即可.
root=node(1212)




#下面给定一个字典key表示节点名称,value表示权重.也就是频率.

dic={'a':1,'b':2,'c':3,'d':4,'e':5}
savedic=dic
count=0
keep={}  #用来保证对象不会重新创立,保证节点的链接是正确的

for i in dic:
    keep[node(i)]=1



while len(dic)>1:  #最后dic里面的节点会变成1.就是最后的root.就可以停止建立树了.剑豪了.
    #先找dic中value最小的2个
    dic1=    sorted(dic,key=lambda x:dic[x])
    #加入和节点.
    select=dic1[:2]
    dic['jihao' + str(count)] =dic[select[0]]+dic[select[1]]


    #建立树

    root=node('jihao' + str(count))
    keep[root]=1
    for i in keep:
        if i.name==select[0]:
            root.left =i
        if i.name==select[1]:
            root.right =i




    for i in select:
      dic.pop(i)
    count += 1


print(root.name)

print(root.right.name)
print(root.left.name)
print(root.left.left.name)
print(root.left.right.left.name)
print(root.left.right.right.name)


#以上实现了一个效率比较低的haffman编码树.还没有想好如何把最小堆利用到频率排序上.


####################下面写一个树的按层遍历来看hafman树的效果.


print("打印树layer遍历")

def layerBianli(list1):
    print(' '.join(i.name for i in list1))
    list2=[]
    for i in list1:
        if i.left!=None:
         list2.append(i.left)
        if i.right != None:
         list2.append(i.right)
    list1=list2

    if list1!=[]:
        layerBianli(list1)


layerBianli([root])

print("以上就是haffman编码的树")
print("对应的haffman编码就是左子树取0,优子树取1,进行0,1编码即可.")



















