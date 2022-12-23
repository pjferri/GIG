import random
import tkinter as tk

# List of game ideas
game_ideas = [
"Create a game where you play as a time traveler who has to fix historical events gone wrong",
"Design a game where you control a team of robots on a mission to save the world from an alien invasion",
"Make a game about a group of animals who have to work together to escape from a zoo",
"Create a game where you play as a superhero who has to stop villains from taking over the city",
"Design a game where you control a group of space explorers on a mission to colonize a distant planet",
"Make a game about a group of friends who have to survive a zombie apocalypse",
"Create a game where you play as a detective who has to solve mysteries in a city full of secrets",
"Design a game where you control a group of treasure hunters on a quest to find a lost civilization",
"Make a game about a group of farmers who have to save their farm from a zombie invasion",
"Create a game where you play as a wizard who has to save the world from dark magic",
"Design a game where you control a team of superheroes on a mission to save the galaxy",
"Make a game about a group of animals who have to save their forest from destruction",
"Create a game where you play as a detective who has to solve supernatural mysteries",
"Design a game where you control a group of pirates on a quest to find a hidden treasure",
"Make a game about a group of survivors who have to rebuild society after an apocalyptic event",
"Create a game where you play as a dragon who has to defend your hoard from adventurers",
"Design a game where you control a team of astronauts on a mission to explore deep space",
"Make a game about a group of animals who have to escape from a laboratory",
"Create a game where you play as a superhero who has to stop a mad scientist from taking over the world",
"Design a game where you control a group of soldiers on a mission to stop a global threat",
"Make a game about a group of kids who have to save their town from monsters",
"Create a game where you play as a wizard who has to save the world from an evil sorcerer",
"Design a game where you control a team of superheroes on a mission to stop a supervillain",
"Make a game about a group of animals who have to rescue their friends from a pet store",
"Create a game where you play as a detective who has to solve crimes in a city full of superheroes and supervillains",
"Design a game where you control a group of pirates on a quest to find a lost treasure",
"Make a game about a group of survivors who have to fight off a horde of zombies",
"Create a game where you play as a dragon who has to save your kingdom from an evil sorcerer",
"Design a game where you control a team of astronauts on a mission to explore a distant planet",
"Make a game about a group of kids who have to save their school from monsters",
"Create a game where you play as a superhero who has to stop a criminal organization from taking over the world",
"Design a game where you control a group of soldiers on a mission to stop a terrorist",
"Make a game about a group of friends who have to survive a post-apocalyptic wasteland",
"Create a game where you play as a detective who has to solve mysteries in a futuristic city",
"Design a game where you control a team of superheroes on a mission to save the universe from an evil villain",
"Make a game about a group of animals who have to escape from a laboratory and save their forest from destruction",
"Create a game where you play as a wizard who has to save the world from an evil sorcerer and his army of monsters",
"Design a game where you control a team of treasure hunters on a quest to find a legendary artifact that can save the world",
"Make a game about a group of survivors who have to rebuild society after an apocalyptic event and defend against the dangers of the wasteland",
"Create a game where you play as a dragon who has to defend your kingdom from an invading army of orcs",
"Design a game where you control a team of astronauts on a mission to explore a mysterious alien planet",
"Make a game about a group of kids who have to save their town from an alien invasion",
"Create a game where you play as a detective who has to solve mysteries in a city full of supernatural beings",
"Design a game where you control a group of treasure hunters on a quest to find a hidden city of gold",
"Make a game about a group of survivors who have to navigate the dangers of a post-apocalyptic world and rebuild society",
"Create a game where you play as a superhero who has to save the world from a villainous organization bent on world domination",
"Design a game where you control a team of space explorers on a mission to colonize a distant planet and face challenges along the way",
"Make a game about a group of animals who have to escape from a laboratory and reunite with their families in the wild",
"Create a game where you play as a detective who has to solve crimes in a city full of superheroes and supervillains and unravel the mystery behind a string of crimes",
"Design a game where you control a group of pirates on a quest to find a cursed treasure and defeat the ghostly pirate who guards it",
"Make a game about a group of survivors who have to defend their community from a horde of zombies and find a way to survive in the long term",
"Create a game where you play as a dragon who has to save your kingdom from an evil sorcerer and his army of dark creatures",
"Design a game where you control a team of superheroes on a mission to save the universe from an evil villain and his army of space monsters",
"Make a game about a group of animals who have to save their forest from destruction and protect their home from human encroachment."
]

# Function to generate a random game idea
def generate_game_idea():
  # Select a random game idea from the list
  random_index = random.randint(0, len(game_ideas) - 1)
  random_game_idea = game_ideas[random_index]

  # Update the game idea label with the new game idea
  game_idea_label.config(text=random_game_idea)

# Create the main window
root = tk.Tk()
root.title("Game Idea Generator")

# Set the window size and position
#root.geometry("400x200+300+300")
root.state('zoomed')


# Create a frame to hold the game idea label and button
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create a label to display the title
title_label = tk.Label(frame, text="Game Idea Generator", font=("Helvetica", 20, "bold", "underline"))
title_label.pack(pady=10)

# Create a label to display the game idea
game_idea_label = tk.Label(frame, text="Click the button to generate a game idea!", font=("Helvetica", 18))
game_idea_label.pack(pady=10)

# Create a button to generate a new game idea
generate_button = tk.Button(
  frame,
  text="Generate",
  command=generate_game_idea,
  font=("Helvetica", 20, "bold"),
  bg="#4CAF50",
  fg="white"
)

# Create a button to generate a new game idea
generate_button = tk.Button(
  frame,
  text="Generate",
  command=generate_game_idea,
  font=("Helvetica", 20, "bold"),
  bg="#4CAF50",
  fg="white"
)
generate_button.pack(pady=10)

# Start the main event loop
root.mainloop()