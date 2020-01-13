#!/usr/bin/env python3

def display_welcome():
    print("The Quarterly Sales program")
    print("")

def get_scores():
    scores = []
    for i in range(1,5):
        scores.append(float(input("Enter sales for Q" + str(i) + ":")))
    return scores
    round (score, 2)
def process_scores(scores):
    # calculate average score
    score_total = 0
    for score in scores:
        score_total += score 
    scores = sorted(scores)
    low = scores[0]
    high = scores[len(scores) - 1]
    round (score, 2)

    # format and display the result
    print()
    print("Total:\t\t\t", score_total)
    print("Average Quarter:\t", score_total / len(scores))
    print("Lowest Quarter:\t\t", low)
    print("Highest Quarter:\t", high)
    round (score, 2)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

