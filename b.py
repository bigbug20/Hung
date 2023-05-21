with open('draft.txt') as f:
    data = f.readlines()
    
idx = 0 
length = len(data)
new_data = ""

while idx < length:
    line_list = data[idx].split()
    idline = 0
    length_line = len(line_list)
    while idline < length_line:
        if line_list[idline] == 'Kteam':
            line_list[idline - 1] = 'How'
        idline += 1
    new_data += " ".join(line_list) + "\n"
    idx += 1
    
with open("Kteam.txt", "w+") as new_f :
    new_txt = new_f.write(new_data)