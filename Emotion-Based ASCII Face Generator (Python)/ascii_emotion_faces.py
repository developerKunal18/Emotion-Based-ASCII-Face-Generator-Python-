import random
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def choose(options):
    return random.choice(options)

def generate_face(emotion):
    # All parts are short text, and we will center them inside the box
    brows_map = {
        "happy":  ["^^", "~~", ""],
        "sad":    ["´ ´", "` `", ""],
        "angry":  ["> <", "^^", "¬ ¬"],
        "shock":  ["° °", "", ""],
        "smirk":  ["~  ", " ~", ""],
        "sleepy": ["- -", "¯ ¯", ""],
        "robot":  ["[==]", "[--]", ""],
    }

    eyes_map = {
        "happy":  ["^ ^", "o o", "• •"],
        "sad":    ["T T", "· ·", "u u"],
        "angry":  ["> <", "ಠ ಠ", "ò ò"],
        "shock":  ["O O", "0 0"],
        "smirk":  ["- .", ". -"],
        "sleepy": ["- -", "- .", ". -"],
        "robot":  ["0 0", "| |", "= ="],
    }

    mouth_map = {
        "happy":  ["___", "_U_", "\\_/", "‿‿‿"],
        "sad":    ["_n_", "‾‾_", "_‾‾", "︵"],
        "angry":  ["_▃_", "皿", "益"],
        "shock":  [" O ", "(O)", " 0 "],
        "smirk":  ["~__", "__~", "¯)", "(¯"],
        "sleepy": ["___", " z ", "-_-"],
        "robot":  ["[__]", "{==}", "(==)"],
    }

    # Nose is mostly fixed
    nose_options = [" | ", " : ", " ^ "]

    brows = choose(brows_map[emotion])
    eyes = choose(eyes_map[emotion])
    mouth = choose(mouth_map[emotion])
    nose = choose(nose_options)

    inner_width =  nine = 9  # width inside the box

    def line(content=""):
        return "| " + content.center(inner_width) + " |"

    top = "+" + "-" * (inner_width + 2) + "+"

    face = "\n".join([
        top,
        line(""),
        line(brows),
        line(eyes),
        line(nose),
        line(mouth),
        line(""),
        top,
    ])

    return face

def main():
    emotions = ["happy", "sad", "angry", "shock", "smirk", "sleepy", "robot"]

    while True:
        clear()
        print("🎭 ASCII Emotion Face Generator")
        print("Choose an emotion:\n")
        for i, e in enumerate(emotions, 1):
            print(f"{i}. {e.capitalize()}")

        choice = input("\nEnter number (or 'q' to quit): ")

        if choice.lower() == "q":
            break

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(emotions):
                clear()
                emotion = emotions[idx]
                print(f"🎭 Emotion: {emotion.upper()}\n")
                print(generate_face(emotion))
                input("\nPress Enter to generate another face...")
            else:
                print("Invalid choice!")
                input("\nPress Enter to continue...")
        except ValueError:
            print("Invalid input!")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
