# Docker Clarifai

## Background

This docker image is based upon `NodePy` from KBVE but extended out for the Clarifai hackathon from LabLab!
The objective for this repo is to build a CI/CD pipeline that encompases all of the basic pillars needed to build an application ontop of Clarifai's API.


### Dev

For the install, please fork and clone this git repo, then inside of the forked/cloned repo folder, run:

- `yarn install` - Installs the Node modules.
- `poetry install` - Instals the Python modules.

After the packages are installed, you can start the dev environment with:

- `poetry shell` then `yarn start`. 