from string import Template

def main():
    #String formatting using format()
    str = "Name = {} Age = {}".format("Manohar",25)
    print(str)

    #String formatting using template with placeholders and substitute method with keyword arguments.
    temp = Template("Name = ${name} Age = ${age}");
    str = temp.substitute(name = "Manohar", age = "25")
    print(str)

    #Using substitute method with dictonary
    data = {
            "name": "Manohar",
            "age": "25"
            }
    str = temp.substitute(data)
    print(str)

if __name__ == "__main__":
    main()
