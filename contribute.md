## Добавление файлов

# Подготовка
1. Вписать свой GitHub ник напротив имени [здесь](https://docs.google.com/spreadsheets/d/1TWIeTPaqTv-YMjP19-pdxRMWj6SqizAJK3WjhXBWnF4/edit#gid=0)
2. Дождаться приглашения в Collaborators (на почте будет письмо)

# Загрузка
1. Зайти в папку [files](https://github.com/piechart/bachelor-diploma-docs/tree/master/files)
2. Нажать Upload files
![](http://ipic.su/img/img7/fs/Snimokekrana2020-02-06v15.1580993161.png)
3. Выбрать нужные файлы. **Убедиться, что в названиях загружаемых файлов отсутствуют пробелы**
4. Над кнопкой Commit changes переключить селектор на Create new branch, название создаваемой ветки значения не имеет
5. Нажать Propose changes
![](http://ipic.su/img/img7/fs/Snimokekrana2020-02-06v15.1580993392.png)

6. Открыть файл [readme.md](https://github.com/piechart/bachelor-diploma-docs/blob/master/readme.md), НЕ НАЖИМАТЬ РЕДАКТИРОВАТЬ ФАЙЛ
7. Под вкладкой Code слева-сверху переключить активную ветку (с master) на ту, которую вы создали в п. 4.
![](http://ipic.su/img/img7/fs/Snimokekrana2020-02-06v15.1580993484.png)

8. Справа рядом с кнопками Raw, Blame History нажать на карандашик (Edit this file)
![](http://ipic.su/img/img7/fs/Snimokekrana2020-02-06v15.1580993512.png)
9. Добавить активную относительную ссылку на загруженный файл в секцию обязательных или необязательных документов. Формат: `[имя_файла](files/путь_до_файла.pdf)`
10. Нажать внизу Commit changes
11. Перейти в [Pull Requests](https://github.com/piechart/bachelor-diploma-docs/pulls), нажать New Pull Request
12. В блоке Compare changes справа выбрать вашу ветку, в которую вы загрузили файл(ы).
![](http://ipic.su/img/img7/fs/Snimokekrana2020-02-06v15.1580993572.png)
13. Нажать Create Pull Request
14. В названии перечислить добавленные документы
15. Еще раз внизу нажать Create pull request
16. Дождаться прохождения CI (около названия пул реквеста появится зеленая галочка), появления надписи All checks have passed.
![](http://ipic.su/img/img7/fs/Snimokekrana2020-02-06v15.1580993739.png)
В случае возникновения ошибок нужно посмотреть их суть и внести необходимые правки.
Нажимаем Details
![](http://ipic.su/img/img7/fs/Screenshot2020-02-11at18.1581435014.png)
И читаем лог Main Checker
![](http://ipic.su/img/img7/fs/Screenshot2020-02-11at18.1581435037.png)
17. Дождаться ревью, внести правки при необходимости.
18. Засчитанным состоянием добавления файлов является статус Merged вашего Pull Request
![](http://ipic.su/img/img7/fs/Screenshot2020-02-11at18.1581434408.png)
