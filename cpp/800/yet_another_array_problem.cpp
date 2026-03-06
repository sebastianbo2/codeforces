#include <bits/stdc++.h>

using namespace std;

void solve() {
    
    vector<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53};
    
    int n;
    cin >> n;
    
    vector<long long> nums(n);
    
    vector<int> maxes(n);
    
    for (int c = 0; c < n; c++) {
        cin >> nums[c];
    }
    
    for (int i = 0; i < n; i++) {
        maxes[i] = 2;
        
        for (int p = 0; p < primes.size(); p++) {
            if (nums[i] % primes[p] == 0) {
                maxes[i] = max(maxes[i], primes[p + 1]);
            } else {
                break;
            }
        }
    }
    
    int best = maxes[0];
    
    for (int j = 0; j < n; j++) {
        best = min(best, maxes[j]);
    }
    
    cout << best << endl;
    
}

int main() {
	
	int t;
	
	cin >> t;
	
	while (t--) {
	    solve();
	}
	
    return 0;
}
