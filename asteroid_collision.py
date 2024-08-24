
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

# My original thinking: 
# if the asteroid is going to the LEFT
    # if there is an asteroid in the stack that is going RIGHT && greater in size
    # collision will happen, all asteroids in btw are exploded

    # if there are asteroids in the stack that is going RIGHT but none are GREATER in size
    # incoming left asteroid will elimiate all the asteroids up until the last asteroid that is going left


    # if there are no asteroids going RIGHT, that means all astetoids are going LEFT, simply add to stack

# if the asteroid is going to the RIGHT
    # if previous asteroids moved LEFT, do nothing, simply add to stack
    # if previous asteroids moved RIGHT, do nothing as well 



# Somebody elses thinking:
# your while loop can also have the condition of the top asteroid in stack
# is opposite in sign with the one incoming, cuz only when theres opposite sign you want to loop

# key thing is there is no need to immediately append to the stack when you do a comparison, 
# when there are 


# Model solution:
for asteroid in asteroids:
    while stack and asteroid < 0 < stack[-1]:
        # this means that the incoming one is larger by abs value
        if stack[-1] < -asteroid:
            stack.pop() # remove the top one in stack since 
            continue
        elif stack[-1] == -asteroid:
            stack.pop()
        break
    else:
        stack.append(asteroid)

        
