cus_details={1001:"john",1004:"jill",1005:"joe",1003:"jack"}
print(cus_details)
print(len(cus_details))#no of customers
print(sorted(cus_details.values()))#sorting in ascending order
del(cus_details[1005])
print(cus_details)
cus_details[1003] ="mary"
print(cus_details)
print(1002 in cus_details)