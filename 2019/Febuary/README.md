# 2019년 2월 SSAFY 교육

[TOC]

## 7일 목요일

1. sqlite3

- AUTOINCREMENT의 주의사항

INTEGER 컬럼에 대해서만 사용할 수 있다!

- .nullvalue

레코드 삽입 시 비어있는 값을 설정하는 방법

> 참고로 sqlite3에서는 한줄로 INSERT 쿼리를 수행할 수 있다.

```sql
INSERT INTO bands (name, debut) VALUES ("Queen", 1973), ("ColdPlay", 1998), ("MCR", 2001);
```

- ALTER TABLE

sqlite3에서는 `테이블 이름 변경`과 `새로운 컬럼 추가`를 할 수 있다.

```sql
ALTER TABLE test RENAME TO test2;
```
위와 같이 `ALTER TABLE`로 이름을 바꿀 수 있다.

> 참고로 sqlite3에서는 Drop column을 할 수 없다. 만약 하고 싶다면 table의 이름을 바꾼 후 새로운 테이블 생성, 기존 테이블에 데이터 복사하는 방식으로 테이블에 column을 drop 할 수 있다.

[sqlite3 참고](https://www.techonthenet.com/sqlite/)
[sqlite3 공식사이트](https://www.sqlite.org/index.html)
