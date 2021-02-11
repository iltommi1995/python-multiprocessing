import time
from multiprocessing import Pool

def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s

if __name__ == '__main__':
    numbers = range(5)
    # La classe Pool ha un argomento, il numero di processi
    # in cui vogliamo distribuire il pool.
    # Se non specifichiamo il numero, usa il massimo numero di processi
    p = Pool()
    # Questa funziona map mappa i processi
    result = p.map(sum_square, numbers)
    print(result)
    # Questo serve per far sì che tutto ciò che viene
    # dopo questa parte di codice deve aspettare che 
    # sia stata esegita e finita questa parte
    p.close()
    p.join()

