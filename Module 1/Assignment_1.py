# import libraries
import random


def main():
    # create lists of nouns, verbs, adjectives, sentences, and resultant novel sentences
    nouns = ["smartphones", "rocks", "bandicoots", "noses", "buckets", "cars", "boots"]
    verbs = ["steal", "cook", "throw", "masticate", "force", "fabricate"]
    adjectives = ["perfect", "poor", "equine", "geriatric", "opulent", "blue", "scary", "antiquated"]

    sentences = ["The ubiquity of {noun} make them a {adj} tool to {verb} sensitive data from 3-D printers",
                 "Portable {noun} can be used to {verb} otherwise {adj} crowds.",
                 "The {adj} fellow over there is known to {verb} {noun}.",
                 "Be watchful of the {noun}. When they {verb} their food, it can be a {adj} site."]

    novel_sentences = []

    # create a list to hold the lists (we'll use this to quickly get the length of the longest list)
    picklists = [nouns, verbs, adjectives, sentences]
    # get the length of the longest list for use as our top end for user input
    len_longest_list = len(max(picklists, key=len))
    # print(len_longest_list)

    while True:
        # initialize a variable for user input that'll fail validation
        user_number = 0
        """
        1.	Prompt user for a number between 0 and the length of your biggest list
        2.	Validate user input for the following:
              a. Number is in the range defined above  [not larger than len_longest_list]
              b. Numbers are positive                  [greater than zero]
              c. Numbers are integers (Not floats)     [not an instance of type float]
        """
        while user_number > len_longest_list \
                or user_number <= 0 \
                or isinstance(user_number, float):
            try:
                user_number = eval(input('Please type a number from 1 to ' + str(len_longest_list) + " : "))
            except:
                # eat any non-numeric input
                continue
        # print(user_number)
        """
        3. The user’s input should be used as the lower bound used to find a random number.
         a. run the generator and use the resulting number to get 1 sentence from the list
         b. run the generator and use the resulting number to get 1 noun from the list.
         c. run the generator and use the resulting number to get 1 verb from the list.
         d. run the generator and use the resulting number to get 1 adjective from the list.
        """
        pick_index = random.randint(user_number, len(sentences) + user_number)
        novel_sentence = sentences[pick_index - user_number - 1]
        # or condensed
        noun = nouns[random.randint(user_number, len(nouns) + user_number) - user_number - 1]
        verb = verbs[random.randint(user_number, len(verbs) + user_number) - user_number - 1]
        adjective = adjectives[random.randint(user_number, len(adjectives) + user_number) - user_number - 1]
        """
        NOTES:set the upper bound to a value that is the sum of the user provided value and the length of the list
              this will then generate a value that is in a range of values with length equal to the length of the list
              subtracting back out the user_number will shift the value back into the range the length of the list
              and subtracting 1 brings it back into zero index range.
              not sure this is what they are looking for. Perhaps handling ValueError exception was the intent
        """

        # 4. Replace the selected noun, verb, adjective in the selected sentence.
        novel_sentence = novel_sentence.format(noun=noun, verb=verb, adj=adjective)
        """
        5. Check that the resulting sentence is unique(has not been used before).
        6. Print your current mad lib to the user (list of all completed sentences so far)
        NOTE: loop through the existing novel sentences, compare the new one to each and flag it if a match is found
              all the while printing them out so we only have to loop through them once
        """
        # assume the new sentence is unique
        is_unique = True
        for sentence_indexer in range(len(novel_sentences)):
            print(novel_sentences[sentence_indexer])
            if novel_sentence == novel_sentences[sentence_indexer]:
                # if it matches a sentence in the collection then it's not unique
                is_unique = False

        if is_unique:
            # a. If it has not been used before, save it in the list of completed sentences (your mad lib)
            novel_sentences.append(novel_sentence)
            print(novel_sentence)
        else:
            # b. If it has been used before, do not save it and print message letting the user know.
            print("Sorry that sentence has already been created.")
        """
        7. Ask user if he/she wants to keep playing (ans: y or n)
         a. Validate input
         b. If “y” go back to 1
         c. If “n” exit
        """
        go_again = ""
        while str.lower(go_again) != "y" and str.lower(go_again) != "n":
            try:
                go_again = input("Would you like to keep playing (y/n)? ")
            except:
                continue

        if str.lower(go_again) == "n":
            break

main()
