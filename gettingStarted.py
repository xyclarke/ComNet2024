### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "Are encoding and encryption the same? - Yes/No":
        return "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        return "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        return "No"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        return "No"
    elif question == "What is the SHA256 hashing value to the following message: 'NYU Computer Networking Fall 2023' - Use SHA256 hash generator and use the answer in your code":
        return "52a9b9b03b3e6113a89ae37772d20eee00d5fef678adbb1161dfd7a78c089684"
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        return "8e109c794c9af816b4ce3e0869e2c96fa6ce46cb3bd6f8d513ef249e1422f1a1"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        return "No"
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        return int(2)
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        return int(3)
    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        return "pcap"
    else:
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return answer

# Complete all the questions.
if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question_1 = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question_1))

    debug_question_2 = "Is it possible to decrypt a message without a key? - Yes/No"
    print(welcome_assignment_answers(debug_question_2))

    debug_question_3 = "Is it possible to decode a message without a key? - Yes/No"
    print(welcome_assignment_answers(debug_question_3))

    debug_question_4 = "Is a hashed message supposed to be un-hashed? - Yes/No"
    print(welcome_assignment_answers(debug_question_4))

    debug_question_5 = "What is the SHA256 hashing value to the following message: 'NYU Computer Networking Fall 2023' - Use SHA256 hash generator and use the answer in your code"
    print(welcome_assignment_answers(debug_question_5))

    debug_question_6 = "What is the SHA256 hashing value of your NYU email and use the answer in your code -"
    print(welcome_assignment_answers(debug_question_6))

    debug_question_7 = "Is MD5 a secured hashing algorithm? - Yes/No"
    print(welcome_assignment_answers(debug_question_7))

    debug_question_8 =  "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number"
    print(welcome_assignment_answers(debug_question_8))

    debug_question_9 = "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"
    print(welcome_assignment_answers(debug_question_9))


#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value to the following message: 'NYU Computer Networking Fall 2023' - Use SHA256 hash generator and use the answer in your code":
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
