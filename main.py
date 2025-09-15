import cv2
import numpy as np
import os

path = "img.png"
if not os.path.exists(path):
    raise FileNotFoundError(f"Файл не найден: {path}")

img = cv2.imread(path)
h, w = img.shape[:2]

tx, ty = 50, 30
M_shift = np.float32([[1, 0, tx], [0, 1, ty]])
shifted = cv2.warpAffine(img, M_shift, (w, h))

angle = 30
M_rotate = cv2.getRotationMatrix2D((w//2, h//2), angle, 1)
rotated = cv2.warpAffine(shifted, M_rotate, (w, h))

nonlinear = np.zeros_like(rotated)
for y in range(h):
    for x in range(w):
        new_x = int((x**3) / 7) % w
        new_y = y
        nonlinear[new_y, new_x] = rotated[y, x]


cv2.imwrite("shifted.png", shifted)
cv2.imwrite("rotated.png", rotated)
cv2.imwrite("nonlinear.png", nonlinear)

cv2.imwrite("shifted.pbm", cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY))
cv2.imwrite("rotated.pbm", cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY))
cv2.imwrite("nonlinear.pbm", cv2.cvtColor(nonlinear, cv2.COLOR_BGR2GRAY))

print("Готово: сохранены PNG и PBM версии изображений.")
