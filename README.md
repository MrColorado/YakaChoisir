# YakaChoisir

The syntax that you must follow when you commit :
  - [WHATYOUMODIFY] what you have done

# Git branches 101

## Git flow ~

*master* is the release branch. You're not supposed to push into this branch.
Instead, do pull requests on GitHub. That way, other members can review your
code before integrating it.

*dev* branch is the development branch, which is the unstable version of
master.

*feature_branch* starts from *dev*. You're supposed to implement your features
there.

## Merging feature branches onto dev branch

We want to always do fast-forward merges. To do so, do the following:
Let's say you want to merge onto dev.
```
git checkout your_feature_branch
git rebase dev
git checkout dev
git merge your_feature_branch
```
Apparently the following works as well:
```
git checkout dev
git rebase your_feature_branch
```

# Project Architecture

## Django

Django's project is in `./src`, and each of its applications are `src`
subfolders.

## HTML/CSS and Bootstrap

They're all located in `/templates` folders. Either in the global `templates`
folder or in one of the applications' subfolders.

## Create new project application

Execute the following in `src` directory.

```
python3 manage.py startapp app_name
```

## SQL Database

To update database:

```
# Check what has changed and needs to be updated
python manage.py makemigrations

# Actually update the database
python manage.py migrate
```

## To run server

```
python3 manage.py runserver
```
