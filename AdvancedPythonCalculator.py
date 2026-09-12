print("!!Welcome to my CALCULATOR!!")

def operation(num1,num2,op):
    if op =="+":
        answer = num1+num2
        return answer
    elif op =="-":
        answer = num1-num2
        return answer
    elif op =="*":
        answer = num1*num2
        return answer
    elif op =="/":
        answer = num1/num2
        return answer
    else:
        return "Invalid Operation"


def calculation():
    content = []
    cont = True
    while cont:
        number = input("Enter a number: ")
        try:
            content.append(float(number))
        except ValueError:
            print("Invalid Input!")
            return
        ops = input("Enter an operation(+,-,*,/), type 'end' to finish: ")
        if ops == "+" or ops =="-" or ops == "*" or ops =="/":
            content.append(ops)
        elif ops.lower() == "end":
            cont = False
            break
        else:
            print("Invalid Input")
            cont = False
    while len(content)!=1:
        while "*" in content:
            where = content.index("*")
            answer = operation(content[where - 1],content[where + 1],content[where])
            content[where -1 : where +2] = [answer]
        while "/" in content:
            where = content.index("/")
            answer = operation(content[where - 1],content[where + 1],content[where])
            content[where -1 : where +2] = [answer]
        while "+" in content:
            where = content.index("+")
            answer = operation(content[where - 1],content[where + 1],content[where])
            content[where -1 : where +2] = [answer]
        while "-" in content:
            where = content.index("-")
            answer = operation(content[where - 1],content[where + 1],content[where])
            content[where -1 : where +2] = [answer]
    else:
        print(f"Your answer: {content}")

calculation()
