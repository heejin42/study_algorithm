# Linked List
![img](https://www.geeksforgeeks.org/wp-content/uploads/gq/2013/03/Linkedlist.png)

### info
연속적인 메모리 위치에 저장되지 않는 선형 데이터 구조로 포인터로 연결된다.
각 노드는 데이터 필드와 다음 노드에 대한 참조 노드로 구성되어 있다.

### why?
배열은 비슷한 유형의 선형 데이터를 저장하는데 사용할 수 있지만 두가지 제한이 있다.
1. 배열의 크기가 고정되어 있어 미리 필요한 수만큼 할당을 받아야 한다
2. 새로운 요소를 삽입하기 위해서는 공간을 더 만들고 기존 요소를 이동시켜야 하기 때문에 비용이 많이 든다.

반면에 Linked List는?
1. 동적 크기
2. 삽입/삭제 용이

그러나 단점도 존재한다.
- 임의의 액세스는 불가하다. 첫번째 노드부터 순차적으로 액세스해야 한다.
- 포인터 여분의 메모리 공간이 목록의 각 요소마다 필요하다.

### struct
```cpp
struct Node 
{ 
  int data; 
  struct Node *next; 
}; 
```

### 노드 추가
* 앞쪽 추가
```cpp
void push(struct Node** head_ref, int new_data){
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));

    new_node->data = new_data;

    new_node->next = (*head_ref);

    (*head_ref) = new_node;
}
```
* 특정 노드 다음 추가
```cpp
void insertAfter(struct Node* prev_node, int new_data){
    if (prev_node == NULL){
        printf("이전 노드가 NULL이 아니어야 합니다.");
        return;
    }

    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));

    new_node->data = new_data;
    new_node->next = prev_node->next;

    prev_node->next = new_node;
    
}
```
* 맨 끝에 추가
```cpp
void append(struct Node** head_ref, int new_data){
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));

    struct Node *last = *head_ref;

    new_node->data = new_data;

    new_node->next = NULL;

    if (*head_ref == NULL){
        *head_ref = new_node;
        return;
    }

    while(last->next != NULL){
        last = last->next;
    }

    last->next = new_node;
    return;

}
```


