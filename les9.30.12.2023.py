from PIL import Image
from PIL import ImageFilter
with Image.open("завантаження.jpg") as pic_original:
    print("Розмір:", pic_original.size)
    print("Формат:", pic_original.format)
    print("Тип:", pic_original.mode)
    #pic_original.show()
    pic_gray = pic_original.convert('L')
    pic_gray.save("gray.jpg")
    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_up = pic_blured.transpose(Image.ROTATE_180)

    pic_blured.save("blur.jpg")
    pic_up.save("rotate.jpg")