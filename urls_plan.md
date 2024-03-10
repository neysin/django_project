# urls 기획

1. 다음 url이 실제 작동하도록 해주세요.
1.1 'blog/'                     : 블로그 글 목록
1.2 'blog/<int:pk>/'            : 블로그 글 읽기
1.3 'blog/write/'               : 블로그 글 작성
1.4 'blog/edit/<int:pk>/'       : 블로그 글 업데이트
1.5 'blog/delete/<int:pk>/'     : 블로그 글 삭제

###################################
앱이름: main                views 함수이름   html 파일이름  비고
'/'
'/about'
'/contact'

앱이름: blog                views 함수이름   html 파일이름  비고
'blog/'                     blog_list        blog_list.html	
'blog/<int:pk>'             blog_details     blog_details.html
'blog/write/'               blog_write       blog_write.html
'blog/edit/<int:pk>/'       blog_edit        blog_edit.html
'blog/delete/<int:pk>/'     blog_delete      blog_delete.html

앱이름: accounts            views 함수이름   html 파일이름   비고

'/accounts/login'
'/accounts/logout'
'/accounts/signup'
'/accounts/profile'