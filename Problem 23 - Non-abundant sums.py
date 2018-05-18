def divisors(number):
    divisors_=[]
    for i in range(1,number) :
        if number%i == 0 :
            divisors_.append(i)
    return divisors_

abundant_numbers=[]

for i in range(12,28124):
    if i < sum(divisors(i)):
        abundant_numbers.append(i)

sum_two_abundant_number=[]

for i in range(len(abundant_numbers)):
    for j in range(i,len(abundant_numbers)):
        if abundant_numbers[i]+abundant_numbers[j]<28124:
            if abundant_numbers[i]+abundant_numbers[j] not in sum_two_abundant_number:
                sum_two_abundant_number.append(abundant_numbers[i]+abundant_numbers[j])
        else :
            continue


sum_=(28123*28124)/2

x=sum(sum_two_abundant_number)

print(int(sum_ - x))
