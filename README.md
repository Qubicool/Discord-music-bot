# Discord-music-bot
Данный проект разрабатывается для воспроизведения видео/музыки из youtube в discord.
Текущий функционал бота позволяет использовать следующие команды: 
* !play "название трека" или !play "ссылка на ютуб видео", после чего начнется воспроизвдение.
* !stop для остановки воспроизведения
* !pause для приостановки видео/трека
* !resume для продолжения видео/трека
Были использованы следующие технологии:
* Язык программирования python.
* Библиотеки:
* discord
* youtube_dl
* asyncio
* Библиотека discord позволяет нам взаимодействовать с API discord
* Библиотека youtube_dl позволяет нам взаимодействовать с youtube
* Библиотека asyncio позволяет заниматься асихронным программированием
* Для установки проекта необходимо получить токен на портале разработчиков discord, сделать это можно по ссылке https://discord.com/developers/applications
Для начала нужно создать приложение
Это можно сделать нажав на кнопку:

![image](https://user-images.githubusercontent.com/90842082/229178024-22f40a60-21e5-4a21-b54a-4678e97efaa0.png)

Затем перейти в  Bot 

![image](https://user-images.githubusercontent.com/90842082/229178222-9d2662fa-e7c2-44fc-aa97-96b3e073847e.png)

Затем необходимо получить токен

![image](https://user-images.githubusercontent.com/90842082/229178276-2f3afceb-82fd-4d65-8da7-d8707bd1146e.png)

Так же, сразу можно выдать дополнительные разрешения боту

![image](https://user-images.githubusercontent.com/90842082/229178336-5c2f61a6-77aa-40a7-a703-ac52ed8ce387.png)

Чтобы добавить бота на сервер, необходимо перейти OAuth2 –> URL Generator.

![image](https://user-images.githubusercontent.com/90842082/229178396-777f5f4d-07dd-4069-917e-60acb22d8a39.png)

Затем выбрать:

![image](https://user-images.githubusercontent.com/90842082/229178449-c1cb24ad-6b91-4801-bfc6-427c1cd41c62.png)

Затем необходимо скопировать ссылку и вставить в адресную строку браузера.
После чего выбираем тестовый сервер из списка и нажимаем "Продолжить" и далее "Авторизовать".

![image](https://user-images.githubusercontent.com/90842082/229178542-7e9adf00-313f-4d8e-a503-24fd4dd4067b.png)

* Затем необходимо установить библиотеки
* pip install discord.py
* pip install youtube_dl
* pip install asyncio
* Затем для работы с ботом необходимо установить ffmpeg, сделать это можно по ссылке: https://ffmpeg.org/download.html
И необходимо добавить FFMPEG в PATH, сделать это можно в свойствах системы, по кнопке переменные среды.

![image](https://user-images.githubusercontent.com/90842082/229179582-53155b48-0e5e-44cd-b189-6cd69a1f9f4c.png)

После, необходимо добавить 3 exe файла, которые находятся в папке bin

![image](https://user-images.githubusercontent.com/90842082/229179665-3ae08eda-a8b9-4d88-8757-9892205fbd43.png)

Добавить их нужно в PATH кликнув по кнопке изменить, а затем указать путь к папке с 3-мя exe
