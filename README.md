# Music File Renamer Script

This Python script is designed to rename music files in a given directory and its subdirectories based on their metadata (tags), such as artist and title. The script uses the 'TinyTag' library to read the audio file metadata. The purpose of this script is to organize and standardize the names of music files, making them more easily identifiable and manageable.

## Dependencies:
- Python 3.x
- 'os' module: The script uses this module for operating system related functions (e.g., file operations).
- 'tinytag' library: This library is used to extract metadata (tags) from music files. You can install it using 'pip install tinytag'.

## How It Works:
1. The script starts by specifying the directory containing the music files in the variable `dossier_musique`.
2. It then traverses through all the files in the specified directory and its subdirectories using `os.walk()`.
3. For each file encountered, the script checks if it has one of the supported audio file extensions (e.g., .mp3, .aiff, .wav) using `filename.endswith()`.
4. If the file has the required metadata (artist and title), the script constructs a new name using the format `artist__title.extension` and replaces any spaces with underscores. It also replaces certain characters like '/', '\', ':', '*', '?', '"', '<', '>', '|', which might cause issues in file names.
5. If the file lacks the necessary metadata, the script checks for two specific cases:
    a. If the file name starts with two digits followed by an underscore, or
    b. If the file name contains a long sequence of underscores.
   In these cases, it constructs a new name by removing the leading digits and underscore or the long sequence of underscores.
6. After constructing the new name, the script renames the file using `os.rename()`.

## How to Use:
1. Ensure you have Python 3.x and the 'tinytag' library installed.
2. Copy the script into a Python file (e.g., `music_file_renamer.py`).
3. Modify the `dossier_musique` variable to point to the directory containing your music files.
4. Run the script, and it will automatically rename the supported music files in the specified directory and its subdirectories.

## Note:
- Make sure to back up your music files before running the script, as renaming files may lead to data loss if not handled carefully.
- The script only supports music files with proper metadata. Files lacking artist and title information might not be renamed.

## Troubleshooting:
- If you encounter issues while running the script (e.g., some files are not renamed as expected), check the console for any error messages or exceptions printed by the script.

## Disclaimer:
- The script is provided as-is and without any warranty. Use it at your own risk. The script's author is not responsible for any data loss or damage caused by the use of this script.

Happy organizing and renaming your music files with this script!
