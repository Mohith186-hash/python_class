name='arun'
for ch in name:
    print(f"ch = {ch}")
name=['arun','gopal','tarak','venkatesh']
for ch in name:
    print(f"ch = {ch}")


name={'arun','gopal','tarak','venkatesh'}
for ch in name:
    print(f"ch = {ch}")
'''ch = tarak
ch = venkatesh
ch = arun
ch = gopal'''

name={1:'dinesh',2:'gopal',3:'venkatesh',4:'tarak'}

for i in name.keys():
    print(f'(i)-{name[i]}')
'''(i)-dinesh
(i)-gopal
(i)-venkatesh
(i)-tarak'''

#***
name={1:'dinesh',2:'gopal',3:'venkatesh',4:'tarak'}

for i in name.keys():
    print(f'(i):{name[i]}'.title())

'''(I)-Dinesh
(I)-Gopal
(I)-Venkatesh
(I)-Tarak'''

for i in range(0,10):
    print(i)

'''0
1
2
3
4
5
6
7
8
9'''

for i in range(0,21):
    print(f'17 * {i} = {17*i}')
'''17 * 0 = 0
17 * 1 = 17
17 * 2 = 34
17 * 3 = 51
17 * 4 = 68
17 * 5 = 85
17 * 6 = 102
17 * 7 = 119
17 * 8 = 136
17 * 9 = 153
17 * 10 = 170
17 * 11 = 187
17 * 12 = 204
17 * 13 = 221
17 * 14 = 238
17 * 15 = 255
17 * 16 = 272
17 * 17 = 289
17 * 18 = 306
17 * 19 = 323
17 * 20 = 340'''
