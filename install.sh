#!/bin/sh

pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m spacy download fr_core_news_sm