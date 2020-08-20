# mkignore
## Generate .gitignore from templates

### Usage
`mkignore [-h] [-g, --generate] [-u, --update] [-l, --list] [TEMPLATES [TEMPLATES ...]]

Generate .gitignore files

positional arguments:
  TEMPLATES

optional arguments:
  -h, --help      show this help message and exit
  
  -g, --generate  Generate .gitignore
  
  -u, --update    Update available .gitignore templates
  
  -l, --list      List available .gitignore templates`
  
### Example
Generate a .gitignore for a C++ project in a JetBrains IDE.

`mkignore -g c++ jetbrains > .gitignore`