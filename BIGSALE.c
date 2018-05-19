#include<stdio.h>
 int main(){
        int t,n,i;
        double loss=0.0,temp;
        scanf("%d",&t);
        while(t--){
                scanf("%d",&n);
                int cp,q,dis;
                for(i=0;i<n;i++){
                        scanf("%d%d%d",&cp,&q,&dis);
                        temp=cp;
                        temp=temp+(temp*dis/100);
                        loss=loss+(q*(cp-temp+(temp*dis/100)));
                }
                printf("%f\n",loss);
                loss=0.0;
        }
        return 0;
 }
