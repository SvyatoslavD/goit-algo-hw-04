# Аналіз Ефективності Алгоритмів Сортування

Цей аналіз оцінює ефективність трьох алгоритмів сортування: сортування злиттям, сортування вставками, та Timsort (використовується у функціях `sorted()` та `list.sort()` Python).

## Методика

Для порівняння алгоритмів було проведено емпіричне тестування за допомогою модуля `timeit` у Python. Випадкові масиви даних різних розмірів (100, 1000, 10000 елементів) були використані для вимірювання часу виконання кожного алгоритму.

## Результати
```
Size: 100
	Insertion Sort           : 0.000325 seconds
	Merge Sort               : 0.000759 seconds
	Timsort                  : 0.000026 seconds

Size: 1000
	Insertion Sort           : 0.015027 seconds
	Merge Sort               : 0.015719 seconds
	Timsort                  : 0.000556 seconds

Size: 10000
	Insertion Sort           : 1.528116 seconds
	Merge Sort               : 0.145697 seconds
	Timsort                  : 0.009898 seconds
```

### Висновки

1. **Сортування вставками** показує добрі результати на невеликих масивах, але його продуктивність значно знижується при збільшенні розміру даних через квадратичну складність O(n^2).
2. **Сортування злиттям** є стабільно ефективним (O(n log n)) для більших масивів, але воно може бути надмірним для дуже маленьких даних.
3. **Timsort** виявився найбільш ефективним у всіх тестових умовах, завдяки своїй адаптивності та оптимізації для різних типів даних. Це гібридний алгоритм, що поєднує переваги обох сортувань злиттям і вставками.