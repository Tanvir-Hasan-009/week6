filename = input("Enter the file name: ")

try:
    
    with open(filename, "r") as file:
        
        total_confidence = 0.0
        count = 0     
        for line in file:       
            if line.startswith("X-DSPAM-Confidence:"):
                
                confidence_str = line.split(":")[1].strip()
                try:
            
                    confidence = float(confidence_str)
                    
                    total_confidence += confidence
            
                    count += 1
                except ValueError:
                    continue

                
        if count > 0:
            
            average_confidence = total_confidence / count
            
            print(f"Average spam confidence: {average_confidence:.14f}")
        else:
            
            print("No X-DSPAM-Confidence lines found in the file")

except FileNotFoundError:
    
    print(f"File cannot be opened: {filename}")