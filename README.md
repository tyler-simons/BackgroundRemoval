# Background Removal App

A Streamlit application that allows users to upload an image and automatically remove its background using the [rembg](https://github.com/danielgatis/rembg) library.

## Features

- Upload images (PNG, JPG, JPEG formats supported)
- Automatic background removal
- Download the processed image
- Handles large images with automatic resizing
- Progress indicators for better user experience

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository
```bash
git clone https://github.com/tyler-simons/BackgroundRemoval.git
cd BackgroundRemoval
```

2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run bg_remove.py
```

The app will be available at http://localhost:8501 in your web browser.

## Usage Guidelines

- Maximum file size: 10MB
- Large images will be automatically resized for processing
- Supported formats: PNG, JPG, JPEG

## License

MIT
