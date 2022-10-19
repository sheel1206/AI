#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    
    int dp[201][201];
    
    int solve(int n, int k){
        
        if(n == 0 or n == 1){
            return n;
        }
        
        if(k == 1){
            return n;
        }
        
        if(dp[n][k] != -1)
            return dp[n][k];
        
        int ans = INT_MAX;
        
        for(int i = 1; i <= n; i++){
            
            int top, down;
            
            if(dp[i-1][k-1] != -1){
                down = dp[i-1][k-1];
            }
            else{
                down = solve(i-1,k-1);
                dp[i-1][k-1] = down;
            }
            
            if(dp[n-i][k] != -1){
                top = dp[n-i][k];
            }
            else{
                top = solve(n-i,k);
                dp[n-i][k] = top;
            }
            
            int temp = max(down, top) + 1;
            ans = min(ans, temp);
        }
        
        return dp[n][k] = ans;
        
    }  
    
    int eggDrop(int n, int k) 
    {
        for(int i = 0; i < 201; i++){
            for(int j = 0; j < 201; j++){
                dp[i][j] = -1;
            }
        }
        
        return solve(k,n);
    }
};

int main()
{
    
    int t;
    cin>>t;
    while(t--)
    {
        
        int n, k;
        cin>>n>>k;
        Solution ob;
        
        cout<<ob.eggDrop(n, k)<<endl;
    }
    return 0;
}