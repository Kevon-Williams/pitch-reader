# Pitch Reader

A real-time football commentary system that transforms on-screen text into natural speech using OCR technology and artificial intelligence. Captures screen content, processes it through OCR, generates context-aware commentary, and delivers it through high-quality text-to-speech conversion.

## Core Functionality
- **Real-time Screen Capture**: Continuous monitoring of specified screen regions.
- **OCR Processing**: Accurate and efficient text extraction using EasyOCR.
- **AI Commentary Generation**: Dynamic, context-aware commentary using Groq.
- **Natural Speech**: Voice output using ElevenLab's API.

## Requirements

### Hardware Requirements
- Modern GPU (Nvidia recommended for optimal OCR performance).
- Minimum 8GB RAM.
- Modern multi-core processor.

### Software Requirements
- Python 3.8 or higher.
- Windows 10/11.

### API Requirements
- Groq API key with access to:
- ElevenLabs API key

## Installation

### 1. Clone Repository

Clone the repository from GitHub and navigate to the project directory.

### 2. Install Dependencies

Install the required dependencies using `pip`.

### 3. Configuration Setup

Create a `.env` file in the root directory and add your OpenAI API key.

## Usage

Initialize and run the `ScreenReader` to capture screen content, generate commentary, and play audio.

### Custom Configuration

Customize screen capture areas and audio parameters using configuration classes.

### Common Issues

1. **OCR Performance Issues**
   - Screen capture area may need adjusting for better text visibility.

2. **Audio Playback Problems**
   - Occasional static due to GPT model.
   - Audio playback may be delayed based on system performance.

## Future Enhancements

- GUI for live configuration and monitoring.
