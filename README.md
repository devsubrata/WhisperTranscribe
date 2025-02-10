# WhisperTranscribe

WhisperTranscribe is a simple yet powerful transcription tool that uses AI to convert your audio and video files into accurate text. Whether you're working with podcasts, lectures, interviews, or any spoken content, WhisperTranscribe makes transcription fast and easy.

![WhisperTranscribe](E:\ProjectsCode\Python\GUI\TranscriptMediaFile\Releases\WhisperTranscribe.jpg)

## Features

-   **Supports a wide range of media formats**: MP3, WAV, FLAC, OGG, M4A, AAC, WMA, OPUS, MP4, MKV, AVI, MOV, WMV, FLV, and WEBM.
-   **Fast and accurate transcription**: Powered by the Whisper AI model, your files are transcribed quickly with high accuracy.
-   **User-friendly interface**: Load your media files, transcribe them, and save the results with just a few clicks.
-   **Error handling**: If transcription fails, you'll receive a helpful error message to troubleshoot the issue.

## Installation

### Option 1: **Download the Compiled Windows Version**

If you're using **Windows** and want a quick and easy setup, you can download the compiled executable of WhisperTranscribe directly from our GitHub Releases page:

1. Go to the [Releases](https://github.com/devsubrata/WhisperTranscribe/releases) page of this repository.
2. Download the latest `.exe` file for **Windows** (e.g., `WhisperTranscribe-v1.0.0.exe`).
3. Run the executable and start using WhisperTranscribe immediately.

### Option 2: **Install from Source (for Linux/macOS/Windows)**

If you prefer to run WhisperTranscribe from source or want to customize it:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/devsubrata/WhisperTranscribe.git
    ```

2. **Install dependencies**: WhisperTranscribe requires Python and several packages. You can install the necessary packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. **Install FFmpeg**: Whisper requires FFmpeg to process media files. You can download and install FFmpeg from [FFmpeg official website](https://ffmpeg.org/download.html).
4. **Run the application**: After installing all dependencies, you can start the application by running:

    ```bash
    python transcribe_media.py
    ```

## Usage

1. Open the application.
2. Click the **Open File** button to select the audio or video file you wish to transcribe.
3. The app will process the file and generate the transcription.
4. Once the transcription is complete, you can save the text as a `.txt` file.
5. If transcription fails, an error message will be shown explaining the issue.

## Supported Media Formats

WhisperTranscribe supports the following media formats for transcription:

-   **Audio Files**:

    -   MP3 (\*.mp3)
    -   WAV (\*.wav)
    -   FLAC (\*.flac)
    -   OGG (\*.ogg)
    -   M4A (\*.m4a)
    -   AAC (\*.aac)
    -   WMA (\*.wma)
    -   OPUS (\*.opus)

-   **Video Files** (only audio will be transcribed):

    -   MP4 (\*.mp4)
    -   MKV (\*.mkv)
    -   AVI (\*.avi)
    -   MOV (\*.mov)
    -   WMV (\*.wmv)
    -   FLV (\*.flv)
    -   WEBM (\*.webm)

## Troubleshooting

-   **No file opened error**: Ensure that you have selected a valid file.
-   **Transcription failure**: Check for issues with the file format or ensure that the Whisper model and FFmpeg are correctly installed.
-   **Model loading error**: Make sure that your system meets the hardware requirements for running Whisper (preferably with GPU support).

## Compiling for Windows (Creating Executable)

If you want to compile the app into a Windows executable yourself, you can use **PyInstaller**. Follow these steps:

1. **Install PyInstaller**:

    ```bash
    pip install pyinstaller
    ```

2. **Create the executable**: Run the following command in your project directory:

    ```bash
    pyinstaller --onefile --noconsole app.py
    ```

3. The executable file will be generated in the `dist` directory as `app.exe`.
4. You can then upload the `.exe` file to the **Releases** section of your GitHub repo.

## Contributing

We welcome contributions to improve WhisperTranscribe! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

-   Report issues, suggest features, or ask questions via the [GitHub Issues page](https://github.com/devsubrata/WhisperTranscribe/issues).

## License

WhisperTranscribe is released under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy effortless transcription with WhisperTranscribe!
