#include <stdio.h>
int main () {
int i, j;
for(i = 2; i<1000000000; i++) {
for(j = 2; j <= (i/j); j++)
if(!(i%j)) break;
if(j > (i/j)) printf("%d asaldır\n", i);
}
return 0;
}
