# Tigh-sensei webapp

## Presentation

Tigh-sensei is a interactive dashboard helping you with daily genshin tasks as collecting rewards, entering promo codes and deciding which of your artefact to improve (WIP)

## About The Project


## Getting Started

### Installation

First you need to install the packages listed in `requirements.txt` (preferably in a new environment), be careful it's conda compatible but not pip compatible.
- Create a dedicated new environment `<env>` :
```conda
conda create --name <env> --file requirements.txt
```
- Then you will need to run the app.py script after activating the your `<env>`
```conda
conda activate <env>
python app.py
```
### Executable only

If you simply want to run the webapp, just download the files and run the `app.exe` file in the `dist` folder.
## Usage

On your first use you will need to enter your credential by clicking the 'Change Credentials' button.
(Credentials are stored LOCALY in When done, don't forget to connect for the first time.
Now the webapp is connected to your Hoyolab infos.
### Daily Rewards :

By selecting Daily Rewards you will collect your rewards on the Genshin Reward Calendar.

### Collect Promo Codes :

By selecting Collect Promo Codes, the webapp will be able to try to enter every active codes (with a delay of 5 second between each code to prevent to being blocked by the server)
-- UPCOMING -- 
You will be able to select to try out even the old codes in case of some would still work for your (LONG PROCESS !)
-- UPCOMING --
### Tigh-Sensei Chat Bot

There is a Chat Bot to keep you informed of every thing running in the background. The chat bot is still not able to respond to user prompts.

## Roadmap

Current project Roadmap
- [x] Adding a Tighnari themed chatbot
- [x] Creating an easy-of-use .exe file
- [ ] Adding a artifact presentation Subsection
- [ ] Adding advices depending on character builds
- [ ] Adding new login methods:
	- [ ] Connecting through Hoyolab user active instance

## Contributions

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.



 
