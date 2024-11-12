from flask import Flask, render_template, request

app = Flask("main.py")


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/index/1', methods=["GET", "POST"])
def victori_1():
    name = request.form.get("course") + '_' + request.form.get("fio")
    URL = '/2'
    if request.form.get("course") == '2':
        return render_template('index.html', test='1: Выбери 1', one='1', two='2', three='3',
                               otvet_1=f'{name}', otvet_2=f'{name}', otvet_3=f'{name}', URL=URL, rezult='index/2')
    else:
        return render_template('index.html', test=""": Что должно стоять вместо *
        Логарифмом положительного числа b по основанию а (*******)называется показатель степени с,
         в которую нужно возвести а, чтобы получить b""", one='a>0,a≠0', two='a<0,a≠1', three='a>0,a≠1',
                               otvet_1=f'{name}_{1}', otvet_2=f'{name}_{0}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='index/2')


@app.route('/index/2', methods=["GET", "POST"])
def victori_2():
    name = request.form.get('otvet')
    URL = '/3'
    if request.form.get("course") == '2':
        return render_template('index.html', test='', one='', two='', three='',
                               otvet_1=f'{name}_{0}', otvet_2=f'{name}_{0}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='index/3')
    else:
        return render_template('index.html', test="2: Чему ровняется комплексное i²?", one='1', two='0', three='-1',
                               otvet_1=f'{name}_{0}', otvet_2=f'{name}_{0}', otvet_3=f'{name}_{1}', URL=URL,
                               rezult='index/3')


@app.route('/index/3', methods=["GET", "POST"])
def victori_3():
    name = request.form.get('otvet')
    URL = '/4'
    if request.form.get("course") == '2':
        return render_template('index.html', test='', one='', two='', three='',
                               otvet_1=f'{name}_{0}', otvet_2=f'{name}_{0}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='index/4')
    else:
        return render_template('index.html', test="3: Какие две основные координаты используют в функциях?", one='x,y',
                               two='y,z', three='z,x',
                               otvet_1=f'{name}_{1}', otvet_2=f'{name}_{0}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='index/4')


@app.route('/index/4', methods=["GET", "POST"])
def victori_4():
    name = request.form.get('otvet')
    URL = '/5'
    if request.form.get("course") == '2':
        return render_template('index.html', test='', one='', two='', three='',
                               otvet_1=f'{name}_{0}', otvet_2=f'{name}_{0}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='index/5')
    else:
        return render_template('index.html',
                               test="4: Многогранник, две грани которого являются конгруэнтными многоугольниками, лежащими в параллельных плоскостях?",
                               one='Шар', two='Призма', three='Конус',
                               otvet_1=f'{name}_{0}', otvet_2=f'{name}_{1}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='index/5')


@app.route('/index/5', methods=["GET", "POST"])
def victori_5():
    name = request.form.get('otvet')
    URL = '/end'
    if request.form.get("course") == '2':
        return render_template('index.html', test='', one='', two='', three='',
                               otvet_1=f'{name}_{0}', otvet_2=f'{name}_{0}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='end')
    else:
        return render_template('index.html', test="5: Теория вероятности - это?",
                               one='раздел математики, который изучает основные операции с числами: сложение, вычитание, умножение и деление.',
                               two='раздел математики, изучающий случайные события, случайные величины, их свойства и операции над ними.',
                               three='раздел математики, который изучает фигуры, их свойства и взаимоотношения.',
                               otvet_1=f'{name}_{0}', otvet_2=f'{name}_{1}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='end')


@app.route('/end', methods=["GET", "POST"])
def rezult():
    a = request.form.get("otvet").split('_')
    n = int(a[2]) + int(a[3]) + int(a[4]) + int(a[5]) + int(a[6])
    return render_template('result.html', fio = a[1], ball=n, kurs=a[0])


app.run(debug=True)
