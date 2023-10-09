#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define MAX_DIGITS 1000

bool is_prime(int num[], int len) {
    int i, j;

    if (len == 1 && num[0] <= 1) {
        return false;
    }

    for (i = 2; i <= len; i++) {
        if (num[len - i] != 0) {
            break;
        }
    }

    if (i > len) {
        return false;
    }

    for (j = 2; j <= i / 2; j++) {
        if (i % j == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    char str[MAX_DIGITS + 1];
    int num[MAX_DIGITS];
    int len, i;

    printf("Enter a large integer: ");
    fgets(str, MAX_DIGITS + 1, stdin);


    len = strlen(str) - 1;


    for (i = 0; i < len; i++) {
        num[i] = str[i] - '0';
    }

    if (is_prime(num, len)) {
        printf("The number is prime.\n");
    } else {
        printf("The number is not prime.\n");
    }

    return 0;
}


