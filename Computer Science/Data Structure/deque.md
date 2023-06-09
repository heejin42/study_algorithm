# 자료구조 - 덱(deque)
### 데크(deque)의 개념
보통 큐(queue)는 선입선출(FIFO) 방식으로 작동한다. 반면, 양방향 큐가 있는데 그것이 바로 데크(deque)다.   
즉, 앞&뒤 양쪽 방향에서 엘리먼트(element)를 추가하거나 제거할 수 있다.   
데크는 양 끝 엘리먼트의 append와 pop이 압도적으로 빠르다.   

컨테이너(container)의 양끝 엘리먼트(element)에 접근하여 삽입 또는 제거를 할 경우, 일반적인 리스트(list)가 이러한 연산에 O(n)이 소요되는 데 반해, 데크(deque)는 O(1)로 접근 가능하다.   

### 데크(deque) 사용법
데크는 다음처럼 임포트(import)해 사용한다.   

```python
from collections import deque
deq = deque()
# Add element to the start
deq.appendleft(10)
# Add element to the end
deq.append(0)
# Pop element from the start
deq.popleft()
# Pop element from the end
deq.pop()
```

데크(deque)에 존재하는 메서드(method)는 대략 다음과 같다.   

- deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
- deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
- deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
- deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
- deque.remove(item): item을 데크에서 찾아 삭제한다.
- deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).

### 덱(deque), 언제, 왜 써야 하는가?
요약하자면, 데크(deque)는 스택처럼 사용할 수도 있고, 큐 처럼 사용할 수도 있다.   
시작점의 값을 넣고 빼거나, 끝 점의 값을 넣고 빼는 데 최적화된 연산 속도를 제공한다.   
즉, 대부분의 경우에 데크(deque)는 리스트(list)보다 월등한 옵션이다.   

데크는 특히 push/pop 연산이 빈번한 알고리즘에서 리스트보다 월등한 속도를 자랑한다.   

일례로 백준 7576번 “토마토” 문제에서 익은 토마토를 리스트에 담도록 코드를 짜면 시간초과로 통과에 실패하지만, 데크를 사용하면 무난히 통과한다.   