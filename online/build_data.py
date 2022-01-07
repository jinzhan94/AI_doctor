import ramdom 

with open('./data.txt', 'w') as ff:
    for i in range(10):
        num = random.randint(1,5)
        ff.write(str(num)+'\n')

print('data has build')


