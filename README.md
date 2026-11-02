# Morse Code Translator with Optional Sound

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GPL v3 (see LICENSE).

A modern Python 3 Morse code translator. Text-only translation works without Pygame or an audio device. Optional `--play` uses local WAV files and Pygame CE, initialized only when audio is requested. Word boundaries are represented by `/`.

```sh
python3 main.py --text 'SOS'
python3 main.py --text 'Hello world' --play
python3 -m unittest discover -s tests -v
```

For audio, install `pygame-ce>=2.5.8` (see requirements.txt). The original code is preserved on the [old branch](https://github.com/hamdyaea/Python_morse_with_sounds/tree/old).
