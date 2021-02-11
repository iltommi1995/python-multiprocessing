import time
import multiprocessing
import concurrent.futures


# Usiamo il multiprocessing quando velocizza il nostro programma

def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    print('Done Sleeping...')

def without_mp(seconds):
    start = time.perf_counter()
    do_something(seconds)
    do_something(seconds)
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s) without multiprocessing')

def with_mp(seconds):
    start = time.perf_counter()

    # Qui sto creando un processo, prende come parametro la function che voglio 
    # eseguire
    p1 = multiprocessing.Process(target=do_something, args=[seconds])   
    p2 = multiprocessing.Process(target=do_something, args=[seconds])   
    # Se eseguissi adesso non succederebbe nulla, perchè ora ho solo dichiarato i 
    # processi ma non ho eseguito nulla, per eseguire devo fare:
    p1.start()
    p2.start()
    # Se lo eseguissi ora, direbbe comunque che ci impiega 0 secondi, perchè mentre
    # le due funzioni vengono eseguire, il programma continua ad avanzare e stampa
    # la stringa alla fine della function. Per risolvere il problema uso:
    p1.join()
    p2.join()
    
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s) with multiprocessing')


# Provo una terza funzione in cui utilizzo una lista di processi, anziché usare 
# ogni processo a sè stante

def with_mp_list(seconds):
    start = time.perf_counter()
    processes = []

    for _ in range(2):
        p = multiprocessing.Process(target=do_something, args=[seconds])
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s) with multiprocessing and list')



if __name__ == "__main__":
    without_mp(2)
    with_mp(2)
    with_mp_list(2)