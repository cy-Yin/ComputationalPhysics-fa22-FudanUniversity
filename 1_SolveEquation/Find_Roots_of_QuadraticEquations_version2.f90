! Fortran90

! Created on Sep 13 14:58:45 2022
! @author: yinchaoyang
! version: 2.0

PROGRAM Find_Roots_of_Quadratic_Equations
! Finds the roots of quadractic equations
! with the given parameters a, b and c.
IMPLICIT NONE
    REAL :: a, b, c
    REAL :: q, root, root1, root2
    PRINT *, 'Please input 3 numbers as parameters of the equation: a * x^2 + b * x + c = 0:'
    READ *, a, b, c
    
    if(a == 0) then
        if(b == 0) then
            if(c == 0) then
                print*, 'Any real x satisfies the equation.'
            else
                print *, 'No real solution(s) have been found. Please try again.'
            end if
        else
            root = -c / b
            print*, 'root = ', root
        end if
    else
        if(b*b - 4 * a * c >= 0) then
            ! Uses the formula to seek the roots.
            ! In version 1.0, we have ignored the Calculation Error the Floating Point Number brings.
            ! Now we rewrite the expression.
            q = - 1.0 / 2 * (b + sign(1.0, b) * sqrt(b*b - 4 * a * c))
            root1 = q / a
            root2 = c / q
            print *, 'root1 = ', root1, 'root2 = ', root2 
        else
            print *, 'No real solution(s) have been found. Please try again.'
        end if
    end if

END PROGRAM Find_Roots_of_Quadratic_Equations