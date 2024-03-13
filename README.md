# blog
# ERD
Table User {
  UserID INT [PK]
  Name VARCHAR
  Email VARCHAR
  Password VARCHAR
  SignUpDate DATETIME
}

Table Post {
  PostID INT [PK]
  Title VARCHAR
  Content TEXT
  CreatedAt DATETIME
  UserID INT [ref: > User.UserID]
}

Table Comment {
  CommentID INT [PK]
  Content TEXT
  CreatedAt DATETIME
  UserID INT [ref: > User.UserID]
  PostID INT [ref: > Post.PostID]
}

Table Category {
  CatID INT [PK]
  Name VARCHAR
  Description VARCHAR
}

Table Tag {
  TagID INT [PK]
  Name VARCHAR
}

Table PostTag {
  PostID INT [ref: > Post.PostID]
  TagID INT [ref: > Tag.TagID]
  PRIMARY KEY(PostID, TagID)
}

# WBS

```mermaid
gantt
    title Django Blog Project
    dateFormat  YYYY-MM-DD

    section 기획 및 설계
    URL 구조 기획       : 2024-03-07, 1d
    DB 테이블 구조 기획  : 2024-03-07, 1d
    WBS 생성            :2024-03-08  , 1d
    ERD 생성            : 2024-03-08, 1d

    section 요구사항 분석
    Bolg 구성 기능 분석 :2024-03-08 , 1d
    
    section 구현
    CRUD 기능 구현 : 2024-03-09 , 1d
    로그인/회원가입 기능 구현 : 2024-03-09 , 1d
    추가 기능 구현 :  2024-03-010 , 1d

    section UI
    BootStrap 사용 :  2024-03-11 , 1d
    와이어프레임 제작 :  2024-03-11 , 1d


    section 테스트 및 배포
    테스트 : 2024-03-12 , 1d
    배포 : 2024-03-12 , 1d
```
