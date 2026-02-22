#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int times;
    cin >> times;

    while (times--) {
        int n, m;
        long long h;
        cin >> n >> m >> h;

        vector<long long> original(n);
        for (int i = 0; i < n; i++) cin >> original[i];

        vector<long long> a(n);
        vector<int> last_update(n, 0);

        int version = 1;

        for (int i = 0; i < m; i++) {
            int index;
            long long add;
            cin >> index >> add;
            index--;

            long long current = (last_update[index] == version ? a[index] : original[index]);

            if (current + add > h) {
                version++;
            } else {
                a[index] = current + add;
                last_update[index] = version;
            }
        }

        for (int i = 0; i < n; i++) {
            long long val = (last_update[i] == version ? a[i] : original[i]);
            cout << val << (i + 1 < n ? ' ' : '\n');
        }
    }

    return 0;
}
