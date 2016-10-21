#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int main()
{
    for(int i=0;i<9;++i)
        fork();
    system("curl http://cs628:8080");
    return 0;
}
