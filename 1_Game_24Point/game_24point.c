# include <stdio.h>
# include <math.h>

double calculate(double num1, double num2, int mark); // 两数运算
int FindSolution(int a, int b, int c, int d); // 由输入的数字找出最终的解，打印解的形式，返回是否有解
double caseA(double a, double b, double c, double d, int mark1, int mark2, int mark3); // (((A_B)_C)_D)
double caseB(double a, double b, double c, double d, int mark1, int mark2, int mark3); // ((A_(B_C))_D)
double caseC(double a, double b, double c, double d, int mark1, int mark2, int mark3); // (A_((B_C)_D))
double caseD(double a, double b, double c, double d, int mark1, int mark2, int mark3); // (A_(B_(C_D)))
double caseE(double a, double b, double c, double d, int mark1, int mark2, int mark3); // ((A_B)_(C_D))

const double GOAL = 24.00;
const double EPSILON = 1e-6;
const char *mark[4] = {"+", "-", "*", "/"};

int main(void)
{
    int a, b, c, d;
    int found = 0;

    printf("Please input 4 numbers range from 1 to 10:");
    scanf("%d %d %d %d", &a, &b, &c, &d);
    found = FindSolution(a, b, c, d);

    if (found == 0) // 没有找到解
    {
        printf("No solution for this group of numbers you input.\n");
        printf("Please try again.");
    }

    return 0;
}

double calculate(double num1, double num2, int mark) // 两数运算
{
    double result;
    switch(mark)
    {
        case 0: result = num1 + num2; break;
        case 1: result = num1 - num2; break;
        case 2: result = num1 * num2; break;
        case 3: result = num1 / num2; break;
    }

    return result;
}

int FindSolution(int a, int b, int c, int d) // 由输入的数字找出最终的解，打印解的形式，返回是否有解
{
    int found = 0;

    int mark1, mark2, mark3; // 定义3个运算符

    // 对4个数进行全排列
    int num[4];
    double a1, a2, a3, a4;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (i == j) continue;
            for (int k = 0; k < 4; k++)
            {
                if (k == i || k == j) continue;
                for (int m = 0; m < 4; m++)
                {
                    if (m == i || m == j || m == k) continue;
                    num[i] = a;
                    num[j] = b;
                    num[k] = c;
                    num[m] = d;

                    a1 = (double)num[0];
                    a2 = (double)num[1];
                    a3 = (double)num[2];
                    a4 = (double)num[3];

                    // 对每一种排列进行三个运算符的穷举
                    for (mark1 = 0; mark1 < 4; mark1++)
                    {
                        for (mark2 = 0; mark2 < 4; mark2++)
                        {
                            for (mark3 = 0; mark3 < 4; mark3++)
                            {
                                if (fabs(caseA(a1, a2, a3, a4, mark1, mark2, mark3) - GOAL) < EPSILON) // (((A_B)_C)_D)
                                {
                                    printf("(((%d %s %d) %s %d) %s %d)\n", num[0], mark[mark1], num[1], mark[mark2], num[2], mark[mark3], num[3]);
                                    found = 1;
                                }
                                else if (fabs(caseB(a1, a2, a3, a4, mark1, mark2, mark3) - GOAL) < EPSILON) // ((A_(B_C))_D)
                                {
                                    printf("((%d %s (%d %s %d)) %s %d)\n", num[0], mark[mark1], num[1], mark[mark2], num[2], mark[mark3], num[3]);
                                    found = 1;
                                }
                                else if (fabs(caseC(a1, a2, a3, a4, mark1, mark2, mark3) - GOAL) < EPSILON) // (A_((B_C)_D))
                                {
                                    printf("(%d %s ((%d %s %d) %s %d))\n", num[0], mark[mark1], num[1], mark[mark2], num[2], mark[mark3], num[3]);
                                    found = 1;
                                }
                                else if (fabs(caseD(a1, a2, a3, a4, mark1, mark2, mark3) - GOAL) < EPSILON) // (A_(B_(C_D)))
                                {
                                    printf("(%d %s (%d %s (%d %s %d)))\n", num[0], mark[mark1], num[1], mark[mark2], num[2], mark[mark3], num[3]);
                                    found = 1;
                                }
                                else if (fabs(caseE(a1, a2, a3, a4, mark1, mark2, mark3) - GOAL) < EPSILON) // ((A_B)_(C_D))
                                {
                                    printf("((%d %s %d) %s (%d %s %d))\n", num[0], mark[mark1], num[1], mark[mark2], num[2], mark[mark3], num[3]);
                                    found = 1;
                                }
                                if (found == 1) break;
                            }
                            if (found == 1) break;
                        }
                        if (found == 1) break;
                    }
                    if (found == 1) break;
                }
                if (found == 1) break;
            }
            if (found == 1) break;
        }
        if (found == 1) break;
    }

    return found;
}


/*
    24点游戏中，总共有4个数和三个运算符。
    若考虑用括号消除运算符优先级的影响，可采用完全括号表达式。
    一共有以下5种情况：
    - (((A_B)_C)_D)
    - ((A_(B_C))_D)
    - (A_((B_C)_D))
    - (A_(B_(C_D)))
    - ((A_B)_(C_D))
    以下五个函数caseA、caseB、caseC、caseD、caseE讨论以上5种加括号情况
*/

double caseA(double a, double b, double c, double d, int mark1, int mark2, int mark3) // (((A_B)_C)_D)
{
    double result;

    double temp1, temp2;
    temp1 = calculate(a, b, mark1);
    temp2 = calculate(temp1, c, mark2);
    result = calculate(temp2, d, mark3);

    return result;
}

double caseB(double a, double b, double c, double d, int mark1, int mark2, int mark3) // ((A_(B_C))_D)
{
    double result;

    double temp1, temp2;
    temp1 = calculate(b, c, mark2);
    temp2 = calculate(a, temp1, mark1);
    result = calculate(temp2, d, mark3);

    return result;
}

double caseC(double a, double b, double c, double d, int mark1, int mark2, int mark3) // (A_((B_C)_D))
{
    double result;

    double temp1, temp2;
    temp1 = calculate(b, c, mark2);
    temp2 = calculate(temp1, d, mark3);
    result = calculate(a, temp2, mark1);

    return result;
}

double caseD(double a, double b, double c, double d, int mark1, int mark2, int mark3) // (A_(B_(C_D)))
{
    double result;

    double temp1, temp2;
    temp1 = calculate(c, d, mark3);
    temp2 = calculate(b, temp1, mark2);
    result = calculate(a, temp2, mark1);

    return result;
}

double caseE(double a, double b, double c, double d, int mark1, int mark2, int mark3) // ((A_B)_(C_D))
{
    double result;

    double temp1, temp2;
    temp1 = calculate(a, b, mark1);
    temp2 = calculate(c, d, mark3);
    result = calculate(temp1, temp2, mark2);

    return result;
}