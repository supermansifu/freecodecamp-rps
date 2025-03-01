import random

def player(prev_play, opponent_history=[]):
    if not prev_play:
        guess = random.choice(["R", "P", "S"])
    else:
        opponent_history.append(prev_play)

        # Strategies for different opponents:
        if len(opponent_history) > 3:
            #quincy strategy
            if all(x == opponent_history[-1] for x in opponent_history[-3:]):
                if opponent_history[-1] == "R":
                    guess = "P"
                elif opponent_history[-1] == "P":
                    guess = "S"
                else:
                    guess = "R"
            #abbey strategy
            elif opponent_history[-1] == opponent_history[-3]:
                if opponent_history[-1] == "R":
                    guess = "P"
                elif opponent_history[-1] == "P":
                    guess = "S"
                else:
                    guess = "R"
            #kris strategy
            elif len(opponent_history) > 10:
                recent = opponent_history[-10:]
                most_frequent = max(set(recent), key=recent.count)
                if most_frequent == "R":
                    guess = "P"
                elif most_frequent == "P":
                    guess = "S"
                else:
                    guess = "R"
            #mrugesh strategy
            elif len(opponent_history) > 5:
                prediction = ""
                pattern_len = 3
                if len(opponent_history) >= pattern_len:
                    last_pattern = opponent_history[-pattern_len:]
                    potential_next_moves = []
                    for i in range(len(opponent_history) - pattern_len):
                        if opponent_history[i:i + pattern_len] == last_pattern:
                            potential_next_moves.append(opponent_history[i + pattern_len])
                    if potential_next_moves:
                        prediction = max(set(potential_next_moves), key=potential_next_moves.count)
                    if prediction:
                        if prediction == "R":
                            guess = "P"
                        elif prediction == "P":
                            guess = "S"
                        else:
                            guess = "R"
                    else:
                        guess = random.choice(["R", "P", "S"])
                else:
                    guess = random.choice(["R", "P", "S"])
            else:
                guess = random.choice(["R", "P", "S"])
        else:
            guess = random.choice(["R", "P", "S"])

    return guess