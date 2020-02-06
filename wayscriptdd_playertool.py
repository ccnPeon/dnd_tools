# connect a variable above and read its value from the inputs dictionary:
from pprint import pprint
import textwrap
dd_info = {
    'quests': {
        'Old Owl Trouble': '''
            - Daran has heard stories from prospectors that there is someone digging
            around in the hills ot the northeast in the ruins know as 'Old Owl Well.'
            - More disturbingly, several prospectors have reported bing chased from
            the area by undead.
            - He asks the characters to visit the ruins, a two-day march northeast of
            Phandalin, and find out who's there and what they're up to.
            - Daran knows that the ruins are an old watchtower of an ancient magical
            empire known as Netheril, and he worries that the dangerous magic might
            be dormant there.
            ==NPC==
            Doran Edermath - Edermath Orchard - Phandalin
        ''',
        'Halias Job Offer': '''
            - Tells players how the ruffians loiter around the Sleeping Giant Tap House on the east of town.
            - Also tells players that the ruffians have a base under Tresendar Manor on the eastern edge
            of town.
            - Offers characters 100gp to eliminate the Redbrand's leader, Glasstaff, and bring
            any correspondence they find in the leader's quarter.
            ==NPC==
            Halia Thornton - Phandalin Miner's Exchange - Phandalin
        ''',
        'Reidoth the Druid':
        '''
        - Suggests that players visit Reidoth and ask for his help 'since there's not an inch of the land
        he doesn't know.'
        - She tells the characters that Reidoth recently set out for the ruins of
        a town called Thundertree, just west of the Neverwinter Wood.
        - The ruins are about fifty miles northwest of Phandalin, and she provides
        directions so the characters can easily find the place.
        ==NPC==
        Qelline Alderleaf - Alderleaf Farm - Phandalin
        ''',
        'The Banshee\'s Bargain':
        '''
        - Recently, Garacle's superiors asked her to undertake a delicate mission.
        - They want her to pursuade a banshee name Agatha to answer a question about
        a spellbook. 
        - Garacle sought out Agatha in her lair, but the creature did not appear for
        her.
        - Garacle desires an intermediary to bring Agatha a suitable gift, a jeweled
        silver comb, and persuade the creature to tell what she knows about the
        location of a spellbook belonging to the legendar mage named Bowgentle.
        - Sister Garacle believes that a character who flatters Agatha's vanity
        might be able to trade the comb for an answer.
        - She offers the quest to the characters and offers them 3 potions of
        healing as payment for their efforts.
        ==NPC==
        Sister Garacle - Shrine of Luck - Phandalin
        ''',
        'Orc Trouble':
        '''
        - Harbin is looking for someone to head east on the Triboar Trail.
        - Travelers have been reporting trouble with a band of orcs near
        Wyvern Tor.
        - Offers group 100gp if they can take care of the problem.
        ==NPC==
        Harbin Wester - Townmaster's Hall - Phandalin
        ''',
        'Finding Cragmaw Castle':
        '''
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
        ==NPC==
        Sildar Hallwinter - Townmaster's Hall - Phandalin
        ''',
        'Finding Iarno':
        '''
        - After questioning several locals Sildar learns that Iarno Albrek, a
        fellow member of the Lord's Alliance, disappeared while exploring the
        area around Tresendar Manor about 2 months ago, shortly after arriving
        in Phandalin.
        - Sildar asks the party to investigate the manor and the surrounding area
        to find and bring back Iarno (or what's left of him if something killed him).
        - Sildar describes Iarno as a 'short, dark bearded human wizard in his thirties'.
        ==NPC==
        Sildar Hallwinter - Townmaster's Hall - Phandalin
        ''',
    }
}

def main():
    input_text = ''
    search_command = '!quests'
    out_text = ''

    if input_text == search_command:
        for item in dd_info['quests']:
                if item in dd_info['quests']['enabled_quests']:
                    out_text += '*%s*' % item
                    out_text += textwrap.dedent(dd_info['quests'][item])
                    out_text += '\n\n'
        
        if out_text == '':
            return 'No quests found.'
        else:
            out_text = '*=====Quests=====*\n\n' + out_text
            return out_text

    else:
        return 'No quests found.'


 
if __name__ == '__main__':
    return_value = main()
    print(return_value)