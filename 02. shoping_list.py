initial_list= input().split("!")

while True:
    comamnd = input()
    
    if comamnd = "Go Shopping":
        break
    comamnd_parts = comamnd.split()
    action = comamnd_parts[0]
    
    if action == "Urgent":
        item = comamnd_parts[1]
        
        if item not in initial_list:
            initial_list.insert(0, item)
            
    elif action == "Unnecessary":
        item = comamnd_parts[1]
        if item in initial_list:
            initial_list.remove(item)
            
    elif action == "Correct":
        old_item = comamnd_parts[1]
        new_item = comamnd_parts[2]
        if old_item in initial_list:
            index = initial_list.index(old_item)  
            initial_list[index] = new_item
            
    elif action == "Rearrange":
        item = comamnd_parts[1]
        if item in initial_list:
            initial_list.remove(item)
            
print(initial_list)            
                                  