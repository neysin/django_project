gantt
    dateFormat  YYYY-MM-DD
    title       Django Monolithic Blog Development Schedule

    section 계획
    WBS 생성              :done,    wbs, 2024-03-02, 1d
    요구사항 분석          :done,    req, after wbs, 2d
    기획                  :done,    req, after wbs, 1d
    
    section 설계
    ERD 생성              :done,    erd, 2024-03-03, 1d
    모델 관계 설정         :done     uides, after proto, 2d

    section 개발
    URL 디자인            :done,    urldes, 2024-03-05, 1d
    CRUD 구현             :done,    crud, after urldes, 2d

    section UI 제작 및 추가 기능 
    백엔드 추가 기능           :         backend, 2024-03-08, 3d
    피그마 디자인              :         backend, 2024-03-08, 3d
    프론트엔드 기능            :         backend, 2024-03-08, 3d

    section 테스트 & 배포
    테스팅                :         test, 2024-03-10, 2d
    배포                  :         deploy, after test, 1d
    
    section 종료
    프로젝트 종료          :         end, 2024-03-11, 2d
