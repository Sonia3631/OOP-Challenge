class Pet:
    def __init__(self, name, pet_type="dog"):
        self.name = name
        self.pet_type = pet_type  # Customizable pet type
        self.hunger = 0  # Hunger level (0 = full, 10 = very hungry)
        self.energy = 10  # Energy level (0 = tired, 10 = fully rested)
        self.happiness = 5  # Starting happiness level
        self.health = 10  # Health level (0–10)
        self.age = 0  # Pet's age
        self.tricks = []  # List of learned tricks

    def eat(self, food="generic"):
        if food == "treat":
            self.hunger = max(0, self.hunger - 5)  # Treats are extra filling
            self.happiness = min(10, self.happiness + 2)
        else:
            self.hunger = max(0, self.hunger - 3)  # Generic food reduces hunger
            self.happiness = min(10, self.happiness + 1)
        self.update_health()
        print(f"{self.name} enjoyed the {food}! 🍖")

    def sleep(self):
        if self.energy < 10:
            self.energy = min(10, self.energy + 5)  # Restore energy
            print(f"{self.name} is now well-rested! 🛌")
        else:
            print(f"{self.name} is not tired and doesn't need sleep. 🌙")

        self.update_health()

    def play(self):
        if self.energy >= 2:  # Enough energy to play
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} had a great time playing! 🎾")
        else:
            print(f"{self.name} is too tired to play. Let them rest! 😴")
        self.update_health()

    def train(self, trick):
        if self.energy >= 3:  # Ensure energy for training
            self.energy -= 3
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 2)
            print(f"{self.name} learned a new trick: {trick}! 🐾")
        else:
            print(f"{self.name} is too tired to learn new tricks. 💡")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)} 🐕")
        else:
            print(f"{self.name} hasn't learned any tricks yet. 🤷")

    def get_status(self):
        print(f"\nStatus of {self.name} ({self.pet_type}):")
        print(f"🐾 Hunger: {self.hunger}")
        print(f"⚡ Energy: {self.energy}")
        print(f"😊 Happiness: {self.happiness}")
        print(f"❤️ Health: {self.health}")
        print(f"🎂 Age: {self.age}\n")

    def update_health(self):
        # Health decreases if hunger is high or energy is low
        self.health = max(0, 10 - ((self.hunger + (10 - self.energy)) // 2))

    def get_mood(self):
        if self.happiness >= 8:
            mood = "Happy 😊"
        elif 4 <= self.happiness < 8:
            mood = "Content 😌"
        else:
            mood = "Sad 😢"
        print(f"{self.name} is feeling {mood}.")

    def age_pet(self):
        self.age += 1
        self.energy = max(0, self.energy - 1)  # Aging decreases energy
        self.happiness = max(0, self.happiness - 1)  # Aging decreases happiness
        self.update_health()
        print(f"{self.name} is now {self.age} years old! 🎉")

    def cuddle(self):
        self.happiness = min(10, self.happiness + 3)  # Cuddling boosts happiness
        print(f"{self.name} loves cuddling with you! 🤗")