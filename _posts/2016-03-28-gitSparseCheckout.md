---
layout: post
date: 2016-03-28 12:23:00
title: "Cloning specific folders from git"
excerpt: "...[sic] sparse checkoutallows us to sparsely populate the working directory by using skip-worktree bit to inform GIT if the file in the working directory deserves a look."
comments: true
mathjax: true
permalink: git-sparse-checkout
---
<!--##Table of Contents
###[Sparse Checkout](#sparse-checkout)
###[SVN Checkout](#svn-checkout)
## Directory && Sub-directory checkout from git repos-->

This is a relatively newie but a goodie.  Have you ever been stuck trying to clone specific folders from a `git` repo recently?

Well, starting from `git 1.9`, this feature is now part of git features. For the sake of illustration, let's say we want to retrieve only the [examples](https://github.com/PointCloudLibrary/pcl/tree/master/examples) directory of the point cloud repo commited at the[point cloud library git page](https://github.com/PointCloudLibrary).

### Sparse-Checkout
A new feature (available in git 1.9 upwards) called [sparse checkout](https://git-scm.com/docs/git-read-tree/) allows us to sparsely populate the working directory by using skip-worktree bit to inform `GIT` if the file in the working directory deserves a look. <i>git read-tree</i> and other merge commands native to `git` such as `checkout`, `merge`, or `pull` are useful in maintaining the skip-working tree bitmap and working directory update. 

"`$GIT_DIR/info/sparse-checkout` defines the skip-worktree reference bitmap. When git read-tree needs to update the `working directory, it resets the skip-worktree bit in the index based on this file, which uses the same syntax as .gitignore files. If an entry matches a pattern in this file, skip-worktree will not be set on that entry. Otherwise, skip-worktree will be set.

"Then it compares the new skip-worktree value with the previous one. If skip-worktree turns from set to unset, it will add the corresponding file back. If it turns from unset to set, that file will be removed.

"While `$GIT_DIR/info/sparse-checkout` is usually used to specify what files are in, you can also specify what files are not in, using negate patterns. For example, to remove the file unwanted:

```
/*
!unwanted
```

"Another tricky thing is fully repopulating the working directory when you no longer want sparse checkout. You cannot just disable "sparse checkout" because skip-worktree bits are still in the index and your working directory is still sparsely populated. You should re-populate the working directory with the $GIT_DIR/info/sparse-checkout file content as follows:

```
/*
```
"

So to check out the pcl examples directory for example, we could combine the `sparse checkout` and `shallow clone` features. By using the `shallow clone` feature, we cut off the history and the `sparse check out` only pulls files matching the pattern we specify. 

Take a look:
<pre class="terminal"><code>
$ mkdir pcl-examples
$ cd pcl-examples
$ git init 
$ git remote add origin -f https://github.com/PointCloudLibrary.git
$ git config core.sparsecheckout true
$ echo "examples/*" >> .git/info/sparse-checkout
$ git pull --depth=2 origin master
</code></pre>

#### Explanation

The line 
                  <pre class="terminal"><code>$git remote add origin -f https://github.com/PointCloudLibrary.git </code></pre> 

creates an empty repository with the point cloud library github remote, fetches all objects but doesn't check them out.

The files are checked out with the next line's command.

Since we are cloning everything in the examples directory --which, by the way, have a depth of 2-- we pull every darn subdirectory and file under the examples folder by doing:

<pre class="terminal"><code>$ git pull --depth=2 origin master</code></pre> 

### SVN Checkout 

If you are using svn instead of git, there is a straightforward way to do this. Simply cd into your working directory and replace the "`/tree/master`" path within the `url` with `trunk`. To clone the subdirectory `examples` inthe point cloud git repo for example, using `svn`, we would do the following in terminal

<pre class="terminal"><code>$ svn checkout https://github.com/PointCloudLibrary/pcl/trunk/examples</code></pre>


