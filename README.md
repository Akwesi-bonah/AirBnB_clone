# 0x00. AirBnB clone - The console
![Alt text](airbnb.png)


| Table of content             | 
|------------------------------|
| [About this Project](#About) |
| [Setting up](#Setting-Up)    |
| [Environment](#Environment)  |
| [Execution](#Execution)      |



# About
Team project to build a clone of [AirBnB](https://www.airbnb.com/).

The console is a command interpreter to manage objects abstraction between objects and how they are stored.

To see the fundamental background of the project visit the [Wiki](https://github.com/ralexrivero/AirBnB_clone/wiki).

The console will perform the following tasks:

* create a new object
* retrieve an object from a file
* do operations on objects
* destroy an object

##  Resources
- [cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A)
- [uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ)
- [datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA)
- [unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)
- [args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)
- [Python test cheatsheet](https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw)
- [cmd module wiki page](https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ)
- [python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA)
### Storage

All the classes are handled by the `Storage` engine in the `FileStorage` Class.

## Environment

<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a>
<!-- bash --> 
<a href="https://www.gnu.org/software/bash/" target="_blank">
<img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="terminal"></a>
<!-- python--> 
<a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="python"></a> </a>
<!-- vim --> 
<a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Suite CRM"></a>
<!-- git --> 
<a href="https://git-scm.com/" target="_blank"> 
<img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="git distributed version control system"></a>
 <!-- github --> 
<a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github"></a>


## Style guidelines:
  * [pycodestyle (version 2.7.*)](https://pypi.org/project/pycodestyle/)
  * [PEP8](https://pep8.org/)
  
All the development and testing was run over an operating system Ubuntu 20.04 LTS using programming language Python 3.10. 
The editors used were VIM Editor,
Control version using Git 


## Setting-Up

```bash
git clone https://github.com/Akwesi-bonah/AirBnB_clone.git
```

change to the `AirBnb` directory and run the command:

```bash
 ./console.py
```

## How to use it
### Execution
 In interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
In non-interactive
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

```
# AUTHORS
* [George Arhin-Bonnah](arhinbonnah@gmail.com)
* [Godwin Dogbey](godwindogbey95@gmail.com)
