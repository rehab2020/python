s1=['ahmad',18,17,19,5,8,25]
s2=['sami',20,20,19,9,28]
s3=['faris',14.5,16,13,7,23]
x=(input('Enter students name: '))
if x==s1[0]:
    print(s1[0] ,sum(s1[1:6]))
elif x==s2[0]:
    print(s2[0] ,sum(s2[1:6]))
elif x==s3[0]:
    print(s3[0] ,sum(s3[1:6]))
else:
    print('student is not recrd')
