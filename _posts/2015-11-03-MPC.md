---
layout: post
date: 2015-11-03 10:21:00
title: "Optimal Controllers: A Model Predictive Control Approach (I)"
excerpt: "Optimal controllers belong to the class of controllers that minimize a cost function with respect to a <u><b>predicted</u></b> control law over a given <u><b>prediction horizon</u></b>."
permalink: Optimal-Controllers-MPC
comments: true
mathjax: true
---

<!-- Google Tag Manager -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-WXGQX2"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-WXGQX2');</script>
<!-- End Google Tag Manager -->

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  TeX: { equationNumbers: { autoNumber: "AMS" } }
});
</script>

<!--Mathjax Parser -->
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<!--End Mathjax Parser -->

<!--Use Dollar Signs for inline math mode: -->

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
});
</script>

<script type="text/javascript" async src="path-to-mathjax/MathJax.js?config=TeX-AMS_CHTML"></script>

<!--End Use Dollar Signs for inline math mode: -->

<!-- End: Mathjax $ Symbols -->

*This post is part of my series on the state space approach for Optimal Model Predictive Controllers*

<TABLE BORDER="5"    WIDTH="100%"   CELLPADDING="1" CELLSPACING="2">

    <TR>
      <TH COLSPAN="4"><BR><H3>Table of Notations and Abbreviations</H3>
      </TH>
    </TR>

    <TR>
      <TH>Notation</TH>
      <TH>Meaning</TH>
      <TH>Abbreviation</TH>
      <TH>Meaning</TH>
    </TR>

    <TR ALIGN="CENTER">
      <TD>$z^{-1}$</TD>
      <TD>Unit delay operator</TD>  
      <TD>MFD</TD>
      <TD>Matrix Fraction Description</TD>   
    </TR>

    <TR ALIGN="CENTER">
      <TD>$x_{\rm \rightarrow}$</TD>
      <TD>Future values of x</TD>  
      <TD>LTI</TD>
      <TD>Linear Time Invariant</TD>    
    </TR>   

    <TR ALIGN="CENTER">
      <TD>$x_{\rm \leftarrow}$</TD>
      <TD>Past values of x</TD> 
      <TD>FSR</TD>
      <TD>Finite Step Response</TD>     
    </TR>  

    <TR ALIGN="CENTER">
      <TD>$\Delta = 1 - z^{-1}$</TD>
      <TD>Differencing Operator</TD>  
      <TD>FIR</TD>
      <TD>Finite Impulse Response</TD>  
    </TR>  

    <TR ALIGN="CENTER">
      <TD>$z^{-1}$</TD>
      <TD>Backward shift operator (z-transforms)</TD>   
      <TD>TFM</TD>
      <TD>Transfer Function Model</TD>
    </TR>  

    <TR ALIGN="CENTER">
      <TD>$n_y$</TD>
      <TD>Output Prediction Horizon</TD>    
      <TD>SISO</TD>
      <TD>Single-Input Single Output</TD>
    </TR> 

    <TR ALIGN="CENTER">
      <TD>$n_u$</TD>
      <TD>Input Horizon</TD>  
      <TD>MIMO</TD>
      <TD>Multiple-Input Multiple Output</TD>
    </TR>   

    <TR ALIGN="CENTER">
      <TD>$u(k-i)$</TD>
      <TD>Past input</TD> 
      <TD>IMC</TD>
      <TD>Internal Model Control</TD>
    </TR> 

    <TR ALIGN="CENTER">
      <TD>$y(k-i)$</TD>
      <TD>Past output</TD>
      <TD>IM</TD>
      <TD>Independednt Model</TD>
    </TR>      
</TABLE>

###<center>**Optimal Controllers: An Overview**</center>
> If you are already familiar with LQ methods, you can skip this section and go straight to [**Model Predictive Controllers**](#Model-Predictive-Controllers)

Optimal controllers belong to the class of controllers that minimize a cost function with respect to a <u><b>predicted</u></b> control law over a given <u><b>prediction horizon</u></b>. They generate a desired <u><b>output control</u></b> sequence from which the optimal <u><b>_control law_</u></b> may be determined. 

<br></br>
Take your car cruise speed controller for an example. The vehicle dynamics of the car is *_modeled_* into the cruise control system. The road curvature ahead of you gets *_predicted_* online as you drive and <u>_control sequences_</u> are generated based on an _*internal model*_ (*_prediction*_) of the slope of the road/road curvature using past observations; other disturbances (such as rain, friction between tire and road) are modeled into the prediction ideally. At time \\(k + 1\\), only the first element <b>_control action_</b> within the generated control sequence is used as a *feedback* control mechanism for your car. At the next <b>_sampling time instant_</b>, new predictions are made based on the prediction horizon and a new control sequence is generated online. Again, the chosen control action is the first element in the control sequence such  that we are constantly choosing the best among a host of control actions using our anticipated <b>_prediction_</b> of the road curvature and other environmental variables to give the desired <b>_performance_</b>.

<br></br>
Optimal controllers are mostly used in discrete processes ([others](#Gawthrop) have postulated continuous time models for such controllers but the vast majority of commercial users of optimal controllers are in discrete time) and are very useful for processes where the setpoint is known ahead of time. Typically, a criterion function is used to determine how well the controller is tracking a desired trajectory. An example model predictive controller (MPC) criterion function, in its basic form, is given as  

<a name = eqn:cost-function></a>
\begin{equation}            \label{eqn:cost function}
  J  = \sum\nolimits_{i=n\_w}^{n\_y} [\hat{y}(k+i) - r(k + i)]^2 
\end{equation}  

where \\(i\_w\\) is typically taken as 1, \\(n\_y\\) is the prediction horizon, \\(\hat{y}(k+i)\\) is the prediction and \\(r(k+i)\\) is the desired trajectory (or setpoint).

The controller output sequence, \\(\Delta u \\), is obtained by minimizing \\(J\\) over the prediction horizon, \\(n_y\\), with respect to \\(\Delta u \\), i.e.,

\begin{equation}
  \Delta u  = \text{arg} \min\_{\rm \Delta u} J \label{eqn:min J} 
\end{equation}

where \\(\Delta u \\) is the future control sequence.

<br></br>
If equation \eqref{eqn:cost function} is **_well-posed_**<a href="#footnote-1">\\(^{1}\\)</a>, then \\(\Delta u \\) would be optimal with respect to the criterion function and hence [eliminate offset in trajectory tracking](#eqn:carima). 

<div class="fig figcenter fighighlight"> 
  <img src="/downloads/MPC/MPCConcept.jpg" width="50%" height="350", border="0" style="float:left;">
  <img src="/downloads/MPC/LQG.jpg" width="50%" height="350"  border="0" style="float:right;">  
  <div class="figcaption" align="left">Fig.1.0.0. Tracking by a Model Predictive Controller. <div class="figcaption" align="right">Fig. 1.0.1. Reference Tracking by an LQ Controller</a></a>.
  </div></div>
</div>

<!--![MPCControl.jpg](/downloads/MPC/MPCConcept.jpg){: .center-image }-->
<br></br>
It becomes obvious from equation \eqref{eqn:cost function} that minimizing the criterion function is an optimization problem. One useful approach in typical problems is to make \\(J\\) <b>_quadratic_</b> such that the model becomes linear; if there are no contraints, the solution to the quadratic minimization problem is analytic.

#### <center>**Linear Quadratic (LQ) Controllers**</center>
Linear Quadratic Controllers are indeed predictive controllers except for the infinite horizon which they employ in minimizing the criterion function. The criterion function is minimized only once resulting in an optimal controller output sequence from which the controller output is selected.
Similar to model predictive controllers, they are in general discrete time controllers. For a linear problem such as

<a name=eqn:state-model></a>
\begin{gather} \label{eqn:state-model}
  x(k+1) = A \, x(k) + B \, u(k)  \nonumber \newline 
  y(k) = C^T \, x(k)              \nonumber
\end{gather}

The cost function is typically constructed as 

<a name=eqn:LQ-cost></a>
\begin{equation}  \label{eqn:LQ-cost}
J = \sum_{k=0}^n x^T(k)\,Q\,x(k) + R \, u(k)^T \, u(k) + 2 x(k)^T \, N \, u(k)
\end{equation}  

where \\(n\\) is the terminal sampling instant, \\(Q\\) is a symmetric, positive semi-definite matrix that weights the \\(n\\)-states of the matrix, \\(N\\) specifies a matrix of appropriate dimensions that penalizes the cross-product between the input and state vectors, while \\(R\\) is a symmetric, positive defiite weighting matrix on the control vector , \\(u\\). 

Other variants of equation \eqref{eqn:LQ-cost} exist where instead of weighting the states of the system, we instead weight the output of the system by constructing the cost function as

<a name=eqn:LQ-costy></a>
\begin{equation}   \label{eqn:LQ-costy}
  J = \sum_{k=0}^n y^T(k) \,Q \,y(k) + R\, u(k)^T \, u(k) +  2 x(k)^T \, N \, u(k)
\end{equation}

In practice, it is typical to set the eigen values of the \\(Q\\)-matrix to one while adjusting the eigenvalue(s) of the \\(R\\) matrix until one obtains the desired result. \\(N\\) is typically set to an appropriate matrix of zeros. This is no doubt not the only way of tuning the LQ controller as fine control would most likely require weighting the singleton-diagonal terms (eigen-values effectively if \\(Q\\) is block diagonal) of the Q-matrix differently (this is from the author's experience when tuning LQ controllers).

<br></br>
If we model disturbances into the system's states, the optimization problem becomes a stochastic optimization problem that must be solved. The separation theorem applies such that we can construct a state estimator which asymptotically tracks the internal states from observed outputs using the [algebraic Riccati equation](https://en.wikipedia.org/wiki/Algebraic_Riccati_equation) given as 

\begin{equation}    \label{eqn:Riccati}
  A^T P A -(A^T P B + N)(R + B^T P B)^{-1}(B^T P A + N) + Q.
\end{equation}

\\(P\\) is an unknown \\(n \times n\\) symmetric matrix and \\(A\\), \\(B\\), \\(Q\\), and \\(R\\) are known coefficient matrices as in equations \eqref{eqn:LQ-cost} and \eqref{eqn:LQ-costy}. We find an optimal control law by solving the minimization of the deterministic LQ problem, equation \eqref{eqn:LQ-cost} which we then feed into the states. 

<br></br>
The optimal controller gains, \\(K\\) are determined from the equation

\begin{equation}
  K\_{lqr} = R^{-1}(B^T \, P + N^T)
\end{equation}

where \\(P\\) is the solution to the algebraic Riccati equation \eqref{eqn:Riccati}.

In classical control, we are accustomed to solving a control design problem by determining design parameters based on a given set of design specifications (e.g. desired overshoot, gain margin, settiling time, e.t.c). Discrete LQ controllers pose a significal difficulty with respect to solving such problems as it is challenging to solve the criterion function in terms of these design parameters since the discrete state space matrices hardly translate to any physical meaning. It turns out that if the cost function is quadratic in the parameters and the state space matrices are in  **_continuous time_**, the weighting matrices would no longer correspond to the artificial, \\(A, B, and C\\) matrices (which is indeed what they are in discrete state space).

<a name=Model-Predictive-Controllers></a>
####**<center>Model Predictive Controllers (MPC)**</center>
A key thing about LQ closed loop problems is that we can pretty much guarantee closed loop stability if the prediction horizon, \\(N \rightarrow \infty\\). Model Predictive Controllers, on the other hand, employ a receding (which is a finite) horizon concept in determining the control sequence and closed-loop stability is generally not guaranteed. Basically, for inifinite horizon controllers such as LQ methods, this means there is no model mismatch between the predictor model and plant. In practice, this is tough to achieve as disturbances play a large role in virtually all real-world systems. One way of avoiding mismatch is to include an integrator in the prediction model as an **_internal model_** of the disturbance. This could be a **CARIMA**  (**C**ontrolled **A**uto **R**egressive **I**ntegral **M**oving **A**verage) model, for example. A typical **CARIMA** model takes the polynomial form

<a name=eqn:carima></a>
\begin{equation}  \label{eqn:carima}
  A(z^{-1})\,y(k) = B(z^{-1})\,u(k) + \dfrac{C(z^{-1})}{1-z^{-1}}\,e(k)
\end{equation}

where \\(A\\), \\(B\\), and \\(C\\) are polynomials in the backward shift operator \\(z^{-1}\\) given by


\begin{equation} \label{eqn:poly}
  A(z^{-1}) = 1 + a_1\,z^{-1} + a\_2 + \, z^{-2} + \cdots + a\_{n\_a}z^-{n\_a}  \nonumber
\end{equation}

\begin{equation}
  B(z^{-1}) = b\_1 + b\_2\, z^{-1} + b\_3 \, z^{-2} + \cdots + b\_{n_b}z^-{n\_b}  \nonumber
\end{equation}

\begin{equation}
  C(z^{-1})) = c\_0 + c\_1\, z^{-1} + c\_2 \, z^{-2} + \cdots + c\_{n_b}z^-{n\_c},
\end{equation}

and \\(y(k), u(k) and e(k), k = 1, 2, \cdots \\)  are respectively the plant output, input and integrated noise term in the model. 

MPC's are generally good and better if correctly implemented in that they handle disturbances typically well and can anticipate future disturbances well making the control action more effective as a result. This is because of an **internal model** of the plant that allows them to anticipate future "behavior" of plant output and mitigate such errors before the plant reaches the "future time". 

<br></br>
[Rossiter](https://www.sheffield.ac.uk/acse/staff/jar) gives a classic analogy in the way human beings cross a road. It is not sufficient that a road is not busy with passing cars on it. As you cross, you constantly look at ahead (your prediction horizon) to anticipate oncoming vehicles and update your movement (=control action) based on your prediction (based on past observations).

>**Accurate prediction over a selected horizon is critical to a successful MPC implementation**. 

We give a brief overview of common models employed in MPC algorithms. Readers are referred to System Identification texts e.g., [Box and Jenkins](#box-jenkins),  [Billings](#billings), or [Ljung](#Ljung) where data modeling and system identification are elucidated in details.

<div class="fig figcenter fighighlight"> 
  <img src="/downloads/MPC/lrpc.jpg" width="75%" height="450", border="0" style="float:center;"> 
  <div class="figcaption" align="center">Fig.2.1. Receding Horizon Concept (Copyright: Mahdi Mahfouf, University of Sheffield, 2011 - 2012). 
</div>
</div>


<br></br>
####<center>**Linear Models in Predictive Control**</center>
An essential part of an MPC design is the internal model of the plant. If we want a high-fidelity control, we would want to develop a high fidelity model. For optimal control, our controller would only be as good as our model. If our understanding of the plant is faulty and this transfers to the model, we would typically have model mismatch between plant and predictor and our implementation of the MPC may even be worse than using an infinite horizon control.
 
We briefly discuss the common classical models that have been accepted as a standard by the control community in the past two-some decades. 

Linear models obey the superposition principle. Put differently, their internal structure can be approximated by a linear function in the proximity of the desired operating point. In general, linear system identification belong in two large categories: parametric and non-paramnetric methods. We briefly discuss parametric methods as these are the most commonly employed models in MPC approaches.

<br></br>
#####<center> **Autoregressive Moving Average with Exogenous Input Model (ARMAX)** </center>

The general structure of the linear finite-horizon system can be written as 

\begin{equation} \label{eqn:ARMAX}
  A(z^{-1})\,y(k) = \dfrac{B(z^{-1})}{F(z^{-1})}\,u(k) + \dfrac{C(z^{-1})}{D(z^{-1})}\,e(k)
\end{equation}

with \\(A(z^{-1}), \, B(z^{-1}), \, C(z^{-1}) \\) defined as in equation [\eqref{eqn:poly}](#eqn:poly) and the \\(F(z^{-1}), \text{ and } D(z^{-1})\\) polynomials defined as

\begin{equation}
  D(z^{-1}) = 1 + d_1\,z^{-1} + d\_2 + \, z^{-2} + \cdots + d\_{n\_d}z^-{n\_d}  \nonumber
\end{equation} 

\begin{equation}
  F(z^{-1})) = 1 + f_1\,z^{-1} + f\_2 + \, z^{-2} + \cdots + f\_{n\_f}z^-{n\_f} 
\end{equation}

The autoregressive part is given by the component \\(A(z^{-1}) \, y(k)\\), while the noise term is modeled as a moving average regression model in \\(\dfrac{C(z^{-1})}{D(z^{-1})}\,e(k)\\); the exogenous component is given by \\(\dfrac{B(z^{-1})}{F(z^{-1})}\,u(k)\\). 

<br></br>
#####<center> **Autoregressive Model (AR)** </center>

If in equation \eqref{eqn:ARMAX},  \\(B(z^{-1}) = 0\\) and \\(C(z^{-1}) = D(z^{-1}) = 1\\) then  we have an AR model,

\begin{equation}
  y(k) = -a\_1 \, y(k-1) -  a\_2 \,  y(k-2) - \cdots - a\_{n_a} \, y(k-{n\_a})
\end{equation}

Alternatively, if \\(A(z^{-1}) = 1\\) , \\(B(z^{-1}) = 0, \,  \text{ and } \, C(z^{-1}) = 1 \\) then we end up with the regression

\begin{equation}
  y(k) = - d\_1 \, y(k-1) - d\_2 \, y(k-2) - \cdots - d\_{n\_d} y(k - n\_d) + e(k) 
\end{equation}

<br></br>
#####<center> **Moving Average Model (MA)** </center>

If \\(A(z^{-1}) = 1\\), \\(B(z^{-1}) = 0\\) and \\(D(z^{-1}) = 1\\), then we have the following moving average noise model

\begin{equation}
  y(k) = e(k)+ c\_1e(k-1) + \cdots + c\_{n\_c}e(k-n\_c)
\end{equation}

<br></br>
#####<center> **Autoregressive  with Exogenous Input Model (ARX)** </center>

If \\(F(z^{-1}) = 1\\), and \\(C(z^{-1}) = D(z^{-1}) =1\\), we obtain the ARX structure
\begin{equation}
\begin{split}
  y(k) & = -a\_1 \, y(k-1) - \cdots - a\_{n_a} \, y(k-{n\_a}) + b\_1u(k-1) \\
       &+\cdots + b\_{n\_b}u(k-n\_b) + e(k)
       \end{split} 
\end{equation}

<br></br>
#####<center> **Autoregressive Moving Average Model (ARMA)** </center>

Setting \\(B(z^{-1}) = 0\\), and \\(D(z^{-1}) = 1\\), we obtain the ARMA model,
\begin{equation}
\begin{split}
  y(k) & = -a\_1 \, y(k-1) - \cdots - a\_{n_a} \, y(k-{n\_a}) + c\_1eu(k-1) \\
       &+\cdots + c\_{n\_c}e(k-n\_c)
       \end{split} 
\end{equation}


<br></br>
#####<center> **Finite Impulse Response Model (FIR)** </center>

If in equation \eqref{eqn:ARMAX}, \\(A(z^{-1}) = F(z^{-1}) = 1 \text{ and } C(z^{-1}) = 0\\), we have an FIR model. This can be rewritten as 

\begin{equation}
  y(k+i) = \sum\_{j=0}^{n\_y - 1} \, h\_j\, u(k-j+i-1)
\end{equation}

for predictions of the process output at \\(t = k+i\\) with \\(i \geq 1\\). 

The FIR model has the advantage of being simple to construct in that no complex calculations are required of the model and model assumptions are required. They are arguably the most commonly used in commercial MPC packages. However, it does come up short for unstable systems and it also requires a lot of parameters to estimate an FIR model.

The author's [Github repo](https://github.com/SeRViCE-Lab/Matlab-Files/blob/master/ident_data/) has various examples where typical [ARX, ARMAX, Impulse Response and AR models](https://github.com/SeRViCE-Lab/Matlab-Files/blob/master/ident_data/Filtered%20GWN/carimaFWGN.m), are identified from finite data. 

<br></br>
#####<center> **Box-Jenkins (BJ) Model** </center>
The BJ Model is obtained by setting 
\begin{equation} \label{eqn:BJ}
  y(k) = \dfrac{B(z^{-1})}{F(z^{-1})}\,u(k) + \dfrac{C(z^{-1})}{D(z^{-1})}\,e(k)
\end{equation}

<br></br>
<a name=fsr></a>

#####<center> **Finite Step Response Model (FSR)** </center>

\begin{equation}
  y(k) = \sum\_{j=0}^{n\_s - 1} \, s\_j\, \Delta u(k-j-1)
\end{equation}

where \\(\Delta\\) is the differencing operator (\\(\Delta = 1 - q^{-1}\\)) and \\(q^{-1}\\) is the backward shift operator. \\(n\_s\\) is the number of step response elements \\(s\_j\\) used in predicting \\(y\\).
<br></br>


> **Continued in [Optimal Controllers: An MPC State Space Approach (II)](http://lakehanne.github.io/Optimal-Controllers-MPC-II/)**



<br></br>
<a name=box-jenkins></a>[Box and Jenkins]: Box, G.E.P. and Jenkins, G.M., '*Time Series Analysis:Forecasting and Control. San Francisco, CA*', Holden Day, 1970.

<a name=billings></a>[Billings] :  Stephen A. Billings. '*Nonlinear System Identification. NARMAX Methods in the Time, Frequency and Spatio-Temporal Domains*'. John Wiley & Sons Ltd, Chichester, West Sussex, United Kingdom,  2013.

<a name=Gawthrop></a>[Gawthrop] : '*Continuous-Time Self-Tuning Control*' Vols I and II, Tannton, Research Studies Press, 1990.

<a name=Ljung></a>[Ljung] : L. Ljung. '*System Identification Theory for the User*'. 2nd Edition. Upper Saddle River, NJ, USA. Prentice Hall, 1999.


<!--
####<left>Table 1.1</left>

<left>**Notation and variable names**</left>

| Notation | Description |
| :------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
-->

<br></br>
<p id="footnote-1">[1] A well-posed \\(J\\) should have an unbiased predictions in steady state. That is the minimizing argument of \\(J\\) must be consistent with an offset-free tracking. This implies the predicted control sequence to maintain zerto tracking error must be zero. The minimum of \\(J = 0\\) in steady state is equivalent to \\(r\_{\rm \rightarrow}\\) \\(- \, y\_{\rm \rightarrow} = 0\\) and \\(u\_{k+i} - u\_{k+i-1} = 0\\).

(Note that \\(x\_{\rm \rightarrow}\\) denotes future values of \\(x\\) ). 