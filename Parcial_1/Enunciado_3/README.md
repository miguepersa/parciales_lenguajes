## Simulador de BuddySystem

### Ejecucion
```python client.py <CANTIDAD_DE_MEMORIA>```

### Comandos
Reservar CANTIDAD de memoria y asignarle NOMBRE
```RESERVAR <CANTIDAD> <NOMBRE>```

Liberar el espacio de memoria que tenga asignado NOMBRE
```LIBERAR <NOMBRE>```

Mostrar el estado actual del sistema
```MOSTRAR```

Terminar la ejecucion del sistema
```SALIR```

### Tests
Se requiere tener instalado pytest en el sistema. Para instalarlo, ejecutar:
`pip install pytest`

Para ejecutar los tests:
```pytest```
o
```python -m pytest```