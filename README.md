# Pymanujan :sparkles:
### Python powered Calculator. As simple as that.
#### Introduction
Whole code is written in pure Python :snake:. Moreover, as a beginner myself, new developers and contribtors can easily go through the code to understand the logic behind the program. I tried to include as much as comments and documentations within the code itself. Feel free to ping me for any updates. This program has a lot of scope for improvement :sparkles:. Development best-suited for new developers and programmers, this simple program provides a stage for immense develpoment of one's skill, expertise and familiarity of Python programming language :snake:.

Currently the program supports 'Addition :heavy_plus_sign:', 'Subtraction :heavy_minus_sign:', 'Multiplication :heavy_multiplication_x:' and 'Division :heavy_division_sign:'. Check **Tasks List** issues pending on *feature-requests*. Check **Contribution** for more details to get started on developing the program.

#### User interface of Pymanujan *v2.0-alpha* :desktop_computer:

![As of v2.0-alpha](https://drive.google.com/file/d/1nH_8BpzOnZnRF5_wheERnEylybSPEaxf/view?usp=sharing)

#### Tasks List :writing_hand:
- [x] **Refactor ~~source.py~~ source code.**
- [x] Add 'Copy' functionality, to copy the result. Currently 'Copy' button does not do anything.
- [x] Dynamic font size in result label.
- [x] Bind 'Number-pad' keys to enter input.
- [x] Option to switch between 'Simple' to 'Advanced' mode. Advanced mode should have more funtionalities.

#### Developer Installation:
Clone this repository from Github. Then create a virtual-environment and install the dependencies.
```bash
git clone https://github.com/maddypie/Pymanujan.git
git checkout dev
python3 -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
```

#### Contribution :nerd_face:
All are welcome :pray: to contribute to this project. Start from going through the ```source.py``` which has good amount comments and documentation along the code. Currently the focus is on improving the GUI. Create an *Issue* and start a discussion before working on a seperate *Fork*, collabaration always results in better ideas!

Goal :soccer: towards your contribution should always be to improve expertise on Python :snake:.
> Though a calculator app is no path-breaking project to work on, it gives confidence to a new-devloper the abilty to build something from scratch.

#### Note for Linux users:
For 'Copy' button to work as intended, make sure ```xclip``` is installed.
Distribution | Installation command
-------------|---------------------
Debian | `sudo apt install xclip`
Fedora based distro | `dnf install xclip`
CentOS based distro | `yum install xclip`
OpenSUSE based distro | `zypper install xclip`
