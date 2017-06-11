---
layout: post
date: 2016-06-14 12:23:00
title: "Control Theory and Machine Learning"
excerpt: ""
comments: true
permalink: ml-control
category: [Q&A,machine-learning,control]
---

### Is there any relation between control systems and Machine Learning?

Answered [here](https://www.quora.com/Is-there-any-relation-between-control-systems-and-Machine-Learning/answers/21063329) originally.

You bet there is. I'll start with the basic building block of the modern machine learning paradigm: the perceptron. This was a hardware structure built in the 50's by Rosenblatt to mimic the real neural network in our brains. It arose out of control theory literature when people were trying to identify highly complex and nonlinear dynamical systems. Neural networks -- artificial neural networks -- were first used in a supervised learning scenario in control theory. Hornik, if I remember correctly, was the first to find that neural networks were universal approximators.

You've heard about the classic sigmoid nonlinear activation function often used in machine/deep learning as a nonlinear squasher? It came out of control theory literature. Without classical control theory, you could say there would be no back-propagation (invented by Rumelhart & Hinton in the '80's based on inspiration from control theory); there would be no back propagation through time (largely due to Werbos' work in his 1990 classic paper, Backpropagation Through Time: What it entails) now used in recurrent neural networks by modern machine learning practicists; there would probably not be the LSTM (invented by Horchreiter in 1996) which are used in modeling tapped delay lines in memory-based neural networks. These have found massive use in speech recognition, language models or time-series sequences.

The conflict between exploration and exploitation in reinforcement learning is known in control engineering as the conflict between identification (or estimation) and control (e.g., Witten, 1976). You could arguably say massive reinforcement learning problems arose out of Control Engineering research. Read Andrew Ng’s [Thesis](http://rll.berkeley.edu/deeprlcourse/docs/ng-thesis.pdf) for a perspective.

If you read the works of modern machine learning theorists, you'll find control jargons camouflaged into new diction to make their ideas sound new or sexy. I think there is some sort of dis-ingenuity among these researchers by not acknowledging that these algorithms arose out of a domain they are often not willing to give credit to. What they call backprop, for example, is nothing more than old-fashioned calculus-based differential chain rule. Variants of recurrent neural networks are simply NARX models (Ilya Suskever [Thesis](http://www.cs.utoronto.ca/~ilya/pubs/ilya_sutskever_phd_thesis.pdf)) that you would encounter in any system identification literature. So to answer your question, modern machine learning is a derived class of classical control theory.
