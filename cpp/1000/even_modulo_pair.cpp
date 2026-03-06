#include <bits/stdc++.h>

using namespace std;

void solve() {
    
    int n;
    
    cin >> n;
    
    vector<long> a(n);
    
    for (int c = 0; c < n; c++) {
        cin >> a[c];
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if ((a[j] % a[i]) % 2 == 0) {
                cout << a[i] << " " << a[j] << endl;
                return;
            }
        }
    }
    
    cout << -1 << endl;
    
}

int main() {
	
	int t;
	
	cin >> t;
	
	while (t--) {
	    solve();
	}
	
    return 0;
}
