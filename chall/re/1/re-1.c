#include <stdio.h>
#include <string.h>

int main() {
    const char password[] = "OIIAIOIIIAI";
    char input[64];

    printf("Enter the password: ");
    fgets(input, sizeof(input), stdin);

    input[strcspn(input, "\n")] = '\0';

    if (strcmp(input, password) == 0) {
        printf("Access granted!\n");
        printf("This is the flag for you: re{zbCMD2NqhYL2zoER47OoWhJ3}\n");
    } else {
        printf("Access denied!\n");
    }
    return 0;
}
