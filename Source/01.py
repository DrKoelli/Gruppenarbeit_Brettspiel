def save(name,win):
    #opening the save file to read and write
    fobj=open("scores.txt", "r+")
    #saving the content of the file into a list of strings
    lines = fobj.readlines()

    # check if the given name already exists
    #enumerate keeps track of the index of each line -> enumerate(['a', 'b', 'c'])-->(0, 'a'), (1, 'b'), (2, 'c')
    for i, line in enumerate(lines):
        if line.startswith(name + ","):
                #splitting the line into two parts, the second entry->[1] should be the number of already existing wins
            parts = line.strip().split(", ")
            #saving the number of wins into a variable
            existing_win = int(parts[1])

                # Updating the score
            updated_win = existing_win + win
            #writing the file  into the line the name was found in the list named files
            lines[i] = f"{name}, {updated_win}\n"
            #navigating to the beginning of the file
            fobj.seek(0)
            #deleting the contents of the file
            fobj.truncate()
            #rewriting the file with the updated list
            fobj.writelines(lines)
            print("USER FOUND!")
            return
     #if the name does not exist we create a new entry       
    fobj.write("{}, {}\n".format(name, win))
    fobj.close()
