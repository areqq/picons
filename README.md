# Idea

Celem projektu jest zbudowanie bazy picon w różnych wersjach, którą będzie łatwo aktualizować i dostosowywać do zmian na orbicie. Na podstawie tych danych mogą byc budowane ipk z zestawem picon, może powstać plugin zaciągający picony do aktualnej listy kanałów itp. 

# Założenia

channels.txt - zawiera listę nazwy kanałów dla których mamy picony- lista jest unikalna i posortowana alfaberycznie, w pliku mogą być komentarze w liniach zaczynających się od #

ref2channels.txt - zawiera przypisanie referencja kanału do nazwa kanału z channels.txt, referancja jest unikalna, plik posortowany alfabetycznie

channels2ref.py - skrypt budujący w out - zestaw pikon do podegrania na tuner

picon - folder z zestawiami picon, struktura dwupoziomowa: rozmiar, wersja picon np: picon/100x60/gos_marcin/

ConsistencyCheck.py - skrypt weryfukujący spójność danych, przed commitem do repo należy go uruchomić i poprawić ewentualne błędy

attic - folder z todo i plikami do przejrzenia/uporządkowania



