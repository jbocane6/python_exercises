file = open("primos.txt", "w")
two = []
three = []
five = []
seven = []
for num in range(0,10000):
    if num % 2 == 0:
        two.append(num)
        val = "múltiplo de 2: "+str(num)+"\n"
    elif num % 3 == 0:
        three.append(num)
        val = "múltiplo de 3: "+str(num)+"\n"
    elif num % 5 == 0:
        five.append(num)
        val = "múltiplo de 5: "+str(num)+"\n"
    elif num % 7 == 0:
        seven.append(num)
        val = "múltiplo de 7: "+str(num)+"\n"
    print(f"{val}")
    #file.writelines("\t\tMULTIPLOS\n\n")
    #file.writelines("\t2\t3\t5\t7\n\n")
    #for (tw) in (two):
        #file.writelines(f"\t{tw}\t{tw}\t{tw}\t{tw}\n")
    file.writelines(val)
file.close()