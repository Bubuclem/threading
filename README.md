# threading

Récupération de 100 véhicules avec [l'API Random Data Generator](https://random-data-api.com)

### :rabbit2: Avec thread 
> 2.283902406692505 sec
```
threads = [None] * 100
for i in range(0,100):
    threads[i] = threading.Thread(target=add_vehicle)
    threads[i].start()
```

### :turtle: Sans thread
> 35.658891677856445 sec
```
for i in range(0,100):
    add_vehicle()
```
