Opis poszczególnych kroków:

Używamy oficjalnego obrazu Pythona 3.9 jako warstwy bazowej.
Dodajemy metadane - autor pliku Dockerfile.
Ustawiamy zmienną środowiskową PORT na wartość 8000.
Kopiujemy plik z kodem aplikacji (server.py) do katalogu /app w obrazie.
Ustawiamy katalog roboczy na /app.
Instalujemy wymaganą bibliotekę http.server przy pomocy pip.
Uruchamiamy serwer poprzez wykonanie pliku server.py za pomocą komendy CMD.
Określamy port, na którym nasłuchuje serwer, za pomocą EXPOSE.

Zadanie 3:
a. Polecenie do zbudowania obrazu kontenera:
 docker build -t server .
b. Polecenie do uruchomienia kontenera na podstawie zbudowanego obrazu:
docker run -p 8000:8000 server
c. Aby uzyskać informacje wygenerowane przez serwer w trakcie uruchamiania kontenera, można użyć polecenia docker logs:
docker logs zad1
d. Aby sprawdzić, ile warstw posiada zbudowany obraz, można użyć polecenia docker history:
docker history server