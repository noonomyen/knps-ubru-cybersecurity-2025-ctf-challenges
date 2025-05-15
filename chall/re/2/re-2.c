#include <stdio.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

uint8_t flag[] = {0x05,0x02,0x6d,0x01,0x6f,0x6e,0x76,0x06,0x67,0x06,0x47,0x4f,0x65,0x5b,0x7e,0x45,0x01,0x00,0x73,0x64,0x71,0x05,0x59,0x71,0x37};

const uint16_t flag_checksum = 1836;

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
