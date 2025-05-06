Rozwiązanie zaimplementowane bez użycia konteneryzacji, oraz wymaga podania szczegółów połączenia z bazą danych Postgres w pliku config/settings.py.
Kroki wymagane do uruchomienia:
- Zainstalowanie wymaganych bibliotek: pip install -r requirements.txt
- Stworzenie migracji: python manage.py makemigrations
- Puszczenie migracji: python manage.py migrate
- Wymagana komenda do populowania bazy danych (20 hitów, 4 artystów): python manage.py populate_hits
- Odpalenie serwera: python manage.py runserver

Dostępne endpointy:
- [GET] /api/v1/hits - wyświetla listę 20 najnowszych utworów posortowanych po dacie dodania
- [GET] /api/v1/hits/{title_url} - wyświetla szczegóły pojedynczego utworu
- [POST] /api/v1/hits - tworzy nowy hit na podstawie przekazanych informacji: artist_id, title
- [PUT] /api/v1/hits/{title_url} – aktualizuje wybrany hit (można zaktualizować pola: artist_id, title)
- [DELETE] /api/v1/hits/{title_url} – usuwa wybrany hit
- [GET] /api/v1/artists - wyświetla listę artystów
