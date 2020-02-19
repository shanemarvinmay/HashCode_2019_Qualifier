def read_file(file_name):
    f = open(file_name, 'r')

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