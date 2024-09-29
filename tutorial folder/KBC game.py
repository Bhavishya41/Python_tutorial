print("Let's play 'Kaun banega crorepati'")
print("Are you ready?")
input()

questions = [
    "Question 1: You must have used the UPI facility. What does this mean?",
    "Question 2: Portuguese were the first European to come to India. When did the Portuguese leave India?",
    "Question 3: Who was said to be the last viceroy of India?",
    "Question 4: Where is the headquarters of the World Economic Forum?",
    "Question 5: What is the currency of Iraq?",
    "Question 6: Lake Tanganyika is the world's longest freshwater lake located in?",
    "Question 7: Where is the Keshopur Ramsar Site situated?",
    "Question 8: What is the total number of members in BIMSTEC?",
    "Question 9: When was the State Bank of India founded?",
    "Question 10: Name any two examples of cryptocurrency.",
    "Question 11: How many schedules were there in the original Constitution of India?",
    "Question 12: If there was Monday on Jan 1, 1992, then which day was there on Jan 1, 1993?",
    "Question 13: Where is City Birds Wildlife Sanctuary?",
    "Question 14: Which mountains serve as the boundary between Europe and Asia?",
    "Question 15: Where is Bandhavgarh & Panna National Park located?",
    "Question 16: What are the official languages of Mizoram?"
]

options = [
    "a) Unified Payments Interface\nb) Unified Payments Interface\nc) Unified Payment Interface\nd) Unified Payments Interface",
    "a) 1947\nb) 1955\nc) 1961\nd) 1975",
    "a) Lord Curzon\nb) Lord Mountbatten\nc) Lord Wavell\nd) Lord Linlithgow",
    "a) New York, USA\nb) Geneva, Switzerland\nc) Paris, France\nd) Davos, Switzerland",
    "a) Dinar\nb) Rial\nc) Pound\nd) Lira",
    "a) North America\nb) Europe\nc) Africa\nd) Asia",
    "a) Punjab\nb) Haryana\nc) Rajasthan\nd) Gujarat",
    "a) 5\nb) 6\nc) 7\nd) 8",
    "a) 1947\nb) 1955\nc) 1969\nd) 1976",
    "a) Bitcoin and Ethereum\nb) Dollar and Euro\nc) Litecoin and Yen\nd) Rupee and Ripple",
    "a) 8\nb) 10\nc) 12\nd) 14",
    "a) Tuesday\nb) Wednesday\nc) Thursday\nd) Friday",
    "a) Delhi\nb) Punjab\nc) Gujarat\nd) Maharashtra",
    "a) Andes\nb) Himalayas\nc) Ural Mountains\nd) Alps",
    "a) Madhya Pradesh\nb) Uttar Pradesh\nc) Karnataka\nd) Rajasthan",
    "a) Mizo and Hindi\nb) Mizo and English\nc) Mizo and Bengali\nd) Mizo and Assamese"
]

answers = ["a", "c", "b", "d", "a", "c", "a", "c", "b", "a", "a", "b", "a", "c", "a", "b"]
correct_answers = [
    "a) Unified Payments Interface", "c) 1961", "b) Lord Mountbatten", "d) Davos, Switzerland", "a) Dinar", 
    "c) Africa", "a) Punjab", "c) 7", "b) 1955", "a) Bitcoin and Ethereum", "a) 8", "b) Wednesday", 
    "a) Delhi", "c) Ural Mountains", "a) Madhya Pradesh", "b) Mizo and English"
]

prize_amounts = [
    "1000rs", "2000rs", "3000rs", "5000rs", "10000rs", "20000rs", "40000rs", "80000rs", "160000rs", 
    "320000rs", "640000rs", "1250000rs", "2500000rs", "5000000rs", "1CR", "7CR"
]

for i in range(len(questions)):
    print(f"Here's your question for {prize_amounts[i]}\n{questions[i]}")
    print(options[i])
    print("Enter your answer in either a, b, c or d:")
    user_input = input().strip().lower()
    if user_input == answers[i]:
        print(f"Your answer is correct. You won {prize_amounts[i]}.")
        if i < len(questions) - 1:
            print("Moving on to the next question.")
    else:
        print("Sorry, you're wrong.")
        print(f"The correct answer is: {correct_answers[i]}")
        print("It was nice playing with you. Better luck next time!")
        break
else:
    print("Congratulations! You've answered all the questions correctly and won the grand prize!")