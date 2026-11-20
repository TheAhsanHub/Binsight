# ♻️ Binsight

**AI-powered smart bin assistant that tells you which bin your waste belongs in.**

Binsight uses real-time computer vision to recognise items held up to a camera and instantly shows the user the correct bin, helping cut contamination in recycling.

## How it works
1. The user holds an item up to the camera
2. A YOLO model detects and identifies the item
3. Binsight looks it up in a waste database (`waste_db.json`)
4. The correct bin and a short instruction appear on screen

## Tech stack
- Python 3.13
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) – object detection
- OpenCV – live camera feed and on-screen display
- JSON – waste category database

## Getting started
```bash
git clone https://github.com/TheAhsanHub/Binsight.git
cd Binsight
pip install ultralytics opencv-python
python main.py
```
Press **q** to quit. The YOLO model downloads automatically on first run.

## Roadmap
- [ ] Train a custom model on the waste dataset (battery, cardboard, glass, metal, plastic, paper, e-waste and more)
- [ ] Add sensors (e.g. bin fill level, lid control)
- [ ] Pilot proposal to Cardiff Council

## Author
**Ahsan** – BSc Computer Science student, Cardiff
