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
        printf("This is the flag for you: re{7h3_c47_15_5p1nn1n999999}\n");
    } else {
        printf("Access denied!\n");
    }
    return 0;
}
