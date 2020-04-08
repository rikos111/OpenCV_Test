import cv2  # Импортируем модуль OpenCV (cv2)

img1 = cv2.imread('C:/Users/Ramil/PycharmProjects/OpenCV_Test/img/1.jpg')  # Загружаем 1 изображение
img2 = cv2.imread('C:/Users/Ramil/PycharmProjects/OpenCV_Test/img/3.jpg')  # Загружаем 2 изображение


# Функция разворота картинки

def rotate90(src, grad):
    rotated = src
    if grad == 90:
        rotated = cv2.rotate(src, 2, cv2.ROTATE_90_COUNTERCLOCKWISE)
    if grad == 0:
        rotated = cv2.rotate(src, 0, cv2.ROTATE_90_CLOCKWISE)
    return rotated


def calc_src_hash(src):
    image = src
    resize = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)  # Уменьшим картинку
    gray_image = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)  # Переведем в черно-белый формат
    avg = gray_image.mean()  # Среднее значение пикселя
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  # Бинаризация по порогу

    # Рассчитаем хэш
    _hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x, y]
            if val == 255:
                _hash = _hash + "1"
            else:
                _hash = _hash + "0"

    return _hash


# Сравнение хеш сумм

def compare_hash(hash1, hash2):
    i = 0
    count = 0
    while i < len(hash1):
        if hash1[i] != hash2[i]:
            count += 1
        i += 1
    return count


# Сравнение картинок

def compare_src():
    hash1 = calc_src_hash(img1)
    hash2 = calc_src_hash(img2)
    hash3 = calc_src_hash(rotate90(img2, 90))
    hash4 = calc_src_hash(rotate90(img2, -90))
    hash_all = [hash2, hash3, hash4]
    i = 0
    ret = []
    while i < len(hash_all):
        ret.append(compare_hash(hash1, hash_all[i]))
        i += 1
    return ret


# Анализ и результат

def analytics(data_hash):
    if min(data_hash) <= 10:
        ret = 'Картинки схожи'
    elif 10 < min(data_hash) < 20:
        ret = 'Картинки возможно схожи'
    else:
        ret = 'Картинки не схожи'
    return ret


print(compare_src())
print(analytics(compare_src()))
