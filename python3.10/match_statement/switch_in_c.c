#include <stdio.h>  
int main()  
{  
    char lang_prefix = 'P';
    switch(lang_prefix)  
    {  
        case 'P':   
        printf("PYTHON \n");  
        break;   
        case 'R':   
        printf("RUST \n");  
        break;  
        default:   
        printf("WRONG ANSWER \n");  
    }            
}
