# YT-vocal-extractor

## Documentation for ytmp3.py

### Overview

`ytmp3.py` is a Python script that allows users to download and convert YouTube videos to either MP4 or MP3 format. It utilizes popular Python libraries such as `pytube` for YouTube video downloading, `pydub` for audio conversion, and `youtubesearchpython` for searching YouTube videos. The script supports both individual video download and batch download based on search queries.

### Usage

#### 1. Individual Video Download and Conversion

To download and convert a specific YouTube video to MP3 format, use the following command:

```bash
python ytmp3.py --url <YouTube Video URL>
```

- Example:

```bash
python ytmp3.py --url https://www.youtube.com/watch?v=example
```

This will download the video, convert it to MP3, and save it in the specified output path.

#### 2. Search and Download (MP4 Format)

To search for YouTube videos and download them in MP4 format, use the following command:

```bash
python ytmp3.py --search <Search Query>
```

- Example:

```bash
python ytmp3.py --search "Python programming tutorials"
```

This will search for videos related to Python programming tutorials, download them, and save each video in a separate folder under the default MP4 output path.

#### 3. Search and Convert (MP3 Format)

To search for YouTube videos and convert them to MP3 format, use the following command:

```bash
python ytmp3.py --search-convert <Search Query>
```

- Example:

```bash
python ytmp3.py --search-convert "Acoustic guitar covers"
```

This will search for acoustic guitar cover videos, download and convert them to MP3, and save each audio file in the default MP3 output path.

#### Optional Arguments

- `--depth-scan`: Specifies the number of videos to pick from search results. Default is set to 1.

### File Organization

The script organizes downloaded videos and converted audio files into separate folders. For individual video downloads, a folder is created with the video title. For search-based downloads, each video is saved in a separate folder named after its title.

### Helper Functions

The script includes several helper functions:

- `sanitize_filename`: Removes invalid characters from a filename.
- `create_output_folder`: Creates an output folder with a sanitized folder name.
- `download_video`: Downloads a YouTube video in MP4 format.
- `download_and_convert`: Downloads a video and converts it to MP3 format.
- `search`: Searches YouTube videos and downloads them in MP4 format.
- `search_and_convert`: Searches YouTube videos and converts them to MP3 format.

### Output Paths

Default output paths are specified for both MP4 and MP3 formats:

- MP4 Output Path: 'mp4_output'
- MP3 Output Path: 'mp3_output'

## Documentation for extract.py

### Overview

`extract.py` is a Python script that uses the Spleeter library to extract vocals and instrumental parts from MP3 files. It is designed to be used in conjunction with the `ytmp3.py` script to process downloaded MP3 files and separate them into vocals and instrumental tracks.

### Usage

The script assumes that the input MP3 files are stored in folders within a specified parent folder. It provides a menu for the user to select a folder for processing.

To run the script, use the following command:

```bash
python extract.py
```

This will display a list of available folders within the specified parent folder and prompt the user to choose a folder for processing.

### Helper Functions

- `extract_vocals_instrumental_spleeter`: Uses Spleeter to separate vocals and instrumental tracks from MP3 files and saves them in WAV format.
- `choose_folder_and_extract_spleeter`: Allows the user to choose a folder for processing and invokes the extraction function.

### Output

Separated audio files are saved in the same folder as the input MP3 files. The script provides a progress bar during the extraction process.

### Note

Ensure that the Spleeter library is installed in your Python environment before running the script. Install it using:

```bash
pip install spleeter
```

The script assumes a default parent folder name of 'mp3_output,' which corresponds to the default MP3 output path used in the `ytmp3.py` script. If your MP3 files are stored in a different parent folder, modify the `parent_folder` variable in the script accordingly.
