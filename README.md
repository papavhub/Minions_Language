# Minions_Language

Minions Language는 rycont/umjunsik-lang과 cjaewon/umlang에 영감을 받아, 참고하여 작성하였습니다.


## 참고한 언어
- 아래의 미니언 용어 사전을 참고하였습니다.

![image](https://github.com/user-attachments/assets/3173c153-2ab3-4704-a5a5-bc73e6fa99fa)


## 문법
### 1. 프로그램 시작
안녕!인 Bello!로 시작합니다.
```
Bello!
```

### 2. Int
Haha, Dul, Sae, Muak을 사용합니다.
```
Hana -> 1
Dul -> 2
Sae -> 3

Muak -> 1
Muak-Muak -> 2
Muak-Muak-Muak-Muak -> 4
```

### 3. 선언
변수에 값을 할당합니다.
```
Gelato bananacorn yummy -> bananacorn = yummy
```

### 4. 입력
String(string) 또는 Int(int)를 입력받아 변수에 값을 할당합니다.
```
Tulaliloo ti amo! String gelatocorn -> gelatocorn = str(input())
Tulaliloo ti amo! Int gelatocorn -> gelatocorn = int(input())
```

### 5. 출력
할당된 변수가 존재한다면 변수의 값, 존재하지 않는다면 입력된 값을 외칩니다.
```
Kanpai! bananacorn gelatocorn hemmnnn -> bananacorn 변수 값, gelatocorn 변수 값, "hemmnnn"  Print
Kanpai! M I N I O N S
->
M!
I!
N!
I!
O!
N!
S!
```

### 6. Banana
Banana를 N번 외칩니다.
```
Banana Muak-Muak-Muak-Muak
->
Banana!
Banana!
Banana!
Banana!
```
### 7. 프로그램 종료
잘가!인 Poopaye!로 프로그램을 종료합니다.
```
Poopaye!
```

## 실행 예시
```
git clone 
python __main__.py example.minions
```

## version
- 1.0 : Original
- 2.0 : 변수 할당을 data[N]으로 할당하는 구조에서, 딕셔너리 형으로 변경함
