# connect a variable above and read its value from the inputs dictionary:
from pprint import pprint
import textwrap
dd_info = {
    'locations': {
        'stonehillinn': {
            'name': 'Stonehill Inn',
            'npcs': ['Toblen Stonehill', 'Narth', 'Elsa', 'Lanar', 'Trilena',
            'Pip', 'Freda'],
            'description': '''
            In the center of town stands a large, newly built roadhouse of
            fieldstone and routh-hewn timbers. The common room is filled
            with locals nursing mugs of ale and cider, all of them eyeing
            you with curiosity.
            ''',
            'tags': ['lodging','drinking','dining']
        },
        'barthensprovisions': {
            'name': 'Barthen\'s Provisions',
            'npcs': ['Elmar Barthen', 'Ander', 'Thistle'],
            'description': '''
            - Open from sunup to sundown.
            - No items for more than 25gp.
            - DM Reference: For prices, see 'Adventuring Gear' in the handbook.
            ''',
            'tags': ['trading', 'trade', 'provisions'],
        },
        'edermathorchard': {
            'name': 'Edermath Orchard',
            'npcs': ['Daran Edermath'],
            'description': '''
            A lovely orchard on the nortwest side of town. Has a decent barn with lofts
            of hay. They look pretty comfortable.
            ''',
            'tags': ['lodging', 'quests','guilds'],
        },
        'lionshieldcoster': {
            'name': 'Lionshield Coster',
            'npcs': ['Linene Graywind'],
            'description': '''
            - Hanging above the front door of this modest trading post is a sign shaped
            like a wooden shield with a blue lion painted on it.
            - Owned by the Lionshields, a merchant company based in the city of Yartar,
            over a hundred miles to the east.
            - They ship finished goods to Phandalin and other small settlements throughout
            the region, the this outpost has been hit hard by banditry.
            - The most recent Lionshield caravan was due in Phandalin, but never arrived.
            - DM Reference: The caravan was attacked by the cragmaw goblins.
            ''',
            'tags': ['weapons', 'armor', 'gear']
        },
        'phandalinminersexchange': {
            'name': 'Phandalin Miner\'s Exchange',
            'npcs': ['Halia Thornton'],
            'description': 'a more rugged building on the southwest part of town.',
            'tags': ['quests','guilds']
        },
        'alderleaffarm': {
            'name': 'Alderleaf Farm',
            'npcs': ['Qelline Alderleaf', 'Carp Alderleaf'],
            'description': '''
            An older family farm with a comfy vibe, which makes the haylofts look
            even more comfy''',
            'tags': ['lodging', 'quests']
        },
        'shrineofluck': {
            'name': 'Shrine of Luck',
            'npcs': ['Sister Garaele'],
            'description': '''Small shrine made of stones taken from nearby ruins. It
            is dedicated to Tymora, goddess of luck and good fortune.''',
            'tags': ['quests','guilds'],
        },
        'sleepinggianttaphouse': {
            'name': 'Sleeping Giant Tap House',
            'npcs': ['Redbrands'],
            'description': '''
            - Rundown, dirty, and dangerous watering hole at the eastern
            end of Phandalin's main street.
            - If characters go here, initiat 'Redbrand Ruffians' on page 19 for only
            those who go there.''',
            'tags': ['encounter']
        },
        'townmastershall': {
            'name': 'Townmaster\'s Hall',
            'npcs': ['Harbin Wester', 'Sildar Hallwinter (after rest)'],
            'description': '''
            - Has sturdy stone walls and a pitched wooden roof.
            - Has a bell tower at the back.
            - Posted on a board next to the front door is a notice written in Common
            that reads 'REWARD - Orcs near Wyvern Torl! Those of a mind to face the
            orc menace should inquire within.'
            - The notice bears the town's seal and an indecipherable signature.
            - Has a small, but serviceable jail in the cellar. 2 cells.
            ''',
            'tags': ['quests']
        },
        'tresendarmanor': {
            'name': 'Tresendar Manor',
            'npcs': ['Redbrands'],
            'description': '''
            - More of a castle than a house. Stands at the eastern edge of Phandalin
            on a low hillside amid woods and thickets.
            - Long been abandoned
            - DM Reference: Its cellars have been converted into a Redbrand
            stronghold.
            - DM Reference: If the characters investigate this place, they find the
            entrance to the Redbrand's hideout.
            ''',
            'tags': ['encounter']
        }
    },
    'npcs': {
        'all': {
            'name': 'All NPCs',
            'description': 'All NPCs',
            'location': 'N/A',
            'topics': '''
            - Phandalin: All NPCs in Phandalin know that the Redbrands frequent the 
            Sleeping Giant Tap House at the east end of town... And that ruffians are
            trouble.
            '''
        },
        'toblenstonehill': {
            'name': 'Toblen Stonehill',
            'description': 'Young Human Male',
            'location': 'Stonehill Inn',
            'topics': '''
            - Triboar Native (Town to the East)
            - Wanted to prospect, but found he knew more
            about innkeeping than mining.
            - Upset that Redbrands have been allowed to terrorize
            Phandalin and that townmaster "Harbin Wester" has done
            nothing to stop them.
            - Doesn't want to stir up trouble due to fear that 
            Redbrands will retaliate.
        '''
        },
        'narth': {
            'name': 'Narth',
            'description': 'Old Farmer',
            'location': 'Stonehill Inn',
            'topics': '''
            - Sister Garaele, who oversees the Shrine of Luck, recently left town
            for a few days, then returned wounded and exhausted.
            - DM Reference: See the 'Shrine of Luck' section for more information.
            '''
        },
        'elsa': {
            'name': 'Elsa',
            'description': 'A gossipy barmaid',
            'location': 'Stonehill Inn',
            'topics': '''
            - Daran Edermath, the orchard keeper, is a former adventurer.'
            - DM Reference: See the 'Edermath Orchard' section for more information.
            '''
        },
        'lanar': {
            'name': 'Lanar',
            'description': 'A miner',
            'location': 'Stonehill Inn',
            'topics': '''
            - Orc raiders have been seen on the east end of Triboar Trail.
            - The townmaster is looking for someone to run them off.
            - DM Refernce: OSee the 'Townmaster's Hall' section for more information. 
            '''
        },
        'trilena': {
            'name': 'Trilena',
            'description': 'The Innkeeper\'s wife',
            'location': 'Stonehill Inn',
            'topics': '''
            - Thel Dendrar, a local woodcarver, stood up to the Redbrands a tenday ago
            when they came to the shop to leer at his wife.
            - The ruffians murdered him.
            - Several townsfolk saw it happen.
            - The Redbrands grabbed his body, and now his wife, daughter,
            and son are missing too.
            - DM Reference: Unbeknownst to Trilena and the other townsfolk, the Redbrands
            took The's wife and children to their secret hideout.
            '''
        },
        'pip': {
            'name': 'Pip Stonehill',
            'description': 'Toblen\'s young son',
            'location': 'Stonehill Inn',
            'topics': '''
            - Qelline Alderleaf's son Carp said he found a secret tunnel in the woods,
            but the Redbrands almost caught him.
            - DM Reference: See the 'Alderleaf Farm' section for more information.
            '''
        },
        'freda': {
            'name': 'Freda',
            'description': 'A weaver',
            'location': 'Stonehill Inn',
            'topics': '''
            - The Redbrands hassle every business in town, except for the Phandalin
            Miner's Exchange.
            - They don't want trouble with Halia Thornton, who runs it.
            - DM Reference: See the 'Phandalin Miner's Exchange section for more information.
            '''
        },
        'elmarbarthen': {
            'name': 'Elmar Barthen',
            'description': 'A lean and balding human male shopkeeper of fifty years with a kindly manner',
            'location': 'Barthen Provisions',
            'topics': '''
            - He employs a couple of young clerks, Ander and Thistle, to help load/unload
            wagons when he is not around.
            - If asked how things are going, Barthen tells them tha the Redbrands are making
            it hard on everyone, shaking down local businesses and flouting the townmaster's
            authority.
            - If characters want to help with Redbrands, Barthen tells them they frequent
            the Sleeping Giant Tap House on the east side of town.
            - DM Reference: Deliver 'Meet Me in Phandalin' supplies to Elmar.
            (10gp to each character)
            
            ==Specific Info==
            - If characters tell Elmar of Gundren Rockseeker's capture, he is saddened
            and encourages the party to find and rescue the dwarf.
            - He considers Gundren a friend and was excited by talk of discovering the
            lost mine on the Phandelver's Pact in the nearby hills.
            - If the party does not already know the details of the mine, Sildar Hallwinter
            (after a 15 Intelligence DC) can recall the information from the first 2 paragraphs
            of the background. 
            - Elmar also mentions that there are two more Rockseeker brothers, Nundro and
            Tharden, that are camped somewhere outside of town (See the 'Part 4: Wave Echo Cave'
            section for more information)
            '''
        },
        'ander': {
            'name': 'Ander',
            'description': 'A young clerk',
            'location': 'Barthen Provisions',
            'topics': '''
            - Helps load/unload wagons.
            '''
        },
        'thistle': {
            'name': 'Thistle',
            'description': 'A young clerk',
            'location': 'Barthen Provisions',
            'topics': '''
            - Helps load/unload wagons.
            '''
        },
        'daranedermath': {
            'name': 'Daran Edermath',
            'description': 'Fit, silver haired half-elf well over 100 years old.',
            'location': 'Edermath Orchard',
            'topics': '''
            - Retired adventurer.
            - Can be convinced to let the characters lodge in the hayloft.
            - Fighter who served as a marshal and herald for many years in the lands
            of the Dragon Coast, far to the southeast.
            - Upon retiring, he returned to the Neverwinter region, which is his
            original home.
            - Member (Non-Active) of the Order of the Gauntlet, a devout and vigilant group that
            seeks to protect others from the depredations of evildoers.
            - The order is always vigilant and ready to smite evil, enforce justice,
            and enact retribution against any who try to subjugate or harm others.
            - Though he is not active, he still keeps an eye on the happenings around
            Phandalin.
            - Happy to trade news with fellow adventurers, especially those who appear
            to hold to these virtues.
            - Concerned about the Redbrands, and he would like to see a group of
            adventurers teach the ruffians a lesson.
            - Say's that it's time for someone to take a stand against the Redbrand's
            leader, Glasstaff.
            - Knows the Redbrands hang around the Sleeping Giant Tap Room at the eastern
            part of Phandalin.
            - Knows that the main Redbrands safe house lies under the Tresendar Manor,
            the Ruin at the eastern edge of town.
            - DM Reference: See the 'Tresendar Manor' section for more information.

            ==Quests==

            Old Owl Trouble:
            - Daran has heard stories from prospectors that there is someone digging
            around in the hills ot the northeast in the ruins know as 'Old Owl Well.'
            - More disturbingly, several prospectors have reported bing chased from
            the area by undead.
            - He asks the characters to visit the ruins, a two-day march northeast of
            Phandalin, and find out who's there and what they're up to.
            - Daran knows that the ruins are an old watchtower of an ancient magical
            empire known as Netheril, and he worries that the dangerous magic might
            be dormant there.
            DM Reference: See the 'Old Owl Well' section on page 29 for more information.

            ==Bonus==
            - If the players deal with the Redbrands and investigate the Old Owl Well,
            Daran privately approaches certain members of the group to urge them to join
            the Order of the Gauntlet.
            - He only speaks to those who exemplify the virtues of the order (such as
            honor and vigilance).
            - If a character agrees, the person is awarded the title of 'Chevall'.
            '''
        },
        'linenegraywind': {
            'name': 'Linene Graywind',
            'description': 'Sharp-tongued human woman of 35.',
            'location': 'Lionshield Coster',
            'topics': '''
            - Knows that the bandits have raided the Lionshield caravans.
            - Does not know who is behind the raiding.
            - In the back room, she keeps a supply of weapons and armor.
            - Wont sell to anyone who she thinks is a threat to the town.
            - Among the people she will not do business with are the Redbrands.
            = Warns characters that the ruffians are trouble and advises them
            to avoid the Sleeping Giant tap house.
            - DM Reference: For prices, see 'Adventuring gear' in the handbook.
            
            =Special Info=
            - If the players recover the goods from area 8 in the Cragmaw Hideout,
            or left the goods and can reveal where they can be found, Linene will
            give the group a reward of 50gp and will help them in any way she can.
            '''
        },
        'haliathornton': {
            'name': 'Halia Thornton',
            'description': 'An ambitious and calculating human woman.',
            'location': 'Phandalin Miner\'s Exchange',
            'topics': '''
            - Doesn't know the location of Cragmaw Castle, but knows that the Redbrands
            have a goblin minion serving them.
            - She suggests the goblin likely knows the location of Cragmaw Castle.
            - She leverages this information to persuate the characters to help her
            with the Redbrands.
            - DM Reference: In her attempts to establish the miner's exchange as the closest
            thing the town has as a governing authority, she acts as more of
            a simple merchant.
            - DM Reference: Agent of Zhentrarim, a powerful organization that seeks to exert
            secret control over the North through wealth and influence.
            - DM Reference: Working to slowly bring Phandalin under her control, and can be valuable
            to the characters if they do not cross her.

            ==Quests==
            Halias Job Offer:
            - DM Reference: If approached by characters she believes she can control, she will explain
            that the Redbrands are a problem.
            - Tells players how the ruffians loiter around the Sleeping Giant Tap House on the east of town.
            - Also tells players that the ruffians have a base under Tresendar Manor on the eastern edge
            of town.
            - Offers characters 100gp to eliminate the Redbrand's leader, Glasstaff, and bring
            any correspondence they find in the leader's quarter.
            - DM Reference: Halia wants to take over the operation for herself. Does not reveal this.
            - DM Reference: DC 15 Wisdom (Insight) check indicates she has ulterior motives for wanting
            the Redbrands leader out of the picture.

            ==Bonus==
            - If the party disposes of the Redbrand's leader, Halia approaches certain members
            to urge them to join the Zhentarim.
            - Speaks only with those that share the Zhentarim pursuits, such as wealth and power.
            - Even if the party wipes out the Redbrand gang, Halia may still extend the offer
            to gain friends (and spies) within the party.
            - If any character agrees, Halia awards the character the title of 'Fang.'
            '''
        },
        'qellinealderleaf': {
            'name': 'Qelline Alderleaf',
            'description': 'Wise female halfling of 45.',
            'location': 'Alderleaf Farm',
            'topics': '''
            - Seems to know about everything going on in town.
            - Kind Host and willing to let the characters stay in her hayloft if they
            don't want to stay at Stonehill Inn.

            ==Quests==
            Reidoth the Druid:
            - Qelline is a long time friend of a druid named Reidoth.
            - If she figures out that the characters are looking for specific sites in
            the area, such as Cragmaw Castle or Wave Echo Cave, she suggests that they
            visit Reidoth and ask for his help 'since there's not an inch of the land
            he doesn't know.'
            - She tells the characters that Reidoth recently set out for the ruins of
            a town called Thundertree, just west of the Neverwinter Wood.
            - The ruins are about fifty miles northwest of Phandalin, and she provides
            directions so the characters can easily find the place.
            - DM Reference: If the party pursues this quest, see the 'Ruins of Thundertree' section on
            page 30.
            '''
        },
        'carpalderleaf': {
            'name': 'Carp Alderleaf',
            'description': 'Qelline\'s son. A spirited and precocious halfling lad of 10.',
            'location': 'Alderleaf Farm',
            'topics': '''
            - Enchanged with the idea of being an adventurer.
            - Says that he is playing in the woods near Tresendar Manor, when he found
            a secret tunnel un a thichet.
            - A couole of "big ugly bandits" came out of the tunnel when he was there
            and met with a pair of Redbrands.
            - They didn't see him, but it was close.
            - Thinks that the bandits have a secret lair under the old manor house.
            - He can take the characters to the tunnel or provide them with directions
            to the location.
            - The tunnel leads to area 8 in the Redbrand's hideout.
            '''
        },
        'sisterGaraele': {
            'name': 'Sister Garaele',
            'description': 'A zealous young elf',
            'location': 'Shrine of Luck',
            'topics': '''
            - Despairs of ever ridding Phandalin of the Redbrands.
            - Member of the Harpers, a scattered network of adventurers and spies
            who advocate equality and covertly oppose the abuse of power.
            - The Harpers gather information throughout the land in order to thwart
            tyrants and any leader, government, or group that grows too strong.
            - They aid the weak, the poor, and the oppressed.
            - Sister Garaele regularly reports to her superiors on events in and
            around Phandalin.

            ==Quests==
            The Banshee's Bargain:
            - Recently, Garaele's superiors asked her to undertake a delicate mission.
            - They want her to pursuade a banshee name Agatha to answer a question about
            a spellbook. 
            - Garaele sought out Agatha in her lair, but the creature did not appear for
            her.
            - Garaele desires an intermediary to bring Agatha a suitable gift, a jeweled
            silver comb, and persuade the creature to tell what she knows about the
            location of a spellbook belonging to the legendar mage named Bowgentle.
            - Sister Garaele believes that a character who flatters Agatha's vanity
            might be able to trade the comb for an answer.
            - She offers the quest to the characters and offers them 3 potions of
            healing as payment for their efforts.
            - DM Reference: If the party pursues the quest, see the 'Conyberry and
            Agatha's Lair' section on page 28 for more information.
            ''',
        },
        'harbinwester': {
            'name': 'Harbin Wester',
            'description': 'Male Human Banker. Fat and pompous old fool,',
            'location': 'Townmasters Hall',
            'topics': '''
            - Claims that they are 'just a mercenary guild, and not all that much
            trouble, really.'
            - DM Reference: Completely intimidated by the Redbrands.
            - Carries the keys to the cell doors of the jail.

            ==Quest==
            Orc Trouble:
            - Harbin is looking for someone to head east on the Triboar Trail.
            - Travelers have been reporting trouble with a band of orcs near
            Wyvern Tor.
            - Offers group 100gp if they can take care of the problem.
            - If the party pursues the quest, see the "Wyvern Tor" section
            on page 35 for more information.
            '''
        },
        'sildarhallwinter': {
            'name': 'Sildar Hallwinter',
            'description': 'Human Warrior',
            'location': 'Townmaster\'s Hall',
            'topics': '''

            ==Quests==
            1) Finding Cragmaw Castle (After Sildar Rest):
                - After resting at the Stonehill Inn, Sildar establishes himself at
                the townmaster's hall.
                - As an agent of the Lord's Alliance, his goal is to bring law and order
                to Phandalin.
                - As such, he wants to find the lost mine of Wave Echo Cave and help
                the Rockseeker brothers put it back into production, believing that
                bringing prosperity to the region will help civilize the town.
                - Encourages the characters to keep up the pressure on the Cragmaw goblins.
                - Offers the party a 500gp reward if they can locate Cragmaw Castle
                and defeat or drive off the tribe's chieftain.
                - Suggests the party might find the castle by searching the lands around
                the Triboar Trail for more raiding parties.
                - DM Reference: If the players accept the quest, see 'Wilderness Encounters' in the
                'Triboar Trail' section of Part 3 for more information.
            2) Finding Iarno:
                - After questioning several locals Sildar learns that Iarno Albrek, a
                fellow member of the Lord's Alliance, disappeared while exploring the
                area around Tresendar Manor about 2 months ago, shortly after arriving
                in Phandalin.
                - Sildar asks the party to investigate the manor and the surrounding area
                to find and bring back Iarno (or what's left of him if something killed him).
                - Sildar describes Iarno as a 'short, dark bearded human wizard in his thirties'.
                - DM Reference: Unknown to Sildar, Iarno created the Redbrands, installed himself
                as their leader, and took the alias 'Glasstaff' to conceal his identity.
                - DM Reference: The Redbrands call him 'Glasstaff' because he carries a glass staff.
            3) After Finding Iarno:
                - Once Sildar learns the truth about Iarno, Sildar expresses a
                desire to have the wizard captured and transported to Neverwinter to face the
                judgement of a higher authority.
                - Regardless of Iarno's fate, Sildar rewards the party with 200gp for
                eliminating the Redbrand threat.

            ==Bonus==
            - If the party eliminates the goblin threat from Cragmaw Castle or uncovers Iarno's
            treachery, Sildar privately approaches certain members of the group to urge them to
            join the Lord's Alliance.
            - He speaks only with those who exemplify a desire for the security of civilization
            through action.
            - If a character agrees, Sildar awards them with the title of 'Cloak.'
            '''
        }
    } 
}

def main():
    input_var = raw_input('Enter search string: ')
    out_text = ''

    input_vars = input_var.split(' ') if ' ' in input_var else [input_var]

    if 'tag' in input_var and len(input_vars) == 2:
        for location in dd_info['locations']:
            if 'tags' not in dd_info['locations'][location]:
                pass
            else:
                if input_vars[1] in dd_info['locations'][location]['tags']:
                    out_text += dd_info['locations'][location]['name']
                    out_text += '\n'
        
        return out_text

    else:
        pass

    if len(input_vars) == 2:
        try:
            search_area = [item for item in dd_info if input_vars[0] in item.lower()]
            search_item = [item for item in dd_info[search_area[0]] if input_vars[1] in item.lower()]
        except:
            out_text += 'Item not found.'
            return out_text
        if search_area == [] or search_item == []:
            out_text += 'Item not found.'
        else:
            out_text += '\n\n\n=====%s=====\n' % dd_info[search_area[0]][search_item[0]]['name']
            for area in dd_info[search_area[0]][search_item[0]]:
                out_text += '\n*%s*\n' % area
                out_text += textwrap.dedent(str(dd_info[search_area[0]][search_item[0]][area]))
                out_text += '\n'

    elif len(input_vars) == 1:
        try:
            search_area = [item for item in dd_info if input_vars[0] in item.lower()]
        except:
            out_text += 'Item not found.'
            return out_text
        if search_area == []:
            out_text += 'Item not found.'
        else:
            out_text += '\n\n\n=====%s=====\n' % search_area[0].capitalize()
            for item in dd_info[search_area[0]]:
                out_text += dd_info[search_area[0]][item]['name'] +'\n'

    elif len(input_vars) == 3:
        try:
            search_area = [item for item in dd_info if input_vars[0] in item.lower()]
            search_item = [item for item in dd_info[search_area[0]] if input_vars[1] in item.lower()]
            search_info = [item for item in dd_info[search_area[0]][search_item[0]] if input_vars[2] in item.lower()]
            print(search_info)
        except:
            out_text += 'Item not found.'
            return out_text
        if search_area == [] or search_item == [] or search_info == []:
            out_text += 'Item not found.'
        else:
            out_text += '\n\n\n=====%s=====\n' % dd_info[search_area[0]][search_item[0]]['name']
            out_text += '\n*%s*\n' % search_info[0]
            out_text += textwrap.dedent(str(dd_info[search_area[0]][search_item[0]][search_info[0]]))
            out_text += ' '

    else:
        out_text += 'Item not found.'

    return out_text
 
if __name__ == '__main__':
    while True:
        return_value = main()
        print(return_value)