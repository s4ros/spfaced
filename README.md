# s4ros Python Face Detector
Simple Project just-for-fun. Enjoy :)

Short description of the project files:

- [spface.py](spface.py) - Python code which detects faces using WebCAM, cut
detected faces and save them in `head{epoch}.png` files.
- [run-docker-apache.sh](run-docker-apache.sh) - simple script which runs the
Docker container with simple Apache2 configuration and server the [index.html](index.html) site
- [index.html](index.html) - simple web page for displaying captured faces

## Requirements

- install `python-opencv` package
```bash
sudo apt install python-opencv
```
