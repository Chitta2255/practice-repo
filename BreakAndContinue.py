#multiple of 3 [1 to 50] => 27
for i in range (1,51):
    if i == 27:
        break
    if i % 3 == 0:
            print(i)

print("out of the loop")
        #Continue
for i in range (1,51):
        if i==27:
            continue
        if i % 3 == 0:
            print(i)
print("out of the loop")