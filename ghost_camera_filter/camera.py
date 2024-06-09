import os 
import cv2 as cv 
import pyautogui as auto
import numpy as np
import os 
'''
Takes screenshots, photos and records videos from target device 

[] - add target address to this module testing

[X] - Testing all aspects of the module is a pass
'''

def takeScreenshot():
    output_path = "img/image_001.png"
    img = auto.screenshot()
    if not output_path.endswith(".png"):
        output_path += ".png"
        img.save(output_path)
        output = f"Image saved to {output_path}.\n"
        
def captureImage():
     cap = cv.VideoCapture(0)

     if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Read a single frame from the camera
     ret, frame = cap.read()

     if not ret:
        print("Error: Could not read frame.")
        return

    # Release the camera
     cap.release()

    # Save the captured frame as an image file
     image_filename = "captured_image.jpg"
     cv.imwrite(image_filename, frame)
     print(f"Image captured and saved as {image_filename}")

def recordVideo():
    duration_seconds = 120 
    output_filename = "video/recored_video_001.avi" #Modify the code to "video/recorded_video002" as you record new videos 
     # Open the first camera device (0) or change the index if you have multiple cameras
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')  # You can change the codec as needed
    fps = 30  # Frames per second
    resolution = (640, 480)  # Video resolution
    out = cv.VideoWriter(output_filename, fourcc, fps, resolution)

    print(f"Recording video to {output_filename} for {duration_seconds} seconds...")

    start_time = cv.getTickCount()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Write the frame to the output video file
        out.write(frame)

        # Check if the recording duration has been reached
        elapsed_time = (cv.getTickCount() - start_time) / cv.getTickFrequency()
        if elapsed_time >= duration_seconds:
            break

        # Display the recording in a window (optional)
        cv.imshow("Recording", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and video writer
    cap.release()
    out.release()

    # Close any open windows
    cv.destroyAllWindows()

    print(f"Video recording complete. Saved as{output_filename}\n")

def record_screen():
    duration_seconds=10
    output_filename="screen_recorded_video.avi"
    # Set the screen resolution (you may need to adjust this based on your screen size)
    screen_width, screen_height = auto.size()

    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')  # You can change the codec as needed
    fps = 20  # Frames per second
    resolution = (screen_width, screen_height)
    out = cv.VideoWriter(output_filename, fourcc, fps, resolution)

    print(f"Recording screen to {output_filename} for {duration_seconds} seconds...")

    start_time = cv.getTickCount()

    while True:
        # Capture the screen frame
        screenshot = auto.screenshot()
        frame = np.array(screenshot)
        frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

        # Write the frame to the output video file
        out.write(frame)

        # Check if the recording duration has been reached
        elapsed_time = (cv.getTickCount() - start_time) / cv.getTickFrequency()
        if elapsed_time >= duration_seconds:
            break

    # Release the video writer
    out.release()
    print(f"Screen recording complete. Saved as {output_filename}")