from flask import Flask, render_template, request

app = Flask("main.py")


@app.route('/123')
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/quiz/1', methods=["GET", "POST"])
def victori_1():
    name = request.form.get("course") + '_' + request.form.get("fio")
    URL = '/2'
    name_1 = name.split('_')
    if int(name_1[0]) == 2:
        return render_template('quiz.html',
                               test='1: Какой из следующих методов используется для нахождения производной сложной функции?',
                               one='Правило цепочки.', two='Метод интегрирования по частям.', three='Метод Ньютона.',
                               otvet_1=f'{name}_{1}', otvet_2=f'{name}_{0}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='quiz/2')
    else:
        return render_template('quiz.html', test=""": Что должно стоять вместо *
        Логарифмом положительного числа b по основанию а (*******)называется показатель степени с,
         в которую нужно возвести а, чтобы получить b""", one='a>0,a≠0', two='a<0,a≠1', three='a>0,a≠1',
                               otvet_1=f'{name}_{1}', otvet_2=f'{name}_{0}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='quiz/2')


@app.route('/quiz/2', methods=["GET", "POST"])
def victori_2():
    name = request.form.get('otvet')
    URL = '/3'
    name_1 = name.split('_')
    if int(name_1[0]) == 2:
        return render_template('quiz.html',
                               test='2: Как называется среднее значение выборки в математической статистике?',
                               one='Мода.', two='Среднее арифметическое.', three='Медиана.',
                               otvet_1=f'{name}_{0}', otvet_2=f'{name}_{1}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='quiz/3')
    else:
        return render_template('quiz.html', test="2: Чему ровняется комплексное i²?", one='1', two='0', three='-1',
                               otvet_1=f'{name}_{0}', otvet_2=f'{name}_{0}', otvet_3=f'{name}_{1}', URL=URL,
                               rezult='quiz/3')


@app.route('/quiz/3', methods=["GET", "POST"])
def victori_3():
    name = request.form.get('otvet')
    URL = '/4'
    name_1 = name.split('_')
    if int(name_1[0]) == 2:
        return render_template('quiz.html',
                               test='3: Что из перечисленного является характеристическим числом матрицы?',
                               one='Минор матрицы.', two='Собственное число матрицы.', three='Ранг матрицы.',
                               otvet_1=f'{name}_{0}', otvet_2=f'{name}_{1}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='quiz/4')
    else:
        return render_template('quiz.html', test="3: Какие две основные координаты используют в функциях?", one='x,y',
                               two='y,z', three='z,x',
                               otvet_1=f'{name}_{1}', otvet_2=f'{name}_{0}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='quiz/4')


@app.route('/quiz/4', methods=["GET", "POST"])
def victori_4():
    name = request.form.get('otvet')
    URL = '/5'
    name_1 = name.split('_')
    if int(name_1[0]) == 2:
        return render_template('quiz.html',
                               test='4: Как называется вероятность события, которое уже наступило?',
                               one='Вероятность в долгосрочной перспективе.', two='Апостериорная вероятность.',
                               three='Частотная вероятность.',
                               otvet_1=f'{name}_{0}', otvet_2=f'{name}_{1}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='quiz/5')
    else:
        return render_template('quiz.html',
                               test="4: Многогранник, две грани которого являются конгруэнтными многоугольниками, лежащими в параллельных плоскостях?",
                               one='Шар', two='Призма', three='Конус',
                               otvet_1=f'{name}_{0}', otvet_2=f'{name}_{1}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='quiz/5')


@app.route('/quiz/5', methods=["GET", "POST"])
def victori_5():
    name = request.form.get('otvet')
    URL = '/end'
    name_1 = name.split('_')
    if int(name_1[0]) == 2:
        return render_template('quiz.html', test='5: Как называется вероятность события, которое уже наступило?',
                               one='Вероятность в долгосрочной перспективе.', two='Апостериорная вероятность.',
                               three='Частотная вероятность.',
                               otvet_1=f'{name}_{0}', otvet_2=f'{name}_{0}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='end')
    else:
        return render_template('quiz.html', test="5: Теория вероятности - это?",
                               one='раздел математики, который изучает основные операции с числами: сложение, вычитание, умножение и деление.',
                               two='раздел математики, изучающий случайные события, случайные величины, их свойства и операции над ними.',
                               three='раздел математики, который изучает фигуры, их свойства и взаимоотношения.',
                               otvet_1=f'{name}_{0}', otvet_2=f'{name}_{1}', otvet_3=f'{name}_{0}', URL=URL,
                               rezult='end')


@app.route('/end', methods=["GET", "POST"])
def rezult():
    a = request.form.get("otvet").split('_')
    n = int(a[2]) + int(a[3]) + int(a[4]) + int(a[5]) + int(a[6])
    return render_template('result.html', fio=a[1], ball=n, kurs=a[0])


app.run(debug=True)
