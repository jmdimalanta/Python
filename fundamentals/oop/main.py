import ninja
import pets

scorpion = ninja.Ninja("Hanzo", "Hasashi", "biscuits", "rice", "dog")

bruce = pets.Pet("Bruce", "dog", "fetch")

scorpion.walk(bruce)
scorpion.feed(bruce)
scorpion.bathe(bruce)
