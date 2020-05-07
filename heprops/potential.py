'''
potential.py

Author: Adrian Del Maestro
Date: 2020-05-07

Implement various helium-helium interaction potentials.
'''

import numpy as np

# compute some factorials
factorials = [np.math.factorial(i) for i in range(20)]

# ------------------------------------------------------------------------
def lennard_jones(r,ε=10.956,σ=2.6413813):
    '''Lennard-Jones potential where ϵ in K and σ in Å.

       \begin{equation}
       V(r) = 4\varepsilon \left[\left(\frac{\sigma}{r}\right)^{12}
              - \left(\frac{\sigma}{r}\right)^6\right]
       \end{equation}
       
       Parameters taken from: R. A. Aziz, A. R. Janzen, and M. R. Moldover, 
       Phys. Rev. Lett. 74, 1586 (1995).  
       https://doi.org/10.1103/PhysRevLett.74.1586

    '''
    x = σ/r
    return 4.0*ε*(x**12 - x**6)

# ------------------------------------------------------------------------
'''
Aziz Potential


1979: R. A. Aziz, V. P. S. Nain, J. S. Carley, W. L. Taylor, and G. T. McConville, 
J. of Chem. Phys. 70, 4330 (1979).  
https://doi.org/10.1063/1.438007

1987: R. A. Aziz, F. McCourt, and C. Wong, Mol. Phys. 61, 1487 (1987). 
https://doi.org/10.1080/00268978700101941

1995: R. A. Aziz, A. R. Janzen, and M. R. Moldover, 
Phys. Rev. Lett. 74, 1586 (1995).  
https://doi.org/10.1103/PhysRevLett.74.1586

\begin{equation}
V(r)= \varepsilon\left[A \exp (-\alpha x + \beta x^2)-F(x) \sum_{j=0}^{2}\frac{C_{2 j+6}}{x^{2 j+6}}\right]
\label{eq:Vaziz}
\end{equation}

where

\begin{equation}
F(x)=
\begin{cases}
\exp \left[-\left(\frac{D}{x}-1\right)^{2}\right] &,&  x<D \\
1 &,& x \geq D
\end{cases}
\end{equation}

and 

\begin{align}
\varepsilon=10.8\ \mathrm{K}, & \qquad  C_{6}=1.3732412\\
r_{m}=2.9673\ Å, &\qquad C_{8}=0.4253785\\
D = 1.241314, &\qquad C_{10}=0.1781\\
\alpha=13.353384, &\qquad  A=0.5448504 \times 10^{6} \\
\beta = 0, & \\
\end{align}
'''

# Setup the Aziz parameter dictionary
Aziz_params = {}

Aziz_params['1979'] = {}
Aziz_params['1979']['ε'] = 10.8 # K
Aziz_params['1979']['rₘ'] = 2.9673 # Å
Aziz_params['1979']['D'] = 1.241314
Aziz_params['1979']['α'] = 13.353384
Aziz_params['1979']['β'] = 0.0
Aziz_params['1979']['C'] = np.zeros(11)
Aziz_params['1979']['C'][6] = 1.3732412
Aziz_params['1979']['C'][8] = 0.4253785
Aziz_params['1979']['C'][10] = 0.1781
Aziz_params['1979']['A'] = 0.5448504E6

Aziz_params['1987'] = {}
Aziz_params['1987']['ε'] = 10.948 # K
Aziz_params['1987']['rₘ'] = 2.9673 # Å
Aziz_params['1987']['D'] = 1.4826
Aziz_params['1987']['α'] = 10.43329537
Aziz_params['1987']['β'] = -2.27965105
Aziz_params['1987']['C'] = np.zeros(11)
Aziz_params['1987']['C'][6] = 1.36745214
Aziz_params['1987']['C'][8] = 0.42123807
Aziz_params['1987']['C'][10] = 0.17473318
Aziz_params['1987']['A'] = 1.8443101E5

Aziz_params['1995'] = {}
Aziz_params['1995']['ε'] = 10.956 # K
Aziz_params['1995']['rₘ'] = 2.9683 # Å
Aziz_params['1995']['D'] = 1.438
Aziz_params['1995']['α'] = 10.5717543
Aziz_params['1995']['β'] = -2.07758779
Aziz_params['1995']['C'] = np.zeros(11)
Aziz_params['1995']['C'][6] = 1.35186623
Aziz_params['1995']['C'][8] = 0.4149514
Aziz_params['1995']['C'][10] = 0.17151143
Aziz_params['1995']['A'] = 1.86924404E5

# ------------------------------------------------------------------------
def __F(x,D): 
    if x >= D:
        return 1.0
    t = (D/x-1.0)**2
    return np.exp(-t)
F = np.vectorize(__F)

# ------------------------------------------------------------------------
def V_phenom(x,C,D):
    t = 0
    for j in range(3):
        t += C[2*j+6]/x**(2*j+6)
    return F(x,D)*t

# ------------------------------------------------------------------------
def aziz(r,p):
    '''The Aziz potential in kelvin.'''
    x = r/p['rₘ']
    return p['ε']*(p['A'] * np.exp(-p['α']*x + p['β']*x**2)-V_phenom(x,p['C'],p['D']))

aziz_1979 = lambda r : aziz(r,Aziz_params['1979'])
aziz_1987 = lambda r : aziz(r,Aziz_params['1987'])
aziz_1995 = lambda r : aziz(r,Aziz_params['1995'])

# ------------------------------------------------------------------------
'''
 ## Szalewicz 2012
 * M. Przybytek, W. Cencek, J. Komasa, G. Łach, B. Jeziorski, and K. Szalewicz, 
   Phys. Rev. Lett. 104, 183003 (2010).  
   https://doi.org/10.1103/PhysRevLett.104.183003
 * W. Cencek, M. Przybytek, J. Komasa, J. B. Mehl, B. Jeziorski, and K. Szalewicz, 
   J. Chem. Phys. 136, 224303 (2012).  
   https://doi.org/10.1063/1.4712218
 
 \begin{equation}
  V(R)= e^{-a R}\sum_{j=0}^{2}P_{j}R^j+e^{-b R}\sum_{j=0}^{1}Q_{j}R^j -\sum_{n=3}^{16} f_{n}(\eta R) \frac{C_{n}}{R^{n}}
 \end{equation}
 
 where $f_n(x)$ is the Tang-Toennies damping function:
 
 \begin{equation}
 f_{n}(x)=1-e^{-x} \sum_{k=0}^{n} \frac{x^{k}}{k !}
 \end{equation}
 
 ### Parameters
 ![](Szalewicz_parameters.png) 
 
 ### Conversion Factors
 Factors of 315774.65 from atomic units to kelvins and of 0.52917720859 from 
 bohrs to angstroms were assumed.
'''

# ------------------------------------------------------------------------
def f(n,x):
    '''Tang-Toennies damping function.'''
    s1 = 0.0
    for i in range(n+1):
        s1 += x**(i)/factorials[i]
    return 1.0 - (np.exp(-x)*s1)

# ------------------------------------------------------------------------
def szalewicz_2012(r):
    '''Need to convert things to Bohr'''
    
    # convert from Angstrom to Bohr
    R = r/0.52917720859

    ε = 315774.65
    C = [0.0,
      0.0,
      0.0,
      0.000000577235,
      -0.000035322,
      0.000001377841,
      1.461830,
      0.0,
      14.12350,
      0.0,
      183.7497,
      -0.7674e2,
      0.3372e4,
      -0.3806e4,
      0.8534e5,
      -0.1707e6,
      0.286e7]
    a = 3.64890303652830
    b = 2.36824871743591
    η = 4.09423805117871
    P = [-25.4701669416621, 269.244425630616, -56.3879970402079]
    Q = [38.7957487310071, -2.76577136772754]
        
    t1 = 0.0
    for j in range(3):
        t1 += P[j]*R**j
    t1 *= np.exp(-a*R)
    
    t2 = 0.0
    for j in range(2):
        t2 += Q[j]*R**j
    t2 *= np.exp(-b*R)
    
    t3 = 0.0
    for n in range(3,17):
        t3 += f(n,η*R)*C[n]/R**n
    
    return ε*(t1+t2-t3)
