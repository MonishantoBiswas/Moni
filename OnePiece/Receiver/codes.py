class unipolar:
    def __init__(self) -> None:
        self.prev = None
    def manchester(self, data) -> None:
        """Manchester coding
        The data is preceded by one low (0) bit and succeded by one low (0) bit
        for the sake of synchronization
        Data must be therefore of 19 characters long in total."""
        byte = ""
        if self.prev and data[:2] == self.prev:
            return
        try:
            for i in range(2, len(data) - 2, 2):
                pair = data[i:i+2]
                if pair == "10":
                    byte += "0"
                elif pair == "01":
                    byte += "1"
                else:
                    #print("<!>", end="", flush=True)
                    return
        except Exception as e:
            print(e)
            return
        char = chr(int(byte, 2))
        print(char, end="", flush=True)
        self.prev = data[:2]
        
    
    def NRZ(data) -> None:
        "Non Return to Zero coding"
        print("NRZ:", data) # Placeholder