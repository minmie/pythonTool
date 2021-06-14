


mapping={
    "properties":{
        'name':{
            'type':"test", # name字段可进行分词
            'index': True  # 可以被索引
        },
        'sex':{
            'type':'keyword',  # sex字段不能被分词，必须完全匹配
            'index':True
        },
        'tel':{
            'type':'keyword',
            'index':False  # 不能进行索引，也就是不能通过这个字段来查询
        }
    }
}