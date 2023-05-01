# 트라이(Trie)
### 개념 - C++
트라이(Trie)의 형태
![img](https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Trie_example.svg/375px-Trie_example.svg.png)

- 트라이(Trie)란 문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 자료구조입니다.
- 위에 보이는 트리의 루트에서부터 자식들을 따라가면서 생성된 문자열들이 트라이 자료구조에 저장되어 있다고 볼 수 있습니다. 저장된 단어는 끝을 표시하는 변수를 추가해서 저장된 단어의 끝을 구분할 수 있습니다.
- DFS 형태로 검색을 해보면 사진의 번호에 나와있듯이 to, tea, ted, ten, A, i, in, inn이라는 단어들이 자료구조에 들어가 있음을 알 수 있습니다.


### 사용 목적
문자열 탐색 시에 빠르게 탐색이 가능하다. 하지만 각 노드에서 자식들에 대한 포인터를 배열로 모두 저장해야 한다는 점에서 저장 공간의 크기가 크다는 단점이 있다.
주로 검색어 자동완성, 사전에서 찾기, 문자열 검사 등과 같은 부분에서 사용한다.

### 시간 복잡도
제일 긴 문자열의 길이를 L, 총 문자열의 수를 M이라 할 때, 시간복잡도는 아래와 같다.
생성 시: O(M*L) - 모든 문자열 M개에 대해 자료구조에 넣는 시간은 가장 긴 문자열 길이만큼 걸린다고 할 수 있다.
탐색 시: O(L) - 트리를 타고 들어가봤자 가장 긴 문자열 길이만큼이 최대이다.

```cpp
struct Trie{

	bool is_terminal; // this represents end of string
	Trie * children[ALPHABETS];

	// Constructor
	Trie(): is_terminal(false){
		memset(children, 0, sizeof(children));
	}

	// Delete all children
	~Trie(){
		for(int i = 0; i < ALPHABETS; ++i){
			if(children[i])
				delete children[i];
		}
	}

	void insert(const char * key){
		if(*key == '\0'){
			is_terminal = true;
		}
		else{
			int index = char_to_index(*key);

			if(children[index] == 0)
				children[index] = new Trie();
			children[index]->insert(key + 1);
		}
	}

	Trie* find(const char * key){
		if(*key == 0){
			return this;
		}

		int index = char_to_index(*key);
		if(children[index] == 0){
			return NULL;
		}

		return children[index]->find(key+1);
	}

	bool string_exist(const char * key){
		if(*key == 0 && is_terminal){
			return true;
		}

		int index = char_to_index(*key);
		if(children[index] == 0){
			return false;
		}
		return children[index]->string_exist(key + 1);
	}

};
```

메인 함수 코드
```cpp
int main (){

	Trie * root = new Trie();

	const char * words[5] = {"be", "bee", "can", "cat", "cd"};

	for(int i = 0; i < 5; ++i){
		printf("insert: %s\n", words[i]);
		root->insert(words[i]);
	}

	printf("\n");

	printf("%s: be\n", root->find("be") != 0 ? "Prefix Exist" : "Prefix Not Exist");
	printf("%s: can\n", root->find("can") != 0 ? "Prefix Exist" : "Prefix Not Exist");
	printf("%s: a\n", root->find("a") != 0 ? "Prefix Exist" : "Prefix Not Exist");
	printf("%s: cat\n", root->find("cat") != 0 ? "Prefix Exist" : "Prefix Not Exist");
	printf("%s: c\n", root->find("c") != 0 ? "Prefix Exist" : "Prefix Not Exist");

	printf("\n");

	printf("%s: c\n", root->string_exist("c") != 0 ? "String Exist" : "String Not Exist");
	printf("%s: be\n", root->string_exist("be") != 0 ? "String Exist" : "String Not Exist");
	printf("%s: bee\n", root->string_exist("bee") != 0 ? "String Exist" : "String Not Exist");
	printf("%s: candy\n", root->string_exist("candy") != 0 ? "String Exist" : "String Not Exist");
	printf("%s: cd\n", root->string_exist("cd") != 0 ? "String Exist" : "String Not Exist");

	delete root;

	return 0;
}
```
