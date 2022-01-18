# Payhere 과제

### 과제 요구사항

1. 고객은 이메일과 비밀번호 입력을 통해서 회원 가입을 할 수 있습니다. 
2. 고객은 회원 가입이후, 로그인과 로그아웃을 할 수 있습니다. 
3. 고객은 로그인 이후 가계부 관련 아래의 행동을 할 수 있습니다. 
    1. 가계부에 오늘 사용한 돈의 금액과 관련된 메모를 남길 수 있습니다. 
    2. 가계부에서 수정을 원하는 내역은 금액과 메모를 수정 할 수 있습니다. 
    3. 가계부에서 삭제를 원하는 내역은 삭제 할 수 있습니다. 
    4. 삭제한 내역은 언제든지 다시 복구 할 수 있어야 한다.
    5. 가계부에서 이제까지 기록한 가계부 리스트를 볼 수 있습니다. 
    6. 가계부에서 상세한 세부 내역을 볼 수 있습니다. 
4. 로그인하지 않은 고객은 가계부 내역에 대한 접근 제한 처리가 되어야 합니다.

![스크린샷 2022-01-18 오후 3 45 35](https://user-images.githubusercontent.com/67960152/149884734-c593e35a-4256-480a-9cb7-104df21fea7b.png)

### api 
1. 고객은 이메일과 비밀번호 입력을 통해서 회원 가입을 할 수 있습니다. 
```python
- Request
{
  "email": "payhere@gmail.com",
  "name": "payhere",
  "password": "payhere1"
}

- Response
{
  "id": 2,
  "email": "payhere@gmail.com",
  "name": "payhere",
  "password": "$2b$12$UERycABBH3EqSAgel6uqm.S7c3VXKgP8HHrAyOXXncaGm.VL0Q136",
  "created_at": "2022-01-18T06:47:21",
  "updated_at": "2022-01-18T06:47:21"
}
```
2. 고객은 회원 가입이후, 로그인과 로그아웃을 할 수 있습니다. (로그아웃을 구현하지 못했습니다.)
```python
- Request
{
  "email": "payhere@gmail.com",
  "password": "payhere1"
}

- Response
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoxLCJleHAiOjE2NDI0OTIxNjV9.YUwzg7nm2dpFVPVRt05ELUIULsdn75kfiA_LPv4XAdM",
  "token_type": "bearer"
}
```
3. 가계부에 오늘 사용한 돈의 금액과 관련된 메모를 남길 수 있습니다.
```python
- Request
{
  "memo": "편의점 과자 구매",
  "price": 3000,
  "transfer": "출금"
}

- Response
{
  "id": 1,
  "user_id": 1,
  "memo": "편의점 과자 구매",
  "transfer": "지출",
  "price": 3000,
  "created_at": "2021-11-11T07:50:54.289Z",
  "updated_at": "2021-11-11T07:50:54.289Z"
}
```
4. 가계부에서 수정을 원하는 내역은 금액과 메모를 수정 할 수 있습니다. 
```python
- Request
'http://0.0.0.0:8000/household_ledger/update/1'
{
  "memo": "편의점 과자 환불",
  "price": 3000,
  "transfer": "입금"
}

- Response
{
  "memo": "편의점 과자 환불",
  "price": 3000,
  "transfer": "입금"
}

```
5. 가계부에서 삭제를 원하는 내역은 삭제 할 수 있습니다.
```python
- Request
curl -X 'PATCH' \'http://0.0.0.0:8000/household_ledger/delete/2'

- Response
{
  "id": 1
}
```
6. 삭제한 내역은 언제든지 다시 복구 할 수 있어야 한다.
```python
- Request
curl -X 'PATCH' \'http://0.0.0.0:8000/household_ledger/delete/restoration/1'
- Response
{
  "id": 1
}
```
7. 가계부에서 이제까지 기록한 가계부 리스트를 볼 수 있습니다.
```python
- Request
curl -X 'GET' \ 'http://0.0.0.0:8000/household_ledger/list'

- Response
[
  {
    "id": 1,
    "memo": "편의점 과자 구매",
    "transfer": "출금",
    "price": 3000,
    "created_at": "2022-01-18T07:00:06"
  },
  {
    "id": 2,
    "memo": "편의점 라면 환불",
    "transfer": "입금",
    "price": 3000,
    "created_at": "2022-01-19T06:57:33"
  },
  {
    "id": 3,
    "memo": "편의점 껌 구매",
    "transfer": "출금",
    "price": 3000,
    "created_at": "2022-01-16T09:25:40"
  },
  {
    "id": 4,
    "memo": "편의점 아이스크림 구매",
    "transfer": "출금",
    "price": 3000,
    "created_at": "2022-01-16T23:54:53"
  }
]
```
8. 가계부에서 상세한 세부 내역을 볼 수 있습니다. 
```python
- Request
curl -X 'GET' \ 'http://0.0.0.0:8000/household_ledger/1'

- Response
{
  "id": 1,
  "user_id": 1,
  "memo": "편의점 과자 구매",
  "transfer": "입금",
  "price": 3000,
  "created_at": "2022-01-18T07:00:06",
  "updated_at": "2022-01-18T07:00:06"
}

```
9. 가계부에서 삭제한 가계부 리스트를 볼 수 있습니다. 
```python
- Request
curl -X 'GET' \ 'http://0.0.0.0:8000/household_ledger/delete/list'

- Response
[
  {
    "id": 1,
    "memo": "편의점 과자 환불",
    "transfer": "입금",
    "price": 3000,
    "created_at": "2022-01-18T07:16:27"
  },
  {
    "id": 2,
    "memo": "편의점 과자 환불",
    "transfer": "입금",
    "price": 3000,
    "created_at": "2022-01-18T07:16:31"
  }
]
```
### 과제 하면서 아쉬운점
과제를 하면서 아쉬운 점은 로그아웃과 도커를 구현하지 못한점이 아쉽습니다. 

로그아웃은 쿠기를 다루는 부분이 부족하여 찾아봤지만 2틀동안 투자하였는데 안돼서 다른 기능을 구현하였습니다. 

docker는 dockerfile은 만들었는데 어떻게 사용하는지 이해가 안가서 추 후 공부를 한 후에 다시 docker에 대해 도전할 예정입니다. 

감사합니다. 
