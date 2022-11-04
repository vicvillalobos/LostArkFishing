# Lost Ark Fishing Bot

This is a simple fishing bot for Lost Ark. It uses OpenCV to detect the exclamation point [!] in the screen.

## Requirements
- Python 3.6+
- PIP
- virtualenv or conda (optional, recommended)

## Download
- **Option 1**: Click the green clone button of the repository in Github, select `Download ZIP` and extract in a directory of your choice.
- **Option 2**: Clone the repository using git

## Installation
2. Set up virtual environment (Recommended)
3. Install requirements with `pip install -r requirements.txt`

## Usage
1. Open a terminal
2. Activate virtual environment (if you set one up)
3. Make sure `config.ini` has the correct resolution and monitor identification number.
4. Run the bot with `python fish.py` in the project directory.
5. You have 5 seconds to switch to the game window and point the cursor at the fishing spot. The Trade Skill mode must be active (B).

## Notes
- For the time being, the bot will only work in the main monitor.
- The bot will run endlessly, so you will have to stop it manually by pressing Ctrl+C in the terminal.

## Planned features
- [ ] Automatic resolution detection
- [ ] Hotkey to start/stop/exit the bot
- [ ] Pet function tool repair (repairs the fishing rod after a certain number of casts)

## Disclaimer
Using bots is probably against Lost Ark's Terms of Service, so use this software at your own risk.  
I am not responsible for any bans or other consequences that may arise from using this software.


