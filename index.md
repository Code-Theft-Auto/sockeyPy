<img width="100" height="100" align="left" style="float: left; margin: 0 10px 0 0;" alt="Sockeypic" src="https://cdn.discordapp.com/attachments/970962518606479380/976737385062739988/avatar.png">  

# sockey
[![CI](https://github.com/Code-Theft-Auto/sockeyPy/actions/workflows/main.yml/badge.svg)](https://github.com/Code-Theft-Auto/sockeyPy/actions/workflows/main.yml)
[![website](https://img.shields.io/badge/website-online-green.svg)](https://code-theft-auto.github.io/sockeyPy/)
[![python](https://img.shields.io/badge/python-3.10.4-yellow.svg)](https://www.python.org/downloads/release/python-3104/)
[![Linux](https://img.shields.io/badge/os-linux-blue.svg)](https://github.com/torvalds/linux)
[![license](https://img.shields.io/badge/license-CC0_1.0-green.svg)](https://github.com/Code-Theft-Auto/sockeyPy/blob/master/LICENSE)

*A simple [discord.py](https://github.com/Rapptz/discord.py) general purpose music bot*
 
sockey is an open source Discord bot by [DevER-M](https://github.com/DevER-M). that is constantly growing. You can invite it  
to your Discord server using [this](https://discord.com/api/oauth2/authorize?client_id=916685474364534805&permissions=275147647024&scope=bot%20applications.commands) link! It comes packaged with a variety of commands.
Feel free to add a star :star: to the repository to promote the project!  


## Features
*   🎉  **Fun**: `cat`, `dog`, `rnum`, `gs`, `dice` and many more comming soon!
*   🎵  **Music**: `play`, `queue`, `shuffle`, `loop`, `volume` and **8** more
*   ❔  **Misc**: `ecode`, `decode`, `ping`, `servers` and many more comming soon!
*more commands comming soon....*

## Self hosting
### Docker:
  - make sure you have docker installed
  - `docker pull ghcr.io/code-theft-auto/sockeypy:latest`
  -  `docker run --env TOKEN=<YOUR TOKEN HERE> ghcr.io/code-theft-auto/sockeypy`
### Manual:
  - `git clone https://github.com/Code-Theft-Auto/sockeyPy.git`
  - `cd sockeyPy`
  - *make sure you have python and pip in the latest version*
  - `pip install -r requirements.txt`
  - make a file called .env or `export TOKEN="YOUR_TOKEN"` in shell (if you use linux or macos)
  - if you don't want to use environ ment variables you can add your token in this [line](/main.py#L42) ```bot.run(<YOURTOKEN>)```
  - `python main.py` or `py main.py`
## Contributing

Contributions, issues and feature requests are welcome.
Feel free to check **[issues](/issues)** page if you want to contribute.

## License
Code-Theft-Auto/sockeyPy is licensed under the **Creative Commons Zero v1.0 Universal** license

## Credits

- [DangVietH](https://github.com/DangVietH/) - Pagination for help command [here](https://github.com/DangVietH/DangVietBot/tree/master/utils)
- [vbe0201](https://github.com/vbe0201) - some code for shuffle and loop command

******
**Bot made by** *`FishStick#3365`*
