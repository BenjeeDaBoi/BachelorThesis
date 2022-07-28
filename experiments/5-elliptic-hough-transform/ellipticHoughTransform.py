# Elliptische Hough Transformation - EHT
# zur Ermoeglichung der Bachelorarbeit

# EHT von Eiern mit Bluring und Canny Kantenerkennung
# von Ellipsen und Eiern im Nest

# geschrieben von Benjamin H.
# Studiengang: Informatik - Software & Information Engineering
# 6. Semester - Sommersemester 2022

import matplotlib.pyplot as plt
import numpy as np
import cv2

from skimage import color, img_as_ubyte, io
from skimage.feature import canny
from skimage.transform import hough_ellipse
from skimage.draw import ellipse_perimeter

# Lade Bild und wende Graustufenkonvertierung, Gausssche Unschaerfe
# und eine Canny Kantenerkennung an
image_rgb = cv2.imread("../0-test-images/brightsample01.tiff")[:,:,:3]
image_rgb = cv2.resize(image_rgb, (480, 270))
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
image_gaussian = cv2.GaussianBlur(image_gray, (9, 9), 0)
image_gaussian = cv2.Canny(image_gray, 60, 60)

# Anzeige des Bildes
cv2.imshow('Test', image_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Speichere die Resultate der Elliptischen Hough Transformation
result = hough_ellipse(image_gaussian, accuracy=1, threshold=120, min_size=10, max_size=20)
result.sort(order='accumulator')

# Bekomme die Beste Ellipse von der Transformation
best = list(result[-1])
yc, xc, a, b = [int(round(x)) for x in best[1:5]]
orientation = best[5]

# Zeichne Ellipse auf das Bild
cy, cx = ellipse_perimeter(yc, xc, a, b, orientation)
image_rgb[cy, cx] = (0, 0, 255)

# Zeichne die Kanten in Weiss und die Ellipse in Rot
edges = color.gray2rgb(img_as_ubyte(image_gaussian))
edges[cy, cx] = (250, 0, 0)

# Zeichne die jeweiligen Bilder
fig2, (ax1, ax2) = plt.subplots(ncols=2, nrows=1, figsize=(8, 4),
sharex=True, sharey=True)

ax1.set_title("Original")
ax1.imshow(image_rgb)
ax2.set_title("Result")
ax2.imshow(edges)
plt.show()