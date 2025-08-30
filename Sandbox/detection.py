import cv2
from matplotlib import pyplot as plt

def main():
    # Load the image
    image_path = '../Receiver/Frames/4.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, threshold1=300, threshold2=400)

    #cv2.imshow("view", edges)
    #if cv2.waitKey(0) & 0xFF == ord('q'):
    #    pass
    plt.subplot(121),plt.imshow(gray_image,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()
    #return
    # Analyze the edges to identify bright and dark stripes
    # You can use various techniques like histogram analysis, pixel intensity analysis, etc.

    # For instance, you can calculate the average pixel intensity of bright and dark areas
    average_bright = gray_image[edges > 0].mean()
    average_dark = gray_image[edges == 0].mean()

    print(average_bright, average_dark)
    # frame_180.jpg: 56.64458048253511 82.38796217735654
    # frame_181.jpg: error + nan 99.33378134645062
    # frame_182.jpg: error + nan 98.8542472029321
    # cropped.jpg: 70.05433901054339 128.92943450278628
    # Set thresholds based on the average pixel intensities
    brightness_threshold = 200
    darkness_threshold = 50

    # Check if the image contains bright and dark stripes
    contains_bright_stripes = average_bright > brightness_threshold
    contains_dark_stripes = average_dark < darkness_threshold

    if contains_bright_stripes and contains_dark_stripes:
        print("The image contains both bright and dark stripes.")
    elif contains_bright_stripes:
        print("The image contains bright stripes.")
    elif contains_dark_stripes:
        print("The image contains dark stripes.")
    else:
        print("The image does not appear to contain bright or dark stripes.")

if __name__ == "__main__":
    main()
