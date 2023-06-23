# Crypto
Для того, чтобы воспользоваться приложением необязательно запускать код, можно открыть exe-файл, который находится по пути /Main/dist/Main.exe
A - абонент, который шифрует. B - абонент, который дешифрует.

Алгоритм шифрования RSA
1) A нажимает "Получить числа", а затем "Сохранить числа" и отправляет их B.
2) B нажимает "Загрузить числа", у него формируется его открытый ключ - e, который ему надо сохранить, нажав на "Сохранить e", и отправить его A.
3) A загружает открытый ключ B, нажав "Выбрать e".
4) A выбирает файл, который необходимо зашифровать, нажав на "Выбрать файл", формируется хэш и число c.
5) A сохраняет число c, нажав на "Сохранить c", и нажимает "Зашифровать", после чего формируется ЭЦП.
6) A нажимает "Сохранить ЭЦП" и отправляет число c, зашифрованный файл и ЭЦП пользователю B.
7) B нажимает "Выбрать файл", "Выбрать c", "Выбрать ЭЦП", чтобы загрузить переданную информацию.
8) B нажимает "Расшифровать" и если подпись подтверждается, то B получает расшифрованный текст.

Алгоритм шифрования EGSA
1) A нажимает "Получить числа", а затем "Сохранить числа" и отправляет их B.
2) B нажимает "Загрузить числа", у него формируется его открытый ключ - y, который ему надо сохранить, нажав на "Сохранить y", и отправить его A.
3) A загружает открытый ключ B, нажав "Выбрать y".
4) A выбирает файл, который необходимо зашифровать, нажав на "Выбрать файл", формируется хэш и число r.
5) A нажимает "Зашифровать", после чего файл шифруется и формируется число s.
6) A нажимает "Сохранить ЭЦП", которое состоит из чисел r и s, и отправляет зашифрованный файл и ЭЦП пользователю B.
7) B нажимает "Выбрать файл" и "Выбрать ЭЦП", чтобы загрузить переданную информацию.
8) B нажимает "Расшифровать" и если подпись подтверждается, то B получает расшифрованный текст.

Алгоритм шифрования DSA
1) A нажимает "Получить числа", а затем "Сохранить числа" и отправляет их B.
2) B нажимает "Загрузить числа", чтобы загрузить переданную информацию.
3) A выбирает файл, который необходимо зашифровать, нажав на "Выбрать файл", формируется хэш и число r.
4) A нажимает "Получить ЭЦП", после чего формируется число s.
5) A нажимает "Сохранить ЭЦП", которое состоит из чисел r и s, и отправляет файл и ЭЦП пользователю B.
6) B нажимает "Выбрать файл" и "Выбрать ЭЦП", чтобы загрузить переданную информацию.
7) B нажимает "Проверить ЭЦП" и если подпись подтверждается, то B получает подтверждённый текст.

Алгоритм шифрования ГОСТ 34.10-94
1) A нажимает "Получить числа", а затем "Сохранить числа" и отправляет их B.
2) B нажимает "Загрузить числа", чтобы загрузить переданную информацию.
3) A выбирает файл, который необходимо зашифровать, нажав на "Выбрать файл", формируется хэш и число r.
4) A нажимает "Получить ЭЦП", после чего формируется число s.
5) A нажимает "Сохранить ЭЦП", которое состоит из чисел r и s, и отправляет файл и ЭЦП пользователю B.
6) B нажимает "Выбрать файл" и "Выбрать ЭЦП", чтобы загрузить переданную информацию.
7) B нажимает "Проверить ЭЦП" и если подпись подтверждается, то B получает подтверждённый текст.