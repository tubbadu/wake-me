# wake-me

A simple command line alarm clock to remind you everything!

## Dependencies

```bash
# gtts
pip3 install gTTS
# dunstify
    # debian based OS
    sudo apt install dunstify
    # red hat based OS
    sudo dnf install dunstify
# optional, KDE connect
```

## installation

```bash
pip3 install ./wake-me
```

## usage

```bash
wake-me in 10m 30s "pasta is cooked!"
```

```bash
wake-me at 19.30 "remember to call the doctor!"
```

using the `-s` flag, no voice will be spoken, keeping the alert silent

## todo

+ add all flags cases into this readme

+ add an installation script :)

+ perhaps release it on pypi

+ add a flag for "sound until it's stopped"
