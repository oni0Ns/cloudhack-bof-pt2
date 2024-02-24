#include <stdio.h>

void fun(){
    
    asm("jmp %esp");
}

void super_secure(){
    
    char buffer[16];
        
        printf("This my super secure server\n");
        printf("Input anything and it will deny you:\n");
        scanf("%s", buffer);
        printf("Denied!!!\n");
}

int main(){
    
    super_secure();
    
    return 0;
}
