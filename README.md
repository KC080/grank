<div align="center">
    <h1>Grank</h1>
    <img src="https://styles.redditmedia.com/t5_3ozad/styles/communityIcon_xvlhdypngrq61.png?width=256&s=d8079b417dde76bf9f6015d5dec902e0756e5c4f" alt="Dank Memer Logo">
</div>

<div align="center">
    <a href="https://github.com/didlly">
    <img src="https://img.shields.io/github/license/didlly/grank">
    <img src="https://img.shields.io/github/languages/top/didlly/grank">
    <img src="https://img.shields.io/bitbucket/issues-raw/didlly/grank">
    </a>
    <a href="https://didlly.github.io/grank">
    <img src="https://img.shields.io/website?down_color=lightgrey&down_message=Offline&up_color=blue&up_message=Online&url=https%3A%2F%2Fdidlly.github.io%2Fgrank%2F">
    </a>
</div>

<div align="center">
    <sub>Inspired by <a href="https://github.com/dankgrinder/dankgrinder">this</a> repository. This is a WIP and there will be more functions added in the future. Special thanks to <a href="https://github.com/V4NSH4J">V4NSH4J </a> for helping me solve lots of the problems I encountered.</sub>
</div>

## Contents

* [What is Grank?](https://github.com/didlly/grank#what-is-grank)
* [Features](https://github.com/didlly/grank#features)
* [Supported commands](https://github.com/didlly/grank#getting-started)
* [Todo](https://github.com/didlly/grank#todo)
* [Getting started](https://github.com/didlly/grank#supported-commands-more-to-be-added-in-the-future)
	* [Setting up the environment.](https://github.com/didlly/grank#setting-up-the-environment)
	* [Getting your Discord token and channel ID.](https://github.com/didlly/grank#getting-your-discord-token-and-channel-id)
* [Config file](https://github.com/didlly/grank#config-file)
	* [```commands``` category](https://github.com/didlly/grank#commands-category)
	* [```cooldowns``` category](https://github.com/didlly/grank#cooldowns-category)
	* [```logging``` category](https://github.com/didlly/grank#logging-category)
* [Disclaimer](https://github.com/didlly/grank#disclaimer)

## What is Grank?
<div align="center">
    <img src="https://raw.githubusercontent.com/didlly/grank/main/assets/cover.png" alt="Cover image">
</div>

Grank is a feature-rich script that automatically grinds Dank Memer for you. It is based on [dankgrinder](https://github.com/dankgrinder/dankgrinder). Since it has been discontinued and the [recommended fork](https://github.com/V4NSH4J/dankgrinder) has also been discontinued, I decided to make my own version from scratch in Python.

## Features
- Free
- Efficiently coded.
- Smart - if the user doesn't have a required item to run a command like ```pls pm```, it will buy the required item so long as there are sufficient funds in the user's wallet & bank.

## Supported commands
- ```pls daily```
- ```pls beg```
- ```pls dig```
- ```pls fish```
- ```pls hunt```
- ```pls search```
- ```pls highlow```
- ```pls postmeme```

## Todo
- ```pls trivia```
- ```pls stream```

## Getting Started

### Setting up the environment
When the majority of Dank Memer commands are supported, compiled versions of the code will be made available. However, since ```v1``` has not been acheived yet, you will have to have Python installed to run Grank.

- Install [Python](https://www.python.org/) (Grank has been tested on Python version ```3.10.0 64-Bit```). Make sure to have the ```Install Pip``` option ticked.
- Download this repository by clicking [this](https://github.com/didlly/grank/archive/refs/heads/main.zip) link. 
- Extract the files, and open a command prompt window in ```/src/```.
- Run ```pip install -r requirements.txt```

### Getting your Discord token and channel ID
To use Grank, you will have to provide your Discord token and a channel ID. Don't worry - these details are never shared with anyone. It is best if only you and Dank Memer can send messages in the channel you get the ID of. This is to avoid confusion with other people's interactions.

#### How do you get this information
- [Useful article on how to get your Discord token.](https://discordhelp.net/discord-token)

- [Useful article on how to get a channel ID.](https://docs.statbot.net/docs/faq/general/how-find-id/)

You are now ready to use the program. Run ```src/main.py``` to start the program. You do not have to have Discord open to run the program, so you can have the program running in the background while you do other things!

## Config file
The ```config.yml``` file is used to change the way the program runs.

### ```commands``` category
Values in the ```commands``` category tell the program whether or not to run certain commands.

| Name  | Type | Default Value | Description | 
| ------------- | ------------- | ------------- | ------------- |
| ```daily```  | ```Boolean``` | ```True```  | Tells the program whether or not to run the command ```pls daily```. |
| ```beg```  | ```Boolean``` | ```True```  | Tells the program whether or not to run the command ```pls beg```. |
| ```dig```  | ```Boolean``` | ```True```  | Tells the program whether or not to run the command ```pls dig```. |
| ```fish```  | ```Boolean``` | ```True```  | Tells the program whether or not to run the command ```pls fish```. |
| ```hunt```  | ```Boolean``` | ```True```  | Tells the program whether or not to run the command ```pls hunt```. |
| ```search```  | ```Boolean``` | ```True```  | Tells the program whether or not to run the command ```pls search```. |
| ```highlow```  | ```Boolean``` | ```True```  | Tells the program whether or not to run the command ```pls highlow```. |
| ```postmeme```  | ```Boolean``` | ```True```  | Tells the program whether or not to run the command ```pls postmeme```. |
| ```auto_buy```  | ```Boolean``` | ```True```  | Tell the program whether or not to buy items  (like ```laptop```) needed to run commands if there are sufficient funds. |

### ```cooldowns``` category
Values in the ```cooldowns``` category tell the program the cooldowns between commands and the loop cooldown.

| Name  | Type | Default Value | Description |
| ------------- | ------------- | ------------- | ------------- |
| ```commands```  | ```Integer``` | ```1```  | Cooldown between commands. |
| ```timeout```  | ```Integer``` | ```5```  | Timeout for waiting for responses from Dank Memer to commands that require user interaction (like ```pls search```). |

### ```logging``` category
Values in the ```logging``` category tell the program whether or not to log ```debug``` and ```warning``` messages. We would recommend having *at least* ```warning``` set to ```True```. Fatal errors will be logged regardless of the configuration.

| Name  | Type | Default Value | Description |
| ------------- | ------------- | ------------- | ------------- |
| ```debug```  | ```Boolean``` | ```True```  | Tells the program whether or not to log ```debug``` messages. |
| ```warning```  | ```Boolean``` | ```True```  | Tells the program whether or not to log ```warning``` messages. |

***NOTE***: Values in the ```logging``` category do not affect logging messages sent when the configuration file is being loaded and the token is being verified.

## Disclaimer
This is a self-bot. Self-bots are against Discord's TOS. Automation of Dank Memer commands also breaks Dank Memer's rules. By using this program you acknowledge that I can take no responsibility for actions taken against you if you are caught.

This being said, I believe the chance of being caught running this script is low, provided you take the appropriate measures. The only probable way you will be caught is if someone tries to send you a message and you don't respond.