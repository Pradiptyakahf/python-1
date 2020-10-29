nilai = int(input('Berapa nila Anda? '))

if nilai >= 90:
    grade = 'A'
elif nilai >= 80:
    grade = 'B+'
elif nilai >= 70:
    grade = 'B'
elif nilai >= 60:
    grade = 'C+'
else :
    grade = 'D'
print('Grade : {}'.format(grade))
