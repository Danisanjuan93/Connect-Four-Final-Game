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
Finalmente devolvemos la diferencia entre los potenciales cuatro en raya de la máquina y el jugador humano, siendo esta negativa si es una posición ventajosa para el jugador humano o positiva en caso contrario.

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

Declaración de los legal_moves

```python
def legal_moves(state):

    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y-1) in state.board]
```

Para finalizar, utilizamos la función ```python k_in_row``` para recorrer en todas las direcciones los posibles cuatro en raya.
Para el cálculo de este valor, ponderamos, dependiendo de si se trata de un cuatro en raya vertical, horizontal o diagonal, con un valor diferente siguiendo siempre el siguiente criterio:
            - Si se trata de un cuatro en raya en vertical, ponderamos con un valor de 50 si se trata de un espacio vacío lo que estamos observando, cuyo valor irá disminuyendo según vayamos recorriendo el tablero de manera vertical; y con un valor de 100 si se trata de un jugador (para player='O' ó player='X'). Esta misma ponderación se utiliza para la búsqueda en diagonal.
            - Para la búsqueda en horizontal ponderamos con 50 si se trata de un espacio vacío, y con un valor de 100 si se trata de un player.
Asímismo, contabilizamos la cantidad de fichas pertenecientes al mismo jugador que se encuentren de manera consecutiva (Ej/: XX_X es una posición ventajosa para la X, ya que produce su victoria de manera inmediata). Esto nos permite añadir un valor extra para dar prioridades a nuestra máquina en los casos de que se encuentren 3,4 o más fichas consecutivas.

```python
def k_in_row (board, move, player,(delta_x,delta_y)):
    x, y = move
    n = 0
    p = 1
    z = 0
    while (board.get((x, y)) == None or board.get((x, y)) == player) and y < 7 and x < 8:
         if x == (x + delta_x):
             if board.get((x, y)) == None:
                 n += 50 * p
                 p -= 0.10
         elif y == (y + delta_y):
             if board.get((x, y)) == player:
                z += 1
                n += 100
             elif board.get((x, y)) == None:
                n += 50
         elif y != (y + delta_y) and x != (x + delta_x):
             if board.get((x, y)) == player:
                 z += 1
                 n += 100
             elif board.get((x, y)) == None:
                 n += 50 * p
                 p -= 0.10
         x, y = x + delta_x, y + delta_y

    x, y = move
    p = 1
    while (board.get((x, y)) == None or board.get((x, y)) == player) and y > 0 and x > 0:
        if x == (x - delta_x):
             if board.get((x, y)) == player:
                 z += 1
                 n += 100
        elif y == (y - delta_y):
             if board.get((x, y)) == player:
                 z += 1
                 n += 100
             elif board.get((x, y)) == None:
                 n += 50
        elif y != (y - delta_y) and x != (x - delta_x):
             if board.get((x, y)) == player:
                 z += 1
                 n += 100
             elif board.get((x, y)) == None:
                 n += 50 * p
                 p -= 0.10
        x, y = x - delta_x, y - delta_y

    if z == 3:
        if player == 'X':
            n *= 6
        else:
            n *= 12
    if z >= 4:
        if player == 'X':
            n *= 9
        else:
            n *= 18
    return n
```
