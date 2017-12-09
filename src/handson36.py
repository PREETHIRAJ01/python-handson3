student_marks={"john":86.5,"jack":91.2,"jill":84.5,"harry":72.1,"joe":80.5}
p=len(student_marks)
print(student_marks)
sv=sorted(student_marks.values())
print("ascendingorder=",sv)
l=len(sv)
d = []
while l!=0:
    d.append(sv[l - 1])
    l = l - 1
print ("descendingorder=",d)

print(sum(student_marks.values())/float(len(student_marks)))#average










