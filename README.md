# Kurze Anleitung

🇩🇪 [Deutsch](#kurze-anleitung) | 🇬🇧 [English](#quick-guide)

## Voraussetzung: Python und pip
Falls Python noch nicht installiert ist: https://www.python.org/downloads/ <br>
pip ist ab Python 3.4 automatisch dabei. <br>
Check per Terminal, ob beides vorhanden ist:

```sh
python --version
pip --version
```

Um die beiden Skripte auszuführen, muss man die jeweiligen Python-Pakete installieren. <br>

## Alle benötigten Pakete auf einmal installieren (empfohlen)

Im Projektordner liegt eine `requirements.txt`, mit der sich alle benötigten Pakete direkt installieren lassen:

```sh
pip install -r requirements.txt
```

## Alternativ: Pakete einzeln installieren

### Für den Image-Generator muss man Pillow installieren:

```sh
pip install pillow
```
Für mehr Infos:
https://pypi.org/project/pillow/ <br>
https://pillow.readthedocs.io/en/stable/installation.html <br>

### Für den QR-Code Generator muss man QR-Code installieren:

```sh
pip install qrcode
```
Für mehr Infos:
https://pypi.org/project/qrcode/ <br>
<br>
Dann einfach die benötigten Daten im Skript eintragen und dann das Skript ausführen. <br>
Dafür einfach die Kommentare im Code beachten. <br>
<br>
Das war`s. :)

---

# Quick Guide

## Prerequisite: Python and pip
If Python is not yet installed: https://www.python.org/downloads/ <br>
pip is included automatically from Python 3.4 onwards. <br>
Check in the terminal whether both are available:

```sh
python --version
pip --version
```

To run the two scripts, you need to install the respective Python packages. <br>

## Install all required packages at once (recommended)

The project folder contains a `requirements.txt`, which lets you install all required packages directly:

```sh
pip install -r requirements.txt
```

## Alternative: Install packages individually

### For the Image Generator, you need to install Pillow:

```sh
pip install pillow
```
For more info:
https://pypi.org/project/pillow/ <br>
https://pillow.readthedocs.io/en/stable/installation.html <br>

### For the QR Code Generator, you need to install qrcode:

```sh
pip install qrcode
```
For more info:
https://pypi.org/project/qrcode/ <br>
<br>
Then simply enter the required data in the script and run the script. <br>
Just follow the comments in the code for that. <br>
<br>
That's it. :)
