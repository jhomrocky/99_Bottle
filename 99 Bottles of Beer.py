"""
99 bottles of beer on the wall:
Rules: If list is used, use built-in function rather than hardcoding #'s
       No numbers/names directly in lyrics
       1 bottle left = "bottles" => "bottle"
       Blank line between each verse
"""

line_one = "bottles of beer on the wall"
line_two = "bottles of beer"

one_left = "more bottle of beer on the wall"
one_left_secondline = "more bottle of beer"
one_left_thirdline = "no more bottles of beer on the wall"


bottle_count = input("How many bottles you got? ")
bottle_count = int(bottle_count)
bottle_count_next = bottle_count - 1

while bottle_count >= 0:
    if bottle_count == 1:
        print("%d %s, %d %s. You take it down, pass it around, %s."% (bottle_count, one_left, bottle_count,
                                                                          one_left_secondline, one_left_thirdline))
        bottle_count -= 1
    elif bottle_count == 0:
        print("No more beer :(")
        break
    else:
        print("%d %s, %d %s. You take one down, pass it around, %d %s." % (bottle_count, line_one, bottle_count,
                                                                          line_two, bottle_count_next, line_one))
        bottle_count -= 1
        bottle_count_next -= 1

