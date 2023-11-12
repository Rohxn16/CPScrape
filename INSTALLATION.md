# Follow the steps below to set up the system locally in your device for development

## In order to follow the steps below, you need to first make sure that python 3.10 or above and pip is installed in your system

1. Fork the [upstream repository](https://github.com/Rohxn16/CPScrape) in your account first.
2. Navigate to the folder that you are going to work in, here lets call it 'work'.
3. Install [virtualenv](https://pypi.org/project/virtualenv/) which will allow you to create a clean and isolated system within your local system to work on this specific project only witout getting your global packages mixed up with the ones specific to this project only. `pip install virtualenv` or `pip install python-virtualenv`.
4. Create the virtualenv, lets call it 'venv' : `virtualenv venv`
5. Activate the environment to start working in it [If you are using git bash on windows follow the steps for linux or the preferred terminal emulator would be power shell]: <br>
- Linux / Mac : `source venv/bin/activate`
- Windows : `.\venv\scripts\activate.ps1`
6. Now, our virtual environment is active and we have a clean python environment to start working
7. Clone the forked repo into the work folder, in the same level as the venv folder. `git clone https://github.com/${YOUR_UNAME}/CPScrape`
8. Navigate to the cloned repository and install the dependencies : `cd CPScrape && pip install -r requirements.txt`
9. Now you are all set up and the server is ready to be launched in your local enviroment. To launch the server execute this command in your terminal `python main.py`
*In case there are multiple python versions installed try running `python3 main.py` or `python3.x main.py`*
