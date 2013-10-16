Keglebone
=========

A Kegbot-inspired system for Beaglebone Black.

Authored by Kevin Chabreck and Kyle Bishop.

##Setup

*This guide assumes you are installing the Keglebone service on a Beaglebone Black running Ubuntu Raring 13.04*

The first thing you'll want to do is install the Keglebone service. 

```
git clone git@github.com:kevinchabreck/Keglebone.git
```

Keglebone requires [pip](https://github.com/pypa/pip) and [virtualenv](https://pypi.python.org/pypi/virtualenv) to run. Directions for installing pip can be found [here](http://www.pip-installer.org/en/latest/installing.html#using-package-managers), and directions for installing virtualenv can be found [here](https://pypi.python.org/pypi/virtualenv).

Pip is included in most package managers, usually under the name `python-pip`. Install it on your Beaglebone with the following command:

```
sudo -s
apt-get update
apt-get install python-pip
```

Next, switch to the Keglebone directory and install/initialize virtualenv:

```
cd Keglebone
pip install virtualenv
virtualenv ENV
source ENV/bin/activate
```

Finally, install [Twython](https://github.com/ryanmcgrath/twython) in your new python virtual environment. Twython is a great twitter wrapper for python, and is also required for Keglebone to run. [Here](https://twython.readthedocs.org/en/latest/usage/starting_out.html) is a guide for installing and getting started with Twython.

```
pip install twython
```

Make sure your environment includes the following variables (these all correspond to your twitter app's account credentials):

```
export APP_KEY="your.personal.app.key"
export APP_SECRET="your.personal.secret.key"
export OAUTH_TOKEN="your.personal.oauth.token" 
export OAUTH_TOKEN_SECRET="your.personal.oauth.token.secret"
```

If you place these lines in a shell script called `Keglebone/config/credentials.sh`, git will ignore them by default.