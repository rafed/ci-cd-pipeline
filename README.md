![](https://github.com/rafed/ci-cd-pipeline/workflows/Deploy/badge.svg)

## Hello World DevOps

Hello bros, this repo is a very easy and simple implementation of a DevOps pipeline. This pipeline does the following:
- Starts running when code is pushed to main branch
- Run tests on CI server
- If tests pass, deploys to heroku

To implement this do the following:

#### Step 1: Setup heroku

1. Open a heroku account (it's free!)
1. Create new app from dashboard, name it whatever you want
1. Go to heroku settings. At the bottom of the page, there should be an API key. Copy it and save it somewhere, we'll need it later

#### Step 2: Setup a hello world app

Clone/download the code of this repo and include it in your project. If you are feeling adventurous you may write your own app. When writing your own make sure to do the following:
- It should be a web app
- Write tests
- Make a dependencies file (requirements.txt/ package.json)

#### Step 3: Setup Github Actions

1. Create a github action in your project root at path .github/workflows/main.yml
1. Copy the action instructions of this repo to your main.yml
1. Go to your repo settings and under "Secrets"  add the API key copied from Step 1
1. Try to understand what the actions in main.yml is doing

#### Step 4: Test the deployed app

1. Push the contents of your repo
1. Run the app at https://app-name.herokuapp.com (https://rafed-add.herokuapp.com)
1. Make many changes to your app and deploy. On each deploy check-
    - the actions tab when the build is running
    - whether the app is deployed when tests fail
    - whether the app is deployed when all tests pass

