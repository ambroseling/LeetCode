
def solution(asteroids):
    stack = []
    # import ipdb;ipdb.set_trace()
    for i in range(len(asteroids)):
        # if the asteroid is going RIGHT
        if asteroids[i] > 0:
            stack.append(asteroids[i])

        # if the asteroid is going LEFT
        else:
            # if there are no asteroids yet add it to the stack
            if len(stack) == 0:
                stack.append(asteroids[i])
            else:
                while len(stack) > 0: #there are more collisions possible
                    # if the incoming asteroid 
                    if abs(asteroids[i]) >  abs(stack[-1]):
                        if stack[-1] > 0:
                            stack.pop()
                            if len(stack) == 0:
                                stack.append(asteroids[i])
                                break
                        else:
                           stack.append(asteroids[i])
                           break
                    elif abs(asteroids[i]) == abs(stack[-1]):
                        if stack[-1] > 0:
                            stack.pop()
                            break
                        else:
                            stack.append(asteroids[i])
                            break
                    elif abs(asteroids[i]) < abs(stack[-1]):
                        if stack[-1] > 0:
                            break
                        else:
                            stack.append(asteroids[i])
                            break

                    

    return stack
         
            
if __name__ == "__main__":
    asteroids =[-2,-2,1,-2]

    output = solution(asteroids)
    print(output)

# -5
#     # Testcases:  [3,-5,-1,1,2,-5]
#     # Testcase : [-2,-1,1,2]
#     # Testcase: [-2,-2,1,-2]


# 5,1,3,-6
# 10 2 -5

# if the asteroid is going to the LEFT
    # if there is an asteroid in the stack that is going RIGHT && greater in size
    # collision will happen, all asteroids in btw are exploded

    # if there are asteroids in the stack that is going RIGHT but none are GREATER in size
    # incoming left asteroid will elimiate all the asteroids up until the last asteroid that is going left


    # if there are no asteroids going RIGHT, that means all astetoids are going LEFT, simply add to stack

# if the asteroid is going to the RIGHT
    # if previous asteroids moved LEFT, do nothing, simply add to stack
    # if previous asteroids moved RIGHT, do nothing as well 






