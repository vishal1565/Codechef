#include<iostream>
#include<algorithm>
using namespace std;

int main(){
	int t,steps;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		long int a[n];
		for(int i=0;i<n;i++){
			cin>>a[i];
		}
		sort(a,a+n);
		steps=0;
		for(int i=1;i<n;i++){
			if(a[i]==a[i-1]){
				steps++;
			}
		}
		cout<<steps<<endl;
		steps=0;
	}
}
