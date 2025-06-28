import os
import shutil

# Define video extensions
VIDEO_EXTENSIONS = {'.mp4'} # , '.avi', '.mkv', '.mov', '.flv', '.wmv', '.webm'

# Set root directory and destination folder
root_dir = r'C:\Users\naimp\Downloads\Coursera - Mathematics for Machine Learning and Data Science Specialization'
destination_folder = os.path.join(root_dir, 'collected_videos')

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Counter for renamed videos
video_counter = 1

# Walk through sorted directories
for dirpath, dirnames, filenames in sorted(os.walk(root_dir)):
    # Skip the destination folder if already created inside root
    if destination_folder in dirpath:
        continue

    for filename in sorted(filenames):
        file_ext = os.path.splitext(filename)[1].lower()

        if file_ext in VIDEO_EXTENSIONS:
            original_path = os.path.join(dirpath, filename)
            new_filename = f"{video_counter}.mp4"
            new_path = os.path.join(destination_folder, new_filename)

            # Copy and rename
            shutil.copy2(original_path, new_path)
            print(f"Copied: {original_path} -> {new_path}")

            video_counter += 1

print("✅ All videos have been copied and renamed.")



# Set the correct path including the file name
output_path = os.path.join(destination_folder,'file_list.txt')

# Create file_list.txt with '1.mp4' to '7.mp4'
with open(output_path, 'w', encoding='utf-8') as f:
    for i in range(1, video_counter):
        f.write(f"file '{i}.mp4'\n")

print(f"✅ file_list.txt created successfully at:\n{output_path}")


import subprocess

# Path to the directory containing your videos and file_list.txt
video_dir = destination_folder   # Use forward slashes or raw string

# ffmpeg command as a list (recommended)
cmd = ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'file_list.txt', '-c', 'copy', 'output.mp4']

# Run the command in the specified directory
result = subprocess.run(cmd, cwd=video_dir)

if result.returncode == 0:
    print("✅ Videos merged successfully!")
else:
    print("❌ ffmpeg command failed.")
