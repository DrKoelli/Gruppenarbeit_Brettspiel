"""
A school project
Designing a popular game
"""

def save(name,win):
    fobj=open("scores.txt", "r+")
    lines = fobj.readlines()

    # check if name already exists
    for i, line in enumerate(lines):
        if line.startswith(name + ","):
                # Parse the existing score value
            parts = line.strip().split(", ")
            existing_win = int(parts[1])

                # Update the score and write the file back
            updated_win = existing_win + win
            lines[i] = f"{name}, {updated_win}\n"
            fobj.seek(0)
            fobj.truncate()
            fobj.writelines(lines)
            print("USER FOUND!")
            return
            
    fobj.write("{}, {}\n".format(name, win))
    fobj.close()
