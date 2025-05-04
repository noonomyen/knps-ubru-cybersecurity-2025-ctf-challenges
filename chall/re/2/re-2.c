#include <stdio.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

uint8_t flag[] = {
    0x66, 0x2e, 0x2c,
    0x41, 0x76, 0x2a,
    0x2b, 0x41, 0x26,
    0x2f, 0x2f, 0x70,
    0x7a, 0x41, 0x2b,
    0x6e, 0x2e, 0x29,
    0x2b, 0x41, 0x2f,
    0x78, 0x41, 0x2e,
    0x26, 0x2b, 0x2d,
    0x2c, 0x68, 0x2d,
    0x7a, 0x1e
};

const uint16_t flag_checksum = 2265;

bool verify() {
    uint16_t checksum = 0;
    for (size_t i = 0; i < sizeof(flag); i++) checksum += (uint16_t)(flag[i]);

    return (checksum == flag_checksum) && (flag[sizeof(flag) - 1] == 0);
}

void decrypt_flag(uint8_t pin) {
    for (size_t i = 0; i < sizeof(flag); i++) flag[i] ^= pin;
}

int main() {
    int pin;

    printf("Enter PIN code: ");
    scanf("%d", &pin);

    if (pin < 0 || pin > 255) {
        printf("Invalid PIN code!\n");
        return 1;
    }

    decrypt_flag((uint8_t)(pin));

    if (verify()) {
        printf("Access granted!\n");
        printf("This is the flag for you: re{%s}\n", (char*)(flag));
    } else {
        printf("Access denied!\n");
    }

    return 0;
}
