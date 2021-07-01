# 기능 개발
import math

def Solution(progresses: 'List', speeds: 'List') -> 'List[int]':
    """[summary]
    개발공수가 맨 앞(front)에 있는 것보다 커지면 그 전까지 있던 작업을 배포(append)하고 front 교체.
    """
    answer = []
    deploy = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)] 
    front = 0
    for idx in range(len(deploy)):
        if deploy[idx] > deploy[front]:
            answer.append(idx - front)
            front = idx
    answer.append(len(deploy) - front)
            
    return answer


# progresses, speeds = [93, 30, 55], [1, 30, 5]
# print(Solution(progresses, speeds))  # [2, 1]
