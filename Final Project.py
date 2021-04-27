#Final Project
import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


tools = 0

required = ("\nUse only A, B, or C\n")
restart = ("\n Enter Y or N to play again!")
end1 = ("Thanks for playing! Be weary of ancient desert temples!")
end2 = ("Don't ever try to fight off mobs unarmed! It almost never works!")
end3 = ("Why did you think that would work? A skeleton with a bow and arrow would never befriend an idiot with a bone!")
end4 = ("Really wish you could've made it to the village! You were SO close!")
end5 = ("Be weary of weak vines! Especially when you don't have any armor or enchantments")
end6 = ("Better luck next time!")
end7 = ("Maybe don't build your house with such flammable materials next time!")
def intro():
  print ("You create a new Minecraft world and spawn inside of a great plains biome. "
         "To the North is a desert biome, and to the South, there is a jungle biome. Will you move on to "
         "another biome or stay where you're at? You will:")
  time.sleep(1)
  print ("""\nA. Move north towards the desert
  \nB. Move south towards the jungle
  \nC. Stay in the great plains """)
  choice = input(">>> ")
  if choice in answer_A:
    option_desert()
  elif choice in answer_B:
    option_jungle()
  elif choice in answer_C:
    option_greatplains()
  else:
    print (required)
    intro()

def option_desert(): 
  print ("\nYou move north into the desert. In the distance you see an ancient desert temple. "
         "Will you:")
  time.sleep(1)
  print ("""\nA. Enter the ancient temple
  \nB. Keep traveling past the temple""")
  choice = input(">>> ")
  if choice in answer_A:
    option_temple()
  elif choice in answer_B:
      option_passtemple()
  else:
    print (required)
    option_desert()

def option_passtemple():
     print ("\nYou decide to move on past the temple further into the desert. "
            "Your hunger meter begins to run very low and night is quickly approaching. You begin "
            "to see skeletons quickly approaching. You can also see a distant light source just beyond the "
            "horizon. You will:")
     time.sleep(1)
     print ("\nA. Try to stand your ground in the desert and fight off the skeletons "
      "\nB. Run quickly towards the distant light source"
      "\nC. Try to befriend the skeletons with an old bone close by")
     choice = input(">>> ")
     if choice in answer_A:
        print("\nYou attempt to fight off the skeletons but your hunger is low and you are unarmed. "
              "You give it your all, but it isn't enough and you are shot to death by skeletons. The last sound "
              "you hear is the jingle of their hollow skeletons.")
        print(restart)
        choice = input(">>> ")
        if choice in yes:
            intro()
        elif choice in no:
            print(end2)
     elif choice in answer_B:
        print("\nYou slowly approach the lights in the distance. Extremely fatigued and hungry you begin to"
          " slip in and out of consciousness as you approach what appears to be a small village "
          "You pass out just before you reach the village. When you awaken you're surrounded by zombies"
          " and you are too weak to flee. You died!")
        print(restart)
        choice = input(">>> ")
        if choice in yes:
            intro()
        elif choice in no:
            print(end4)
     elif choice in answer_C:
        print("\nThe skeletons misunderstood your act of kindess and instead interpreted it as a sign of "
              "disrespect. They now really hate you and waste no time shooting you to death with arrows.")
        print(restart)
        choice = input(">>> ")
        if choice in yes:
            intro()
        elif choice in no:
            print(end2)
     else:
        print (required)
        option_passtemple()

     
def option_temple():
    print("\nYou enter the ancient desert temple. There is a strange pattern on the floor made up of"
          " different colored blocks of wool. You decide to break out the middle piece of the pattern and"
          " jump down into the dark chamber within the temple. You land on a stone pressure plate and hear "
          "the sounds of 9 pieces of TNT being ignited all at once. \nYou died in the booby trapped temple.")
    print(restart)
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        print(end1)
        
def option_jungle():
  print ("\nYou move deep into the jungle. There are lots of trees"
         " everywhere you look. You hear some rustling in the nearby bushes"
         " Do you stop to cut some wood and craft some tools?. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    tools = 1
  else:
    tools = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  if tools >0:
      print ("""\nA. Climb a jungle tree for a better view of the surrounding area
  \nB. Upgrade your tools from wooden to stone
  \nC. Investigate the nearby bushes""")
  else:
      print("""\nA. Climb a jungle tree for a better view of the surrounding area
  \nB. Wait for something to happen
  \nC. Investigate the nearby bushes""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nYou begin to ascend the tree but one of the vines snaps and you fall to your death!"
           "\nYou Died")
    print(restart)
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        print(end5)
  elif choice in answer_B:
   if tools > 0:
    print ("\nYou upgrade your tools to stone and get attacked by a pack of wild wolves. "
           "The wolves know they are no match for your stone tools so they befriend you. "
           "You are accepted into the pack as one of the wolves and together you rule the jungle. "
           "\nCongrats! You reached the King of the Jungle Ending! Thanks for playing!")
    
   else: 
     print ("\nYou're attacked by a pack of wolves from beyond the bushes and "
            "You are not prepared for a fight. You die to the wolves! Maybe you should have "
            "stopped to craft some tools.")
     print(restart)
     choice = input(">>> ")
     if choice in yes:
        intro()
     elif choice in no:
        print(end6)
  elif choice in answer_C:
     print ("You approach the nearby bushes and discover a wild pack of wolves. "
            "You accidently step on a nearby twig alerting the wolves of your presence. "
            "You are eaten alive by a hungry pack of wolves!")
     print(restart)
     choice = input(">>> ")
     if choice in yes:
        intro()
     elif choice in no:
        print(end6)


    
def option_greatplains():
  print ("\nYou begin to explore around in the great plains biome."
         " You gather some materials and tools. To begin building your first house. "
         " Do you build your house out of stonebrick or wood?")
  print("""\nA. Wooden house
  \nB. Stonebrick house""")
  choice = input(">>> ")
  if choice in answer_A:
    print("A thunderstorm is coming. You can hear lightning strikes in the distance, so you "
         "enter your house to wait out the storm. ")
    print ("\nYour house is struck by lightning several times and the wood catches fire while you're asleep. "
     "\nYou died in a house fire! Maybe you should have used a less flammable block to build your house!")
    print(restart)
    choice = input(">>> ")
    if choice in yes:
        intro()
    elif choice in no:
        print(end7)
  elif choice in answer_B:
    print ("A thunderstorm is coming. You can hear lightning strikes in the distance, so you "
         "enter your house to wait out the storm. ")
    time.sleep(1)
    print ("\nLightning strikes your house several times! Good thing you chose to build your house with stonebricks. "
    "\nCongrats! You made it to the House on a Prairie Ending! Thanks for playing!")
  else:
    print(required)
    option_greatplains()


intro()
