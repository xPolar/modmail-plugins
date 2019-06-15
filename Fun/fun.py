import discord
from discord.ext import commands

class fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Eightball
    @commands.command(aliases = ["8ball, eball"])
    async def eightball(self, ctx, *, question = None):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful."]
        embed = discord.Embed(
            color = 0x2f302f
        )
        embed.set_author(name = "Eightball", icon_url = "https://cdn.discordapp.com/attachments/581288417619607552/581649634561097733/ball-pool-png-open-2000.png")
        embed.add_field(name = "Question", value = f"{question} ", inline = True)
        embed.add_field(name = "Answer", value = f"{random.choice(responses)}", inline = False)
        await ctx.send(embed=embed)

    #Youtube search
    @commands.command()
    async def youtube(self, ctx, *, search = None):
        if ctx.message.author.id in blocked_users:
            embed = discord.Embed(
                title = "You are blocked from using this bot!",
                color = 0xdd0000
            )
            await ctx.send(embed = embed)
        else:
            if search == None:
                embed = discord.Embed(
                    title = "Make sure to search something!",
                    color = 0xdd0000
                )
                await ctx.send(embed = embed)
            else:
                search = search.replace(" ", "+")
                embed = discord.Embed(
                    title = "**Here's your search!**",
                    url = f"https://www.youtube.com/results?search_query={search}",
                    color = 0xc4302b
                )
                await ctx.send(embed = embed)

    #Funfact
    @commands.command()
    async def funfact(self, ctx):
        if ctx.message.author.id in blocked_users:
            embed = discord.Embed(
                title = "You are blocked from using this bot!",
                color = 0xdd0000
            )
            await ctx.send(embed = embed)
        else:
            funfacts = ["December 12th, 2012 was the last day that the date, month, and year were the same number for the 21st century. (12/12/12)",
                        "Banging your head against a wall for one hour burns 150 calories.",
                        "In Switzerland it is illegal to own just one guinea pig.",
                        "Pteronophobia is the fear of being tickled by feathers.",
                        "A flock of crows is known as a murder.",
                        "The oldest “your mom” joke was discovered on a 3,500 year old Babylonian tablet.",
                        "29th May is officially “Put a Pillow on Your Fridge Day”.",
                        "Cherophobia is an irrational fear of fun or happiness.",
                        "7 percent of American adults believe that chocolate milk comes from brown cows.",
                        "If you lift a kangaroo’s tail off the ground it can’t hop.",
                        "Bananas are curved because they grow towards the sun.",
                        "Billy goats urinate on their own heads to smell more attractive to females.",
                        "The inventor of the Frisbee was cremated and made into a Frisbee after he died.",
                        "During your lifetime, you will produce enough saliva to fill two swimming pools.",
                        "Polar bears could eat as many as 86 penguins in a single sitting…",
                        "King Henry VIII slept with a gigantic axe beside him.",
                        "An eagle can kill a young deer and fly away with it.",
                        "In 2017 more people were killed from injuries caused by taking a selfie than by shark attacks.",
                        "A lion’s roar can be heard from 5 miles away.",
                        "Approximately 10-20 percent of U.S. power outages are caused by squirrels.",
                        "While trying to find a cure for AIDS, the Mayo Clinic made glow in the dark cats.",
                        "A swarm of 20,000 bees followed a car for two days because their queen was stuck inside.",
                        "J.K. Rowling chose the unusual name ‘Hermione’ so young girls wouldn’t be teased for being nerdy.",
                        "Los Angeles’s full name is 'El Pueblo de Nuestra Senora la Reina de los Angeles de Porciuncula.",
                        "It snowed in the Sahara desert for 30 minutes on the 18th February 1979.",
                        "Mike Tyson once offered a zoo attendant 10,000 dollars to let him fight a gorilla.",
                        "ABBA turned down 1 billion dollars to do a reunion tour.",
                        "There has never been a verified snow leopard attack on a human being.",
                        "The first alarm clock could only ring at 4 a.m.",
                        "Dying is illegal in the Houses of Parliaments.",
                        "The most venomous jellyfish in the world is the Irukandji.",
                        "The 20th of March is Snowman Burning Day.",
                        "Vincent van Gogh only sold one painting in his lifetime.",
                        "The average person walks the equivalent of five times around the world in their lifetime.",
                        "Michael Jackson offered to make a Harry Potter musical, but J.K. Rowling rejected the idea.",
                        "The world record for stuffing drinking straws into your mouth at once is 459.",
                        "In 2011, more than 1 in 3 divorce filings in the U.S. contained the word 'Facebook'.",
                        "George W. Bush was once a cheerleader.",
                        "Coca-Cola owns all website URLs that can be read as ahh, all the way up to 62 h’s.",
                        "Samuel L. Jackson requested to have a purple lightsaber in Star Wars in order for him to accept the part as Mace Windu.",
                        "Kleenex tissues were originally used as filters in gas masks.",
                        "In 1998, Sony accidentally sold 700,000 camcorders that had the technology to see through people’s clothes.",
                        "During your lifetime, you will spend around thirty-eight days brushing your teeth.",
                        "Ketchup was a medicine in the early 1800s.",
                        "The Longest Wedding Veil Was the Same Length as 63.5 Football Fields.",
                        "The Total Weight of Ants on Earth Once Equaled the Total Weight of People.",
                        "A Dozen Bodies Were Found in Benjamin Franklin’s Basement.",
                        "Chinese Police Use Geese Squads.",
                        "For 100 Years, Maps Have Shown an Island That Doesn’t Exist.",
                        ]

            embed = discord.Embed(
                title = "Here's a funfact!",
                description = f"{random.choice(funfacts)}",
                color = 0x9b037d
            )
            embed.set_author(name = "Fun fact")
            await ctx.send(embed=embed)

        #Dadjoke
        @commands.command()
        async def dadjoke(self, ctx):
            if ctx.message.author.id in blocked_users:
                embed = discord.Embed(
                    title = "You are blocked from using this bot!",
                    color = 0xdd0000
                )
                await ctx.send(embed = embed)
            else:
                jokes = ["Did you hear about the restaurant on the moon? Great food, no atmosphere.",
                        "What do you call a fake noodle? An Impasta.",
                        "How many apples grow on a tree? All of them.",
                        "Want to hear a joke about paper? Nevermind it's tearable.",
                        "I just watched a program about beavers. It was the best dam program I've ever seen.",
                        "Why did the coffee file a police report? It got mugged.",
                        "How does a penguin build it's house? Igloos it together.",
                        "Dad, did you get a haircut? No I got them all cut.",
                        "What do you call a Mexican who has lost his car? Carlos.",
                        "Dad, can you put my shoes on? No, I don't think they'll fit me.",
                        "Why did the scarecrow win an award? Because he was outstanding in his field.",
                        "Why don't skeletons ever go trick or treating? Because they have no body to go with.",
                        "Ill call you later. Don't call me later, call me Dad.",
                        "What do you call an elephant that doesn't matter? An irrelephant.",
                        "Want to hear a joke about construction? I'm still working on it.",
                        "What do you call cheese that isn't yours? Nacho Cheese.",
                        "Why couldn't the bicycle stand up by itself? It was two tired.",
                        "What did the grape do when he got stepped on? He let out a little wine.",
                        "I wouldn't buy anything with velcro. It's a total rip-off.",
                        "The shovel was a ground-breaking invention.",
                        "Dad, can you put the cat out? I didn't know it was on fire.",
                        "This graveyard looks overcrowded. People must be dying to get in there.",
                        "Whenever the cashier at the grocery store asks my dad if he would like the milk in a bag he replies, 'No, just leave it in the carton!'",
                        "5/4 of people admit that they’re bad with fractions.",
                        "Two goldfish are in a tank. One says to the other, 'do you know how to drive this thing?'",
                        "What do you call a man with a rubber toe? Roberto.",
                        "What do you call a fat psychic? A four-chin teller.",
                        "I would avoid the sushi if I was you. It’s a little fishy.",
                        "To the man in the wheelchair that stole my camouflage jacket... You can hide but you can't run.",
                        "The rotation of earth really makes my day.",
                        "I thought about going on an all-almond diet. But that's just nuts.",
                        "What's brown and sticky? A stick.",
                        "I’ve never gone to a gun range before. I decided to give it a shot!",
                        "Why do you never see elephants hiding in trees? Because they're so good at it.",
                        "Did you hear about the kidnapping at school? It's fine, he woke up.",
                        "A furniture store keeps calling me. All I wanted was one night stand.",
                        "I used to work in a shoe recycling shop. It was sole destroying.",
                        "Did I tell you the time I fell in love during a backflip? I was heels over head.",
                        "I don’t play soccer because I enjoy the sport. I’m just doing it for kicks.",
                        "People don’t like having to bend over to get their drinks. We really need to raise the bar."]
                embed = discord.Embed(
                    title = "Here's a dad joke!",
                    description = f"{random.choice(jokes)}",
                    color = 0x5627d8
                )
                embed.set_author(name = "Dad joke")
                await ctx.send(embed = embed)

        #Cat
        @commands.command()
        async def cat(self, ctx):
            if ctx.message.author.id in blocked_users:
                embed = discord.Embed(
                    title = "You are blocked from using this bot!",
                    color = 0xdd0000
                )
                await ctx.send(embed = embed)
            else:
                choices = ["http://i.imgur.com/vTbe1VL.jpg",
                          "https://i.redd.it/5a2b5t3zv6zx.jpg",
                          "https://i.reddituploads.com/beb4181f5ad54ea396a4c16f48dda6a1?fit=max&h=1536&w=1536&s=d6725e107cac20a2d63c17ceed41cadc",
                          "http://i.imgur.com/54ZNGsq.jpg",
                          "http://i.imgur.com/avo5CE2.gifv",
                          "https://i.imgur.com/74oEb8a.jpg",
                          "https://i.imgur.com/mUm8RkG.jpg",
                          "https://i.reddituploads.com/21738376035841e8a435a7aa1781f1a2?fit=max&h=1536&w=1536&s=b30153a27838ee69dbfbf6b6a53952b6",
                          "http://i.imgur.com/729sGVJ.gifv",
                          "https://i.redd.it/hpqurtsrb6qy.jpg",
                          "http://i.imgur.com/GyEeYt8.gifv",
                          "http://i.imgur.com/OlTgWUD.jpg",
                          "https://i.redd.it/hzxejchmn9yy.jpg",
                          "https://i.redd.it/lslm1romx5jy.jpg",
                          "https://i.redd.it/x3kdiz7u9u2z.jpg",
                          "http://i.imgur.com/XwgNL3n.gifv",
                          "https://i.imgur.com/gallery/rWyFWmR.jpg",
                          "http://i.imgur.com/2mbzfWq.jpg",
                          "https://i.reddituploads.com/7e6fbe4ce57e450e833bcd2737d65e2c?fit=max&h=1536&w=1536&s=5e7014cfe4baad5afff0df1ce459c584",
                          "https://i.reddituploads.com/bb1a7d55ff184458b39cf3e3deb819c1?fit=max&h=1536&w=1536&s=7afe46b4fe8e90e38e4b5ba6464ca1db",
                          "http://i.imgur.com/jfsHXUV.gifv",
                          "https://i.imgur.com/sI8AJqR.jpg",
                          "https://i.imgur.com/18D2DjF.jpg",
                          "https://i.imgur.com/CrSttq4.jpg",
                          "https://i.imgur.com/J2DwMXw.jpg",
                          "http://i.imgur.com/nGDUUhY.jpg",
                          "http://i.imgur.com/IDFyJ4x.gifv",
                          "https://i.redd.it/x7rsfzcrouyy.jpg",
                          "https://i.redd.it/2tinfjwyb1iy.jpg",
                          "https://i.redd.it/mnwbovkwsvzy.gif",
                          "https://i.redd.it/3rcut5hqn5oy.jpg",
                          "https://i.redd.it/t5orvjahk30z.jpg",
                          "http://i.imgur.com/m5HjhY1.gif",
                          "https://i.reddituploads.com/7a3a8ba46ee7436a8f1288a5c003946a?fit=max&h=1536&w=1536&s=241ccd5f8c688411c4e11350cfe6259a",
                          "https://i.reddituploads.com/ac8fc17c17404b2f80700a2c2a9ed20f?fit=max&h=1536&w=1536&s=d02059c1fd931118921373cf3ce3ecc8",
                          "https://i.redd.it/5mefhrz4nqoy.jpg",
                          "http://i.imgur.com/6c7QM8W.png",
                          "http://i.imgur.com/2gmDAnm.jpg",
                          "http://i.imgur.com/9My4X1v.jpg",
                          "https://i.reddituploads.com/a60b53b7694440c6a4b969334a74b9ae?fit=max&h=1536&w=1536&s=a79a1467a3bf4760201b7c816dcea456",
                          "http://i.imgur.com/vCh7XNd.gif",
                          "https://i.imgur.com/BtlL2JX.jpg",
                          "http://i.imgur.com/xmLJFy8.jpg",
                          "http://i.imgur.com/vCh7XNd.gif",
                          "http://i.imgur.com/zTzCybb.png",
                          "http://i.imgur.com/VLmihnM.gifv",
                          "https://i.imgur.com/3opZ020.jpg",
                          "http://i.imgur.com/w5oJxQZ.gifv",
                          "http://i.imgur.com/3xnCwVD.jpg",
                          "http://i.imgur.com/vTbe1VL.jpg",
                          "https://i.redd.it/ebdfl0tg64ny.jpg",
                          "https://i.imgur.com/rSRcGti.gifv",
                          "https://i.imgur.com/a/OBY8r.jpg",
                          "http://i.imgur.com/WS3peGa.jpg",
                          "https://i.imgur.com/PkIO1ul.jpg"]
                choice = random.choice(choices)
                embed = discord.Embed(
                    title = "Cat",
                    url = f"{choice}",
                    color = 0xe24646
                )
                embed.set_image(url = f"{choice}")
                await ctx.send(embed = embed)

        #Dog
        @commands.command()
        async def dog(self, ctx):
            if ctx.message.author.id in blocked_users:
                embed = discord.Embed(
                    title = "You are blocked from using this bot!",
                    color = 0xdd0000
                )
                await ctx.send(embed = embed)
            else:
                choices = ["https://i.imgur.com/HE1U0VT.jpg",
                           "http://i.imgur.com/EpqYB9k.jpg",
                           "http://i.imgur.com/Km1bsfg.jpg",
                           "https://i.imgur.com/sHmmiu1.jpg",
                           "http://i.imgur.com/9f2up2N.jpg",
                           "https://i.redd.it/nbwlt4ny8w6z.jpg",
                           "http://i.imgur.com/wYWCpSw.jpg",
                           "https://i.imgur.com/qbZXaOJ.jpg",
                           "https://i.reddituploads.com/48c314206ad64b8dbb823b0b88e91ff8?fit=max&h=1536&w=1536&s=38650b4ccdaf2ef959bfc2a3fa44e483",
                           "http://i.imgur.com/PP4Ua3e.jpg",
                           "https://i.imgur.com/gZRYFxZ.jpg",
                           "https://i.redd.it/im9ksyjw5j0z.jpg",
                           "https://i.imgur.com/8U4TpO2.jpg",
                           "https://i.reddituploads.com/d3880620f4494722b9018d4b94a3ee33?fit=max&h=1536&w=1536&s=d702664cb72de6c3560a2158ca31df53",
                           "http://i.imgur.com/15JO3RI.jpg",
                           "https://i.imgur.com/Rb3kfIi.jpg",
                           "http://i.imgur.com/ndDWJBT.jpg",
                           "http://i.imgur.com/88C6sGg.gifv",
                           "https://i.reddituploads.com/e3a400c4b893423c84d92a3a6cafa679?fit=max&h=1536&w=1536&s=1b7ce9359e66a690ddc941f323c0eae6",
                           "https://i.redd.it/40tudj1le67z.",
                           "https://i.reddituploads.com/fbbcba8521fc45d5bd2516500dbc57c9?fit=max&h=1536&w=1536&s=a7d1c115ef7664cae73817686915f2d4",
                           "https://i.reddituploads.com/e6ec337b392a49be9eab05babb5d7712?fit=max&h=1536&w=1536&s=b9e80c7e0d724db25fa284fb9d231899",
                           "https://i.imgur.com/U9yHXIb.jpg",
                           "https://i.imgur.com/iixtzvW.jpg",
                           "https://i.reddituploads.com/7e8b85cbd79b46f38f33957be9000f66?fit=max&h=1536&w=1536&s=e1bb51bd4ace1bc88c8bb1be2658410f",
                           "https://i.redd.it/jedufst1dy8y.jpg",
                           "https://i.imgur.com/O9SuTXk.jpg",
                           "http://i.imgur.com/bRrk2hc.jpg",
                           "https://i.imgur.com/Xi5CSC7.jpg",
                           "https://i.redd.it/71wt3wssbw5z.jpg",
                           "http://i.imgur.com/E5CfwdF.jpg",
                           "https://i.redd.it/xnsodxwvpmiy.jpg",
                           "https://i.imgur.com/0L95gP0.jpg",
                           "https://i.reddituploads.com/4f858baa9ced4a0e9188b05f02b53569?fit=max&h=1536&w=1536&s=54e5b7d7aa71317fe554349fe209d0c6",
                           "https://i.imgur.com/upavcb6.jpg",
                           "https://i.redd.it/qeq6u2tvzc2y.jpg",
                           "https://i.imgur.com/ZgWsQIK.jpg",
                           "https://i.imgur.com/1KaYCKa.jpg",
                           "https://i.redd.it/eieguisu55vy.jpg",
                           "http://i.imgur.com/ef25y11.jpg",
                           "http://i.imgur.com/wI9BQXu.jpg",
                           "https://i.redd.it/mnc10w90ln6z.jpg",
                           "https://i.imgur.com/B0sDssw.jpg",
                           "http://i.imgur.com/33HL7Zd.jpg",
                           "http://i.imgur.com/BxO2Zoi.jpg",
                           "http://i.imgur.com/J1m5fgv.jpg",
                           "https://i.imgur.com/gallery/F9Zi8PG.jpg",
                           "https://i.redd.it/dd54g2foc0ly.jpg",
                           "https://i.redd.it/fuqaxzodohuy.jpg",
                           "http://i.imgur.com/FZ0Ngxr.jpg",
                           "https://i.imgur.com/09Gwa5a.jpg",
                           "https://i.reddituploads.com/ce47d2c46be24a0689bf3b43942e920a?fit=max&h=1536&w=1536&s=792384b6a138f5ad61cc5046995e12e6",
                           "https://i.redd.it/biond94mq8jy.jpg",
                           "http://i.imgur.com/c2tOO8h.jpg",
                           "http://m.imgur.com/d13JoUg",
                           "https://i.redd.it/m4i2b3fusvnx.jpg"]
                choice = random.choice(choices)
                embed = discord.Embed(
                    title = "Dog",
                    url = f"{choice}",
                    color = 0xe24646
                )
                embed.set_image(url = f"{choice}")
                await ctx.send(embed = embed)

        #Rock Paper Scissors
        @commands.command()
        async def rps(self, ctx, choice = None):
            if ctx.message.author.id in blocked_users:
                embed = discord.Embed(
                    title = "You are blocked from using this bot!",
                    color = 0xdd0000
                )
                await ctx.send(embed = embed)
            else:
                choice = choice.lower()
                correctchoices = ["rock",
                                  "paper",
                                  "scissors"]
                if choice == None:
                    embed = discord.Embed(
                        title = "You need to choose either rock paper or scissors!",
                        color = 0xdd0000
                    )
                    await ctx.send(embed = embed)
                if choice in correctchoices:
                    possible = ["rock",
                                "paper",
                                "scissors"]
                    chosen = random.choice(possible)
                    if choice == "rock":
                        if chosen == "rock":
                            embed = discord.Embed(
                                title = "Rock VS Rock",
                                description = "It's a tie!",
                                color = 0x07999b
                            )
                            embed.set_author(name = "Rock Paper Scissors", icon_url = "https://cdn.discordapp.com/attachments/581288417619607552/582445464264114186/rock.png")
                            await ctx.send(embed = embed)
                        if chosen == "paper":
                            embed = discord.Embed(
                                title = "Rock VS Paper",
                                description = "You lost!",
                                color = 0xdd0000
                            )
                            embed.set_author(name = "Rock Paper Scissors", icon_url = "https://cdn.discordapp.com/attachments/581288417619607552/582445464264114186/rock.png")
                            await ctx.send(embed = embed)
                        if chosen == "scissors":
                            embed = discord.Embed(
                                title = "Rock VS Scissors",
                                description = "You won!",
                                color = 0x00cc1b
                            )
                            embed.set_author(name = "Rock Paper Scissors", icon_url = "https://cdn.discordapp.com/attachments/581288417619607552/582445464264114186/rock.png")
                            await ctx.send(embed = embed)
                    if choice == "paper":
                        if chosen == "rock":
                            embed = discord.Embed(
                                title = "Paper VS Rock",
                                description = "You won!",
                                color = 0x00cc1b
                            )
                            embed.set_author(name = "Rock Paper Scissors", icon_url = "https://cdn.discordapp.com/attachments/581288417619607552/582445487798353937/paper.png")
                            await ctx.send(embed = embed)
                        if chosen == "paper":
                            embed = discord.Embed(
                                title = "Paper VS Paper",
                                description = "It's a tie!",
                                color = 0x07999b
                            )
                            embed.set_author(name = "Rock Paper Scissors", icon_url = "https://cdn.discordapp.com/attachments/581288417619607552/582445487798353937/paper.png")
                            await ctx.send(embed = embed)
                        if chosen == "scissors":
                            embed = discord.Embed(
                                title = "Paper VS Scissors",
                                description = "You lost!",
                                color = 0xdd0000
                            )
                            embed.set_author(name = "Rock Paper Scisors", icon_url = "https://cdn.discordapp.com/attachments/581288417619607552/582445487798353937/paper.png")
                            await ctx.send(embed = embed)
                    if choice == "scissors":
                        if chosen == "rock":
                            embed = discord.Embed(
                                title = "Scissors VS Rock",
                                description = "You lost!",
                                color = 0xdd0000
                            )
                            embed.set_author(name = "Rock Paper Scissors", icon_url = "https://cdn.discordapp.com/attachments/581288417619607552/582445467170766874/scissors.png")
                            await ctx.send(embed = embed)
                        if chosen == "paper":
                            embed = discord.Embed(
                                title = "Scissors Vs Paper",
                                description = "You won!",
                                color = 0x00cc1b
                            )
                            embed.set_author(name = "Rock Paper Scissors", icon_url = "https://cdn.discordapp.com/attachments/581288417619607552/582445467170766874/scissors.png")
                            await ctx.send(embed = embed)
                        if chosen == "scissors":
                            embed = discord.Embed(
                                title = "Scissors VS Scissors",
                                description = "It's a tie!",
                                color = 0x07999b
                            )
                            embed.set_author(name = "Rock Paper Scissors", icon_url = "https://cdn.discordapp.com/attachments/581288417619607552/582445467170766874/scissors.png")
                            await ctx.send(embed = embed)
                else:
                    embed = discord.Embed(
                        title = "You need to choose either rock paper or scissors!",
                        color = 0xdd0000
                    )
                    await ctx.send(embed = embed)

        #Hug command
        @commands.command()
        async def hug(self, ctx, member : discord.Member = None):
        if ctx.message.author.id in blocked_users:
            embed = discord.Embed(
                title = "You are blocked from using this bot!",
                color = 0xdd0000
            )
            await ctx.send(embed = embed)
        else:
            if member == None:
                embed = discord.Embed(
                    title = "You need to specify a user!",
                    color = 0xdd0000
                )
                await ctx.send(embed = embed)
            else:
                choices = ["https://media1.tenor.com/images/18474dc6afa97cef50ad53cf84e37d08/tenor.gif?itemid=12375072",
                           "https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif?itemid=7552075",
                           "https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/tenor.gif?itemid=9200935",
                           "https://media1.tenor.com/images/074d69c5afcc89f3f879ca473e003af2/tenor.gif?itemid=4898650",
                           "https://media1.tenor.com/images/4d89d7f963b41a416ec8a55230dab31b/tenor.gif?itemid=5166500",
                           "https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?itemid=7324587",
                           "https://media1.tenor.com/images/1069921ddcf38ff722125c8f65401c28/tenor.gif?itemid=11074788",
                           "https://media1.tenor.com/images/40aed63f5bc795ed7a980d0ad5c387f2/tenor.gif?itemid=11098589",
                           "https://media1.tenor.com/images/b77fd0cfd95f89f967be0a5ebb3b6c6a/tenor.gif?itemid=7864716",
                           "https://media1.tenor.com/images/7e30687977c5db417e8424979c0dfa99/tenor.gif?itemid=10522729",
                           "https://media1.tenor.com/images/b0de026a12e20137a654b5e2e65e2aed/tenor.gif?itemid=7552093",
                           "https://media1.tenor.com/images/54e97e0cdeefea2ee6fb2e76d141f448/tenor.gif?itemid=11378437",
                           "https://media1.tenor.com/images/b4ba20e6cb49d8f8bae81d86e45e4dcc/tenor.gif?itemid=5634582",
                           "https://media1.tenor.com/images/45b1dd9eaace572a65a305807cfaec9f/tenor.gif?itemid=6238016",
                           "https://media1.tenor.com/images/af76e9a0652575b414251b6490509a36/tenor.gif?itemid=5640885",
                           "https://media1.tenor.com/images/11889c4c994c0634cfcedc8adba9dd6c/tenor.gif?itemid=5634578",
                           "https://media1.tenor.com/images/d3dca2dec335e5707e668b2f9813fde5/tenor.gif?itemid=12668677"]

                embed = discord.Embed(
                    title = f"{ctx.message.author.name} hugged {member.name}!",
                    color = 0xad29c4
                )
                embed.set_image(url = f"{random.choice(choices)}")
                await ctx.send(embed = embed)

        #Pat
        @commands.command()
        async def pat(self, ctx, member : discord.Member = None):
            if ctx.message.author.id in blocked_users:
                embed = discord.Embed(
                    title = "You are blocked from using this bot!",
                    color = 0xdd0000
                )
                await ctx.send(embed = embed)
            else:
                if member == None:
                    embed = discord.Embed(
                        title = "You need to specify a user!",
                        color = 0xdd0000
                    )
                    await ctx.send(embed = embed)
                else:
                    choices = ["https://media1.tenor.com/images/116fe7ede5b7976920fac3bf8067d42b/tenor.gif?itemid=9200932",
                               "https://media1.tenor.com/images/54722063c802bac30d928db3bf3cc3b4/tenor.gif?itemid=8841561",
                               "https://media1.tenor.com/images/005e8df693c0f59e442b0bf95c22d0f5/tenor.gif?itemid=10947495",
                               "https://media1.tenor.com/images/183ff4514cbe90609e3f286adaa3d0b4/tenor.gif?itemid=5518321",
                               "https://media1.tenor.com/images/1e92c03121c0bd6688d17eef8d275ea7/tenor.gif?itemid=9920853",
                               "https://media1.tenor.com/images/f330c520a8dfa461130a799faca13c7e/tenor.gif?itemid=13911345",
                               "https://media1.tenor.com/images/266e5f9bcb3f3aa87ba39526ee202476/tenor.gif?itemid=5518317",
                               "https://media1.tenor.com/images/60991d021f0f2d4f065ac9b4f00948dc/tenor.gif?itemid=11728232",
                               "https://media1.tenor.com/images/5466adf348239fba04c838639525c28a/tenor.gif?itemid=13284057",
                               "https://media1.tenor.com/images/282cc80907f0fe82d9ae1f55f1a87c03/tenor.gif?itemid=12018857",
                               "https://media1.tenor.com/images/71e74263a48a6e9a2c53f3bc1439c3ac/tenor.gif?itemid=12434286",
                               "https://media1.tenor.com/images/c2232aec426d8b5e85e026cbca410463/tenor.gif?itemid=11648944",
                               "https://media1.tenor.com/images/5a692dc246f2468ca0e37446b4964054/tenor.gif?itemid=13949497",
                               "https://media1.tenor.com/images/078599227bc087959b79ea111fbc0f3a/tenor.gif?itemid=13596135",
                               "https://media1.tenor.com/images/cf9a587a3fc4ef2e8f9f92bae63cb0d0/tenor.gif?itemid=13793739",
                               "https://media1.tenor.com/images/4b52ac769cbef524ee000ba3f84afab0/tenor.gif?itemid=13758199",
                               "https://media1.tenor.com/images/13f385a3442ac5b513a0fa8e8d805567/tenor.gif?itemid=13857199",
                               "https://media1.tenor.com/images/857aef7553857b812808a355f31bbd1f/tenor.gif?itemid=13576017",
                               "https://media1.tenor.com/images/e71e45362fccc0b9a2ccce97bff93780/tenor.gif?itemid=11115628",]

                    embed = discord.Embed(
                        title = f"{ctx.message.author.name} patted {member.name}!",
                        color = 0xad29c4
                    )
                    embed.set_image(url = f"{random.choice(choices)}")
                    await ctx.send(embed = embed)

        #Coinflip command
        @client.command()
        async def coinflip(ctx):
            if ctx.message.author.id in blocked_users:
                embed = discord.Embed(
                    title = "You are blocked from using this bot!",
                    color = 0xdd0000
                )
                await ctx.send(embed = embed)
            else:
                choices = ["Heads",
                           "Tails"]
                embed = discord.Embed(
                    title = f"The coin landed on {random.choice(choices)}",
                    color = 0xc1c113
                )
                embed.set_author(name = "Coinflip")
                await ctx.send(embed = embed)

            #Dice command
            @client.command()
            async def dice(ctx, sides = None):
                if ctx.message.author.id in blocked_users:
                    embed = discord.Embed(
                        title = "You are blocked from using this bot!",
                        color = 0xdd0000
                    )
                    await ctx.send(embed = embed)
                else:
                    if sides == None:
                        land = random.randint(1, 6)
                        embed = discord.Embed(
                            title = f"The dice landed on {land}!",
                            color = 0xFFFFFF
                        )
                        await ctx.send(embed = embed)
                    else:
                        digit = sides.isdigit()
                        if digit == True:
                            sides = float(sides)
                            land = random.randint(1, sides)
                            embed = discord.Embed(
                                title = f"The dice landed on {land}!",
                                color = 0xFFFFFF
                            )
                            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(fun(bot))
