def solution(input:str):
    stack = ""
    for i in range(len(input)):
        if input[i] == "*":
            stack = stack[:-1]
        else:
            stack += input[i]
    return stack

if __name__ == "__main__":
    output = solution("leet**cod*e")
    print(output)
    # 10 ms