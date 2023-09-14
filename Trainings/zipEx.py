### Zip function

students = ["John","Mark","Melissa","Mary"]

departments = ["Math","Phys","Econ","Astro"]

ages = [23,24,21,32]

new_list = list(zip(students,departments,ages))

#print(new_list)

###
### Lambda 
###

sum = lambda a,b : a+b

#print(sum(4,5))

###
### Map
###

salaries = [1000,3000,2000,2500]

def newPay(x):
    return x * 20 / 100 + x

#print(newPay(salaries[0]))


print(list(map(newPay,salaries)))
print(list(map(lambda x : x *20 / 100 + x , salaries)))


