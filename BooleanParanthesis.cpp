#include <bits/stdc++.h>
using namespace std;


class Solution{
public:

    int dp[201][201][2];
    int mod = 1003;
    
    int solve(string s, int i, int j, int isTrue){
        
        if(i > j){
            return false;
        }
        
        if(i == j){
            if(isTrue == 1){
                return s[i] == 'T';
            }
            else{
                return s[i] == 'F';
            }
        }
        
        
        if(dp[i][j][isTrue] != -1){
            return dp[i][j][isTrue];
        }
        
        int ans = 0;
        
        for(int k = i+1; k <= j-1; k = k + 2){
            
            int lt, lf, rt, rf;
            
            if(dp[i][k-1][1] != -1 ){
                lt = dp[i][k-1][1]; 
            }
            else{
                lt = solve(s,i,k-1,1);
                dp[i][k-1][1] = lt;
            }
            
            
            if(dp[i][k-1][0] != -1 ){
                lf = dp[i][k-1][0]; 
            }
            else{
                lf = solve(s,i,k-1,0);
                dp[i][k-1][0] = lf;
            }
            
            if(dp[k+1][j][1] != -1){
                rt = dp[k+1][j][1];
            }
            else{
                rt = solve(s,k+1,j,1);
                dp[k+1][j][1] = rt;
            }
            
            if(dp[k+1][j][0] != -1){
                rf = dp[k+1][j][0];
            }
            else{
                rf = solve(s,k+1,j,0);
                dp[k+1][j][0] = rf;
            }
        
            
            if(s[k] == '&'){
                if(isTrue == 1){
                    ans = (ans%mod + lt*rt%mod)%mod;
                }
                else{
                    ans = (ans%mod + lt*rf%mod + lf*rt%mod + lf*rf%mod)%mod;
                }
            }
            else if(s[k] == '|'){
                if(isTrue == 1){
                    ans = (ans%mod + lf*rt%mod + lt*rf%mod + lt*rt%mod)%mod;
                }
                else{
                    ans = (ans%mod +  lf*rf%mod)%mod;
                }
            }
            else if(s[k] == '^'){
                if(isTrue == 1){
                    ans = (ans%mod + lt*rf%mod + lf*rt%mod)%mod;
                }
                else{
                    ans = (ans%mod + lt*rt%mod + lf*rf%mod)%mod; 
                }
            }
            
        }
        
        return dp[i][j][isTrue] = ans%mod;
        
    }
    
    int countWays(int N, string S){
        for(int i = 0; i < 201; i++){
            for(int j = 0; j < 201; j++){
                for(int k = 0; k < 2; k++){
                    dp[i][j][k] = -1;
                }
            }
        }
        return solve(S,0,N-1, 1);
        
    }
};


int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        string S;
        cin>>S;
        
        Solution ob;
        cout<<ob.countWays(N, S)<<"\n";
    }
    return 0;
}