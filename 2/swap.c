#include <stdio.h>

void swap(int *a, int *b) {
    if (a == b) return ;
    int temp = 0;

    temp = *a;
    *a = *b;
    *b = temp;
}

void xor_swap(int *a, int *b) {
    if (a == b) return ;
    *a ^= *b;
    *b ^= *a;
    *a ^= *b;
}

int main(void) {
    int a = 1;
    int b = 2;

    printf("%d %d\n", a, b);
    // swap(&a, &b);
    // xor_swap(&a, &b);
    printf("%d %d\n", a, b);
}
