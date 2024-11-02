gene_exp_1 = 3.5
gene_exp_2 = 3.2
gene_exp_3 = 2.4
gene_exp_4 = 9.3
gene_exp_5 = 7.2

# 1. List creation
gene_exp = [3.5, 3.2, 2.4, 9.3, 7.2, 7.1, 8.2, 2.1, 3.9, 1.1]
print(gene_exp)
# 2. Query
print(gene_exp[3])
print(gene_exp[4])
print(gene_exp[0])
print(gene_exp[-2])
print(gene_exp[2:6])
print(gene_exp[5:9])
print(gene_exp[4:])
print(gene_exp[:3])
print(gene_exp)
print(gene_exp[-3:])
gene_exp = [3.5, 3.2, 2.4, 9.3, 7.2, 7.1, 8.2, 2.1, 3.9, 1.1]
print(gene_exp[-2:-5:-1])
print(gene_exp[-4:-1])
print(gene_exp[1:-1: 2])
print(gene_exp[-2::-3])

# Update
gene_exp = [3.5, 3.2, 2.4, 9.3, 7.2, 7.1, 8.2, 2.1, 3.9, 1.1]
gene_exp[-1] = 7.7
print(gene_exp)
print(gene_exp[-1])
gene_exp[2] = 2.5
print(gene_exp)

gene_exp = [3.5, 3.2, 2.5, 9.3, 7.2, 7.1, 8.2, 10.1, 3.9, 7.7]

gene_exp[-2] = (gene_exp[-1] + gene_exp[-3])/2
print(gene_exp)

# append
gene_exp = [3.5, 3.2, 2.5, 9.3, 7.2, 7.1, 8.2, 10.1, 8.9, 7.7]
gene_exp.append(20.2)
print(gene_exp)

# insert
gene_exp.insert(2, 5.2)
print(gene_exp)

# delete
gene_exp = [3.5, 3.2, 5.2, 2.5, 9.3, 7.2, 7.1, 8.2, 10.1, 8.9, 7.7, 20.2]
gene_exp.pop()
print(gene_exp)
gene_exp.pop(2)
print(gene_exp)
gene_exp.pop(-1)
print(gene_exp)
gene_exp.remove(9.3)
print(gene_exp)



# find
gene_exp = [3.5, 3.2, 5.2, 2.5, 9.3, 7.2, 7.1, 8.2, 10.1, 8.9, 7.7, 20.2]
print(gene_exp.index(10.1))

# len
print(len(gene_exp))

# count
gene_exp = [3.5, 3.2, 5.2, 2.5, 9.3,5.2 ,7.2, 7.1, 5.2, 10.1, 8.9, 7.7, 20.2]
print(gene_exp.count(5.2))


# reverse
gene_exp = [3.5, 3.2, 5.2, 2.5, 9.3,5.2 ,7.2, 7.1, 5.2, 10.1, 8.9, 7.7, 20.2]
gene_exp.reverse()
print(gene_exp)

# sort
gene_exp.sort()
print(gene_exp)

gene_exp.sort(reverse=True)
print(gene_exp)





gene_exp = [3.5, 3.2, 5.2, 2.5, 9.3, 7.2, 7.1, 8.2, 10.1, 8.9, 7.7, 20.2]
gene_exp.sort()
print(gene_exp)
print(gene_exp.index(7.2))
print(gene_exp[gene_exp.index(7.2):])
print(gene_exp[:5])
print(gene_exp[4:8])


seq = "ATATGACCAGTGACCAGTGACCAGTAG"
print(seq.count("G"))
print(seq.count("C"))

print((seq.count("C") + seq.count("G")) / len(seq)*100)

C_count = seq.count("C")
print(C_count)
G_count = seq.count("G")
print(G_count)

GC_count = (C_count + G_count) / len(seq) *100
print(GC_count)


print(round(GC_count, 2))


print(len(seq))


sequence = input("Enter your sequence: ")

print(round((sequence.count("C") + sequence.count("G")) / len(sequence)* 100 , 2))
print(len(seq))

input()