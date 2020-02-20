def scoring(input_file, output_file):
    score = 0
    h = dict()
    v = dict()
    tags = dict()

    #read from the input file
    inputs = open(input_file, 'r')

    pictures = inputs.read() 
    pictures = pictures.split('\n')
    pictures.pop(0) # getting rid of the number of images
    pictures.pop(-1) # getting rid of the empty last line

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
    
    #create superV

    #read from output_file
    output = open(output_file, 'r')
    slideshow = output.read()

    slideshow = slideshow.split('\n')
    del slideshow[0]


    for x in range(len(slideshow)-1):
        cur_image = int(slideshow[x][-1])
        compare_image = int(slideshow[x+1][0])

        score += calculate_score(tags.get(cur_image), tags.get(compare_image))
    
    # return score
    print(tags)
    print(slideshow)


def create_tags:

def calculate_score(cur_image, image):
    unique_tags = list() #list of venn diagram unique, intersect, unquie
    unique_value = 0 #the number that will be added to list
    
    #calculate the unqinue of cur_image
    for tag in cur_image:
        if not(tag in image):
            unique_value+= 1

    unique_tags.append(unique_value) #the unique of cur_image appeneded
    unique_tags.append(len(cur_image) - unique_value) #the number of intersecting

    unique_value = 0

     #calculate the unqinue of image
    for tag in image:
        if not(tag in cur_image):
            unique_value+= 1
    
    unique_tags.append(unique_value)
    
    return min(unique_tags) #return the minimum of the three


scoring("a_example.txt", "a_sample_answer.txt")