
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😊",
        ":(" : "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return  output


msg = input(">")
converted = emoji_converter(msg)
print(converted)