{{ cookiecutter.package_name }}: {{ cookiecutter.repo_name }}
=============================

{{ cookiecutter.description }}

Project Structure
-----------------

``` python
├── .flake8                         <- Configuration for style and quality checks by flake8.
│
├── .gitignore                      <- Specifies files which git should ignore. E.g. makes sure you don't
│                                      commit build files.
│
├── .pre-commit-config-yaml         <- Configuration for pre-commit hooks.
│
├── azure-pipelines.yml             <- Configuration for continuous integration pipeline.
│
├── CONTRIBUTING.md                 <- Readme about contributing to the development of this package.
│
├── pyproject.toml                  <- Configuration file, here used to configure Black code formating.
│
├── README.md                       <- The top-level README for developers using this project.
│
├── setup.py                        <- Makes this package pip installable (pip install -e .) so it can be imported.
│
├── models                          <- Trained and serialized models, model predictions, or model summaries.
│                                      NOTE: only use for temporary storage before storing them with e.g. MLflow.
│
├── notebooks                       <- Jupyter notebooks. Naming convention is ticket number,
│                                      creator's initials, and a short description (delimited with `_`).
│                                      E.g. `42_RB_initial_data_exploration`.
│
├── {{cookiecutter.package_name}}   <- Package source code for use in this project.
│   └── __init__.py                 <- Makes this a Python module. Further structure depends on the project.
│
├── tests                           <- For testing with pytest. For unit tests keep same file structure as the
│                                      source code structure and prefix all files with 'test_'.
```
