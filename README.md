# Machine Learning in Computer Vision

### Before we begin
Before start using a project, you should have pre-installed poetry.
If you don't have it, you can use next command:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
If you get any problem please check the documentation
https://python-poetry.org/docs/#installation.

### Run demo
After completing an installation step, you must follow next steps:
* Change the directory to the project dir
```bash
cd east_text_detector
```
* Use `poetry install` to read the pyproject.toml file, resolves the dependencies, and installs them.
```bash
poetry install
```
* Use `poetry shell` to activate virtual environment
```bash
poetry shell
```
* After that change the directory to source files
```bash
cd east_text_detector
```
* Run the program
```bash
python3 demo.py
```
* Finally, to deactivate virtual environment simply use `exit` command
```bash
exit
```
* If you want to directly run program with command line, you can use next command:
```bash
poetry run demo
```
### Build Project
* Builds the source and wheels archives:
```bash
poetry build
```
* To install a package directly from the repository link
```bash
pip3 install git+https://github.com/AlexeusPodbeltsev/east_text_detector.git
```




