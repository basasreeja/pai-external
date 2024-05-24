import math
def score(nodeIndex):
    
    return scores[nodeIndex]

def minimax(curDepth, nodeIndex, MaxTurn, scores, targetDepth):
    if curDepth == targetDepth:
        return score(nodeIndex)

    if MaxTurn:
        bestVal = float('-inf')
        for i in range(2):
            val = minimax(curDepth + 1, nodeIndex * 2 + i, False, scores, targetDepth)
            bestVal = max(bestVal, val)
        return bestVal
    else:
        bestVal = float('inf')
        for i in range(2):
            val = minimax(curDepth + 1, nodeIndex * 2 + i, True, scores, targetDepth)
            bestVal = min(bestVal, val)
        return bestVal

scores = [10, -3, -19, 11, 11, 0, -2, -2, -2, 14, -16, 2, 17, 15, -14, 15, -15, 13, -19, -9, 4, -9, 2, 9, -14, 2, -18]
treeDepth = int(math.log(len(scores), 2))

print("The optimal value:", end=" ")
print(minimax(0, 0, True, scores, treeDepth))

