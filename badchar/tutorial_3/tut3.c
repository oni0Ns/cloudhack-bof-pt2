#include <stdio.h>
#include <string.h>

void bad_word_guesser(){
    char buffer[16];

    printf("Welcome to word guesser:\n");
    printf("Input word: ");
    scanf("%s", buffer);

}

int main(){
    bad_word_guesser();

    return 0;
}