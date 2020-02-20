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
    pictures.pop(-1) # getting rid of the empty last picture

    idx = 0
    for picture in pictures:
        img = picture.split(' ')
        # getting img tags
        img_tags = set()
        for i in range(2, len(img)):
            img_tags.add(img[i])

        # putting the img in either h or v
        if img[0] == 'H':
            h[str(idx)] = img_tags
        else: 
            v[str(idx)] = img_tags
        idx += 1
    
    #create superV
    v = create_super_v(v)

    #create tags
    tags.update(h)
    tags.update(v)

    #read from output_file
    output = open(output_file, 'r')
    slideshow = output.read()
    slideshow.replace(" ", "_")

    slideshow = slideshow.split('\n')
    del slideshow[0]

    #replacing all spaces with _
    for x in range(len(slideshow)):
        # print(image)
        if len(slideshow[x]) > 1:
            slideshow[x] = slideshow[x].replace(" ", "_")

    for x in range(len(slideshow) - 1):
        cur_image = (slideshow[x])
        compare_image = (slideshow[x+1])
        print(cur_image, tags.get(cur_image))
        print(compare_image, tags.get(compare_image))

        # score += calculate_score(tags.get(cur_image), tags.get(compare_image))
    
    # return score
    # print(tags)
    # print(slideshow)


def get_dff(t1, t2):
    return max( t1.difference(t2), t2.difference(t1) )

def create_super_v(v):
    super_v = {}
    # getting img with most tags 
    max_tags = 0
    max_idx = -1

    for img in v:
        if len(v[img]) > max_tags:
            max_tags = len(v[img])
            max_idx = img

    # finding matches with the greatest difference
    ignore = set()
    v_list = list(v.keys())
    v_list.insert(0, max_idx)

    for img in v_list:
        max_diff = -1 
        max_idx = -1

        if img in ignore:
            continue

        ignore.add(img)

        for jmg in v:
            if jmg in ignore:
                continue

            diff = get_dff(v[img], v[jmg])

            if diff > max_diff:
                max_diff = diff
                max_idx = jmg

        combined_key = str(img) + '_' + str(max_idx) 

        super_v[ combined_key ] = v[img]
        super_v[ combined_key ].update(v[max_idx])
    
        ignore.add(max_idx)
    
    return super_v

def calculate_score(cur_image, image):
    unique_tags = list() #list of venn diagram unique, intersect, unquie
    unique_value = 0 #the number that will be added to list
    
    # print(cur_image)
    # print(image)

    #calculate the unqinue of cur_image
    # for tag in cur_image:
    #     if not(tag in image):
    #         unique_value+= 1

    # unique_tags.append(unique_value) #the unique of cur_image appeneded
    # unique_tags.append(len(cur_image) - unique_value) #the number of intersecting

    # unique_value = 0

    #  #calculate the unqinue of image
    # for tag in image:
    #     if not(tag in cur_image):
    #         unique_value+= 1
    
    # unique_tags.append(unique_value)
    
    return 0#min(unique_tags) #return the minimum of the three


print(scoring("a_example.txt", "a_sample_answer.txt"))