#include <stdio.h>
#include <stdlib.h>
//BilLAb dersi kum saati 
int main()
{
int x ;
label: printf("Pozitif bir tek sayi giriniz :") ;
scanf("%d",&x) ;
if(x>0 && x%2==1){
for(int i=1 ;i<=((x+1)*0.5) ;i++){
   for(int j=1 ;j<=i-1 ;j++){
   printf("   ") ;
   }
   for(int j=0 ; j<=(x-((2*i)-1)) ;j++){
   printf(" X ") ;
   }
printf("\n");
}
for(int i=1 ;i<=(x+1)*0.5; i++){
   for(int j=(x+1)*0.5 ;j>i ;j--){
   printf("   ") ;
   }
   for(int j=1 ;j<=(2*i)-1 ; j++){
   printf(" X ") ;
   }
printf("\n");
}
}
else {
goto label ;
}
}


