## Занятие #56. Лабораторная работа
Перепишите прототип магазина (лабораторная работа #48) на классовые представления.
# Этап 1
Перепишите CRUD для товара на классовые представления: ListView, DetailView, CreateView, UpdateView и DeleteView.

Внесите следующие изменения:
Пагинируйте товары на главной по 5-10 записей (добавьте в базу достаточно товаров, чтобы хватило хотя бы на 2 страницы и обновите фикстуру).
Добавьте поисковую строку (можете использовать SearchView).
Напишите модельную форму для товара и используйте её в CreateView и UpdateView.

Следующие требования остаются неизменными (см. лабораторную #48):
Не выводите на главной товары, остаток которых меньше 1 единицы.
Отсортируйте товары на главной по категориям и названиям в алфавитном порядке.
В форме или модели товара валидируйте остаток, чтобы он не мог быть < 0.
Удаление - с подтверждением (стандартный DeleteView).  

Прочие требования проверяться не будут, просто убедитесь, что вы ничего не сломали, из того, что у вас было сделано.
# Этап 2
Добавьте модель "Товар в корзине".
Товар - внешний ключ к товару.
Количество - сколько этого товара сейчас в корзине.

На страницах, где выводятся товары (главная, просмотр товара) сделайте кнопку "Добавить в корзину":
На главной у каждого товара должна быть своя кнопка.
Можно вывести кнопку в форме или стилизованную под кнопку.
pk товара должен передаваться в url.

Напишите представление для добавления товара в корзину.
Если товара ещё нет в корзине, он добавляется с количеством 1. Если на складе нет этого товара (остаток = 0), то он не должен добавляться.
Если товар уже есть в корзине, его количество увеличивается на 1. Если новое количество товара больше, чем остаток на складе, то количество не должно меняться.
После добавления редирект на главную страницу

Добавьте страницу "Корзина", где можно просмотреть товары в корзине в виде таблицы.
Выведите название товара, его цену, количество в корзине и сумму.
В конце таблицы выведите итого.
Возле каждого товара выведите кнопку для удаления товара.
Выведите ссылку на эту страницу в меню.

Напишите представление для удаления товара из корзины.
Представление удаляет из корзины запись о товаре с заданным pk.
После удаления редирект на страницу корзины.

# Указания:
В качестве кнопок добавления и удаления можно вывести ссылки, стилизованные под кнопки. 
pk товара, который добавляется или удаляется из корзины должен передаваться внутри ссылок, по которым выполняется запрос.

# Бонус (+0.2 балла):
Сделайте редирект на ту страницу, с которой пришёл запрос - если с главной, то на главную (с учётом пагинации), если со страницы товара - обратно на страницу товара.

# Бонус (+0.2 балла):
Дайте возможность пользователю сразу указывать количество, сколько товаров он хочет добавить в корзину. Проверка на остаток должна учитывать введённое количество. Выведите поле для ввода количества возле каждой кнопки для добавления товара в корзину.

# Бонус (+0.2 балла):
Дайте пользователю возможность удалять товары из корзины по одному. Если количество товара в корзине > 1, его количество уменьшается на 1. Если количество товара в корзине = 1, запись о нём удаляется из корзины.
# Этап 3
Добавьте модель "Заказ".
Товары - многие-ко-многим к товарам. 
У каждого товара в заказе нужно хранить количество.
Имя пользователя - строчное поле, обязательное.
Телефон - строчное поле, обязательное.
Адрес - строчное поле, обязательное.
Дата и время создания - автозаполнение.

Выведите на странице корзины под списком товаров форму с полями:
Имя
Адрес
Телефон

И кнопку "Оформить заказ"

Напишите представление для создания заказа, которое:
Переносит все товары в корзине вместе с количеством в заказ.
Заполняет оставшиеся поля из формы.
Сохраняет заказ.
Удаляет все товары из корзины.

Зарегистрируйте заказы в админке, чтобы их можно было просмотреть там.

# Бонус (+0.1 балла):
В списке заказов в админке выведите pk, имя, телефон и дату и время создания.
В списке заказов в админке отсортируйте их по дате и времени создания в убывающем порядке.

# Бонус (+0.2 балла):
Выведите список товаров в заказе и их количество прямо на странице заказа в админке.

