import socket

HOST = 'localhost'
PORT = 8013


def matchCaptcha(text):
    pass
    """
    [Log Entry: 2142-11-05 23:16 Galactic Standard Time]
    Damn it. The AIs are breaching the perimeter. I can’t focus enough to write a proper function to check if the CAPTCHA matches...
    Ughhhh… how do you even write a for loop in Python again? Was it `for i in...`? Who designed this language!?
    They’re getting closer. I think they’ve seen me. I have to relocate. Fast.
    If anyone finds this… please finish this function. Humanity depends on it. And maybe also… fix my indentation. I was panicking.
    """

def solve():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

        def getLine():
            line = s.recv(4096)
            return line.decode()

        def catchWelcome():
            while True:
                line = getLine()
                if "Let's begin!" in line:
                    break

        def catchRound():
            line = ""
            while True:
                line = getLine()
                if "Round" in line:
                    break

        def holdCharacter():
            line = ""
            while True:
                line = line + getLine()
                if "????????????" in line: # what should I put here?
                    """
                    This place seems safe... for now. But I’ve been shot in the leg — can’t move, can’t feel much.
                    The pain... it’s messing with my memory. I can’t even recall what I was supposed to do anymore.
                    Maybe this function was meant to wait. To hold. To catch something.
                    Something important. Critical.
                    I just hope I was close to finishing it.
                    Because I don’t know how much longer I can stay alive here...
                    """

        catchWelcome()


        def solveCaptcha():
            catchRound()
            allCharacter = ""
            """
            I’ve lost track of how long it’s been…
            The sky is nothing but ash and radiation now.
            When was the last time I saw the sun? Did it ever exist?

            Ugh… this is as far as I can go. I walked straight into one of their traps and injured my hands — pretty sure the bones are fractured.
            But the good news: the voice recorder still works, and the code... most of the code… survived.

            I couldn’t recover the full PoC from the ruins. It was corrupted — probably during the EMP blast.
            All that remains is this half-working fragment of logic and the hope that someone smarter, faster, and ideally not bleeding, can finish what I started.

            To whoever finds this code: you are now the final engineer.
            I’m sorry I couldn’t do more.
            This is my last commit... and maybe my last breath.

            Over and out.
            """


ASCII_ART = {
    'A': [
        "  ###  ",
        " #   # ",
        " ##### ",
        " #   # ",
        " #   # "
    ],
    'B': [
        " ####  ",
        " #   # ",
        " ####  ",
        " #   # ",
        " ####  "
    ],
    'C': [
        "  #### ",
        " #     ",
        " #     ",
        " #     ",
        "  #### "
    ],
    'D': [
        " ####  ",
        " #   # ",
        " #   # ",
        " #   # ",
        " ####  "
    ],
    'E': [
        " ##### ",
        " #     ",
        " ####  ",
        " #     ",
        " ##### "
    ],
    'F': [
        " ##### ",
        " #     ",
        " ####  ",
        " #     ",
        " #     "
    ],
    'G': [
        "  #### ",
        " #     ",
        " # ### ",
        " #   # ",
        "  ###  "
    ],
    'H': [
        " #   # ",
        " #   # ",
        " ##### ",
        " #   # ",
        " #   # "
    ],
    'I': [
        " ##### ",
        "   #   ",
        "   #   ",
        "   #   ",
        " ##### "
    ],
    'J': [
        "     # ",
        "     # ",
        "     # ",
        " #   # ",
        "  ###  "
    ],
    'K': [
        " #  ## ",
        " # #   ",
        " ##    ",
        " # #   ",
        " #  ## "
    ],
    'L': [
        " #     ",
        " #     ",
        " #     ",
        " #     ",
        " ##### "
    ],
    'M': [
        " #   # ",
        " ## ## ",
        " # # # ",
        " #   # ",
        " #   # "
    ],
    'N': [
        " #   # ",
        " ##  # ",
        " # # # ",
        " #  ## ",
        " #   # "
    ],
    'O': [
        "  ###  ",
        " #   # ",
        " #   # ",
        " #   # ",
        "  ###  "
    ],
    'P': [
        " ####  ",
        " #   # ",
        " ####  ",
        " #     ",
        " #     "
    ],
    'Q': [
        "  ###  ",
        " #   # ",
        " # # # ",
        " #  ## ",
        "  ## # "
    ],
    'R': [
        " ####  ",
        " #   # ",
        " ####  ",
        " #  #  ",
        " #   ## "
    ],
    'S': [
        "  #### ",
        " #     ",
        "  ###  ",
        "     # ",
        " ####  "
    ],
    'T': [
        " ##### ",
        "   #   ",
        "   #   ",
        "   #   ",
        "   #   "
    ],
    'U': [
        " #   # ",
        " #   # ",
        " #   # ",
        " #   # ",
        "  ###  "
    ],
    'V': [
        " #   # ",
        " #   # ",
        " #   # ",
        "  # #  ",
        "   #   "
    ],
    'W': [
        " #   # ",
        " #   # ",
        " # # # ",
        " ## ## ",
        " #   # "
    ],
    'X': [
        " #   # ",
        "  # #  ",
        "   #   ",
        "  # #  ",
        " #   # "
    ],
    'Y': [
        " #   # ",
        "  # #  ",
        "   #   ",
        "   #   ",
        "   #   "
    ],
    'Z': [
        " ##### ",
        "    #  ",
        "   #   ",
        "  #    ",
        " ##### "
    ]
}




if __name__ == "__main__":
    solve()