digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']

numbers = {}
for r in range(len(digits)):
    numbers[digits[r]] = {'english': en[r], 'french': fr[r]}

print(numbers)