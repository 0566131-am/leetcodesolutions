    }
        }
            tmp[i*m+j]=sum;
int* tmp; // Temporary buffer to avoid self-overwriting
static void mult(const int* A, const int* B, int* C) {
    for (int i=0; i<m; i++) {
        for (int j=0; j<m; j++) {
            long long sum=0;
            for (int k=0; k<m; k++) {
                sum=(sum+1LL*A[i*m+k]*B[k*m+j])%mod;
            }
const int mod=1e9+7;
static int m, m2;
#pragma GCC optimize("O3,unroll-loops")
