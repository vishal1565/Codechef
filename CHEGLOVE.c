#include<stdio.h>

int main(){
        int t,n,f=0,b=0;
        scanf("%d",&t);
        while(t--){
               scanf("%d",&n);
               long long int glove[n],finger[n];
               for(int i=0;i<n;i++){
                        scanf("%lld",&finger[i]);
               }
               for(int i=0;i<n;i++){
                        scanf("%lld",&glove[i]);
                        if(glove[i]<finger[i]){f++;}
                        if(glove[i]<finger[n-1-i]){b++;}
               }/*
               for(int i=n-1;i>=0;i--){
                        if(glove[i]<finger[n-i-1]){b++;}
                        break;
               }*/
               if(f==0 && b==0){
                        printf("both\n");
               }
               else if(f!=0 && b==0){
                        printf("back\n");
                        f=0;
               }
               else if(f==0 && b!=0){
                        printf("front\n");
                        b=0;
               }
               else if(f!=0 && b!=0){
                        printf("none\n");
                        f=0;
                        b=0;
               }
        }
        return 0;
}
