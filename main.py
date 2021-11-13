# Write a program that asks the user how many
# people are in their dinner group. If the answer is
# more than eight, print a message saying they will
# have to wait for a table. Otherwise, report that
# their table is ready.
prompt = "How many people are in your dinner " \
         "party?: "
party = input(prompt)

if party >= str(8):
    print(f"I apologize, but your party of {party} is "
          f"greater than or equal to 8, and you will have "
          f"to wait to be seated.")
else:
    print(f"Your party of {party} is ready to be seated.")
