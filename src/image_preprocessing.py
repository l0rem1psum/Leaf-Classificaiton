from PIL import Image
import sys
import os

def fill_image(image):
    width, height = image.size
    new_image_length = width if width > height else height
    new_image = Image.new(image.mode, (new_image_length, new_image_length), color='black')
    if width > height:
        new_image.paste(image, (0, int((new_image_length - height) / 2)))
    else:
        new_image.paste(image, (int((new_image_length - width) / 2), 0))
    return new_image

def save_image(image, image_name):
    image.save('../preprocessed_images/' + image_name + '.jpg', 'JPEG')

if __name__ == '__main__':
    for i in range(1584):
        image = Image.open('../images/images/{}.jpg'.format(i + 1))
        image = fill_image(image)
        save_image(image, str(i + 1))