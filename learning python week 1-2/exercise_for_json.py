f = open("E://Python//custion_for_datascience//funny.txt", "r")
f_out = open("E://Python//custion_for_datascience//funny_wc.txt", "w")
for line in f:
    tokens = line.split(" ")
    f_out.write("wordcount:" + str(len(tokens)) + line)

f.close()
f_out.close()
