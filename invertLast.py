import numpy as np
import cv2 as cv

def Image_Inversion(Image):
    Height = Image.shape[0]
    Width = Image.shape[1]
    Channels = Image.shape[2]

    Size = (Height, Width, Channels)

    New_Image = np.zeros(Size, np.uint8)

    for x in range(0, Height):
        for y in range(0, Width):
            for c in range(0, Channels):
                New_Image[x, y, c] = 255 - Image[x,y,c]
    return New_Image


def main():
    Input_Image = cv.imread("2.jpg")
    #kodun yazili oldugu klasore jpg dosyasını atmaniz gereklidir.

    Inverted_Image = Image_Inversion(Input_Image)

    cv.imwrite("2_ters.jpg", Inverted_Image)

    input("Lütfen Enter'a Basın...")


if __name__ == '__main__':
    main()