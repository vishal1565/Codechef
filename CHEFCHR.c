#include<stdio.h>
#include<string.h>

int main(){
  int t,len,i,j,count=0;
  char str[500000];
  scanf("%d",&t);
  while(t){
    scanf("%s",&str);
    len=strlen(str);
    int c=0,h=0,e=0,f=0;
    if(len<=3){printf("normal\n");}
    else{
      for(i=0;i<len-3;i++){
        for(j=0;j<4;j++){
          switch (str[i+j]){
            case 'c':
            c=1;break;
            case 'h':
            h=1;break;
            case 'e':
            e=1;break;
            case 'f':
            f=1;break;
          }
        }
        if(c*h*e*f!=0){count++;}
        c=0;h=0;e=0;f=0;
      }
      if(count!=0){printf("lovely %d\n",count);}
      else{printf("normal\n");}
      count=0;
    }

    t--;
  }
  return 0;
} 
