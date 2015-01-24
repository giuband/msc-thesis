#!/bin/bash
# My first script

cd /home/giuseppe/Thesis
pdflatex -synctex=1 -interaction=nonstopmode main.tex
evince main.pdf