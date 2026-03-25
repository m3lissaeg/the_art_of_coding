# The Art of Coding

A collection of creative coding scripts, visual concepts, and AI explorations.

## Featured Scripts & Concepts

This repository contains several scripts that explore the fascinating intersection of mathematics, algorithms, and art:

### 1. Kaprekar's Constant (6174)
Explores the mathematical phenomenon discovered by D. R. Kaprekar. If you take any four-digit number (with at least two different digits), arrange the digits in descending and then ascending order, and subtract the smaller from the larger, you will eventually reach exactly `6174`.
* **Interesting Detail:** Once you reach 6174, the process simply repeats `7641 - 1467 = 6174`. It will never take more than 7 iterations to reach this "magic number."

### 2. Harold Cohen's Algorithmic Art
Inspired by Harold Cohen and his pioneering AI program, **AARON**. Cohen was a visionary who taught a computer rules of composition and drawing, creating one of the earliest and most profound examples of artificial intelligence generating original, physical art.
* **Interesting Detail:** AARON didn't just manipulate existing images; it understood abstract concepts like "foreground," "background," and basic human anatomy to generate entirely original compositions from scratch.

### 3. Conway's Game of Life
An implementation of the famous cellular automaton devised by British mathematician John Horton Conway in 1970. It is a "zero-player game," meaning its evolution is determined strictly by its initial state, requiring no further input.
* **Interesting Detail:** Despite having only four simple rules (dealing with underpopulation, survival, overpopulation, and reproduction), the Game of Life is functionally *Turing complete*, meaning it can simulate any computer algorithm given a large enough grid and infinite time.

### 4. Painting to Music (Sonic Pi)
A project merging visual and auditory arts. By interpreting image data (such as colors, brightness, and spatial contrast) from famous paintings, this script translates visual characteristics into a musical sequence generated via **Sonic Pi**.
* **Interesting Detail:** This approach simulates a form of digital synesthesia—mapping HSV (Hue, Saturation, Value) or RGB color data onto pitch, tempo, and timbre to let you literally "hear" a piece of fine art.

## Setup Instructions

### Prerequisites
- Python 3.12.13

### Installation

1. **Navigate to the scripts folder** (where the project files are located):
   ```bash
   cd scripts
   ```

2. **Create a virtual environment** using Python 3.12.13:
   ```bash
   python3.12 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```cmd
     .\venv\Scripts\activate
     ```

4. **Install the dependencies**:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

### Environment Variables

Some scripts in this project (like the generative AI ones) require a Gemini API key. You will need to add it as an environment variable before running those scripts.

- **On macOS/Linux:**
  ```bash
  export GEMINI_API_KEY="your_api_key_here"
  ```

- **On Windows (Command Prompt):**
  ```cmd
  set GEMINI_API_KEY="your_api_key_here"
  ```

- **On Windows (PowerShell):**
  ```powershell
  $env:GEMINI_API_KEY="your_api_key_here"
  ```

*(Optional: To make it persistent on macOS/Linux, you can also add the export line to your `~/.zshrc` or `~/.bashrc` file.)*
