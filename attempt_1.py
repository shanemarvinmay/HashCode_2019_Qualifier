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
    uniqueTags = list() #list of venn diagram unique, intersect, unquie
    uniqueVal = 0 #the number that will be added to list
    
    #calculate the unqinue of cur_image
    for tag in cur_image:
        if not(tag in image):
            uniqueVal += 1

    uniqueTags.append(uniqueVal) #the unique of cur_image appeneded
    uniqueTags.append(len(cur_image) - uniqueVal) #the number of intersecting

    uniqueVal = 0

     #calculate the unqinue of image
    for tag in image:
        if not(tag in cur_image):
            uniqueVal += 1
    
    uniqueTags.append(uniqueVal)
    
    return min(uniqueTags) #return the minimum of the three

image1 = {"cat", "beach", "sun", "world"}
image2 = {"cat", "garden", "beach", "hello"}

print(calulateScore(image1, image2))

