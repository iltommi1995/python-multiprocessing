import time
from PIL import Image, ImageFilter
from multiprocessing import Pool

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg'
]
# Imposto un counter


# Modifico le immagini

def process_image(img_name, size, folder):
    img = Image.open('img/'+img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)

    img.save(f'img/processed_{folder}/{img_name}')
    print(f'{img_name} was processed...')

def process_image_for_mp(img_name):
    size = (1200, 1200)
    img = Image.open('img/'+img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)

    img.save(f'img/processed_mp/{img_name}')
    print(f'{img_name} was processed...')

# Tempo alla fine


def process_images_nomp(images, folder):
    t1 = time.perf_counter()

    size = (1200, 1200)
    for img in images:
        process_image(img, size, folder)

    t2 = time.perf_counter()
    print(f'****** Finished in {t2-t1} seconds without multiprocessing ******')


def process_images_mp(images):
    t1 = time.perf_counter()
    p = Pool()
    result = p.map(process_image_for_mp, images)
    p.close()
    p.join()

    t2 = time.perf_counter()
    print(f'****** Finished in {t2-t1} seconds with multiprocessing ******')


if __name__ == '__main__':
    process_images_nomp(img_names, "nomp")
    process_images_mp(img_names)
    