<p align="center">
    <img src="img/kb-plugin-logo.png?raw=true" width="400"/>
</p>

# kb-plugin - a plugin manager for kb, the minimalist knowledge base manager.


![Main Build](https://github.com/alshapton/kb-plugin/workflows/KB-PLUGINS-BUILD/badge.svg?branch=main)

![CodeQL](https://github.com/alshapton/kb-plugin/workflows/CodeQL/badge.svg)
#### You can get support for kb [here](https://xscode.com/gnebbia/kb)

Author: alshapton <alshapton@gmail.com>˜

Copyright: © 2021, alshapton

Date: 2021-JAN-30

Version: 0.0.1


## Table of Contents

* [Purpose](#Purpose-of-kb)
* [Purpose of kb-plugin](#Purpose-of-kb-plugin)
* [Installation](#installation)
    * [Prerequisites](#Prerequisites)
    * [Connecting to kb](#Connecting-to-kb)
* [Upgrade](#upgrade)
* [Donations](#donations)
* [Upgrade](#upgrade)
* [Copyright](#copyright)
    
## Purpose of kb

kb is a text-oriented minimalist command line knowledge base manager. kb can be considered a quick note collection and access tool oriented toward software developers, penetration testers, hackers, students or whoever has to collect and organize notes in a clean way.  Although kb is mainly targeted on text-based note collection, it supports non-text files as well (e.g., images, pdf, videos and others).

In few words kb allows a user to quickly and efficiently:

- collect items containing notes, guides, procedures, cheatsheets into  an organized knowledge base;
- filter the knowledge base on different metadata: title, category,  tags and others;
- visualize items within the knowledge base with (or without) syntax highlighting;
- grep through the knowledge base using regexes;
- import/export an entire knowledge base;

Basically, kb provides a clean text-based way to organize your knowledge.

## Purpose of kb-plugin

kb-plugin is an extension to kb which will allow 3rd-parties to include new commands and features
within kb.

kb-plugin consists of:

- hooks into the base kb software
- a plugin manager to manage and interrogate plugins
- an example plugin with documentation which will allow users to construct their own plugins
- a clearly documented configuration file in an industry-standard toml format
- a clear set of function definitions that are used to integrate the plugins with the base kb software




## Installation

**Prerequisites:**
- Python 3.6 or above
- kb-manager or above

To install the most recent stable version of kb just type:
```sh
pip install -U kb-plugins
```

If you want to install the bleeding-edge version of kb (that may have
some bugs) you should do:
```sh
git clone https://github.com/gnebbia/kb
cd kb
pip install -r requirements.txt
python setup.py install

# or with pip
pip install -U git+https://github.com/gnebbia/kb
```

**Connecting to kb:**

Once you have downloaded/installed kb-plugin, confirm that the installation has worked as follows:
![](./images/term-1.gif)

You should see the current version of kb, kb-plugin and the connection status (which at this stage should show as **`Disconnected`**)

Now, connect your kb-plugin instance to your installation of kb as shown below (check your connectivity status before and after)

![](./images/term-2.gif)

Should you attempt to connect kb-plugin to kb when it is already connected, you will receive this message: **`kb-plugin is already connected to the kb instance`**

### List plugins





## UPGRADE

If you want to upgrade kb to the most recent stable release do:
```sh
pip install -U kb-manager
```

If instead you want to update kb to the most recent release
(that may be bugged), do:
```sh
git clone https://github.com/gnebbia/kb
cd kb
pip install --upgrade .
```

## DONATIONS

The primary developer of the kb-manager package is an independent developer working in his free time,
if you like kb and its ecosystem, and would like to say thank you, buy him a beer! Without him, kb-plugins would not exist!

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/nebbione)

## COPYRIGHT

Copyright 2021 Andrew Shapton.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
