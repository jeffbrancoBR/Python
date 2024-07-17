#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
# edited by Juan Rodriguez 7/17/24
#



def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else
    if x<y:
        result="x is less than y"
    elif x==y:
        result="x is the same as y" 
    else:
        result="x is greater than y"
    
    print(result)

    # conditional statements let you use "a if C else b"
    result = "x is less than y" if x<y else "x is greater than or the same as y"

    # match-case makes it easy to compare multiple values
    value = "one"
    match value:
        case "one":
            print("this is one")
        case "two":
            print("this is two")
        case "three" | "four":
            print("this is three or four")
        case _:
            print("this is something else")

    print(result)

if __name__ == "__main__":
    main()
