#include<stdio.h>
#include<stdlib.h>

int main()
{
	int t,n,q;
	scanf("%d",&t);
	while(t!=0){
		scanf("%d%d",&n,&q);
		int d,i;long long int div=1;
		for(i=0;i<n;i++)
		{
			scanf("%d",&d);
			div=div*d;
		}
		int x;
		for(i=0;i<q;i++){
			scanf("%d",&x);
			x=x/div;
			printf("%d ",x);
		}
		printf("\n");
		t--;
	}
	return 0;
}
