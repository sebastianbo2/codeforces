#include <bits/stdc++.h>

using namespace std;

int main() {
	
	int q;
	
	cin >> q;
	
	while (q--) {
	    
	    long a, b, n, S;
	    
	    cin >> a >> b >> n >> S;
	    
	    if (a * n + b < S) {
	        cout << "NO" << endl;
	        continue;
	    }
	    
	    if (S - ((int) S / n) * n <= b) {
	        cout << "YES" << endl;
	    } else {
	        cout << "NO" << endl;
	    }
	    
	}
	
	
// 	cout << "Hello world!";
	
    return 0;
}
