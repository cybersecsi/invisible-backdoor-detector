# Invisible Backdoor Detector
<p align="center">
  <img id="header" src="https://raw.githubusercontent.com/cybersecsi/invisible-backdoor-detector/main/docs/logo.png" />
</p>

<p align="center">
  <a href="https://github.com/cybersecsi/invisible-backdoor-detector/blob/main/README.md"><img src="https://img.shields.io/badge/Documentation-complete-green.svg?style=flat"></a>
  <a href="https://github.com/cybersecsi/invisible-backdoor-detector/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
</p>


**Invisible Backdoor Detector** is a little *Python* script that allows you to **spot** and **remove** Bidi characters that could lead to an **invisible backdoor**. If you don't know what that is you should check the related paragraph.

## Table of Contents
  - [What is an Invisible Backdoor](#what-is-an-invisible-backdoor)
  - [Install](#install)
  - [Usage](#usage)
  - [Examples](#examples)
  - [Contributions](#contributions)
  - [Credits](#credits)
  - [License](#license)

## What is an Invisbile Backdoor
An Invisible Backdoor is exactly what you think: a backdoor that you cannot see! It was described by *Wolfgang Ettlinger* at *Certitude* in [this blog post](https://certitude.consulting/blog/en/invisible-backdoor/). It leverages the presence of Unicode characters (Bidi characters) which behaves like normal spaces. In conjunction with the Javascript object destructuring those characters may allow an attacker to introduce a backdoor into an open-source project without anyone noticing it. Check out the blog post for more info.

## Install
You can easily install it by running:
```
pip install invisible-backdoor-detector
```

## Usage
```
invisible-backdoor-detector -h
```

```
 Usage: invisible-backdoor-detector [OPTIONS] PATH                                                                          
                                                                                                                            
╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    path      TEXT  Path of the folder to check [default: None] [required]                                              │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --remove  -r        Remove the Bidi characters found                                                                     │
│ --help    -h        Show this message and exit.                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

## Example
The *example* folder provides a working example of an invisible backdoor in Node.js, you may test the script on that folder. 
If you want to try out the backdoor you can add the following parameter to the query string:
```
%E3%85%A4=<any command>
```

## Contributions
Everyone is invited to contribute!
If you are a user of the tool and have a suggestion for a new feature or a bug to report, please do so through the issue tracker.

## Credits
Developed by Angelo Delicato [@SecSI](https://secsi.io)

## License
*invisible-backdoor-detector* is released under the [MIT LICENSE](https://github.com/cybersecsi/invisible-backdoor-detector/blob/main/LICENSE.md)

