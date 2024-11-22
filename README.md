# Pitch Reader

A real-time football commentary system that transforms on-screen text into natural speech using OCR technology and artificial intelligence. Captures screen content, processing it through OCR, generating context-aware commentary, and delivering it through high-quality text-to-speech conversion, emualating the style of Martin Tyler.

## Core Functionality
- **Real-time Screen Capture**: Continuous monitoring of specified screen regions
- **OCR Processing**: Accuarate and efficient text extraction using EasyOCR with GPU acceleration
- **AI Commentary Generation**: Dynamic, context-aware commentary using GPT-4
- **Natural Speech**: Voice output using OpenAI's TTS API
- **Context Management**: Buffer-based context management system retains relevant conversation history for coherent commentary
- **Configurable Settings**: Customizable screen capture areas, audio parameters and commentary style 

## Requirements

### Hardware Requirements
- Modern GPU (Nvidia recommended for optimal OCR performance)
- Minimum 8GB RAM
- Modern multi-core processor

### Software Requirements
- Python 3.8 or higher
- Windows 10/11


### API Requirements
- OpenAI API key with access to:
  - GPT-4 model
  - TTS API

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/Kevon-Williams/pitch-reader.git
cd pitch_reader
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configuration Setup

Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=api_key
```

## Component Overview

### 1. Screen Reader (`core/reader.py`)
The `ScreenReader` class drives the system:

```python
reader = ScreenReader(api_key, buffer_size=10)
reader.take_screenshot_and_process(duration=300, sleep_time=5)
```

Key parameters:
- `buffer_size`: Number of previous texts to maintain for context
- `duration`: Total runtime in seconds
- `sleep_time`: Interval between screenshots

### 2. OCR Service (`services/ocr.py`)
Handles text extraction from screen captures:

```python
ocr = Ocr()
text = ocr.process_image(image_array)
```

### 3. Commentary Generator (`core/generate_text.py`)
Generates dynamic football commentary using GPT-4:

```python
commentary = Commentary(api_key)
response = commentary.generate_commentary(previous_texts)
```

Commentary guidelines:
- Natural speaking patterns
- Tactical insights
- Context-aware responses
- Maximum 70 characters per commentary

### 4. Audio Service (`services/audio.py`)
Manages text-to-speech conversion and audio playback:

```python
audio = Audio(api_key)
audio.start_audio_stream(text)
audio.stop_audio()
```

### Basic Usage

```python
from pitch_reader.core.reader import ScreenReader
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize and run the reader
reader = ScreenReader(api_key)
reader.take_screenshot_and_process(duration=300)  # Run for 5 minutes
reader.close_audio_stream()
```

### Custom Configuration

```python
from pitch_reader.core.config import ScreenConfig, AudioConfig

# Custom screen configuration
screen_config = ScreenConfig()
screen_config.top = 1000
screen_config.left = 500
screen_config.width = 800
screen_config.height = 30

# Custom audio configuration
audio_config = AudioConfig()
audio_config.rate = 44100
audio_config.channels = 2
```

### Common Issues

1. **OCR Performance Issues**
   - Screen capture area may need adjusting for better text visibilty

2. **Audio Playback Problems**
   - Occasional static due to GPT model
   - Audio playback may be delayed based on system performance

## Future Enhancements

- Multi-language support
- Custom voice models
- Improved context management
- GUI for live configuration and monitoring
