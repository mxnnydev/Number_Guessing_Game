from time import sleep
def life_health():
    health = 3
    score = 0


health = ["❤️", "❤️", "❤️"]


for x in range(len(health) - 1, -1, -1):
    health[x] =  "💔"
    print(" ".join(health))
    sleep(.5)


