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
