#include<iostream>
#include<algorithm>
using namespace std;

int main(){
  int n;
  cin>>n;
  int a[n];
  for(int i=0;i<n;i++){
    cin>>a[i];
  }
  long long int energy=0;
  sort(a,a+n);
  for(int i=1;i<n;i++){
    energy+=a[i-1]*a[i];
  }
  cout<<energy<<endl;
}
