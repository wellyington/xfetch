# xfetch

A simple Python app for downloading YouTube videos and converting them to MP3 using Kivy and pytube.

# Table of Contents
* Description
* Installation
* Usage
* Requirements
* How to Use

# Description

xfetch.py is a basic Kivy application that allows users to download YouTube videos or convert them to MP3. The app features a clean interface with a URL input, a download option selector, and a "Download" button. It uses the pytube library to fetch YouTube videos and supports concurrent downloads using Python threading.

The UI is defined in the xfetch.kv file, and it uses Menlo as the default font for a sleek appearance. The app's visual elements include an image header, a URL input field, a download option selector, and a download button.

# Installation

1. Clone the repository:

   `git clone https://github.com/wellyington/xfetch.git`

2. Install the required dependencies:

   `pip install -r requirements.txt`

# Usage

1. Run the xfetch.py script:

   `python xfetch.py`

2. Enter a valid YouTube URL in the provided input field.
3. Choose between downloading the video or the MP3 version using the provided selector.
4. Click the "Download" button to initiate the download.

# Requirements

The app relies on the following Python libraries, all listed in the requirements.txt file:

* certifi==2023.11.17
* charset-normalizer==3.3.2
* decorator==4.4.2
* docutils==0.20.1
* idna==3.6
* imageio==2.33.0
* imageio-ffmpeg==0.4.9
* Kivy==2.2.1
* Kivy-Garden==0.1.5
* moviepy==1.0.3
* numpy==1.26.2
* Pillow==10.1.0
* proglog==0.1.10
* Pygments==2.17.2
* pytube==15.0.0
* requests==2.31.0
* tqdm==4.66.1
* urllib3==2.1.0

Make sure to install these dependencies before running the application.

# How to Use

1. Launch the app by running xfetch.py.
2. Enter a valid YouTube URL in the provided input field.
3. Select either "Video" or "Mp3" using the provided dropdown menu.
4. Click the "Download" button to initiate the download.
5. Monitor the console for progress and completion messages.

Feel free to contribute or provide feedback. Happy downloading!
