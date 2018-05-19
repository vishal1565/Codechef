#include<stdio.h>
#include<stdlib.h>

int main()
{
	int t,no,temp,sum;
	scanf("%d",&t);
	while(t!=0){
	scanf("%d",&no);
	sum=no%10;
	while(no!=0){
	if(no/10==0)
	{sum=sum+(no%10);}
	no=no/10;}
	printf("\n%d",sum);sum=0;
	t--;}
	return 0;
} 
