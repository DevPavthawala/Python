with open("E://2k23//data scientist//practice problem program//practice problelm week1-2//13_read_write_files//stocks.csv","r") as f,open("E://2k23//data scientist//practice problem program//practice problelm week1-2//13_read_write_files//output.csv","w") as out:
    out.write("Company Name,PE ratio,PB ratio\n")
    next(f)  # this will skip the first line
    for line in f:
        tokens = line.split(',')
        stocks = tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price/eps,2)
        pb = round(price/book,2)
        out.write(f"{stocks},{pe},{pb}\n")

