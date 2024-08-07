:: req library
::pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
::pip install pytube whisper langdetect torch tiktoken tqdm numba more-itertools
::python -m pip install numpy==1.26.4
::install chocolatey -> choco install ffmpeg
:: create env
echo # Creating environment
python -m venv .venv
:: use env
call .\.venv\Scripts\activate.bat
:: install libr
echo # Installing library needed
python -m pip install -r requirements.txt
cls
::python -m yaudio_to_text.py
python -m youtube_audio_to_text.py
pause
