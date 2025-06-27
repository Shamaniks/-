import subprocess

PYTHON = "python3"
FILE = "app.py"

def test_case_1():
    """
    Ищется форма, но такой не существует
    """
    test_input = "--field1_0=text"
    test_output = "{\n\tfield1_0: text\n}\n"

    result = subprocess.run([PYTHON, FILE, test_input], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout

def test_case_2():
    """
    Ищется форма с одним полем
    """
    test_input = "--field2_1=text"
    test_output = "form2"

    result = subprocess.run([PYTHON, FILE, test_input], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout

def test_case_3():
    """
    Ищется форма с полем под почту
    """
    test_input = "--field3_1=ShamanskiyYuA23@st.ithub.ru"
    test_output = "form3"

    result = subprocess.run([PYTHON, FILE, test_input], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout

def test_case_4():
    """
    Ищется форма с полем под дату
    """
    test_input = "--field4_1=13.12.2026"
    test_output = "form4"

    result = subprocess.run([PYTHON, FILE, test_input], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout

def test_case_5():
    """
    Ищется форма с полем под дату с другим форматом
    """
    test_input = "--field5_1=2026-12-13"
    test_output = "form5"

    result = subprocess.run([PYTHON, FILE, test_input], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout

def test_case_6():
    """
    Ищется форма с полем под дату c неправильным месяцем
    """
    test_input = "--field6_1=12.13.2026"
    test_output = "form6"

    result = subprocess.run([PYTHON, FILE, test_input], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout

def test_case_7():
    """
    Ищется форма с полем под дату c неправильным месяцем с другим форматом
    """
    test_input = "--field7_1=2026-13-12"
    test_output = "form7"

    result = subprocess.run([PYTHON, FILE, test_input], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout

def test_case_8():
    """
    Ищется форма с полем под телефон
    """
    test_input = "--field8_1=+7 800 555 35 35"
    test_output = "form8"

    result = subprocess.run([PYTHON, FILE, test_input], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout

def test_case_9():
    """
    Проверка маски ввода телефона
    """
    test_input = "--field9_1=8 800 555 35 35"
    test_output = "{\n\tfield9_1: text\n}\n"

    result = subprocess.run([PYTHON, FILE, test_input], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout

def test_case_10():
    """
    Проверка маски ввода почты
    """
    test_input = "--field10_1=user@@site.com"
    test_output = "{\n\tfield10_1: text\n}\n"

    result = subprocess.run([PYTHON, FILE, test_input], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout

def test_case_11():
    """
    Поиск формы с 3 полями по 1 полю
    """
    test_input = "--field11_1=text"
    test_output = "form11"

    result = subprocess.run([PYTHON, FILE, test_input], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout

def test_case_12():
    """
    Поиск двух форм с совпадающим поле в поиске
    """
    test_input = "--field12-13_1=text"
    test_output = "form12\nform13"

    result = subprocess.run([PYTHON, FILE, test_input], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout

def test_case_13():
    """
    Поиск одной формы с совпадающим полем и уникальным полем в поиске
    """
    test_input = ["--field12-13_1=text", "--field13_2=text"]
    test_output = "form13"

    result = subprocess.run([PYTHON, FILE, *test_input], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout

def test_case_14():
    """
    В поиске указана почта, но находится форма с текстовым полем
    """
    test_input = "--field14_1=ShamanskiyYuA23@st.ithub.ru"
    test_output = "form14"

    result = subprocess.run([PYTHON, FILE, test_input], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout

def test_case_15():
    """
    Вызов подсказки
    """

    test_output = "Применение: python app.py [<имя поля>=<значение>]*"

    result = subprocess.run([PYTHON, FILE], capture_output=True, text=True)
    assert result.returncode == 0
    assert test_output in result.stdout
