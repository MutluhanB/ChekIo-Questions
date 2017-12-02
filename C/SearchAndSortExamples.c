//Mutluhan Boz 02.12.2017
#include <stdio.h>
#include <math.h>
void selectionSort(int x[]){
int temp ;
    for(int i=0;i<10;i++){
        for(int j=0;j<10;j++){
            if(x[i]<x[j]){
                temp = x[i];
                x[i] = x[j];
                x[j] = temp;
            }
        }
    }
}
void diziYaz(int x[]){
    for(int i=0;i<10;i++){
        printf("%d\t",x[i]);
    }
}
void linearSearch(int x[],int aranan){
int yer=-1;
    for(int i=0;i<10;i++){
        if(x[i]==aranan){
            yer=i;
        }
    }
    if(yer!=-1){
       printf("\n \n%d elemani dizinin %d. indexindedir.",aranan,yer);
    }
    else{
        printf("\n \n%d elemani dizide mevcut degil !",aranan);
    }
}
int binarySearch(int x[],int aranan,int uzunluk){
int alt=0;
int ust=uzunluk-1;
int orta=1;
        while(alt<=ust){
        orta=(alt+ust)/2;
        if(x[orta]==aranan){
            return orta;
        }
        if(x[orta]>aranan){
            ust=orta-1;
        }
        else{
            alt=orta+1;
        }
        }
        while(alt>ust){
            return 11;
        }
}
void bubleSort(int x[]){
int pass,mov,temp;
    for(pass=1;pass<10;pass++){
        for(mov=0;mov<10-1;mov++){
            if(x[mov]>x[mov+1]){
                temp=x[mov];
                x[mov]=x[mov+1];
                x[mov+1]=temp;
            }
        }
    }
}
void main(){
int n,arananSayi;
int x[]={6,3,1,5,7,9,10,2,14,11};
printf("\t \t \t \t--UNSORTED-- \n ") ;
diziYaz(x);
printf("\n \t \t \t \tLinear Search") ;
printf("\n Lineer Search ile aramak istediginiz elemani giriniz :");
scanf("%d",&n);
linearSearch(x,n);
printf("\n \t \t \t \t--BUBLE SORTED--- \n") ;
bubleSort(x);
diziYaz(x);
printf("\n !!TEKRAR KARIÞTIRILIYOR!!\n");
printf("\t \t \t \t--UNSORTED-- \n ") ;
int x2[]={6,3,1,5,7,9,10,2,14,11};
diziYaz(x2);
printf("\n \t \t \t \t--SELECTION SORTED--- \n") ;
selectionSort(x2);
diziYaz(x);
printf("\n \t \t \t \tLinear Search") ;
printf("\n Lineer Search ile aramak istediginiz elemani giriniz :");
scanf("%d",&n);
linearSearch(x,n);
printf("\n \t \t \t \tBinary Search") ;
printf("\nBinary search ile dizi icinde aramak istediginiz elemani giriniz : ");
scanf("%d",&n);
arananSayi=binarySearch(x,n,10);
while(arananSayi<10){
    printf("\n%d elemani dizinin %d. indexindedir.",n,arananSayi);
    break;
}
while(arananSayi>=10){
    printf("\n %d elemani dizide mevcut degildir !",n);
    break;
}



}

