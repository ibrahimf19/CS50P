def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):

   if len(plate)<7 and len(plate)>1 and plate[0:2].isalpha() and plate.isalnum():
       for i in range(len(plate)-1):
           if plate[i] == "0" and plate[i-1].isdigit()==False:
               return False
           if plate[i].isdigit() and plate[i+1].isalpha():
               return False
       return plate
   return False

if __name__ == "__main__":
    main()
