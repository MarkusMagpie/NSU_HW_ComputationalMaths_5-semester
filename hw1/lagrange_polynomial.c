#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double computeLagrange(double x, int n, double nodes[], double values[]) {
    double result = 0.0;

    for (int i = 0; i < n; i++) {
        double tmp = values[i];
        for (int j = 0; j < n; j++) {
            if (j != i) {
                tmp *= (x - nodes[j]) / (nodes[i] - nodes[j]);
            }
        }

        result += tmp;
    }

    return result;
}

int main(int argc, char *argv[]) {
    double h = atof(argv[1]);
    double a = -1.0;
    double b = 1.0;
    int n = (int)((b - a) / h) + 1;
    

    double nodes[n];
    double values[n];

    // заполнение узлов (x_i) и значений функции (f(x_i))
    for (int i = 0; i < n; i++) {
        nodes[i] = a + i * h;
        values[i] = fabs(nodes[i]);
    }

    // пример вычисления для конкретного x
    double x = 0.3;
    double lagrangeValue = computeLagrange(x, n, nodes, values);
    printf("L_%d(x = %.1f) = %.6f\n", n, x, lagrangeValue);

    return 0;
}