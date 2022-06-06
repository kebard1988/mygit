Flask server

https://nuancesprog.ru/p/7105/

Если вы просто хотите инициализировать свою БД в самый первый раз, вы можете использовать этот простой способ.

volumes:
      - [the scripts dir]:/docker-entrypoint-initdb.d
