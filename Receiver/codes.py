class unipolar:
    def __init__(self) -> None:
        self.prev = None
    def manchester(self, data) -> None:
        """Manchester coding
        The data is preceded by one low (0) bit and succeded by one low (0) bit
        for the sake of synchronization
        Data must be therefore of 18 characters long in total."""
        if len(data) != 18 or data[0] != "0" or data[-1] != "0":
            #print("<!>", end="", flush=True) # Invalid Byte
            return
        byte = ""
        try:
            for i in range(1, len(data) - 2, 2):
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
        if char != self.prev:
            print(char, end="", flush=True)
            self.prev = char
        
    
    def NRZ(data) -> None:
        "Non Return to Zero coding"
        print("NRZ:", data) # Placeholder