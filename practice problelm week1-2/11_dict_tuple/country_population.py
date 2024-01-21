d = {"China":143,"India":136,"USA":32,"Pakistan":21}

def print_all():
    for country,p in d.items():
        print(f"{country}==>{p}")

def add():
    input_country = input("Enter the countrty name :")
    if input_country in d:
        print("it exist ")
    else:
        input_population = input("Enter the countrty population :")
        d[input_country]=input_population
        print_all()

def remove():
    input_remove = input("Enter the countrty name that you have to remove:")
    if input_remove in d:
        del d[input_remove]
        print(f"The countrty {input_remove} is successfully removed....")
        print_all()
    else:
        print("Enter the valid country ")

def query():
    input_query = input("Enter the countrty that you have query :")
    if input_query in d:
        print(f"The current population of {input_query} is ",d[input_query])
    else:
        print("Enter the valid country ")


def main():
    input_main = input("Enter operation (add, remove, query or print):")

    if input_main == "add":
        add()
    elif input_main == "remove":
        remove()
    elif input_main == "query":
        query()
    elif input_main == "print":
        print_all()
    else:
        print("operation is not valid")


if __name__ == '__main__':
    main()