fruit = ['lemon', 'apple', 'orange', 'blueberry']

#使用List生成式
print('%9s'%'字串', '%3s'%'長度')
print('\n'.join( ['%10s:%3d'%(
    item, len(item)) for item in fruit]))

#以for/in廻圈讀取
'''
print('%9s'%'字串', '%3s'%'長度')
for i in fruit: #原有的for廻圈讀取
    print('{0:>10s}:{1:2d}'.format(i, len(i)))
'''
