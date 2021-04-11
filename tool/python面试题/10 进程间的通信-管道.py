import multiprocessing
"""
Pipe实现进程间通信
Pipe 直译过来的意思是“管”或“管道”，该种实现多进程编程的方式，和实际生活中的管（管道）是非常类似的。通常情况下，管道有 2 个口，而 Pipe 也常用来实现 2 个进程之间的通信，这 2 个进程分别位于管道的两端，一端用来发送数据，另一端用来接收数据。

使用 Pipe 实现进程通信，首先需要调用 multiprocessing.Pipe() 函数来创建一个管道。该函数的语法格式如下：
conn1, conn2 = multiprocessing.Pipe( [duplex=True] )

其中，conn1 和 conn2 分别用来接收 Pipe 函数返回的 2 个端口；duplex 参数默认为 True，表示该管道是双向的，即位于 2 个端口的进程既可以发送数据，也可以接受数据，而如果将 duplex 值设为 False，则表示管道是单向的，conn1 只能用来接收数据，而 conn2 只能用来发送数据。

另外值得一提的是，conn1 和 conn2 都属于 PipeConnection 对象，它们还可以调用表 2 所示的这些方法。

表 2 Pipe 对象可调用的方法
方法名	功能
send(obj)	发送一个 obj 给管道的另一端，另一端使用 recv() 方法接收。需要说明的是，该 obj 必须是可序列化的，如果该对象序列化之后超过 32MB，则很可能会引发 ValueError 异常。
recv()	接收另一端通过 send() 方法发送过来的数据。
close()	关闭连接。
poll([timeout])	返回连接中是否还有数据可以读取。
send_bytes(buffer[, offset[, size]])	发送字节数据。如果没有指定 offset、size 参数，则默认发送 buffer 字节串的全部数据；如果指定了 offset 和 size 参数，则只发送 buffer 字节串中从 offset 开始、长度为 size 的字节数据。通过该方法发送的数据，应该使用 recv_bytes() 或 recv_bytes_into 方法接收。
recv_bytes([maxlength])	接收通过 send_bytes() 方法发送的数据，maxlength 指定最多接收的字节数。该方法返回接收到的字节数据。
recv_bytes_into(buffer[, offset])	功能与 recv_bytes() 方法类似，只是该方法将接收到的数据放在 buffer 中。
"""


def processFun(conn,name):
    print(multiprocessing.current_process().pid,"进程发送数据：",name)
    conn.send(name)
if __name__ == '__main__':
    #创建管道
    conn1,conn2 = multiprocessing.Pipe()
    # 创建子进程
    process = multiprocessing.Process(target=processFun, args=(conn1,"http://c.biancheng.net/python/"))
    # 启动子进程
    process.start()
    process.join()
    print(multiprocessing.current_process().pid,"接收数据：")
    print(conn2.recv())