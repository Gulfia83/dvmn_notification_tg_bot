# Notification about verified assignments on the Devman course
[Russian](RU_README.md)

The Telegram bot notifies about verified assignments on the Devman course.

### How to install

1. Clone the repository to your local computer.
2. Install the necessary packages using `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory of the project.
4. Add the following variables to the `.env` file:
- `DVMN_API_TOKEN` - your Devman API token.
- `TG_BOT_TOKEN` - your bot token.
- `TG_CHAT_ID` - to get your chat_id, write to a special bot in Telegram: `@userinfobot`

### Example of running in the console and output to Telegram

You can run the script using the `python main.py` command in the command line.

```console
python main.py
```
#### Output to telegram
![Снимок](https://github.com/user-attachments/assets/97f120f2-b914-49fe-8f55-b6abe721d54f)

### Project goal

The code is written for educational purposes in the online course for web developers [dvmn.org](https://dvmn.org/).
