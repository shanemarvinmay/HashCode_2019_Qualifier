def read_file(file_name):
    f = open(file_name, 'r')
    tags = {} # tags to idxs
    h = {} # horizontal image idx to tags
    v = {} # verticle image idx to tags
    f = open(file_name, 'r')
    lines = f.read() #readlines was a cool method but kept the \n in every string
    lines = lines.split('\n')
    lines.pop(0) # getting rid of the number of images
    lines.pop(-1) # getting rid of the empty last line
    print(lines)

read_file('a_example.txt')

def calulateScore(cur_image, image):
    uniqueTags = list()
    uniqueVal = 0
    
    for tag in cur_image:
        if not(tag in image):
            uniqueVal += 1

    uniqueTags.append(uniqueVal)
    uniqueTags.append(len(cur_image) - uniqueVal)

    uniqueVal = 0

    for tag in image:
        if not(tag in cur_image):
            uniqueVal += 1
    
    uniqueTags.append(uniqueVal)
    
    return min(uniqueTags)

image1 = {"cat", "beach", "sun", "world", "grrr"}
image2 = {"cat", "garden", "beach", "hello"}

print(calulateScore(image1, image2))

