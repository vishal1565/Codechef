#include<stdio.h>

int main(){
  int t;
  scanf("%d",&t);
  while(t--){
    int n,i,c,d,s,max=0;
    double res;
    scanf("%d",&n);
    int arr[n];
    for(i=0;i<n;i++){
      scanf("%d",&arr[i]);
      if(max<arr[i]){max=arr[i];}
    }
    scanf("%d%d%d",&c,&d,&s);
    res=((double)max*(c-1));
    printf("%lf\n",res);
  }
}
