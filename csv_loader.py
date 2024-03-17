import os
import pandas as pd
print("Current working directory:", os.getcwd())
# Define the path to your dataset
dataset_path = '/home/free/Downloads/archive(1)/face_age'

# Create an empty DataFrame
df = pd.DataFrame(columns=['imagename', 'age'])

# Loop through the folders in the dataset
for folder in os.listdir(dataset_path):
    try:
        # The age is derived from the folder name
        age = int(folder)
    except ValueError:
        # If the folder name cannot be converted to an integer, skip this folder
        continue

    folder_path = os.path.join(dataset_path, folder)
    
    # Only proceed if the folder_path is indeed a directory
    if os.path.isdir(folder_path):
        # Loop through the files in the folder
        for file in os.listdir(folder_path):
            # Only proceed if the file is an image (ends in .jpg, .png, etc.)
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                # Add a new row to the DataFrame
                df = df._append({'imagename': file, 'age': age}, ignore_index=True)
                
# Save the DataFrame as a CSV file
print(df)
df.to_csv('image_data.csv', index=False)
print('CSV file saved successfully')
