---
layout: post
date: 2017-05-12 11:37:00
title: "<center>Twanging git pull, push and clone</center>"
excerpt: "<center>It is useful to be able to share your work between different computers using the native git commands such as merge, fetch, push, clone, or pull without resolving to using ssh, scp or other such copying commands that copy whole directories or files without the benefit of diff and merge strategies of git.</center>"
comments: true
mathjax: true
permalink: git-twangs
---

- [Table of Contents](#table-o-conts)
- [Introduction](#intro)
- [Pulling/Pushing git remotes from LAN/WAN repos](#pullpush)
- [Cloning git remotes from LAN/WAN repos](#clone)

<a name="intro"></a>
### Introduction

Git is a useful tool mostly for work collaboration, social coding. It is useful to be able to share your work between different computers using the native git commands such as `merge`, `fetch`, `push`, `clone`, or `pull` without resolving to using ssh, scp or other such copying commands that copies whole directories or files without the benefit of `diff` and `merge` strategies of git. More so, not everyone enjoys exposing their incomplete work/code to a remote repo as a server where local git repos can fetch and merge from. This post is meant to show how to go about these git strategies without going through a remote e.g. master.

<a name="pullpush"></a>
#### Pulling/Pushing git remotes from a LAN/WAN repo

We can update local git refs without pulling from a web-based remote. Suppose I have the same git repo on two computers in the same network, we can `git pull` or `git push` without resolving to going through the git repo hosted on a web server. As an example, suppose I have a repo named `sensors` on a computer with username and group name `drumpf@dissembler` and I have a few commits ahead of the repo on a computer named `robots@killem`, I can work across both repos as follows:

1. We could use ssh, git, https, ftp or rsync transport protocols. For instance, if we want to pull from `drump@dissembler:~/Documents/sensors.git` to `robots@killem:~/Documents/sensors.git` repo.

  - via ssh:

    <pre class="robots@killem:~/Documents/sensors"><code>$ git pull ssh://drumpf@dissembler:/~/Documents/sensors.git</code></pre>

  - via https:

      <pre class="robots@killem:~/Documents/sensors"><code>$ git pull http[s]://drumpf@dissembler:/robots/killem/Documents/sensors.git</code></pre>

  - via ftp

      <pre class="robots@killem:~/Documents/sensors"><code>$ git pull ftp[s]://drumpf@dissembler:/robots/killem/Documents/sensors.git</code></pre>

  - via rsync

      <pre class="robots@killem:~/Documents/sensors"><code>$ git pull rsync://drumpf@dissembler:/~/Documents/sensors.git</code></pre>

Note that I have used user expansion for both ssh and git. `ftp[s]` and `rsync` do not so the full path to the repos have to be specified.
Be aware that the https syntax has no authentication and can be dangerous on unsecured networks. If the group names of the computers are not advertised by `/etc/hosts`, you can use the ip address of the computer in place of the host names. Note that ftp/ftps can be used for fetching while rsync can be used for fetching and pushing but they are not very efficient.

All the commands above would also work for `git push`. `scp`-like syntaxes are valid as well but note that the first character after the first column must not be a slash to help distinguish a local path from an ssh url:

  - scp [user@]host.ng:path/to/repo.git/

2. All the above commands also suport pushing/pulling between folders on the same host. All that would need to change would be to replace the LAN/WAN hostname with the path we are cloning from.

git assumes a remote url transport protocol if it does not know what the remote address is. So we could for example have done

<pre class="robots@killem:~/Documents/sensors"><code>$ git push transport::address</code></pre>

where `address` is the path to the repo on the LAN/WAN.

<a name="clone"></a>
#### Cloning git remotes from a LAN/WAN repo

The procedure is the same as above save we replace pull/push with clone, e.g

 -  git clone ssh://[you@]remote.ng[:port]/path/to/repo.git/

 -  git clone  git://remote.ng[:port]/path/to/repo.git/

 -  git clone  http[s]://remote.ng[:port]/path/to/repo.git/

 -  git clone  ftp[s]://remote.ng[:port]/path/to/repo.git/

 -  git clone rsync://remote.ng/path/to/repo.git/

 An alternative scp-like syntax is also valid when using the ssh protocol:

 -  git clone [you@]remote.ng:path/to/repo.git/

 Just as is the case for pull/push, `https` is not secure and should be used with caution
