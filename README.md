# Lost Ark Fishing Bot

This is a simple fishing bot for Lost Ark. It uses OpenCV to detect the exclamation point [!] in the screen.

## Requirements
- Python 3.6+
- PIP

## Download
- **Option 1**: Click the green clone button of the repository in Github, select `Download ZIP` and extract in a directory of your choice.
- **Option 2**: Clone the repository using git

## Installation
1. Open a terminal (PowerShell)
2. Go to the directory where you extracted the files.
   - Example: `cd C:\path\to\bot`
3. [Set up virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments) (Recommended)
   - Example: `python -m venv .venv`
4. Install requirements with `pip install -r requirements.txt`
5. Edit `config.ini` file with the values of your setup correct resolution and monitor identification number.

## Usage
1. Open a terminal (PowerShell)
2. [Activate virtual environment](https://docs.python.org/3/library/venv.html#how-venvs-work) (if you set one up)
   - Example: `.\.venv\Scripts\activate`
3. Run the bot with `python fish.py` in the project directory.
4. Enter your current life energy and leap essence in the terminal to stop the bot before you run out.
5. You have 5 seconds to switch to the game window and point the cursor at the fishing spot. The Trade Skill mode must be active (B).
6. You can press `Ctrl+C` in the terminal to stop the bot at any time.

## Pet Function Auto Repair
If you have pet function enabled (with Crystalline Aura), you can enable auto repair in `config.ini` by setting `times_to_repair` to a value higher than 0. The bot will automatically repair your tools after the specified number of fish are caught.  
 
Setting `times_to_repair` to 0 will disable auto repair.
  
## Troubleshooting
- The bot might 'think' it's fishing when your character is not. This will cause the bot to fail every time due to being out of sync. To fix this you can either restart the bot or press the float fishing key manually to get back in sync.
- If the bot is not reeling when the exclamation point is on screen (false negative), try to decrease the `threshold` value in `config.ini` and restart it.
- If the bot is reeling before the exclamation point is on screen (false positive), try increasing the `threshold` value in `config.ini` and restart it.
- My recommendation is to fish in Sandstar Beach (Punika) because the night lighting makes high contrast against the exclamation point. Also, try pointing the cursor diagonally.

## Planned features
- [ ] Automatic resolution detection
- [ ] Hotkey to start/stop/exit the bot

## Disclaimer
Using bots is probably against Lost Ark's Terms of Service, so use this software at your own risk.  
I am not responsible for any bans or other consequences that may arise from using this software.


