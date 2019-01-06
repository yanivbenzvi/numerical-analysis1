![alt text](https://i.stack.imgur.com/8mSol.png)

# User-Guide : Numerical-Analysis-Project
This project is part of academic course - Numerical-Analysis in [SCE - Shamoon College of Engineering](https://sce.ac.il).

This project is contain mathematics method that we learned and used in order to solve numerical analysis problems. 

#### Roots approximation methods:
1. The Bisection method.
2. Newton Raphson method
3. Secant method.

#### Approximation methods:
1. Poly Approximation
2. Linear Approximation
3. LaGrange
4. Neville
5. Cubic Spline
6. Vandermonde

#### Matrix approximation methods:
1. Gauss Siedle
2. Gauss elimination
3. Jacobi
4. SOR - Successive Over Relaxation

#### Integrals approximation methods:
1. Romberg
2. Simpson
3. Trapezoid
4. Gaussian Quadrature

### Prerequisites

system requirements:

* [Python](https://www.python.org/downloads/) >= 3.7
* [scipy](https://www.scipy.org/)
* [NumPy](http://www.numpy.org/) 

Open folder for this project and clone this repository use follow command:
```
git clone git@github.com:yanivbenzvi/numerical-analysis1.git
```

After Python installion, open cmd and navigate to project folder and run the follow command.:
```
python pip install -r requirements.txt
```

### Project Structure 

The tree below displays the main files and folders structure.
```textile
├── docs                                // docs folder
├── lib                                 // code libary for the math calculation function.
|   ├── Bisection_method.py
|   ├── GaussSiedle_SOR.py
|   ├── NewtonRephson_method
|   ├── plot_it.py
|   ├── Hackathon.py                # Unnecessary
|   ├── Poly_aprox.py
|   ├── Linear aprox.py
|   ├── CubicSpline_method.py
|   ├── LaGrange_method.py          # Unnecessary
|   ├── Lagrange
|   ├── Neville_method.py
|   ├── Romberg_method.py
|   ├── Simpson_method.py
|   ├── Trapezoid_method.py
|   ├── Gauss elimination.py
|   ├── Jacobi.py
|   ├── Main.py
|   ├── Gaussian Quadrature.py
|   └── Secant_method.py
├── test                                // test folder
|   ├── Bisection_method.py
|   ├── GaussSiedle_SOR.py
|   ├── NewtonRephson_method
|   ├── plot_it.py
|   ├── Hackathon.py                # Unnecessary
|   ├── Poly_aprox.py
|   ├── Linear aprox.py
|   ├── CubicSpline_method.py
|   ├── LaGrange_method.py          # Unnecessary
|   ├── Lagrange
|   ├── Neville_method.py
|   ├── Romberg_method.py
|   ├── Simpson_method.py
|   ├── Trapezoid_method.py
|   ├── Gauss elimination.py
|   ├── Jacobi.py
|   ├── Main.py
|   ├── Gaussian Quadrature.py
|   └── Secant_method.py
├── main.py                             // main file
├── requirements.txt                    // Project requirements - installation by python pip.
├── .gitignore                          // Files to not track in git.
```
#Running the test
This project contain unit test for every method we use.
The tests is based on analytic solution.
In order to run the tests we used Pycharm ide.
```
test folder > right click > Run 'nosetest in test'
or
ctrl + shift + F10
```
## Authors

- **[Yaniv Ben Zvi](https://github.com/yanivbenzvi)** 
- **[Boris Leviken](https://github.com/Borisl90)** 
- **[Shiri Rom](https://github.com/shiro1000)**
- **[Omri Elmalam](https://github.com/Omrielmalam)** 
- **[Liron Glickman](https://github.com/LironGlickman)**
- **[Nizan Rosh](https://github.com/nizanrosh)**

##Acknowledgments

