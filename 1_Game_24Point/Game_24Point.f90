! Fortran90
! --- utf-8 ---

! Created on Sep 17 13:30:09 2022
! @author: yinchaoyang
! version: 1.0

PROGRAM Game_24Point ! 主程序
! 24点游戏
! 输入4个数字，如果能够解出24点，给出一种解法
IMPLICIT NONE

    ! 函数定义
    DOUBLE PRECISION,EXTERNAL :: calculate    ! 两数运算
    INTEGER,EXTERNAL          :: FindSolution ! 由输入的数字找出最终的解，打印解的形式，返回是否有解
    DOUBLE PRECISION,EXTERNAL :: caseA        ! (((A_B)_C)_D)
    DOUBLE PRECISION,EXTERNAL :: caseB        ! ((A_(B_C))_D)
    DOUBLE PRECISION,EXTERNAL :: caseC        ! (A_((B_C)_D))
    DOUBLE PRECISION,EXTERNAL :: caseD        ! (A_(B_(C_D)))
    DOUBLE PRECISION,EXTERNAL :: caseE        ! ((A_B)_(C_D))

    INTEGER :: a, b, c, d
    INTEGER :: found = 0    ! 标识是否找到一组解

    print *, "Please input 4 numbers range from 1 to 10:"
    read *, a, b, c, d

    found = FindSolution(a, b, c, d)

    if(found == 0) then
        print *, "No solution for this group of numbers you input."
        print *, "Please try again."
    END if

END PROGRAM Game_24Point


FUNCTION calculate(num1, num2, mark)
IMPLICIT NONE

    DOUBLE PRECISION :: calculate
    DOUBLE PRECISION :: num1, num2
    INTEGER          :: mark

    select case(mark)
        case (1)
            calculate = num1 + num2
        case (2)
            calculate = num1 - num2
        case (3)
            calculate = num1 * num2
        case (4)
            calculate = num1 / num2
    END select
    RETURN

END FUNCTION calculate


FUNCTION FindSolution(a, b, c, d)
! 由输入的数字找出最终的解，打印解的形式，返回是否有解
IMPLICIT NONE

    ! 调用函数
    DOUBLE PRECISION,EXTERNAL :: caseA        ! (((A_B)_C)_D)
    DOUBLE PRECISION,EXTERNAL :: caseB        ! ((A_(B_C))_D)
    DOUBLE PRECISION,EXTERNAL :: caseC        ! (A_((B_C)_D))
    DOUBLE PRECISION,EXTERNAL :: caseD        ! (A_(B_(C_D)))
    DOUBLE PRECISION,EXTERNAL :: caseE        ! ((A_B)_(C_D))

    INTEGER                   :: FindSolution
    INTEGER                   :: a, b, c, d
    INTEGER                   :: found = 0
    CHARACTER                 :: mark(4)
    data                         mark / '+', '-', '*', '/' /
    INTEGER                   :: mark1, mark2, mark3 ! 3个运算符
    INTEGER                   :: numlist(4)
    DOUBLE PRECISION          :: a1, a2, a3, a4
    
    ! 先对4个数字进行全排列
    INTEGER i, j, k, m
    do i = 1, 4
        do j = 1, 4
            if(i == j) cycle
            do k = 1, 4
                if(k == i .or. k == j) cycle
                do m = 1, 4
                    if(m == i .or. m == j .or. m == k) cycle
                    numlist(i) = a
                    numlist(j) = b
                    numlist(k) = c
                    numlist(m) = d

                    a1 = DBLE(numlist(1))
                    a2 = DBLE(numlist(2))
                    a3 = DBLE(numlist(3))
                    a4 = DBLE(numlist(4))

                    ! 对每一种排列进行三个运算符的穷举
                    do mark1 = 1, 4
                        do mark2 = 1, 4
                            do mark3 = 1, 4
                                if (abs(caseA(a1, a2, a3, a4, mark1, mark2, mark3) - DBLE(24.0)) < 1e-6) then       ! (((A_B)_C)_D)
                                    print *, '(((', numlist(1), mark(mark1), numlist(2), & 
                                        ')', mark(mark2), numlist(3), ')', mark(mark3), numlist(4), ')'
                                    found = 1
                                else if (abs(caseB(a1, a2, a3, a4, mark1, mark2, mark3) - DBLE(24.0)) < 1e-6) then  ! ((A_(B_C))_D)
                                    print *, '((', numlist(1), mark(mark1), '(', numlist(2), &
                                        mark(mark2), numlist(3), '))', mark(mark3), numlist(4), ')'
                                    found = 1
                                else if (abs(caseC(a1, a2, a3, a4, mark1, mark2, mark3) - DBLE(24.0)) < 1e-6) then  ! (A_((B_C)_D))
                                    print *, '(', numlist(1), mark(mark1), '((', numlist(2), &
                                        mark(mark2), numlist(3), ')', mark(mark3), numlist(4), '))'
                                    found = 1
                                else if (abs(caseD(a1, a2, a3, a4, mark1, mark2, mark3) - DBLE(24.0)) < 1e-6) then  ! (A_(B_(C_D)))
                                    print *, '(', numlist(1), mark(mark1), '(', numlist(2), &
                                        mark(mark2), '(', numlist(3), mark(mark3), numlist(4), ')))'
                                    found = 1
                                else if (abs(caseE(a1, a2, a3, a4, mark1, mark2, mark3) - DBLE(24.0)) < 1e-6) then  ! ((A_B)_(C_D))
                                    print *, '((', numlist(1), mark(mark1), numlist(2), ')', &
                                        mark(mark2), '(', numlist(3), mark(mark3), numlist(4), '))'
                                    found = 1
                                END if
                                if (found == 1) exit
                            END do
                            if (found == 1) exit
                        END do
                        if (found == 1) exit
                    END do
                    if (found == 1) exit
                END do
                if (found == 1) exit
            END do
            if (found == 1) exit
        END do
        if (found == 1) exit
    END do

    FindSolution = found
    RETURN

END FUNCTION FindSolution


! 24点游戏中，总共有4个数和三个运算符。
! 若考虑用括号消除运算符优先级的影响，可采用完全括号表达式。
! 一共有以下5种情况：
! - (((A_B)_C)_D)
! - ((A_(B_C))_D)
! - (A_((B_C)_D))
! - (A_(B_(C_D)))
! - ((A_B)_(C_D))
! 以下五个函数caseA、caseB、caseC、caseD、caseE讨论以上5种加括号情况

FUNCTION caseA(a, b, c, d, mark1, mark2, mark3) ! (((A_B)_C)_D)
IMPLICIT NONE

    ! 函数调用
    DOUBLE PRECISION,EXTERNAL :: calculate

    DOUBLE PRECISION          :: caseA
    DOUBLE PRECISION          :: a, b, c, d
    INTEGER                   :: mark1, mark2, mark3

    DOUBLE PRECISION          :: temp1, temp2 ! 临时存储中间两步计算过程的值

    temp1 = calculate(a, b, mark1)
    temp2 = calculate(temp1, c, mark2)
    caseA = calculate(temp2, d, mark3)

    RETURN
END FUNCTION


FUNCTION caseB(a, b, c, d, mark1, mark2, mark3) ! ((A_(B_C))_D)
IMPLICIT NONE

    ! 函数调用
    DOUBLE PRECISION,EXTERNAL :: calculate

    DOUBLE PRECISION          :: caseB
    DOUBLE PRECISION          :: a, b, c, d
    INTEGER                   :: mark1, mark2, mark3

    DOUBLE PRECISION          :: temp1, temp2 ! 临时存储中间两步计算过程的值

    temp1 = calculate(b, c, mark2);
    temp2 = calculate(a, temp1, mark1);
    caseB = calculate(temp2, d, mark3);

    RETURN
END FUNCTION


FUNCTION caseC(a, b, c, d, mark1, mark2, mark3) ! (A_((B_C)_D))
IMPLICIT NONE

    ! 函数调用
    DOUBLE PRECISION,EXTERNAL :: calculate

    DOUBLE PRECISION          :: caseC
    DOUBLE PRECISION          :: a, b, c, d
    INTEGER                   :: mark1, mark2, mark3

    DOUBLE PRECISION          :: temp1, temp2 ! 临时存储中间两步计算过程的值

    temp1 = calculate(b, c, mark2);
    temp2 = calculate(temp1, d, mark3);
    caseC = calculate(a, temp2, mark1);

    RETURN
END FUNCTION


FUNCTION caseD(a, b, c, d, mark1, mark2, mark3) ! (A_(B_(C_D)))
IMPLICIT NONE

    ! 函数调用
    DOUBLE PRECISION,EXTERNAL :: calculate

    DOUBLE PRECISION          :: caseD
    DOUBLE PRECISION          :: a, b, c, d
    INTEGER                   :: mark1, mark2, mark3

    DOUBLE PRECISION          :: temp1, temp2 ! 临时存储中间两步计算过程的值

    temp1 = calculate(c, d, mark3);
    temp2 = calculate(b, temp1, mark2);
    caseD = calculate(a, temp2, mark1);

    RETURN
END FUNCTION


FUNCTION caseE(a, b, c, d, mark1, mark2, mark3) ! ((A_B)_(C_D))
IMPLICIT NONE

    ! 函数调用
    DOUBLE PRECISION,EXTERNAL :: calculate

    DOUBLE PRECISION          :: caseE
    DOUBLE PRECISION          :: a, b, c, d
    INTEGER                   :: mark1, mark2, mark3

    DOUBLE PRECISION          :: temp1, temp2 ! 临时存储中间两步计算过程的值

    temp1 = calculate(a, b, mark1);
    temp2 = calculate(c, d, mark3);
    caseE = calculate(temp1, temp2, mark2);

    RETURN
END FUNCTION