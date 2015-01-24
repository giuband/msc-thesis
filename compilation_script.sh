#!/bin/bash
# My first script

pdflatex -synctex=1 -interaction=nonstopmode main.tex
evince main.pdf