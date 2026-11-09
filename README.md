# Juno

Juno is a small **Windows desktop app written in Python**. It has two views:

- **Chat — Juno Core v0.1:** an offline, rule-based demo assistant.
- **Experiments — Juno Imagine v0.1:** creates original pixel-art scenes locally and lets you save them as PNG files.

The pixel art is drawn from code with generated shapes and colors; the prototype does not bundle third-party artwork. Chat replies are simple demo responses, not a connected or trained language model. No chat data is sent to a server.

## Run on Windows

1. Install Python 3.10 or newer from [python.org](https://www.python.org/downloads/windows/). During installation, enable **Add Python to PATH**.
2. Download or clone this repository and open its folder.
3. Double-click `run_juno.bat`. It installs the Pillow image library and starts Juno.

Or use PowerShell in the project folder:

```powershell
py -3 -m pip install -r requirements.txt
py -3 juno_app.py
```

Tkinter is included with the standard Windows Python installer. If it is missing, rerun the Python installer and enable Tcl/Tk support.

## Other platforms

The app also runs on macOS and Linux when Python, Tkinter, and the dependencies in `requirements.txt` are installed:

```bash
python3 -m pip install -r requirements.txt
python3 juno_app.py
```

## Project files

- `juno_app.py` — desktop app, offline chat demo, and pixel-art generator
- `run_juno.bat` — Windows setup-and-launch helper
- `requirements.txt` — Python package dependencies
