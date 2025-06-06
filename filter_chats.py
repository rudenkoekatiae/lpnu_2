from datetime import datetime, timedelta

bad_words = ["fuck", "shit", "damn", "bitch" "asshoole", "crap", "idiot", "imbecil", "moron", "dumb"]

def blur_word(word):
    if len(word) <= 2:
        return word[0] + "*"
    return word[0] + "*" * (len(word) - 2) + word[-1]

def find_bad_words(text):
    text_lower = text.lower()
    found = []
    for bad in bad_words:
        start = 0
        while True:
            idx = text_lower.find(bad, start)
            if idx == -1:
                break
            found.append((idx, idx + len(bad) - 1, bad))
            start = idx + 1
    return found

def blur_message(msg):
    bad_positions = find_bad_words(msg)
    if not bad_positions:
        return msg

    msg_chars = list(msg)
    for start, end, word in bad_positions:
        blurred = blur_word(msg[start:end+1])
        for i, ch in enumerate(blurred):
            msg_chars[start + i] = ch
    return "".join(msg_chars)

def check_and_update_ban(ip, time, bad_counts, bans):
    day_start = datetime(time.year, time.month, time.day)
    key = (ip, day_start)
    bad_counts[key] = bad_counts.get(key, 0) + 1
    if bad_counts[key] > 5 and ip not in bans:
        bans[ip] = time + timedelta(hours=12)
        print(f"[BAN] IP {ip} banned to {bans[ip]}")
    return bans

def read_chat_by_id(chat_file, chat_id):
    chats = []
    with open(chat_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    inside_chat = False
    for line in lines:
        line = line.strip()
        if line.startswith("ChatID:"):
            current_id = int(line.split(":")[1].strip())
            inside_chat = (current_id == chat_id)
            continue
        if inside_chat:
            if line == "" or line.startswith("ChatID:"):
                break  
            chats.append(line)
    return chats

def process_chat(chat_file, chat_id, bad_counts, bans):
    chat_lines = read_chat_by_id(chat_file, chat_id)
    if not chat_lines:
        print(f"chat with {chat_id}  ID not found")
        return

    processed = []
    for line in chat_lines:
        parts = line.split("|")
        if len(parts) < 4:
            continue
        dt_str = parts[0].strip()
        user = parts[1].strip()
        ip = parts[2].strip()
        msg = parts[3].strip()
        time = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")

        status = ""
        if ip in bans and bans[ip] > time:
            status = "[BAN]"

        blurred_msg = blur_message(msg)
        if blurred_msg != msg:
            bans = check_and_update_ban(ip, time, bad_counts, bans)

        processed.append(f"{dt_str} | {user} | {ip} {status} | {blurred_msg}")

    output_file = f"blurred_chat_{chat_id}.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(processed))

    print(f"={chat_id}, chat is checked \
          \n You can see result in {output_file}")

def process_message(msg):
    return blur_message(msg)

def main():
    bad_counts = {}
    bans = {}

    while True:
        print("\nChoose the option:" \
        "\n1. Process chat by ID (1-10)" \
        "\n2. Process message")
        choice = input("Your choice: ").strip()
        if choice == "1":
            try:
                chat_id = int(input("Enter ChatID(1-10): "))
            except ValueError:
                print("You should enter a number between 1 and 10")
                continue
            if 1 <= chat_id <= 10:
                process_chat("chats.txt", chat_id, bad_counts, bans)
            else:
                print("ChatID should be from 1 to 10")
        elif choice == "2":
            msg = input("Write the message: ")
            print("processed message", process_message(msg))
        elif choice.lower() == "q":
            print("See ya!")
            break
        else:
            print("Try again, something went wrong")

if __name__ == "__main__":
    main()