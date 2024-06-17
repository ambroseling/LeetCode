



def solution(s):
    arr:list = s.split(" ")
    count:int = 0
    output:str = ""
    while len(arr) > 0: 
        if arr[0] == "":
            token = arr.pop(0)
        else:
            token = arr.pop(0)
            if count ==0:
                output+=token
                count+=1
            else:
                output=token + " " +output
            
    return output

if __name__ == "__main__":
    input = "the sky is blue"
    output = solution(input)
    print(output)
    # 8 ms