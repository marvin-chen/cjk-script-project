# CJK Script Project - Work in Progress

This project consists of two phases to explore CJK (Chinese, Japanese, Korean) scripts using computer vision and visualization techniques.

---

## Phase 1: CJK Script Classifier with Computer Vision

Build a Convolutional Neural Network (CNN) to classify Chinese (Hanzi), Japanese (Kanji/Kana), and Korean (Hangul) scripts based on visual features like shapes, stroke count, and unique marks.

**Datasets:**
- **Chinese:** CASIA-HWDB  
- **Japanese:** Kuzushiji-MNIST  
- **Korean:** AI Hub Hangul Dataset

**Tools:**  
OpenCV for feature extraction, PyTorch/TensorFlow for CNN training

---

## Phase 2: Evolutionary Script Visualization

Create an interactive timeline visualizing the evolution of CJK scripts from Oracle Bone Script to modern Hanzi, Kanji/Kana, and Hangul.

**Data Sources:**
- Unihan Database  
- KanjiVG

**Methods:**
- Diffusion models for character evolution  
- t-SNE/PCA for radical visualization  
- WebGL/D3.js for interactive timeline

---

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/cjk-script-project.git
    cd cjk-script-project
    ```

2. **Install Python 3.10** (recommended) if not already installed.

3. **Create a virtual environment:**
    ```bash
    python3.10 -m venv venv
    ```

4. **Activate the virtual environment:**

    - **Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```

    - **Windows:**
        ```bash
        venv\Scripts\activate
        ```

5. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Download datasets:**
    ```bash
    python scripts/download_datasets.py
    ```
    *(Follow manual steps for CASIA-HWDB and AI Hub Hangul)*

---

## Directory Structure

<pre>
cjk-script-project/
├── data/               # Datasets (CASIA-HWDB, Kuzushiji-MNIST, AI Hub Hangul, Unihan, KanjiVG)
├── scripts/            # Utility scripts for downloading datasets
├── models/             # Trained models
├── notebooks/          # Jupyter notebooks for data exploration
├── src/
│   ├── classifier/     # Code for CJK Script Classifier
│   └── visualization/  # Code for Evolutionary Script Visualization
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
</pre>

---

## Requirements

- Python 3.10 (recommended for compatibility)
- See `requirements.txt` for full list of dependencies, including:
  - PyTorch 2.6.0  
  - OpenCV  
  - TensorFlow
