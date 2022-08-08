# BachelorThesis
Bachelorarbeit für "Computer Science – Software and Information Engineering" an der FH Vorarlberg.
Topic: "Erkennung und Klassifizierung von Eiern: Diskussion & Vergleiche von unterschiedlichen Algorithmen"

## How to Install

* Git Repo herunterladen
* Python 3.9.5 64-Bit installieren
* pip install -r requirements.txt im Root Verzeichnis des Projekts
* .env Datei im Rootverzeichnis des Projekts erstellen mit folgendem Syntax: rtsp://USERNAME:PASSWORT@RTSP-LINK

### Alternative / Optional: Anaconda installieren und eigene Environment erstellen

* Git Repo herunterladen
* Anaconda installieren: https://www.anaconda.com/products/distribution
* Erstellen eines Python Environments: conda create --name thesiseggs (Falls conda proceed fragt => y)
* In die Environment gehen: conda activate thesiseggs
* pip install -r requirements.txt im Root Verzeichnis des Projekts
* .env Datei im Rootverzeichnis des Projekts erstellen mit folgendem Syntax: rtsp://USERNAME:PASSWORT@RTSP-LINK

### How to Install Detectron2 0.1.3

* Source-Code herunterladen: https://github.com/facebookresearch/detectron2/releases/tag/v0.1.3
* Außerhalb des extrahierten detectron2 Verzeichnisses: py -m pip install -e detectron2
(Falls py nicht geht: "python" verwenden)

## Auführen von Dateien
* py [python-file.py]
(Falls py nicht geht: "python" verwenden)

## Dokumentation

Dokumentation erfolgte über LaTex mithilfe von TeXStudio.  
Aus datenschutzrechtlichen Gründen und eigener Sicherheit ist das Bachelorarbeitdokument samt Tex-Source auf diesem Repo nicht verfügbar.
