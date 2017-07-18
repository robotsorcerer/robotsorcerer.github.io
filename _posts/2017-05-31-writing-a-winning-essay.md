---
layout: post
date: 2017-05-31 9:37:00
title: "<center>Writing a winning essay</center>"
excerpt: "<center>An advice on applying for fellowships, internships and jobs as a grad student.</center>"
comments: true
mathjax: true
permalink: winning-grad-essay
---

- [Table of Contents](#table-o-conts)
- [Introduction](#intro)
- [Pulling/Pushing git remotes from LAN/WAN repos](#pullpush)
- [Cloning git remotes from LAN/WAN repos](#clone)

<a name="intro"></a>
### Introduction

This post is an advice for grad students and people in similar sphere who are applying for scholarships, fellowships and internships. I thought I knew a little about this and I might as well pen my ideas for others to learn from.



<a name="pullpush"></a>
#### Pulling/Pushing git remotes from a LAN/WAN repo

As an example, suppose we have a repo named `sensors` in the `Documents` directory of a computer with username and group name `drumpf@dissembler` and we have a few commits ahead of a tracking repo on a computer named `robots@killem`, we can fetch and merge our recent commits on `drumpf@dissembler` into `robots@killem` as follows:

We could use `ssh`, `http[s]`, `ftp[s]` or `rsync` transport protocols. To pull updates from `drump@dissembler:~/Documents/sensors.git` to `robots@killem:~/Documents/sensors.git` repo, we would do one of the following:

  - via ssh:

    <pre class="terminal"><code>robots@killem:~/Documents/sensors$ git pull ssh://drumpf@dissembler:/~/Documents/sensors.git</code></pre>

  - via https:

      <pre class="terminal"><code>robots@killem:~/Documents/sensors$ git pull http[s]://drumpf@dissembler:/robots/killem/Documents/sensors.git</code></pre>

  - via ftp

      <pre class="terminal"><code>robots@killem:/home/drumpf/Documents/sensors$ git pull ftp[s]://drumpf@dissembler:/robots/killem/Documents/sensors.git</code></pre>

  - via rsync

      <pre class="terminal"><code>robots@killem:/home/drumpf/Documents/sensors$ git pull rsync://drumpf@dissembler:/~/Documents/sensors.git</code></pre>

Note that we have used user expansion for both `ssh` and `git`. `ftp[s]` and `rsync` do not allow user expansion when pulling, pushing or cloning, so the full path to the repo has to be specified.
The `https` syntax has no authentication and can be dangerous on unsecured networks. If the group names of the computers are not advertised by `/etc/hosts`, you can use the ip address of the computer in place of the host names. Note that `ftp[s]` can be used for fetching while `rsync` can be used for both fetching and pushing. Both are not very efficient, however, and they are actually deprecated; so you should refrain from using them as much as you can.

All the commands above would also work for `git push`.

**SCP-like syntaxes are valid as well:**

  <pre class="terminal"><code>scp [user@]host.ng:path/to/repo.git/</code></pre>

but note that the first character after the first column must not be a slash to help distinguish a local path from an ssh url

All of the above commands also support cloning `git` repos from one directory to another on the same host or between workstations on the same `LAN/WAN`. All that would need to change would be to replace the `LAN/WAN` hostname with the path we are cloning from. See examples below:

<a name="clone"></a>
#### Cloning git remotes from a LAN/WAN repo

The procedure is the same as above save we replace pull/push with clone, e.g

 -  <pre class="terminal"><code>git clone ssh://[you@]remote.ng[:port]/path/to/repo.git/</code></pre>

 -  <pre class="terminal"><code>git clone  git://remote.ng[:port]/path/to/repo.git/</code></pre>

 -  <pre class="terminal"><code>git clone  http[s]://remote.ng[:port]/path/to/repo.git/</code></pre>

 -  <pre class="terminal"><code>git clone  ftp[s]://remote.ng[:port]/path/to/repo.git/</code></pre>

 -  <pre class="terminal"><code>git clone rsync://remote.ng/path/to/repo.git/</code></pre>


 If when doing any of the operations specified so far, the transport protocol is not specified, no problem! Git assumes a remote url transport protocol if it does not know what the remote address is. So we could for example do

 <pre class="terminal"><code>robots@killem:~/Documents/sensors$ git push transport::address</code></pre>

 where `address` is the path to the repo on the LAN/WAN and transport is replaced by `https`.

 An alternative scp-like syntax is also valid when using the ssh protocol:

 -   <pre class="terminal"><code>git clone [you@]remote.ng:path/to/repo.git/</code></pre>

 Just as is the case for `pull/push`, `https` is not secure and should be used with caution.
