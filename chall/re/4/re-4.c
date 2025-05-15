#include <stdio.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

uint8_t flag[] = {
    0x03,0x38,0x2b,0x39,0x1f,0x0c,0x1d,0x17,0x38,0x79,0x1e,0x28,0x17,0x7a,0x2a,0x16,0x1a,0x76,0x1c,0x1b,0x79,0x1f,0x2f,0x1b,0x4e
};

const uint16_t flag_checksum = 2043;

bool verify() {
    uint16_t checksum = 0;
    for (size_t i = 0; i < sizeof(flag); i++) checksum += (uint16_t)(flag[i]);

    return (checksum == flag_checksum) && (flag[sizeof(flag) - 1] == 0);
}

void decrypt_flag(uint8_t pin1, uint8_t pin2) {
    for (size_t i = 0; i < sizeof(flag); i++) flag[i] = flag[i] ^ pin1 ^ pin2;
}

int main() {
    int pin1, pin2;

    printf("Enter PIN code [1]: ");
    scanf("%d", &pin1);
    printf("Enter PIN code [2]: ");
    scanf("%d", &pin2);

    if (pin1 < 0 || pin1 > 255 || pin2 < 0 || pin2 > 255) {
        printf("Invalid PIN code!\n");
        return 1;
    }

    decrypt_flag((uint8_t)(pin1), (uint8_t)(pin2));

    if (verify()) {
        printf("Access granted!\n");
        printf("This is the flag for you: re{%s}\n", (char*)(flag));
    } else {
        printf("Access denied!\n");
    }

    return 0;
}
