# Лабораторна робота 2


### Завдання 1
Зчитування графу з файлу
- Матриця інцидентності
- Матриця суміжності
- Словник


### Завдання 2
Рекурсивна реалізація bfs і dfs


### Завдання 3 
Ітеративна реалізація bfs і dfs


### Завдання 4
Реалізувати знаходження радіусу в графі для задання графу матрицю суміжності та словник


### Завдання 5
Порівняльний аналіз розроблених алгоритмів


---
## Розподіл роботи

### Падучак Маргарита:
- реалізація bfs ітеративним способом
- реалізація знаходження радіусу в графі

### Заяць Юліан-Володимир:
- реалізація зчитання графу різними способами
- порівняльний аналіз розроблених алгоритмів

### Яковенко Олена:
- реалізація dfs ітеративним та рекурсивним способами

---
# Опис функцій
---
### Функція read_incidence_matrix(filename)
Зчитує граф з файлу, і робить матрицю інцидентності(ліст лістів), де кожен елемент показує зв'язок між вершинами та дугами. Вона використовує значення -1, 1, 0, і 2 для вихідних, вхідних,без-зв'язкових дуг і петель відповідно.

---
### Функція read_adjacency_matrix(filename)
Зчитує граф з файлу, і робить матриці суміжності, де одиниці означають наявність зв'язку між вершинами, а нулі відсутність.

---
### Функція read_adjacency_dict(filename)
Зчитує граф з файлу, і робить словник суміжності, де ключі це вершини, а значення це списки суміжних вершин.

---
### Функція iterative_adjacency_matrix_bfs (аналогічно для iterative_adjacency_dict_bfs)
#### Ініціалізація:
  Створюється список visited, який відстежує, чи була відвідана кожна вершина. Всі вершини спочатку позначаються як невідвідані (False).
  Черга (queue) ініціалізується стартовою вершиною.
  Список res створюється для збереження порядку обходу вершин.
#### Перший крок:
  Стартова вершина (start) позначається як відвідана.
  Вона додається в чергу.
#### Обхід:
  Поки черга не пуста:
    Витягується вершина ind_v із початку черги.
    Вершина додається до списку результатів (res).
    Для кожної сусідньої вершини ind:
      Якщо ця вершина ще не відвідана:
        Вона позначається як відвідана.
        Додається в чергу.
#### Завершення:
  Коли черга порожня, алгоритм завершується, і повертається список res із BFS-обходом графа.

---
### Функція iterative_adjacency_dict_dfs / iterative_adjacency_matrix_dfs
#### Ініціалізація:
  - visited – це множина, яка зберігає вже відвідані вершини. Спочатку вона порожня.
  - stack – стек ініціалізується стартовою вершиною start. Він використовується для реалізації ітеративного обходу в глибину.
  - traversal – список для збереження порядку обходу вершин. Спочатку він порожній.
#### Перший крок:
  - Стартова вершина start додається до стеку stack.
  - Алгоритм починає обхід зі стартової вершини, поки стек не стане порожнім.
#### Обхід:
  - Поки стек не порожній:
    - Поточна вершина current витягується зі стеку останній елемент і видаляє його.
    - Якщо вершина вже була відвідана, цикл пропускає цю ітерацію.
    - Вершина додається до множини visited та списку traversal.
    - Для всіх сусідів вершини current:
      - Сусіди сортуються у зворотному порядку для коректного обходу (для словника), 
      - для матриці суміжності беремо список з інформацією про суміжність конкретної вершини в оберненому порядку.
      - Якщо сусід ще не був відвіданий, він додається до стеку stack.
#### Завершення:
  - Коли стек порожній, обхід завершується.
  - Список traversal, який містить порядок обходу вершин, повертається як результат.

---
### Функція recursive_adjacency_dict_dfs / recursive_adjacency_matrix_dfs
#### Ініціалізація:
  - path – список, що зберігає відвідані вершини у порядку обходу. Якщо значення path не передано, він ініціалізується як порожній список.
  - start – стартова вершина обходу передається у функцію як аргумент.
  - Параметр path є необов'язковим і має значення за замовчуванням None (оскільки його не передають при першому виклику функції).
  У першому виклику функції необхідно створити порожній список, який буде слугувати контейнером для відвіданих вершин.
#### Перший крок:
  - Стартова вершина start перевіряється на наявність у списку path:
    - Якщо вершина відсутня у списку, вона додається до path.
    - Для рекурсивного виклику використовується структура графа:
      - Список суміжності (adjacency list): Для кожного сусіда вершини start виконується ітерація за допомогою сортування сусідів у зростаючому порядку.
      - Матриця суміжності (adjacency matrix): Виконується ітерація всіх вершин, які мають суміжність із поточною вершиною start.
#### Обхід:
  - Для кожного сусіда вершини:
    - У випадку списку суміжності – сусіди сортуються у зростаючому порядку для коректного обходу.
    - У випадку матриці суміжності – перевіряються всі значення у рядку матриці, де 1 вказує на суміжність.
    - Якщо сусід ще не був відвіданий (відсутній у списку path):
      - Викликається рекурсивний виклик функції з цим сусідом як новою стартовою вершиною.
#### Завершення:
  - Коли всі вершини обійдено, функція повертає список path, що містить порядок обходу вершин.
  - Рекурсія завершується автоматично, коли не залишається жодних сусідів для відвідування.

---
### Функція adjacency_matrix_radius (аналогічно для adjacency_dict_radius)
#### Визначення відстаней за допомогою вкладеної функції bfs_distance:
  Вкладена функція bfs_distance(start) виконує пошук у ширину (BFS) від заданої вершини start.
#### Мета BFS:
  Обчислити відстані від початкової вершини до всіх інших вершин графа.
  Використовує чергу (queue) для обходу вершин, масив visited для позначення відвіданих вершин і масив distance для збереження відстаней.
  Модифікований BFS повертає список відстаней для кожної вершини графа.
#### Обчислення ексцентриситетів:
  Для кожної вершини графа викликається bfs_distance(i) для обчислення списку відстаней.
  Ексцентриситет вершини i визначається як максимальна відстань у цьому списку.
#### Обчислення радіуса графа:
  Радіус графа — це мінімальний ексцентриситет серед усіх вершин.
