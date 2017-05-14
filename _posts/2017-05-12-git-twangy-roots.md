---
layout: post
date: 2017-05-12 11:37:00
title: "<center>Twanging git pull, push and clone</center>"
excerpt: "<center>It is useful being able to share one's work among different computers using native git commands such as merge, fetch, push, clone, or pull without resolving to using ssh, scp which are without the benefits of diff and merge strategies of git.</center>"
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

  Git is a useful tool for remote and online work collaboration, as well as social coding. It is useful being able to share one's work among different computers using native git commands such as `merge`, `fetch`, `push`, `clone`, or `pull` without resolving to using `ssh`, or `scp` which are without the benefits of `diff` and `merge` strategies of `git`. More so, not everyone enjoys exposing their incomplete work/code to a remote repo for the sake of fetching to local `origins` on different computers. This post is meant to show how to go about these git strategies without going through a remote e.g. an http[s] master.

<a name="pullpush"></a>
#### Pulling/Pushing git remotes from a LAN/WAN repo

We can update local git refs without pulling from a web-based remote. Suppose I have the same git repo on two computers in the same local/wide-area network, we can `git pull` or `git push` without resolving to going through the git repo hosted on an http[s] web server. As an example, suppose we have a repo named `sensors` on a computer with username and group name `drumpf@dissembler` and we have a few commits ahead of the repo on a computer named `robots@killem`, we can fetch and merge my updates on `drumpf@dissembler` into `robots@killem` as follows:

1. We could use ssh, git, https, ftp or rsync transport protocols. For instance, if we want to pull from `drump@dissembler:~/Documents/sensors.git` to `robots@killem:~/Documents/sensors.git` repo, we would do one of the following:

  - via ssh:

    <pre class="terminal"><code>robots@killem:~/Documents/sensors$ git pull ssh://drumpf@dissembler:/~/Documents/sensors.git</code></pre>

  - via https:

      <pre class="terminal"><code>robots@killem:~/Documents/sensors$ git pull http[s]://drumpf@dissembler:/robots/killem/Documents/sensors.git</code></pre>

  - via ftp

      <pre class="terminal"><code>robots@killem:~/Documents/sensors$ git pull ftp[s]://drumpf@dissembler:/robots/killem/Documents/sensors.git</code></pre>

  - via rsync

      <pre class="terminal"><code>robots@killem:~/Documents/sensors$ git pull rsync://drumpf@dissembler:/~/Documents/sensors.git</code></pre>

Note that we have used user expansion for both ssh and git. `ftp[s]` and `rsync` do not allow user expansion when pulling, pushing or cloning, so the full path to the repo has to be specified.
The `https` syntax has no authentication and can be dangerous on unsecured networks. If the group names of the computers are not advertised by `/etc/hosts`, you can use the ip address of the computer in place of the host names. Note that ftp/ftps can be used for fetching while rsync can be used for fetching and pushing. Both are not very efficient, however and they are actually deprecated; so you should refrain from using them as much as you can.

All the commands above would also work for `git push`.

SCP-like syntaxes are valid as well:

  - scp [user@]host.ng:path/to/repo.git/

but note that the first character after the first column must not be a slash to help distinguish a local path from an ssh url

2. All the above commands also support cloning git repos from one file directory to another on the same host or between workstations on the same LAN/WAN. All that would need to change would be to replace the LAN/WAN hostname with the path we are cloning from. See examples below:

<a name="clone"></a>
#### Cloning git remotes from a LAN/WAN repo

The procedure is the same as above save we replace pull/push with clone, e.g

 -  git clone ssh://[you@]remote.ng[:port]/path/to/repo.git/

 -  git clone  git://remote.ng[:port]/path/to/repo.git/

 -  git clone  http[s]://remote.ng[:port]/path/to/repo.git/

 -  git clone  ftp[s]://remote.ng[:port]/path/to/repo.git/

 -  git clone rsync://remote.ng/path/to/repo.git/


 If when doing any of the operations specified so far, the transport protocol is not specified, no problem! Git assumes a remote url transport protocol if it does not know what the remote address is. So we could for example do

 <pre class="terminal"><code>robots@killem:~/Documents/sensors$ git push transport::address</code></pre>

 where `address` is the path to the repo on the LAN/WAN and transport is replaced by `https`.

 An alternative scp-like syntax is also valid when using the ssh protocol:

 -  git clone [you@]remote.ng:path/to/repo.git/

 Just as is the case for pull/push, `https` is not secure and should be used with caution.
