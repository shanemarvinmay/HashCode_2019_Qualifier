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

def find_biggest_img(h, super_v):
    bg_idx = 0
    bg_tags = 0
    for i in h:
        if len(h[i]) > bg_tags:
            bg_idx = i
            bg_tags = len(h[i])
    for i in super_v:
        if len(super_v[i]) > bg_tags:
            bg_idx = i
            bg_tags = len(super_v[i])
    return [bg_idx]

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

def create_tags(h, super_v):
    tags = {}

    for img in h:
        for tag in h[img]:
            if tag not in tags:
                tags[tag] = set()

            tags[tag].add(img)

    for img in super_v:
        for tag in super_v[img]:
            if tag not in tags:
                tags[tag] = set()

            tags[tag].add(img)

    return tags

def scoring(slideshow):
    print(slideshow)





a = 'a_example.txt'
b = 'b_lovely_landscapes.txt'
c = 'c_memorable_moments.txt'
d = 'd_pet_pictures.txt'
e = 'e_shiny_selfies.txt'
h, v = read_file(a)

slideshow = find_biggest_img(h, v)
super_v = create_super_v(v)
tags = create_tags(h, v)

# print(super_v)
print(slideshow)
