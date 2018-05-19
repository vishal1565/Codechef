#include<iostream>
using namespace std;
int main(){
  int n,w,wp,r,rp;
  bool valid= true;
  cin>>n;
  cin>>rp>>wp;
  n--;
  while(n--){
    cin>>r>>w;
    if(wp==10){valid=false;}
    if(r<rp || w<wp){
      valid = false;
    }
    wp=w;
    rp=r;
  }
  if(valid){
    cout<<"YES"<<endl;
  }
  else{
    cout<<"NO"<<endl;
  }
  return 0;
}
