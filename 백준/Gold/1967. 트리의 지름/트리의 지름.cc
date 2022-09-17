#include <bits/stdc++.h>

using namespace std;

struct Edge {
	int to;
	int cost;
	Edge(int to, int cost) : to(to), cost(cost) {
	}
};

vector<Edge> a[10001];
bool check[10001];

pair<int, int> dfs(int x) {
	check[x] = true;
	vector<int> heights;
	int ans = 0;
	for (auto &e : a[x]) {
		int y = e.to;
		int cost = e.cost;
		if (check[y] == false) {
			auto p = dfs(y);
			if (ans < p.first) ans = p.first;
			heights.push_back(p.second + cost);
		}
	}
	int height = 0;
	sort(heights.begin(), heights.end());
	reverse(heights.begin(), heights.end());
	if (heights.size() >= 1) {
		height = heights[0];
		if (ans < height) {
			ans = height;
		}
	}
	if (heights.size() >= 2) {
		if (ans < heights[0] + heights[1]) {
			ans = heights[0] + heights[1];
		}
	}
	return make_pair(ans, height);

}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n - 1; i++) {
		int u, v, w;
		scanf("%d %d %d", &u, &v, &w);
		a[u].push_back(Edge(v, w));
		a[v].push_back(Edge(u, w));
	}
	auto ans = dfs(1);
	cout << ans.first << '\n';

	return 0;
}