def solution(alp, cop, problems):
    answer = 1e9
    
    max_alp, max_cop = 0, 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)
    
    alp = min(max_alp, alp)
    cop = min(max_cop, cop)
    dp = [[1e9 for _ in range(max_cop+1)] for _ in range(max_alp+1)]
    dp[alp][cop] = 0
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            if i+1 <= max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j+1 <= max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(max_alp, i+alp_rwd)
                    new_cop = min(max_cop, j+cop_rwd)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
    
    return dp[-1][-1]