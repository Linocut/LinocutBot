from random import randint

factList = [
    "This is linocut. It's a bot that manages custom substitutions in chat. It also has some fun commands like ~wheel and ~bing.",
    "Linocut was created by a user named Cliff. They wanted to make a bot that could aid in roleplay creation and management.",
    "Linocut can solve simple math problems using the ~solve command. It can handle operations like addition, subtraction, multiplication, and division.",
    "The ~wheel command can be used to make random decisions. You can provide options separated by commas, and Linocut will randomly select one for you.",
    "Linocut can manage roles in a Discord server. Admins and users with a specific minimod role can use the .add and .remove commands to manage roles for users in the server.",
    "Linocut can send announcements using the .announce command. This allows admins to broadcast messages to specific channels in the server."
]


async def handle_fact(message):
    number = randint(0, len(factList)-1)
    await message.channel.send(factList[number])
