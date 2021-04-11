#
#
# v1 = [1,2,3]  # 引用c1=1
# v2 = [4,5,6]  # # v2引用为c2=1
#
# v1.append(v2)  #  v2引用为c2=2
# v2.append(v1)  # v1引用为c1=2
#
# del v1  # c1 =1
# del v2  # c2 =2
#
#
# # 小数据池
# n1=666
# n2=666
# a =665
# b=1
# c = a+b
# print(id(n1))  # 2291194317552
# print(id(n2))  # 2291194317552
# print(id(c))  # 2291340438256
#
#
# # free_list
#
# a=[1,2,3]
# print(id(a))  # 1910916149704
# del a
#
# b = [2,3,4]
# print(id(b))  # 1910916149704


"""
此时出现循环引用


python内存管理
python维护着一个循环双向链表，链表中存贮着程序创建的每一个对象，每个对象内部都一个ob_refcnt的引用计数器，当该值为0，则回收对应的内存。
但对于容器类型的数据结构，可能会存在循环引用，固又引入了标记清除和分代回收机制
该机制维护着3个链表，0代 ，1代，2代，当一个0代的数据多次被检测但还没有被销毁，就会给它升级，变成1代，越往后的检测频率越低
0代：当链表中0代个数达到700个，就会扫描
1代：0代扫描1十次，1代扫描1次
2代：1代扫描10次，2代扫描1次


1.引用计数
2。标记清除：扫描是否有循环引用，有就删除
3.分代回收
4.小数据池

5.free_list
python内部还维护了一个free_list，当一个对象的引用计数为0时，不会直接被回收，而是放到free_list当中缓存。以后再创建同类型的对象时，
直接重free_list取出该块内存，而不是重新开辟内存

"""

