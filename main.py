from flask import Flask, render_template
from random import sample

app = Flask(__name__)   # app이라는 이름을 가진 Flask 클래스의 객체 생성

@app.route('/')
def hello_world():
    return 'hello world'

# 사람 수만큼 점심 메뉴 추천
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['자장면', '짬뽕', '라면', '브리또', '사과', '찜닭']
    return f'{sample(menu, people)}'

@app.route('/show')
def show():
    menu = ['자장면.jpg', '짬뽕.jpg']
    pickme = ''.join(sample(menu, 1))
    return render_template('index.html', food_img = pickme)


@app.route('/hello')
def hello_django():
    return '장고로 가는 디딤돌'

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다.{name}님!'

@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return f'{num}의 세제곱은 {result}'

if __name__ == "__main__":
    app.run(debug=1)           # 객체의 run 함수를 이용하여 로컬 서버에서 앱 실행
