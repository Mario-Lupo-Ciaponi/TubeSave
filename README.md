# TubeSave 🎥

A simple YouTube video downloader built with **Python**, **pytubefix**, and **CustomTkinter**.

## Features
- ✅ Download YouTube videos in the highest available resolution.
- ✅ Preview video details before downloading.
- ✅ User-friendly GUI with a dark theme.
- ✅ Error handling for invalid or empty URLs.

## Installation

1. **Clone the repository**
   
```bashUsage
git clone https://github.com/yourusername/tubesave.git
cd tubesave
```

2. **Install dependencies**

Ensure you have Python installed (>=3.8), then install the required packages:

```bash
pip install pytubefix customtkinter
pip install customtkinter
```

## Usage

Run the script to launch the TubeSave GUI:

```bash
Run the script to launch the TubeSave GUI:
```

1. Enter a YouTube video link.
2. Click the Download button.
3. Review the video details.
4. Confirm and download the video.

## File Structure

```bash
/tubesave
│── tubesave.py         # Main application file
│── README.md           # Project documentation
```

## Troubleshooting

- **SSL errors**? Try adding this line at the top of `tubesave.py`:
```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

- **GUI issues**? Ensure `customtkinter` is correctly installed.
- **Invalid URL errors**? Double-check the YouTube link format.

## Contributing

Feel free to fork and submit pull requests to improve the project!

## License

📝 MIT License.

Made with ❤️ by Mario Lupo Ciaponi
