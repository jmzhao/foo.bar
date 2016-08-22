def answer(digest):
    message = []
    raw = 0
    for encrypted in digest :
        raw = decrypt(encrypted, raw)
        message.append(raw)
    return message

def decrypt(encrypted, key) :
    return (encrypted ^ key) * 129 % 256
