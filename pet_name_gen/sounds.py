
class Sound:
    cons = "consonant"
    vowel = "vowel"
    def __init__(self, symbol, pronounce, sound_type):
        self.symbol = symbol
        self.pronounce = pronounce
        self.sound_type = sound_type
    
    def __str__(self):
        return self.symbol + " (" + self.pronounce + ")"
    
    def is_consonant(self):
        return self.sound_type == Sound.cons

consonant_list =   [Sound("b", "Bat", Sound.cons),
                    Sound("d", "Dog", Sound.cons),
                    Sound("f", "Fat", Sound.cons),
                    Sound("g", "Good", Sound.cons),
                    Sound("h", "Her", Sound.cons),
                    Sound("j", "Judge", Sound.cons),
                    Sound("k", "Cat", Sound.cons),
                    Sound("l", "Let", Sound.cons),
                    Sound("m", "Man", Sound.cons),
                    Sound("n", "Nail", Sound.cons),
                    Sound("p", "Pop", Sound.cons),
                    Sound("r", "Rat", Sound.cons),
                    Sound("s", "Saw", Sound.cons),
                    Sound("t", "Tall", Sound.cons),
                    Sound("v", "Very", Sound.cons),
                    Sound("w", "Wet", Sound.cons),
                    Sound("z", "Zap", Sound.cons),
                    Sound("th", "THing", Sound.cons),
                    Sound("tv", "faTHer", Sound.cons),
                    Sound("sh", "shape", Sound.cons),
                    Sound("dg", "beiGe", Sound.cons),
                    Sound("ng", "ring", Sound.cons),
                    Sound("y", "You", Sound.cons)]

vowel_list =       [Sound("a_", "cAke", Sound.vowel),
                    Sound("e_", "kEEp", Sound.vowel),
                    Sound("i_", "bIke", Sound.vowel),
                    Sound("o_", "hOme", Sound.vowel),
                    Sound("u_", "cUte", Sound.vowel),
                    Sound("a", "cAt", Sound.vowel),
                    Sound("e", "bEd", Sound.vowel),
                    Sound("i", "sIt", Sound.vowel),
                    Sound("o", "tOp", Sound.vowel),
                    Sound("uh", "sUn", Sound.vowel),
                    Sound("u", "pUt", Sound.vowel),
                    Sound("oo", "sOOn", Sound.vowel),
                    Sound("aw", "dOg", Sound.vowel),
                    Sound("oi", "join", Sound.vowel),
                    Sound("ow", "ow", Sound.vowel)]