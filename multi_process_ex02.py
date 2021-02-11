import time
from multiprocessing import Pool

def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s

def sum_square_with_mp(numbers):
    # Questo ci permette di fare la time execution di questa funzione
    # prendo il tempo attuale del sistema, prima di fare qualsiasi cosa
    # in questa funzione
    start_time = time.time()
    # La classe Pool ha un argomento, il numero di processi
    # in cui vogliamo distribuire il pool.
    # Se non specifichiamo il numero, usa il massimo numero di processi
    p = Pool()
    # Questa funziona map mappa i processi
    result = p.map(sum_square, numbers)
    # Questo serve per far sì che tutto ciò che viene
    # dopo questa parte di codice deve aspettare che 
    # sia stata esegita e finita questa parte
    p.close()
    p.join()

    # In questo modo ottengo il tempo di esecuzione totale della 
    # funzione
    end_time = time.time() - start_time

    print(f"Processing {len(numbers)} numbers took {end_time} time using multiprocessing.")

# Ora creiamo una funzione che fa la stessa cosa della funzione precedente ma lo fa in modo 
# seriale

def sum_square_no_mp(numbers):
    start_time = time.time()
    result = []
    for i in numbers:
        result.append(sum_square(i))
    end_time = time.time() - start_time
    print(f"Processing {len(numbers)} numbers took {end_time} time using serial processing.")

if __name__ == '__main__':
    numbers = range(20000)
    sum_square_no_mp(numbers)
    sum_square_with_mp(numbers)
