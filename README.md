# Privacy-Mask-OpenCV
> Automatic Privacy Protection Tool using OpenCV

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Privacy-Mask-OpenCV** is an open-source project designed to protect privacy by automatically detecting faces in images and applying a mosaic filter. This tool was developed as a term project for the Open Source Software course at Gachon University.

---

## Demo

Here is the result of the program execution. It automatically detects multiple faces and applies a mosaic blur.

| Original Image (Input) | Processed Image (Output) |
| :---: | :---: |
| <img src="images/input.jpg" width="400" alt="Original Image"> | <img src="images/result.jpg" width="400" alt="Result Image"> |
| *Before* | *After* |

> **Note:** You can test your own images by placing them in the `images/` directory.

---

## Key Features

* **Auto Face Detection:** Utilizes OpenCV's Haar Cascade classifier to accurately detect frontal faces.
* **Privacy Mosaic:** Applies a pixelation (mosaic) filter only to the detected face regions (ROI).
* **Multi-Face Support:** Capable of processing multiple faces in a single image simultaneously.
* **Modular Architecture:** Code is separated into detection and processing modules for better collaboration and maintenance.

---

## Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/dhjang01/Privacy-Mask-OpenCV.git](https://github.com/dhjang01/Privacy-Mask-OpenCV.git)
    cd Privacy-Mask-OpenCV
    ```

2.  **Install dependencies**
    This project requires `opencv-python`.
    ```bash
    pip install opencv-python
    ```

3.  **Check required files**
    Ensure that `haarcascade_frontalface_default.xml` is located in the root directory. This file is essential for face detection.

---

## Usage

Run the `main.py` file to start the program.

```bash
python main.py

---

**Steps:**

1.  Place your target image as `images/input.jpg`.
2.  Run the command above in your terminal.
3.  The processed image will be saved as `images/result.jpg` and a preview window will appear.
4.  Press any key to close the preview window.

---

## Project Structure

We separated the roles for effective collaboration using Git.

```bash
Privacy-Mask-OpenCV/
├── main.py                # [Donghyun Jang] Main logic integration
├── face_detector.py       # [Dongho Lee] Face detection module
├── mosaic.py              # [Hyunwoo Kim] Mosaic filter module
├── haarcascade...xml      # OpenCV Pre-trained model
├── requirements.txt       # Dependency list
└── images/                # Image directory
    ├── input.jpg             # Test Input
    └── result.jpg            # Test Output

---

## Contributors

This project was created by **Team Privacy-Mask-OpenCV**.

* **Donghyun Jang** (@dhjang01): Project Manager, Git Management, Main Logic Integration (`main.py`).
* **Dongho Lee** (@dongramiho): Face Detection Algorithm Implementation (`face_detector.py`).
* **Hyunwoo Kim** (@hyunw0000): Image Processing & Mosaic Filter Implementation (`mosaic.py`).

---

## References

* **OpenCV Documentation:** [Cascade Classifier](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)
* **Image Processing:** [OpenCV Python Tutorial](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
* **Model Source:** [Haarcascade XML](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.