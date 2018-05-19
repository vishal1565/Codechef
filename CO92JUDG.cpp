#include<iostream>
#include<algorithm>
using namespace std;
int main(){
  int t;
  cin>>t;
  while(t--){
    int n,max,alice=0,bob=0;
    cin>>n;
    int a[n],b[n];
    cin>>a[0];
    max=a[0];
    alice=a[0];
    for(int i=1;i<n;i++){
      cin>>a[i];
      alice+=a[i];
      if(max<a[i]){
        max=a[i];
      }
    }
    alice=alice-max;
    cin>>b[0];
    max=b[0];
    bob=b[0];
    for(int i=1;i<n;i++){
      cin>>b[i];
      bob+=b[i];
      if(max<b[i]){
        max=b[i];
      }
    }
    bob-=max;
    if(bob<alice){
      cout<<"Bob"<<endl;
    }
    else if(bob>alice){
      cout<<"Alice"<<endl;
    }
    else{
      cout<<"Draw"<<endl;
    }
  }
}
