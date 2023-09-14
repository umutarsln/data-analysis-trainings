# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"
# make upper even indexes and lower odd indexes

input = "hi my name is john and i am learning python"
# make upper even indexes and lower odd indexes
def solution(str):
    for i in range(len(str)):
        if i % 2 == 0:
            list_str = list(str)
            list_str[i] = list_str[i].upper()
            str = ''.join(list_str)   
        else:
            list_str = list(str)
            list_str[i] = list_str[i].lower()
            str = ''.join(list_str)
    
    print(str)


solution(input)

def alternateSol(str):
    new_str = ""
    for i in range(len(str)):
        if i % 2 == 0:
            new_str += str[i].upper()
        else:
            new_str += str[i].lower()
            
    print(new_str)

alternateSol(input)


def alternateSolEnum(str):
    new_str = ""
    for i,letter in enumerate(str):
        if i % 2 == 0:
            new_str += letter.upper()
        else:
            new_str += letter.lower()
    print(new_str)


alternateSolEnum(input)

