# Connect-Four-Final-Game
A game coded in python

Las siguientes variables se utilizan para escoger cual de las posiciones es la más acertada, y almacenar el valor total
de todas las jugadas posibles.

```python
def h1(state):
      bestO = 0
      bestX = 0
      totalO = 0
      totalX = 0
```
Utilizamos state.utility para comprobar si se a alcanzado el final de la partida.

```python
    if state.utility == 1:
        return infinity
    if state.utility == -1:
        return -infinity
```

En el código que podemos observar a continuación funciona de la siguiente manera:
Para cada legal_moves (posición jugable) calculamos todos los potenciales cuatro en raya que existan (vertical, horizontal y ambas diagonales).
Por cada potencial cuatro en raya calculado, hacemos un pequeño cálculo para saber que jugada es la más óptima.
Finalmente devolvemos la diferencia entre los potenciales cuatro en raya de la máquina y el jugador humano, siendo esta negativa si es una
posición ventajosa para el jugador humano; positiva si es ventajosa para la

```python
    for x in legal_moves(state):
        totalX += k_in_row(state.board, x, 'X',(0,1))
        totalX += k_in_row(state.board, x, 'X',(1,0))
        totalX += k_in_row(state.board, x, 'X',(1,1))
        totalX += k_in_row(state.board, x, 'X',(1,-1))
        totalO += k_in_row(state.board, x, 'O',(0,1))
        totalO += k_in_row(state.board, x, 'O',(1,0))
        totalO += k_in_row(state.board, x, 'O',(1,1))
        totalO += k_in_row(state.board, x, 'O',(1,-1))

        if totalO > bestO:
            bestO = totalO
        if totalX > bestX:
            bestX = totalX
    return bestX - bestO
```

