import cv2

def validate_coordinates(x,y,w,h):
    if x < 0 or x>= w:
        return False
    if y < 0 or y >= h:
        return False
    return True

image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
print(f"Image size: {w} x {h}")

while True:
    try:
        x = int(input(f" X (0-{w - 1}): "))
        y = int(input(f" Y (0-{h - 1}): "))

        if validate_coordinates(x,y,w,h):
            (b, g, r) = image[y, x]
            print(f"Original color ({x}, {y}): R:{r} G:{g} B:{b}")

            image[y, x] = (0, 0, 0)

            print(f"Changed pixel to black: ({x}, {y})")
            break
        else:
            print("Out of size")
            print(f"Must be between: X: 0-{w - 1}, Y: 0-{h - 1}")

    except ValueError:
        print("Integer!")

cv2.imshow("Changed", image)
cv2.waitKey(0)
cv2.destroyAllWindows()