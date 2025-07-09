# Atari Gymnasium In class Activity - Group 3
This code demonstrates random action selection in OpenAI Gymnasium environments as part of a classroom activity.

## Environment
- **Environment Used**: FrozenLake-v1
- **Objective**: Navigate from start to goal without falling in holes
- **Actions**: 0=Left, 1=Down, 2=Right, 3=Up

## Requirements
```bash
pip install gymnasium
```

## How to Run
```bash
python breakout.py
```

## What the Code Does
1. Loads the FrozenLake-v1 environment
2. Takes random actions in a loop
3. Prints after each action:
   - Action taken
   - Next state
   - Reward received
   - Total reward
   - Termination status
4. Terminates when goal reached or max steps exceeded

## Output
The script displays step-by-step information showing:
- Random actions being selected
- State transitions after each action  
- Rewards accumulated
- Episode termination conditions

## Authors
- Eunice Adewusi
- Audry Chivanga
- Humphrey Nyahoja
- Liliane Kayitesi
- Jean Chrisostome
- Ronald Abimbola