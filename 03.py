a = []
for i in range(0,10):
    b = input('please input > ' )
    b = int(b)
    if b<0:
        print('ok')
    a+=str(b)
    print(a)

if '5' not in a:
    print('Boo')
print(a)
