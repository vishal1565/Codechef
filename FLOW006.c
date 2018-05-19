#include<stdio.h>
#include<stdlib.h>

int main()
{
	int t,no,sum=0;
	scanf("%d",&t);
	while(t!=0){
	scanf("%d",&no);
	while(no!=0){
	sum=(no%10)+sum;no=no/10;}
	printf("\n%d",sum);sum=0;
	t--;}
	return 0;
}
