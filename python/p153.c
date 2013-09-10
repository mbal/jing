#define LIM 100000000
#include <time.h>
#include <stdio.h>
#include <math.h>

int gcd(int a, int b) {
    int tmp;
    while (b != 0) {
        tmp = b;
        b = a % b;
        a = tmp;
    }
    return a;
}

int main(void) {
    int a, b, j, m, val;
    unsigned long long int c = 0;
    int MAX = (int)sqrt(LIM);
    for (a = 1; a <= LIM; a++) {
        c += a * (LIM / a);
    }
    for (a = 1; a < MAX; a++) {
        for (b = 1; b < MAX; b++) {
            if (gcd(a, b) != 1)
                continue;
            j = 1;
            m = a*a + b*b;
            if (m > LIM) break;
            val = a << 1;
            while (j * m <= LIM) {
                c += val * j * (LIM / (j * m));
                j += 1;
            }
        }
    }
    printf("%llu\n", c);
    printf("time: %.3lf secs.", (double)(clock()/CLOCKS_PER_SEC));
    return 0;
}

