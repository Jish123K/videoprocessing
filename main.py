import cv2

import numpy as np

import speech_recognition as sr

from moviepy.editor import VideoClip, ImageSequenceClip

# Load the video file

video = cv2.VideoCapture("video.mp4")

# Get the frame rate of the video

fps = video.get(cv2.CAP_PROP_FPS)

# Initialize the object detection and speech-to-text models

object_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

speech_recognizer = sr.Recognizer()

# Create a list to store the important moments in the video

important_moments = []

# Iterate over the frames of the video

while True:

    # Read the next frame

    ret, frame = video.read()

    # If the frame was not read successfully, break out of the loop

    if not ret:

        break

    # Detect objects in the frame

    objects = object_detector.detectMultiScale(frame, 1.1, 4)

    # If any objects were detected, transcribe the audio from the frame

    if len(objects) > 0:

        audio = sr.AudioFile("audio.wav")

        with audio as source:

            audio_data = speech_recognizer.record(source)

        # Get the text from the audio

        text = speech_recognizer.recognize_google(audio_data)

        # If the text is not empty, add it to the list of important moments

        if text:

            important_moments.append((frame, text))

    # Display the frame

    cv2.imshow("Video", frame)
    

    # Wait for a key press

    key = cv2.waitKey(1)

    # If the Esc key was pressed, break out of the loop

    if key == 27:

        break

# Close the video file

video.release()

# Destroy all the windows

cv2.destroyAllWindows()

# Sort the list of important moments by timestamp

important_moments.sort(key=lambda x: x[0])

# Create a new video clip that contains the important moments

video_clip = VideoClip(ImageSequenceClip([frame for frame, text in important_moments]))

# Write the video clip to a file


video_clip.write_videofile("summary.mp4")
# Add a fade in effect to the beginning of the summary

video_clip = video_clip.fadein(1)

# Add a fade out effect to the end of the summary

video_clip = video_clip.fadeout(1)

# Add a title card to the beginning of the summary

title_card = ImageClip("title_card.png")

video_clip = title_card.set_duration(1) + video_clip

# Add a credits card to the end of the summary

credits_card = ImageClip("credits_card.png")

video_clip = video_clip + credits_card.set_duration(1)
# Create a window to display the video

window = tk.Tk()

window.title("Video Summary")

# Create a frame to display the video player

video_frame = tk.Frame(window)

video_frame.pack()

# Create a video player widget

video_player = tk.Label(video_frame, text="")

video_player.pack()

# Create a button to start summarizing the video

start_button = tk.Button(window, text="Start", command=start_summary)

start_button.pack()

# Create a button to stop summarizing the video

stop_button = tk.Button(window, text="Stop", command=stop_summary)

stop_button.pack()

# Create a function to start summarizing the video

def start_summary():

    # Load the video file

    video = cv2.VideoCapture("
                             # Create a label to display the length of the summary

summary_length_label = tk.Label(window, text="Summary Length:")

summary_length_label.pack()

# Create a spinbox to allow the user to customize the length of the summary

summary_length_spinbox = tk.Spinbox(window, from_=1, to=100, increment=1)

summary_length_spinbox.pack()

# Create a label to display the emphasis of the summary

summary_emphasis_label = tk.Label(window, text="Summary Emphasis:")

summary_emphasis_label.pack()

# Create a radiobutton group to allow the user to choose the emphasis of the summary

summary_emphasis_radiobutton_group = tk.Radiobutton(window, text="Faces", value="faces")

summary_emphasis_radiobutton_group.pack()

summary_emphasis_radiobutton_group = tk.Radiobutton(window, text="Audio", value="audio")

summary_emphasis_radiobutton_group.pack()

summary_emphasis_radiobutton_group = tk.Radiobutton(window, text="Both", value="both")

summary_emphasis_radiobutton_group.pack()

# Create a button to generate the summary

generate_summary_button = tk.Button(window, text="Generate Summary", command=generate_summary)

generate_summary_button.pack()

# Create a function to generate the summary

def generate_summary():

    # Get the length of the summary from the spinbox

    summary_length = summary_length_spinbox.get()

    # Get the emphasis of the summary from the radiobutton group

    summary_emphasis = summary_emphasis_radiobutton_group.get()

    # Generate the summary

    video_summary = generate_video_summary(video, summary_length, summary_emphasis)

    # Write the summary to a file

    video_summary.write_videofile("summary.mp4")

    # Display a message to the user

    tk.messagebox.showinfo("Summary Generated", "The summary has been generated.")
                            # Get the total length of the video

video_length = video.get(cv2.CAP_PROP_FRAME_COUNT) * fps

# Get the number of segments in the summary

summary_length = len(important_moments)

# Get the percentage of the video that was included in the summary

summary_percentage = summary_length / video_length * 100

# Display the video analytics information

print("Video length:", video_length)

print("Number of segments in summary:", summary_length)

print("Percentage of video included in summary:", summary_percentage) 
                             # Create a thumbnail for each segment in the summary

thumbnails = [cv2.imread(frame) for frame, text in important_moments]

# Save the thumbnails to a directory

for i, thumbnail in enumerate(thumbnails):

    cv2.imwrite("thumbnails/thumbnail_%d.jpg" % i, thumbnail)
                             # Extract keyframes from each segment in the summary

keyframes = [cv2.imread(frame) for frame, text in important_moments]

# Save the keyframes to a directory

for i, keyframe in enumerate(keyframes):

    cv2.imwrite("keyframes/keyframe_%d.jpg" % i, keyframe)
