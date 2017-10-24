#include <stdio.h>
#include <stdlib.h>

int main()
{
    int g=0,m=0,b=0,puan=0,tatilan=0,tyenilen=0 ;
    while(1){
    int atilan=0,yenilen=0,devam=0 ;
       while(1){
    printf("\n Atılan Gol Sayisi: ") ;
    scanf("%d",&atilan) ;
       if(atilan>=0){
       break ;
       }
       else{
       printf("Gol sayisi sifirdan kucuk olamaz.") ;
       }
       }
       while(1){
    printf("\n Yenilen Gol Sayisi: ") ;
    scanf("%d",&yenilen) ;
       if(yenilen>=0){
       break ;
       }
       else{
       printf("Yenilen gol sayisi sifirdan kücük olamaz.") ;
       }
       }
    if(atilan > yenilen){
    puan+=3 ;
    tatilan+=atilan ;
    tyenilen +=yenilen ;
    atilan = 0 ;
    yenilen = 0 ;
    }
    else if(atilan < yenilen){
    puan+=0 ;
    tatilan+=atilan ;
    tyenilen +=yenilen ;
    atilan = 0 ;
    yenilen= 0 ;
    }
    else{
    puan+=1 ;
    tatilan+=atilan ;
    tyenilen +=yenilen ;
    atilan = 0 ;
    yenilen =0 ;
    }
    printf("Devam etmek istiyor musunuz ? [evet =1,hayir=bir tus]") ;
    scanf("%d",&devam);
    if(devam==1){
    continue ;
    }
    else{
    break ;
    }
    }
    printf(" \n Atilan toplam gol = %d",tatilan) ;
    printf(" \n Yenilen toplam gol = %d",tyenilen) ;
    printf(" \n Toplanan puan = %d ",puan) ;
    return 0;
}

