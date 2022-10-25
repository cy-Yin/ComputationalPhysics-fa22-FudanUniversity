# include <stdio.h>
# include <math.h>

double calculate(double num1, double num2, int mark); // ��������
int FindSolution(int a, int b, int c, int d); // ������������ҳ����յĽ⣬��ӡ�����ʽ�������Ƿ��н�
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

    if (found == 0) // û���ҵ���
    {
        printf("No solution for this group of numbers you input.\n");
        printf("Please try again.");
    }

    return 0;
}

double calculate(double num1, double num2, int mark) // ��������
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

int FindSolution(int a, int b, int c, int d) // ������������ҳ����յĽ⣬��ӡ�����ʽ�������Ƿ��н�
{
    int found = 0;

    int mark1, mark2, mark3; // ����3�������

    // ��4��������ȫ����
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

                    // ��ÿһ�����н�����������������
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
    24����Ϸ�У��ܹ���4�����������������
    ������������������������ȼ���Ӱ�죬�ɲ�����ȫ���ű��ʽ��
    һ��������5�������
    - (((A_B)_C)_D)
    - ((A_(B_C))_D)
    - (A_((B_C)_D))
    - (A_(B_(C_D)))
    - ((A_B)_(C_D))
    �����������caseA��caseB��caseC��caseD��caseE��������5�ּ��������
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