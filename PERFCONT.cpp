#include<iostream>
using namespace std;
int main(){
long long int hard,cakewalk,t,temp;
long long int n,p;
cin>>t;
while(t--){
    hard = cakewalk = 0;
    cin>>n;
    cin>>p;
    while(n--){
        cin>>temp;
        if(temp<=(p/10))
            hard++;
        if(temp>=(p/2))
            cakewalk++;
    }
    if(hard==2 && cakewalk ==1){
        cout<<"yes"<<endl;
    }
    else{
        cout<<"no"<<endl;
    }
}
return 0;
}
