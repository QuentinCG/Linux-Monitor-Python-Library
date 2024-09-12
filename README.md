# Linux Monitor (Python library)
[![PyPI version](https://badge.fury.io/py/Linux-Monitor.svg)](https://badge.fury.io/py/Linux-Monitor) [![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/QuentinCG/Linux-Monitor-Python-Library/blob/master/LICENSE.md) [![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/QuentinCG)

## What is it

This python library is designed to be integrated in python or shell projects to monitor Linux servers.
It is compatible with python 3+ and usable only on Linux.

It is also designed to be easily integrated as discussion channel bots (TODO: Link to discord bot project here)

<img src="https://github.com/QuentinCG/Linux-Monitor-Python-Library/raw/master/welcome.png" width="300">

## Functionalities

Non-exhaustive list of class functionalities:
  - TODO

Non-exhaustive list of shell commands:
  - TODO

## How to install (python script and shell)

  - Install package calling `pip install linux-monitor` (or `python setup.py install` from the root of this repository)
  - Copy and edit [config-example.json file](https://github.com/QuentinCG/Linux-Monitor-Python-Library/blob/master/config-example.json) depending on your need (on first launch, remove all `restart_command` from config file to prevent potential looping service restart issues on your server in case your config file is not well configured)
  - Add rights to user launching the library depending on what you want it to do
```sh
# Only if this library should be able to reboot the server on demand:
echo "USERNAME_HERE ALL=(ALL) NOPASSWD: /sbin/reboot" >> /etc/sudoers.d/USERNAME_HERE
# Only if this library should be able to kill a process on demand:
echo "USERNAME_HERE ALL=(ALL) NOPASSWD: /bin/kill" >> /etc/sudoers.d/USERNAME_HERE

# Add also all processes added in your config JSON file you want the library to be able to execute
# Example for the existing config-example.json file:
echo "USERNAME_HERE ALL=(ALL) NOPASSWD: /bin/systemctl" >> /etc/sudoers.d/USERNAME_HERE
echo "USERNAME_HERE ALL=(ALL) NOPASSWD: /etc/init.d/apache2" >> /etc/sudoers.d/USERNAME_HERE
echo "USERNAME_HERE ALL=(ALL) NOPASSWD: /etc/init.d/ssh" >> /etc/sudoers.d/USERNAME_HERE
echo "USERNAME_HERE ALL=(ALL) NOPASSWD: /etc/init.d/mariadb" >> /etc/sudoers.d/USERNAME_HERE
```
  - Check monitor possibilities (you can find it out by calling `python linux_monitor/linux_monitor.py --help` from the root of this repository)
  - Load your shell or python script

## How to use in shell

```shell
# Get help
python linux_monitor.py --help

# TODO

# Use "--debug" to show more information during command
# Use "--nodebug" to not show any warning information during command
```

## How to use in python script

Example of python script using this library:

```python
from linux_monitor.linux_monitor import linux_monitor

# TODO
```

## License

This project is under MIT license. This means you can use it as you want (just don't delete the library header).

## Contribute

If you want to add more examples or improve the library, just create a pull request with proper commit message and right wrapping.
