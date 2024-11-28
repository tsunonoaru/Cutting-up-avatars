from PIL import Image

image = Image.open("new_image.jpg")
red, green, blue = image.split()
new_image = Image.merge("RGB", (red, green, blue))


image = red
coordinates = ((50, 0, 696, 522))
cropped_left = image.crop(coordinates)

image = red
coordinates = ((25, 0, 671, 522))
cropped_middle = image.crop(coordinates)

image1 = cropped_left
image2 = cropped_middle
red_skew = Image.blend(image1, image2, 0.5)



image = blue
coordinates = ((0, 0, 646, 522))
cropped_left = image.crop(coordinates)

image = blue
coordinates = ((25, 0, 671, 522))
cropped_middle = image.crop(coordinates)

image1 = cropped_left
image2 = cropped_middle
blue_skew = Image.blend(image1, image2, 0.5)


image = green
coordinates = ((25, 0, 671, 522))
green_middle = image.crop(coordinates)



effect_image = Image.merge("RGB", (red_skew, green_middle, blue_skew))
effect_image.save("effect_image.jpg")


image = effect_image
image.thumbnail((80, 80))
image.save("avatar_image.jpg")
