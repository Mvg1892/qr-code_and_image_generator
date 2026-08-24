# Kurze Anleitung

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