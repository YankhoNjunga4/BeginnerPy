print("This Program converts a number in decimal into binary")
num = int(input("enter the number you'd like to convert:"))
number = num
ans = []
final = []

while (num > 0):
    rem = num % 2
    ans.append(rem)
    num = num // 2

c = len(ans)
while ((c) > 0):
    final.append(ans[c - 1])
    c = c - 1

#print(ans)
print("the number", number, "is", final, "to binary")