import cv2 
video_path = r'C:\Users\asrav\OneDrive\Pictures\Desktop\python\ImageProject\sample vedio.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit() 
speed_delay = 25 

print("Press 'q' to quit, 's' for Slow, 'f' for Fast, 'n' for Normal")

while cap.isOpened():
    ret, frame = cap.read() 
    if not ret:
        break 
    cv2.imshow('Video Playback', frame) 
    key = cv2.waitKey(speed_delay) & 0xFF
    
    if key == ord('q'):    
        break
    elif key == ord('s'):  
        speed_delay = 100
    elif key == ord('f'):  
        speed_delay = 1
    elif key == ord('n'): 
        speed_delay = 25 
cap.release()
cv2.destroyAllWindows()