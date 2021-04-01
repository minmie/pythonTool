from urllib import parse


# 对字典进行编码
data = {
 'a': 'test',
  'name': '魔兽'
}
print(parse.urlencode(data))  # a=test&name=%E9%AD%94%E5%85%BD

# 对字符串编码
print(parse.quote('魔兽')) # %E9%AD%94%E5%85%BD

# 解码
print(parse.unquote("%E9%AD%94%E5%85%BD")) # 魔兽