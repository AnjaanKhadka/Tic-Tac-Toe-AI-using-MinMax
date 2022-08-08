# AI Tic-Tac-Toe using Min-Max Algorithm

## Min-Max Algorithm

Min Max algorithm is simple algorithm used in decision making and game theory. This algorithm recursively checks all possible games possible from current state and moves where there is least risk. This algorithm assumes opponent will always move their best move. Even when opponent doesnot move best move, this algorithm works fine.

![Wikipedia Image for min max algorithm](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Minimax.svg/1920px-Minimax.svg.png)

To know more about [Min-Max](https://en.wikipedia.org/wiki/Minimax) algorithm, follow the link.

This algorithm fails to implement [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha–beta_pruning). Alpha Beta pruning is technique to fasten the search process in the decision tree without loosing its efficiency.

## Requirements

All requirements required are listed in [requirements.txt](https://github.com/AnjaanKhadka/Tic-Tac-Toe-AI-using-MinMax/blob/master/requirements.txt) file.

To Install those requirements, execute following code.

    pip install -r reqirements.txt

## Execution

This project compacts all functions / Methods into the same file.

Execute following code to test the AI.

    python main.py

## Results

Generally AI is fast enough to get unnoticed. But ocasionally it needs just more than 1 sec to get its first move. From the second move it always feels instantaneous.

This AI never loses in tic-tac-toe, but there will be some game player will loose. If the player also plays perfect game, no one wins no matter who starts the game

Game Board

![Image of initial game screen](https://github.com/AnjaanKhadka/Tic-Tac-Toe-AI-using-MinMax/blob/master/results/initial_screen.png)

AI winning

![Image of AI winning](https://github.com/AnjaanKhadka/Tic-Tac-Toe-AI-using-MinMax/blob/master/results/AI_win.png)

Game resulting in tie

![Image of a tie game](https://github.com/AnjaanKhadka/Tic-Tac-Toe-AI-using-MinMax/blob/master/results/game_tie.png)