#1st Question
salary = float(input())
if salary <= 250000 :
    print("NO TAX")
elif salary >250000 and salary <500000:
    print(salary*0.05)
elif salary >500000 and salary <=1000000:
    print(salary*0.20)
else:
    print(salary*0.30)

#2nd Question
n=int(input())
total=0
for _ in range(n):
    age=int(input())
if age>=5 and age<=18:
    total+=100
elif age>=19 and age<=60:
    total+=150
elif age>60:
    total+=120
print(total)

#3rd Question

units=int(input())
bill=0
if units<=100:
    bill+=units*1.5
elif units>100 and units<200:
    bill+=150+(units-100)*2.5
elif units>200 and units<=500:
    bill+=400+(units-200)*4
else:
    bill+=1600+(units-500)*6
print(bill)


#4th question

hrs=int(input())
fee=0

if hrs<=2:
    print(fee)
elif hrs>2 and hrs<24:
    fee=30+(hrs-2)*10
    print(fee)
elif hrs>=24:
    print(200)


#5th Question

name=input()
qua=int(input())

if qua==0:
    print("Out of Stock")
elif qua>0 and qua<11:
    print("Low stock")
elif qua>10 and qua<51:
    print("instock")
elif qua>50:
    print("Over Stocked")

#6th question
n=int(input())
for row in range(n):
    for col in range(n):
        if (row+col%2)==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()

# Or we can use directly this without cond statments "print((row+col)%2,end=" ")"

#7th question

while True:
    print('''1.Monthly - ₹500
          2.Quaterly - ₹1300
          3.Yearly - ₹5000''')
    ch=int(input())
    ppl=int(input())
    if ch==1:
        print(ppl*500)
    elif ch==2:
        print(ppl(1300))
    elif ch==3:
        print(ppl*5000)
    else:
        print("Invalid Choice")
        break


#8th question

total=float(input())
if total<1000:
    print(total)
elif total>999 and total <5000:
    print(total-total*0.05)
elif total>4999 and total<10000:
    print(total-total*0.1)
elif total>=10000:
    print(total-total*0.15)


#9th Question

pin=1234
for _ in range(3):
    epin=int(input())
    if epin==pin:
        print("Access Granted")
        break
else:
    print("ATM Blocked.Try Again Later.")


#10th Question

total_seats=int(input())
booked_seats=list(map(int,input().split()))
print(f'Total Seats:{total_seats}')
print(f'Booked: {len(booked_seats)}')
print(f'Available Seats: {total_seats-len(booked_seats)}')