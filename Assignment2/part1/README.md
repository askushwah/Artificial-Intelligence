<h1>Report</h1>
<p>Pichu is a board game which is similar to the chess but with little constraints into it. </p>
<b>Depth to search the tree = 7</b><br>

<b>Approach</b>:
<p>Firstly, functions are created for every board piece and all the possible moves it can make. While calculating the possible moves, the condition was also put in to check that which piece can attack what all pieces. All the possible moves are stored in the list with the following fomate:</p>

<br>"OriginalRow,OriginalColumn,FutureRow,FutureColumn,PieceToCapture"  </b>
<p>This was one of the way to get the position in a constant time. And every time need to change the position, we make changes in such a format only.  </p>

<b>Heuristic function:</b>
We have assigned different weights to each piece on the chessboard and which are as follows:  
1)Parakeet=100 points  
2)Rook=500 points  
3)Nighthawk=300 points  
4)Bishop=300 x  No. of bishops on the board  
5)Queen=900 points  
6)King=1700 points (This figure was actually came through great number of hit and trails J )  

Since one bishop can cover only half of the board, therefore multiply the weight of the bishop with the number of bishops on the chessboard.
The heuristic function is the difference of the weighted sum of all the white pieces and the black pieces on the chessboard.
To explain it more further, the example could be:  
h(n)=100(# of white parakeets - # of black parakeets) + 500(# of white rooks - # of black rooks)+ .....  

The heuristic function will calculate the number of moves possible from a given state, which will be added to the heuristic value.  

<b>Difficulties:</b> 
Special conditions are kept in check so as to avoid the loop going in the negative. This was one of the biggest challenges because there was one condition which failed after integration and it was difficult to find as all the moves for all pieces on the board were jumbled. But the problem aroused, ensued and was overcome J.

