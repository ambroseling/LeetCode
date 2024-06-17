
def reverseVowels(input:str):

    output:str = ""

    vowels = ['a','e','i','o','u']

    words = []

    for i,char in enumerate(input):
        if char in vowels:
            words.append(char)

    for i,char in enumerate(input):
        if char in vowels:
            output+=words[-1]
            words.pop()
        else:
            output+=char
    return output


if __name__ == "__main__":
    input = "leetcode"
    output = solution(input)
    print(output)
    # 15 ms
