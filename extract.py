import os
from spleeter.separator import Separator
from tqdm import tqdm

def extract_vocals_instrumental_spleeter(input_folder, output_folder):
    separator = Separator('spleeter:2stems')

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.mp3'):
                input_file = os.path.join(root, file)
                # Extract vocals and instrumental to the output folder
                separator.separate_to_file(input_file, output_folder, filename_format='{filename}_{instrument}.wav')

def choose_folder_and_extract_spleeter(parent_folder):
    folders = [f for f in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, f))]

    if not folders:
        print("No folders found in the specified directory.")
        return

    print("Available folders:")
    for i, folder in enumerate(folders):
        print(f"{i + 1}. {folder}")

    selection = input("Enter the index of the folder you want to process: ")

    try:
        selected_index = int(selection) - 1
        selected_folder = folders[selected_index]
        selected_path = os.path.join(parent_folder, selected_folder)

        # Extract vocals and instrumental with Spleeter and progress bar
        print("Processing...")
        with tqdm(total=100, desc="Progress", dynamic_ncols=True) as pbar:
            extract_vocals_instrumental_spleeter(selected_path, selected_path)
            pbar.update(100)

        print(f"Separated audio saved to: {selected_path}")

    except (ValueError, IndexError):
        print("Invalid selection. Please enter a valid index.")

if __name__ == "__main__":
    parent_folder = 'mp3_output'
    choose_folder_and_extract_spleeter(parent_folder)
