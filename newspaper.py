def solution(paragraphs,width):
    newspaper = []
    for chunk in paragraphs:
        line = ""
        while chunk:
            word = chunk[0]
            if len(word) + len(line) < width:
                word = chunk.pop(0)
                if line == "":
                    line += word
                else:
                    line += " " + word   
                if not chunk:
                    spaces = width - len(line) 
                    left_spaces = spaces // 2
                    right_spaces = spaces - (spaces //2)
                    line = "*" + " "*left_spaces + line + " "*right_spaces + "*" 
                    newspaper.append(line)
            else:
                spaces = width - len(line) 
                left_spaces = spaces // 2
                right_spaces = spaces - (spaces //2)
                line = "*" + " "*left_spaces + line + " "*right_spaces + "*" 
                newspaper.append(line)
                line = ""
                continue

    return newspaper
                
            
if __name__ == "__main__":
    paragraph = [
        ["Hello" , "world","my"],
        ["name","is"],
        ["King","junior","the","fifth","nihaoma"],
        ["Ambrose","Ling"],
    ]
    width = 16
    s = solution(paragraphs=paragraph,width=width)
    print(s)