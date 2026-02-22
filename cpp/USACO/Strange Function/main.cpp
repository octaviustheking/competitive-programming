#include<bits/stdc++.h>
using namespace std;
const long long MOD=1e9+7;
const long long inv2=500000004;
int main(){
    int T;scanf("%d",&T);
    while(T--){
        static char s[200005];
        scanf("%s",s);
        int n=strlen(s);
        bool allbin=true;
        for(int i=0;i<n;i++)if(s[i]!='0'&&s[i]!='1'){allbin=false;break;}
        int extra=allbin?0:1;
        long long b=0;
        int parity=0;
        bool started=false;
        for(int i=0;i<n;i++){
            int d=s[i]-'0';
            int nd=allbin?d:(d%2);
            if(!started&&nd==0)continue;
            started=true;
            b=(b*2+nd)%MOD;
            parity=nd;
        }
        long long g=(3*b%MOD-parity+MOD)%MOD*inv2%MOD;
        printf("%lld\n",(extra+g)%MOD);
    }
}