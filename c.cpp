#include <bits/stdc++.h>
#include <string.h>
#define ll long long
using namespace std;

int main() {
  ll T;
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    ll l,r,a,b;
    cin>>l>>r;
    string s;
    cin>>s;
    int count =0;
    for(int a=1;a<=r;a++){
        cin>>a>>b;
        string r=s.substr(a-1,b-a);
        string P = r;
        reverse(P.begin(), P.end());
        if (r == P) {
         count++;}
    }
    
    cout << "Case #" << tc << ": " <<count<< endl;
  }
  return 0;
}