#include<stdio.h>
#include<stdlib.h>
int main(){
  int t,n,i;
  scanf("%d",&t);
  while(t){
    scanf("%d",&n);
    int arr[n],count=0;
    for(i=0;i<n;i++){
      scanf("%d",&arr[i]);

      if(arr[i]%2==1){
        count++;
      }}
      if(n==2 && count==1){
        printf("2\n");
      }
      else if(count%2==0 && n%2==0){
        printf("1\n");
        }

        else if(n%2==1 && count%2==0){
          printf("1\n");
        }
      else
      printf("2\n");

  t--;
  }
}
