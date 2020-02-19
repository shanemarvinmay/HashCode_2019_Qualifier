def read_file(file_name):
    tags = {} # tags to idxs
    h = {} # horizontal image idx to tags
    v = {} # verticle image idx to tags
    f = open(file_name, 'r')
    lines = f.read() #readlines was a cool method but kept the \n in every string
    lines = lines.split('\n')
    lines.pop(0) # getting rid of the number of images
    lines.pop(-1) # getting rid of the empty last line
    
    idx = 0
    for line in lines:
        img = line.split(' ')
        # getting img tags
        img_tags = set()
        for i in range(2, len(img)):
            img_tags.add(img[i])
        # putting the img in either h or v
        if img[0] == 'H':
            h[idx] = img_tags
        else: 
            v[idx] = img_tags
        idx += 1
    return h, v

h, v = read_file('a_example.txt')
print(h)
print(v)