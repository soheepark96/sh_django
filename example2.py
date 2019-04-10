# money = True
# if money : 
#     print("돈이 있다.")
# else : 
#     print("돈이 없다.")

# money = 30000
# if money > 30000 : 
#     print('돈이 30000원 보다 많이있다.')
# elif money == 30000 : 
#     print('돈이 30000원 있다.')
# else : 
#     print('돈이 없다.')

# grade = 95
# if grade>90 : 
#     print("A")
# elif grade>80 : 
#     print("B")
# else : 
#     print("C")

# pocket = ['paper', 'cellphone']
# card = True
# if 'money' in pocket : 
#     print("택시를 타고가라")
# elif card : 
#     print("택시를 타고가라")
# else : 
#     print("걸어가라")

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for i in a : 
#     if i%2 != 0 :
#         print(i)

# a = '안녕하세요. 저는 박소희입니다.'
# k = a.split(" ")
# for b in k:
#     print(b)

# sum = 0
# for i in range(1,11):
#     sum = sum + i
#     print(sum)

# for i in range(1,10) :
#     print('2*',i,'=',2*i)

# for i in range(2,10) : 
#     for j in range(1,10) : 
#         print(i,'*',j,'=',i*j)

# a = "멋쟁이 사자처럼 화이팅 멋쟁이 사자"
# b = a.split(" ")
# k={}
# for i in b : 
#     if i in b :
#         k[i]
#     print(k[i])
#     else
#         k[i]=1
#         print(k[i])

a = "멋쟁이 사자처럼 화이팅 멋쟁이 사자"
b= a.split(" ")
k={}
for i in b : 
   
    if i in k : 
        k[i]=k[i]+1
    else : 
        k[i]=1
    # print(k[i]) 숫자 리스트가 뜸
print(k)