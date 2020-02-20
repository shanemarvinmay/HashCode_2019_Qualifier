def read_file(file_name):
    f = open(file_name, 'r')
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
        elif img[0] == 'V': 
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
    if max_idx == -1:
        return {}
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
        combined_key = str(img) + ' ' + str(max_idx) 
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

def find_best_match(img_idx, img_tags, h, super_v, tags, ignore):
    # getting all possible matching imgs 
    matches = set()
    for tag in img_tags:
        for img in tags[tag]:
            if img != img_idx and img not in ignore:
                matches.add(img)
    # find the highest scoring match out of the possible matching imgs 
    biggest_idx = -1
    biggest_score = 0
    for match in matches:
        match_tags = None
        if match in h:
            match_tags = h[match]
        else:
            match_tags = super_v[match]
        score = calculate_score(img_tags, match_tags)
        if score > biggest_score:
            biggest_idx = match
            biggest_score = score
    return biggest_idx, biggest_score

def create_slide_show(h, super_v, tags, slideshow, ignore):
    ignore.add(slideshow[0])

    head = -2
    tail = -2
    while head != -1 and tail != -1:
        # getting old and new head and tail 
        old_head = slideshow[0]
        old_head_tags = None
        if old_head in h:
            old_head_tags = h[old_head]
        else:
            old_head_tags = super_v[old_head]
        old_tail = slideshow[-1]
        old_tail_tags = None
        if old_tail in h:
            old_tail_tags = h[old_tail]
        else:
            old_tail_tags = super_v[old_tail]
        head, head_score = find_best_match(old_head,old_head_tags,h,super_v,tags,ignore)
        tail, tail_score = find_best_match(old_tail,old_tail_tags,h,super_v,tags,ignore)

        # figuring out what to add and where
        if head != tail and head != -1 and tail != -1:
            ignore.add(head)
            ignore.add(tail)
            slideshow.insert(0,head)
            slideshow.append(tail)
        elif head_score > tail_score:
            ignore.add(head)
            slideshow.insert(0,head)
        else:
            ignore.add(tail)
            slideshow.append(tail)
    return slideshow

def write_file(file_name, slideshow):
    f = open(file_name, "w")
    f.write( str(len(slideshow)) + '\n')
    for slide in slideshow:
        f.write(str(slide) + '\n')
    f.close()

a = 'a_example.txt' # 4 
b = 'b_lovely_landscapes.txt' # 80,000 all h
c = 'c_memorable_moments.txt' # 1,000
d = 'd_pet_pictures.txt' # 90,000
e = 'e_shiny_selfies.txt' # 80,000 all v
h, v = read_file(d)
print('h', 'h')
print('v', 'v')
super_v = create_super_v(v)
print('super_v', 'super_v')
slideshow = find_biggest_img(h, super_v)
print('biggest img', 'slideshow')
tags = create_tags(h, super_v)
print('tags', 'tags')
ignore = set() # this is used to hold images that have already been used
slideshow = create_slide_show(h, super_v, tags, slideshow,ignore)
print('slideshow', slideshow)
write_file('d_output.txt',slideshow)
# ignore.add(0)
# ignore.add( find_best_match(0, h[0], h, super_v, tags, ignore)[0] )
# print(  ignore )
# ignore.add( find_best_match(3, h[3], h, super_v, tags, ignore)[0] )
# print( ignore )
