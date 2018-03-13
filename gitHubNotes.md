# About remotes

[Here](https://stackoverflow.com/questions/5617211/what-is-git-remote-add-and-git-push-origin-master) are some excellent notes on understanding the remote concept.

When you execute the command:

> git push origin master

that pushes the changes in the master branch to the remote called origin.  So its important to set the origin of to the remote account you want to push to i.e. github.com/blah, or github.utexas.edu/blah.  To set the remote:

> git remote add origin git@github.com:purplehey/whatever.git

If you want to know what origin is set to, you can:

> Lonestar:purplehey.github.io wes$ git remote -v
> origin  git@github.com:purpleHey/purplehey.github.io.git (fetch)
> origin  git@github.com:purpleHey/purplehey.github.io.git (push)
