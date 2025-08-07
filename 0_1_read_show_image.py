import cv2
import os

image_path = "./images/bird.jpg"

# Check if the file exists
if not os.path.exists(image_path):
    print(f"❌ File not found: {os.path.abspath(image_path)}")
else:
    print(f"✅ File found: {os.path.abspath(image_path)}")

    image = cv2.imread(image_path)
    
    if image is None:
        print("❌ Failed to read the image. The file may be corrupted or in an unsupported format.")
    else:
        print("✅ Image loaded successfully.")
        cv2.imshow("Original", image)
        cv2.waitKey(0)  # Wait until a key is pressed
        cv2.destroyAllWindows()  # Close all OpenCV windows