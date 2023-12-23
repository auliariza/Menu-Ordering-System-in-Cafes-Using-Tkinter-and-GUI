from cProfile import label
import string
from tkinter import *
import random
import csv
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog
from turtle import clear;
from PIL import ImageTk, Image 
from pygame import mixer

def play_background_music():
    mixer.init()
    mixer.music.load("krustykrab.mp3")  # Replace "background_music.mp3" with the path to your music file
    mixer.music.play(1)  # -1 will make the music loop indefinitely

# Start playing background music
play_background_music()

#Membuat Frame aplikasi
root = Tk()

root.geometry("1540x760+0+0") # menentukan ukuran window aplikasi
root.resizable(0,0)
root.title("Krusty Krab Cashier") # nama aplikasi

topFrame=Frame(root,bd=10,relief=RIDGE,bg='white') # frame judul
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Krusty Krab',font=('Krabby Patty',39,'bold'),fg='#461912',bg='#ffeec2', bd=15,width=30) #judul aplikasi
labelTitle.grid(row=0,column=10)

root.config(bg='#784c12') # warna dasar / background
# batas Frame aplikasi

# VARIABLE
# Menentukan variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

# variabel menuiMealsDealshargadariMealsDeals
e_KrabbyPatty=StringVar()
e_KrabbyPattySeaCheese=StringVar()
e_DoubleKrabbyPatty = StringVar()
e_TripleKrabbyPatty = StringVar()
e_KrabbyMeal = StringVar()
e_DoubleKrabbyMeal = StringVar()
e_SailorsSurprise = StringVar()
e_SaltySeaDog = StringVar()
e_FootLong = StringVar()

# variabel menu Drinks
e_KelpShake =StringVar()
e_SmallSeafoamSoda = StringVar()
e_MediumSeafoamSoda = StringVar()
e_LargeSeafoamSoda = StringVar()

# variabel menu SeadSideshargadariSeadSides
e_CoralBits=StringVar()
e_LargeCoralBits = StringVar()
e_KelpRings = StringVar()
e_SaltySauce = StringVar()
e_KrabbyFries = StringVar()
e_SeaweedSalad = StringVar()

# variabel Harga dalam struk
hargadariMealsDealsvar=StringVar()
hargadariDrinksvar=StringVar()
hargadariSeadSidesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()
taxvaluevar=StringVar()

e_KrabbyPatty.set('0')
e_KrabbyPattySeaCheese.set('0')
e_DoubleKrabbyPatty.set('0')
e_TripleKrabbyPatty.set('0')
e_KrabbyMeal.set('0')
e_DoubleKrabbyMeal.set('0')
e_SailorsSurprise.set('0')
e_SaltySeaDog.set('0')
e_FootLong.set('0')

e_KelpShake .set('0')
e_SmallSeafoamSoda.set('0')
e_MediumSeafoamSoda.set('0')
e_LargeSeafoamSoda.set('0')

e_CoralBits.set('0')
e_LargeCoralBits.set('0')
e_KelpRings.set('0')
e_SaltySauce.set('0')
e_KrabbyFries.set('0')
e_SeaweedSalad.set('0')

# FUNGSI
# Awal fungsi perhitungan harga total
tax=(11/100)
def totalcost():
    # mengglobalkan beberapa variable terlebih dahulu
    global hargadariMealsDeals,hargadariDrinks,hargadariSeadSides,subtotalItems,totaltax
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        item1=int(e_KrabbyPatty.get())
        item2=int(e_KrabbyPattySeaCheese.get())
        item3=int(e_DoubleKrabbyPatty.get())
        item4=int(e_TripleKrabbyPatty.get())
        item5=int(e_KrabbyMeal.get())
        item6=int(e_DoubleKrabbyMeal.get())
        item7=int(e_SailorsSurprise.get())
        item8=int(e_SaltySeaDog.get())
        item9=int(e_FootLong.get())

        item10=int(e_KelpShake .get())
        item11=int(e_SmallSeafoamSoda.get())
        item12=int(e_MediumSeafoamSoda.get())
        item13=int(e_LargeSeafoamSoda.get())

        item19=int(e_CoralBits.get())
        item20=int(e_LargeCoralBits.get())
        item21=int(e_KelpRings.get())
        item22=int(e_SaltySauce.get())
        item23=int(e_KrabbyFries.get())
        item24=int(e_SeaweedSalad.get())

        hargadariMealsDeals=(item1*28000) + (item2*32000) + (item3*29000) + (item4*28000) + (item5*31000) + (item6*26000) + (item7*38000) \
        + (item8*27000) + (item9*29000)
        hargadariDrinks=(item10*20000) + (item11*15000) + (item12*15000) + (item13*22000)
        hargadariSeadSides=(item19*18000) + (item20*25000) + (item21*25000) + (item22*28000) + (item23*16000) + (item24*21000) \

        hargadariMealsDealsvar.set(str(hargadariMealsDeals))
        hargadariDrinksvar.set(str(hargadariDrinks))
        hargadariSeadSidesvar.set(str(hargadariSeadSides))

        subtotalItems=hargadariMealsDeals+hargadariDrinks+hargadariSeadSides
        subtotalvar.set(str(subtotalItems))
       #tax=(11/100)
        taxvaluevar.set(str(tax))
        totaltax= subtotalItems*tax
        
        servicetaxvar.set(totaltax)
        
        totalcost=subtotalItems+totaltax
        totalcostvar.set(str(totalcost))

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
# Batas fungsi perhitungan harga total

# awal fungsi cetak struk
def struk():
    global billnumber, date
    if hargadariMealsDealsvar.get() != '' or hargadariSeadSidesvar.get() != '' or hargadariDrinksvar.get() != '':
        textStruk.delete(1.0, END)
        x = random.randint(100, 10000)
        billnumber = 'BILL' + str(x)
        
        # Get the current date and time
        current_datetime = datetime.now()
        date = current_datetime.strftime('%d/%m/%Y %H:%M:%S')
        
        textStruk.insert(END, 'Receipt Ref:\t        ' + billnumber + '\t         ' + date + '\n')
        textStruk.insert(END, '************************************\n')
        textStruk.insert(END, 'Items:\t\t\tQty\t\tTotal Price (Rp)\n')
        textStruk.insert(END, '************************************\n')
    
        # Krabby Patty
        if e_KrabbyPatty.get() != '0':
            quantity_KrabbyPatty = int(e_KrabbyPatty.get())
            total_price_KrabbyPatty = quantity_KrabbyPatty * 27000
            textStruk.insert(END, f'KrabbyPatty\t\t\t{quantity_KrabbyPatty}\t\tRp. {total_price_KrabbyPatty}\n\n')
        
        # Krabby Patty with Sea Cheese
        if e_KrabbyPattySeaCheese.get() != '0':
            quantity_KrabbyPattySeaCheese = int(e_KrabbyPattySeaCheese.get())
            total_price_KrabbyPattySeaCheese = quantity_KrabbyPattySeaCheese * 33000
            textStruk.insert(END, f'KrabbyPattySeaCheese\t\t\t{quantity_KrabbyPattySeaCheese}\t\tRp. {total_price_KrabbyPattySeaCheese}\n\n')

        # Double Krabby Patty
        if e_DoubleKrabbyPatty.get() != '0':
            quantity_DoubleKrabbyPatty = int(e_DoubleKrabbyPatty.get())
            total_price_DoubleKrabbyPatty = quantity_DoubleKrabbyPatty * 25000
            textStruk.insert(END, f'DoubleKrabbyPatty\t\t\t{quantity_DoubleKrabbyPatty}\t\tRp. {total_price_DoubleKrabbyPatty}\n\n')

        # Cinnamon Roll
        if e_TripleKrabbyPatty.get() != '0':
            quantity_TripleKrabbyPatty = int(e_TripleKrabbyPatty.get())
            total_price_TripleKrabbyPatty = quantity_TripleKrabbyPatty * 22000
            textStruk.insert(END, f'TripleKrabbyPatty\t\t\t{quantity_TripleKrabbyPatty}\t\tRp. {total_price_TripleKrabbyPatty}\n\n')

        # Krabby Meal
        if e_KrabbyMeal.get() != '0':
            quantity_KrabbyMeal = int(e_KrabbyMeal.get())
            total_price_KrabbyMeal = quantity_KrabbyMeal * 33000
            textStruk.insert(END, f'KrabbyMeal\t\t\t{quantity_KrabbyMeal}\t\tRp. {total_price_KrabbyMeal}\n\n')

        # Double Krabby Meal
        if e_DoubleKrabbyMeal.get() != '0':
            quantity_DoubleKrabbyMeal = int(e_DoubleKrabbyMeal.get())
            total_price_DoubleKrabbyMeal = quantity_DoubleKrabbyMeal * 46000
            textStruk.insert(END, f'DoubleKrabbyMeal\t\t\t{quantity_DoubleKrabbyMeal}\t\tRp. {total_price_DoubleKrabbyMeal}\n\n')

        # Sailors Surprise
        if e_SailorsSurprise.get() != '0':
            quantity_SailorsSurprise = int(e_SailorsSurprise.get())
            total_price_SailorsSurprise = quantity_SailorsSurprise * 38000
            textStruk.insert(END, f'SailorsSurprise\t\t\t{quantity_SailorsSurprise}\t\tRp. {total_price_SailorsSurprise}\n\n')

        # Salty Sea Dog
        if e_SaltySeaDog.get() != '0':
            quantity_SaltySeaDog = int(e_SaltySeaDog.get())
            total_price_SaltySeaDog = quantity_SaltySeaDog * 27000
            textStruk.insert(END, f'avocado toast\t\t\t{quantity_SaltySeaDog}\t\tRp. {total_price_SaltySeaDog}\n\n')

        # Foot Long
        if e_FootLong.get() != '0':
            quantity_FootLong = int(e_FootLong.get())
            total_price_FootLong = quantity_FootLong * 22000
            textStruk.insert(END, f'tomato soup\t\t\t{quantity_FootLong}\t\tRp. {total_price_FootLong}\n\n')

        # Kelp Shake
        if e_KelpShake .get() != '0':
            quantity_KelpShake  = int(e_KelpShake .get())
            total_price_KelpShake  = quantity_KelpShake  * 20000
            textStruk.insert(END, f'apple juice\t\t\t{quantity_KelpShake }\t\tRp. {total_price_KelpShake }\n\n')

        # Small Seafoam Soda
        if e_SmallSeafoamSoda.get() != '0':
            quantity_SmallSeafoamSoda = int(e_SmallSeafoamSoda.get())
            total_price_SmallSeafoamSoda = quantity_SmallSeafoamSoda * 15000
            textStruk.insert(END, f'lemon tea\t\t\t{quantity_SmallSeafoamSoda}\t\tRp. {total_price_SmallSeafoamSoda}\n\n')

        # Medium Seafoam Soda
        if e_MediumSeafoamSoda.get() != '0':
            quantity_MediumSeafoamSoda = int(e_MediumSeafoamSoda.get())
            total_price_MediumSeafoamSoda = quantity_MediumSeafoamSoda * 15000
            textStruk.insert(END, f'MediumSeafoamSoda\t\t\t{quantity_MediumSeafoamSoda}\t\tRp. {total_price_MediumSeafoamSoda}\n\n')

        # Large Seafoam Soda
        if e_LargeSeafoamSoda.get() != '0':
            quantity_LargeSeafoamSoda = int(e_LargeSeafoamSoda.get())
            total_price_LargeSeafoamSoda = quantity_LargeSeafoamSoda * 22000
            textStruk.insert(END, f'LargeSeafoamSoda\t\t\t{quantity_LargeSeafoamSoda}\t\tRp. {total_price_LargeSeafoamSoda}\n\n')

         # Large Coral Bits
        if e_LargeCoralBits.get() != '0':
            quantity_LargeCoralBits = int(e_LargeCoralBits.get())
            total_price_LargeCoralBits = quantity_LargeCoralBits * 36000
            textStruk.insert(END, f'french fries\t\t\t{quantity_LargeCoralBits}\t\tRp. {total_price_LargeCoralBits}\n\n')

        # Kelp Rings
        if e_KelpRings.get() != '0':
            quantity_KelpRings = int(e_KelpRings.get())
            total_price_KelpRings = quantity_KelpRings * 15000
            textStruk.insert(END, f'fried ice cream\t\t\t{quantity_KelpRings}\t\tRp. {total_price_KelpRings}\n\n')

        # Salty Sauce
        if e_SaltySauce.get() != '0':
            quantity_SaltySauce = int(e_SaltySauce.get())
            total_price_SaltySauce = quantity_SaltySauce * 1500
            textStruk.insert(END, f'cheese cake\t\t\t{quantity_SaltySauce}\t\tRp. {total_price_SaltySauce}\n\n')

        # Krabby Fries
        if e_KrabbyFries.get() != '0':
            quantity_KrabbyFries = int(e_KrabbyFries.get())
            total_price_KrabbyFries = quantity_KrabbyFries * 16000
            textStruk.insert(END, f'ice cream\t\t\t{quantity_KrabbyFries}\t\tRp. {total_price_KrabbyFries}\n\n')

        # Seaweed Salad
        if e_SeaweedSalad.get() != '0':
            quantity_SeaweedSalad = int(e_SeaweedSalad.get())
            total_price_SeaweedSalad = quantity_SeaweedSalad * 21000
            textStruk.insert(END, f'SeaweedSalad\t\t\t{quantity_SeaweedSalad}\t\tRp. {total_price_SeaweedSalad}\n\n')

        textStruk.insert(END,'******************\n')
        if hargadariMealsDealsvar.get()!='Rp 0':
            textStruk.insert(END,f'Meals price\t\t\tRp. {hargadariMealsDeals}\n\n')
        if hargadariDrinksvar.get() != 'Rp 0':
            textStruk.insert(END,f'Drinks price\t\t\tRp. {hargadariDrinks}\n\n')
        if hargadariSeadSidesvar.get() != 'Rp 0':
            textStruk.insert(END,f'Sea sides price \t\t\tRp. {hargadariSeadSides}\n\n')

        textStruk.insert(END, f'Sub Total\t\t\tRp. {subtotalItems}\n\n')
        textStruk.insert(END, f'Service Tax\t\t\tRp. {totaltax}\n\n')
        textStruk.insert(END, f'Total price\t\t\tRP. {subtotalItems+totaltax}\n\n')
        textStruk.insert(END,'******************\n')

    else:
        messagebox.showerror('Error','No items selected')
# batas fungsi cetak struk

# Fungsi simpan dalam perangkat
def save():
    if textStruk.get(1.0, END) == '\n':
        pass
    else:
        # Tentukan path file
        file_path = r'C:\Users\syari\Document\KULIAH\Semester 5\Pemlan\Praktikum\projek\ReceiptHistory.csv'

        bill_data = textStruk.get(1.0, END)

        # Write the data in CSV format
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            # Split the data into lines and write each line as a row
            for line in bill_data.split('\n'):
                writer.writerow([line])

        messagebox.showinfo('Information', 'Your receipt has been saved')
# Batas fungsi simpan dalam perangkat


# awal fungsi reset
def reset():
    textStruk.delete(1.0,END)
    e_KrabbyPatty.set('0')
    e_KrabbyPattySeaCheese.set('0')
    e_DoubleKrabbyPatty.set('0')
    e_TripleKrabbyPatty.set('0')
    e_KrabbyMeal.set('0')
    e_DoubleKrabbyMeal.set('0')
    e_SailorsSurprise.set('0')
    e_SaltySeaDog.set('0')
    e_FootLong.set('0')

    e_KelpShake .set('0')
    e_SmallSeafoamSoda.set('0')
    e_MediumSeafoamSoda.set('0')
    e_LargeSeafoamSoda.set('0')

    e_CoralBits.set('0')
    e_LargeCoralBits.set('0')
    e_KelpRings.set('0')
    e_SaltySauce.set('0')
    e_KrabbyFries.set('0')
    e_SeaweedSalad.set('0')
    # batas untuk variables

    textKrabbyPatty.config(state=DISABLED)
    textKrabbyPattySeaCheese.config(state=DISABLED)
    textDoubleKrabbyPatty.config(state=DISABLED)
    textTripleKrabbyPatty.config(state=DISABLED)
    textKrabbyMeal.config(state=DISABLED)
    textDoubleKrabbyMeal.config(state=DISABLED)
    textSailorsSurprise.config(state=DISABLED)
    textSaltySeaDog.config(state=DISABLED)
    textFootLong.config(state=DISABLED)

    textKelpShake .config(state=DISABLED)
    textSmallSeafoamSoda.config(state=DISABLED)
    textMediumSeafoamSoda.config(state=DISABLED)
    textLargeSeafoamSoda.config(state=DISABLED)

    textCoralBits.config(state=DISABLED)
    textLargeCoralBits.config(state=DISABLED)
    textKelpRings.config(state=DISABLED)
    textSaltySauce.config(state=DISABLED)
    textKrabbyFries.config(state=DISABLED)
    textSeaweedSalad.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    hargadariDrinksvar.set('')
    hargadariMealsDealsvar.set('')
    hargadariSeadSidesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
    taxvaluevar.set('')

# batas fungsi reset

# mengaktifkan fungsi entry menu makanan
def KrabbyPatty():
    if var1.get()==1:
        textKrabbyPatty.config(state=NORMAL)
        textKrabbyPatty.delete(0,END)
        textKrabbyPatty.focus()
    else:
        textKrabbyPatty.config(state=DISABLED)
        e_KrabbyPatty.set('0')

def KrabbyPattySeaCheese():
    if var2.get()==1:
        textKrabbyPattySeaCheese.config(state=NORMAL)
        textKrabbyPattySeaCheese.delete(0,END)
        textKrabbyPattySeaCheese.focus()
    else:
        textKrabbyPattySeaCheese.config(state=DISABLED)
        e_KrabbyPattySeaCheese.set('0')

def DoubleKrabbyPatty():
    if var3.get()==1:
        textDoubleKrabbyPatty.config(state=NORMAL)
        textDoubleKrabbyPatty.delete(0,END)
        textDoubleKrabbyPatty.focus()
    else:
        textDoubleKrabbyPatty.config(state=DISABLED)
        e_DoubleKrabbyPatty.set('0')

def TripleKrabbyPatty():
    if var4.get()==1:
        textTripleKrabbyPatty.config(state=NORMAL)
        textTripleKrabbyPatty.delete(0,END)
        textTripleKrabbyPatty.focus()

    else:
        textTripleKrabbyPatty.config(state=DISABLED)
        e_TripleKrabbyPatty.set('0')

def KrabbyMeal ():
    if var5.get()==1:
        textKrabbyMeal.config(state=NORMAL)
        textKrabbyMeal.delete(0,END)
        textKrabbyMeal.focus()
    else:
        textKrabbyMeal.config(state=DISABLED)
        e_KrabbyMeal.set('0')

def DoubleKrabbyMeal():
    if var6.get()==1:
        textDoubleKrabbyMeal.config(state=NORMAL)
        textDoubleKrabbyMeal.delete(0,END)
        textDoubleKrabbyMeal.focus()
    else:
        textDoubleKrabbyMeal.config(state=DISABLED)
        e_DoubleKrabbyMeal.set('0')

def SailorsSurprise():
    if var7.get()==1:
        textSailorsSurprise.config(state=NORMAL)
        textSailorsSurprise.delete(0,END)
        textSailorsSurprise.focus()
    else:
        textSailorsSurprise.config(state=DISABLED)
        e_SailorsSurprise.set('0')

def SaltySeaDog():
    if var8.get()==1:
        textSaltySeaDog.config(state=NORMAL)
        textSaltySeaDog.delete(0,END)
        textSaltySeaDog.focus()
    else:
        textSaltySeaDog.config(state=DISABLED)
        e_SaltySeaDog.set('0')

def FootLong():
    if var9.get()==1:
        textFootLong.config(state=NORMAL)
        textFootLong.delete(0,END)
        textFootLong.focus()
    else:
        textFootLong.config(state=DISABLED)
        e_FootLong.set('0')
# batas mengaktifkan entry menu makanan

# mengaktifkan entry menu Drinks
def KelpShake ():
    if var10.get()==1:
        textKelpShake .config(state=NORMAL)
        textKelpShake .delete(0,END)
        textKelpShake .focus()
    else:
        textKelpShake .config(state=DISABLED)
        e_KelpShake .set('0')

def SmallSeafoamSoda():
    if var11.get()==1:
        textSmallSeafoamSoda.config(state=NORMAL)
        textSmallSeafoamSoda.focus()
        textSmallSeafoamSoda.delete(0, END)
    else:
        textSmallSeafoamSoda.config(state=DISABLED)
        e_SmallSeafoamSoda.set('0')

def MediumSeafoamSoda():
    if var12.get()==1:
        textMediumSeafoamSoda.config(state=NORMAL)
        textMediumSeafoamSoda.delete(0,END)
        textMediumSeafoamSoda.focus()
    else:
        textMediumSeafoamSoda.config(state=DISABLED)
        e_MediumSeafoamSoda.set('0')

def LargeSeafoamSoda():
    if var13.get()==1:
        textLargeSeafoamSoda.config(state=NORMAL)
        textLargeSeafoamSoda.delete(0,END)
        textLargeSeafoamSoda.focus()
    else:
        textLargeSeafoamSoda.config(state=DISABLED)
        e_LargeSeafoamSoda.set('0')
# batas mengaktifkan entry Drinks

# mengaktifkan entry menu jajanan
def CoralBits():
    if var19.get()==1:
        textCoralBits.config(state=NORMAL)
        textCoralBits.focus()
        textCoralBits.delete(0,END)
    else:
        textCoralBits.config(state=DISABLED)
        e_CoralBits.set('0')

def LargeCoralBits():
    if var20.get()==1:
        textLargeCoralBits.config(state=NORMAL)
        textLargeCoralBits.delete(0,END)
        textLargeCoralBits.focus()
    else:
        textLargeCoralBits.config(state=DISABLED)
        e_LargeCoralBits.set('0')

def KelpRings():
    if var21.get()==1:
        textKelpRings.config(state=NORMAL)
        textKelpRings.delete(0,END)
        textKelpRings.focus()
    else:
        textKelpRings.config(state=DISABLED)
        e_KelpRings.set('0')

def SaltySauce():
    if var22.get()==1:
        textSaltySauce.config(state=NORMAL)
        textSaltySauce.delete(0,END)
        textSaltySauce.focus()
    else:
        textSaltySauce.config(state=DISABLED)
        e_SaltySauce.set('0')

def KrabbyFries():
    if var23.get()==1:
        textKrabbyFries.config(state=NORMAL)
        textKrabbyFries.delete(0,END)
        textKrabbyFries.focus()
    else:
        textKrabbyFries.config(state=DISABLED)
        e_KrabbyFries.set('0')

def SeaweedSalad():
    if var24.get()==1:
        textSeaweedSalad.config(state=NORMAL)
        textSeaweedSalad.delete(0,END)
        textSeaweedSalad.focus()
    else:
        textSeaweedSalad.config(state=DISABLED)
        e_SeaweedSalad.set('0')

# FRAME KIRI
# Membuat frame kiri untuk menu cafe
menuFrame=Frame(root,bd=10,relief=RIDGE,bg='#8ca2d2')
menuFrame.pack(side=LEFT)

hargaFrame=Frame(menuFrame,bd=9,relief=RIDGE,bg='#ffeec2',pady=12)
hargaFrame.pack(side=BOTTOM)
MealsDealsFrame = LabelFrame(menuFrame, text='Meals Deals', font=('Krabby Patty', 19, 'bold'), bd=10, relief=RIDGE, fg='#2f2f2f', bg='#7d6536')
MealsDealsFrame.pack(side=LEFT)

DrinksFrame=LabelFrame(menuFrame,text=' Drinks ',font=('Krabby Patty',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#7d6536')
DrinksFrame.pack(side=LEFT)

SeadSideshargadariSeadSidesFrame=LabelFrame(menuFrame,text=' Sea Sides ',font=('Krabby Patty',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#7d6536')
SeadSideshargadariSeadSidesFrame.pack(side=LEFT)
# batas frame kiri (menu cafe)


# membuat tampilan daftar menu makanan
KrabbyPatty = Checkbutton(MealsDealsFrame, text=' Krabby Patty ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var1, command=KrabbyPatty, bg='#7d6536')
KrabbyPatty.grid(row=0, column=0, sticky=W)

KrabbyPattySeaCheese = Checkbutton(MealsDealsFrame, text=' Krabby Patty with Sea Cheese ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var2, command=KrabbyPattySeaCheese, bg='#7d6536')
KrabbyPattySeaCheese.grid(row=1, column=0, sticky=W)

DoubleKrabbyPatty = Checkbutton(MealsDealsFrame, text=' Double Krabby Patty ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var3, command=DoubleKrabbyPatty, bg='#7d6536')
DoubleKrabbyPatty.grid(row=2, column=0, sticky=W)

TripleKrabbyPatty = Checkbutton(MealsDealsFrame, text=' Triple Krabby Patty ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var4, command=TripleKrabbyPatty, bg='#7d6536')
TripleKrabbyPatty.grid(row=3, column=0, sticky=W)

KrabbyMeal = Checkbutton(MealsDealsFrame, text=' Krabby Meal ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var5, command=KrabbyMeal, bg='#7d6536')
KrabbyMeal.grid(row=4, column=0, sticky=W)

DoubleKrabbyMeal = Checkbutton(MealsDealsFrame, text=' Double Krabby Meal ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var6, command=DoubleKrabbyMeal, bg='#7d6536')
DoubleKrabbyMeal.grid(row=5, column=0, sticky=W)

SailorsSurprise = Checkbutton(MealsDealsFrame, text=' Sailors Surprise ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var7, command=SailorsSurprise, bg='#7d6536')
SailorsSurprise.grid(row=6, column=0, sticky=W)

SaltySeaDog = Checkbutton(MealsDealsFrame, text=' Salty Sea Dog', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var8, command=SaltySeaDog, bg='#7d6536')
SaltySeaDog.grid(row=7, column=0, sticky=W)

FootLong = Checkbutton(MealsDealsFrame, text=' Foot Long ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var9, command=FootLong, bg='#7d6536')
FootLong.grid(row=8, column=0, sticky=W)

textKrabbyPatty = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_KrabbyPatty)
textKrabbyPatty.grid(row=0, column=1)

textKrabbyPattySeaCheese = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_KrabbyPattySeaCheese)
textKrabbyPattySeaCheese.grid(row=1, column=1)

textDoubleKrabbyPatty = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_DoubleKrabbyPatty)
textDoubleKrabbyPatty.grid(row=2, column=1)

textTripleKrabbyPatty = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_TripleKrabbyPatty)
textTripleKrabbyPatty.grid(row=3, column=1)

textKrabbyMeal = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_KrabbyMeal)
textKrabbyMeal.grid(row=4, column=1)

textDoubleKrabbyMeal = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_DoubleKrabbyMeal)
textDoubleKrabbyMeal.grid(row=5, column=1)

textSailorsSurprise = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_SailorsSurprise)
textSailorsSurprise.grid(row=6, column=1)

textSaltySeaDog = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_SaltySeaDog)
textSaltySeaDog.grid(row=7, column=1)

textFootLong = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_FootLong)
textFootLong.grid(row=8, column=1)

# membuat tampilan daftar menu Drinks
KelpShake =Checkbutton(DrinksFrame,text='Kelp Shake',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var10,
                        command=KelpShake , bg='#7d6536')
KelpShake .grid(row=0,column=0,sticky=W)

SmallSeafoamSoda=Checkbutton(DrinksFrame,text='Small Seafoam Soda',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var11,
                        command=SmallSeafoamSoda, bg='#7d6536')
SmallSeafoamSoda.grid(row=1,column=0,sticky=W)

MediumSeafoamSoda=Checkbutton(DrinksFrame,text='Medium Seafoam Soda',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var12,
                        command=MediumSeafoamSoda, bg='#7d6536')
MediumSeafoamSoda.grid(row=2,column=0,sticky=W)

LargeSeafoamSoda=Checkbutton(DrinksFrame,text='Large Seafoam Soda',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var13,
                        command=LargeSeafoamSoda, bg='#7d6536')
LargeSeafoamSoda.grid(row=3,column=0,sticky=W)

# menambahkan fields entri untuk item Drinks
textKelpShake =Entry(DrinksFrame,font=('Krabby Patty','14','bold'),bd=7,width=7,state=DISABLED,textvar=e_KelpShake )
textKelpShake .grid(row=0,column=1)

textSmallSeafoamSoda=Entry(DrinksFrame,font=('Krabby Patty','14','bold'),bd=7,width=7,state=DISABLED,textvar=e_SmallSeafoamSoda)
textSmallSeafoamSoda.grid(row=1,column=1)

textMediumSeafoamSoda=Entry(DrinksFrame,font=('Krabby Patty','14','bold'),bd=7,width=7,state=DISABLED,textvar=e_MediumSeafoamSoda)
textMediumSeafoamSoda.grid(row=2,column=1)

textLargeSeafoamSoda=Entry(DrinksFrame,font=('Krabby Patty','14','bold'),bd=7,width=7,state=DISABLED,textvar=e_LargeSeafoamSoda)
textLargeSeafoamSoda.grid(row=3,column=1)

# membuat tampilan daftar menu SeadSideshargadariSeadSides
CoralBits=Checkbutton(SeadSideshargadariSeadSidesFrame,text='Coral Bits',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var19,
            command=CoralBits, bg='#7d6536')
CoralBits.grid(row=0,column=0,sticky=W)

LargeCoralBits=Checkbutton(SeadSideshargadariSeadSidesFrame,text='Large Coral Bits',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var20,
            command=LargeCoralBits, bg='#7d6536')  
LargeCoralBits.grid(row=1,column=0,sticky=W)

KelpRings=Checkbutton(SeadSideshargadariSeadSidesFrame,text='Kelp Rings',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var21,
            command=KelpRings, bg='#7d6536')
KelpRings.grid(row=2,column=0,sticky=W)

SaltySauce=Checkbutton(SeadSideshargadariSeadSidesFrame,text='Salty Sauce',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var22,
            command=SaltySauce, bg='#7d6536')
SaltySauce.grid(row=3,column=0,sticky=W)

KrabbyFries=Checkbutton(SeadSideshargadariSeadSidesFrame,text='Krabby Fries',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var23,
            command=KrabbyFries, bg='#7d6536')
KrabbyFries.grid(row=4,column=0,sticky=W)

SeaweedSalad=Checkbutton(SeadSideshargadariSeadSidesFrame,text='Seaweed Salad',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var24,
            command=SeaweedSalad, bg='#7d6536')
SeaweedSalad.grid(row=5,column=0,sticky=W)

# menambahkan fields entri untuk item SeadSideshargadariSeadSides
textCoralBits = Entry(SeadSideshargadariSeadSidesFrame, font=('Krabby Patty','14','bold'),bd=7,width=7, state=DISABLED, textvar=e_CoralBits)
textCoralBits.grid(row=0, column=1)

textLargeCoralBits = Entry(SeadSideshargadariSeadSidesFrame, font=('Krabby Patty','14','bold'),bd=7,width=7, state=DISABLED, textvar=e_LargeCoralBits)
textLargeCoralBits.grid(row=1, column=1)

textKelpRings = Entry(SeadSideshargadariSeadSidesFrame, font=('Krabby Patty','14','bold'),bd=7,width=7, state=DISABLED, textvar=e_KelpRings)
textKelpRings.grid(row=2, column=1)

textSaltySauce = Entry(SeadSideshargadariSeadSidesFrame, font=('Krabby Patty','14','bold'),bd=7,width=7, state=DISABLED, textvar=e_SaltySauce)
textSaltySauce.grid(row=3, column=1)

textKrabbyFries = Entry(SeadSideshargadariSeadSidesFrame, font=('Krabby Patty','14','bold'),bd=7,width=7, state=DISABLED, textvar=e_KrabbyFries)
textKrabbyFries.grid(row=4, column=1)

textSeaweedSalad = Entry(SeadSideshargadariSeadSidesFrame, font=('Krabby Patty','14','bold'),bd=7,width=7, state=DISABLED, textvar=e_SeaweedSalad)
textSeaweedSalad.grid(row=5, column=1)

# FRAME KANAN

# Membuat frame kanan untuk (Struk)
rightFrame=Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

strukFrame=Frame(rightFrame,bd=1,relief=RIDGE, bg='#f0f0f0')
strukFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()
# Batas frame kanan (Struk)


# membuat label harga dan kolom entrinya
LabelHargadariMealsDeals=Label(hargaFrame,text='    MEALS PRICE', font=('Krabby Patty',12,'bold'),bg='#ffeec2',fg='#461912')
LabelHargadariMealsDeals.grid(row=0,column=0)

textHargadariMealsDeals=Entry(hargaFrame,font=('Krabby Patty',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadariMealsDealsvar)
textHargadariMealsDeals.grid(row=0,column=1,padx=41)

LabelHargadariDrinks=Label(hargaFrame,text='    DRINKS PRICE', font=('Krabby Patty',12,'bold'),bg='#ffeec2',fg='#461912')
LabelHargadariDrinks.grid(row=1,column=0)

textHargadariDrinks=Entry(hargaFrame,font=('Krabby Patty',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadariDrinksvar)
textHargadariDrinks.grid(row=1,column=1,padx=41)

LabelHargadariSeaSides=Label(hargaFrame,text='  SEA SIDES PRICE', font=('Krabby Patty',12,'bold'),bg='#ffeec2',fg='#461912')
LabelHargadariSeaSides.grid(row=2,column=0)

textHargadariSeaSides=Entry(hargaFrame,font=('Krabby Patty',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadariSeadSidesvar)
textHargadariSeaSides.grid(row=2,column=1,padx=41)

LabelSubTotal=Label(hargaFrame,text='SUB TOTAL', font=('Krabby Patty',12,'bold'),bg='#ffeec2',fg='#461912')
LabelSubTotal.grid(row=0,column=2)
textSubTotal=Entry(hargaFrame,font=('Krabby Patty',14,'bold'),bd=6,width=16,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

LabelTax=Label(hargaFrame,text='Tax'+' '+str(tax*100)+'%', font=('Krabby Patty',12,'bold'),bg='#ffeec2',fg='#461912')
LabelTax.grid(row=1,column=2)

textTax=Entry(hargaFrame,font=('Krabby Patty',14,'bold'),bd=6,width=16,state='readonly',textvariable=servicetaxvar)
textTax.grid(row=1,column=3,padx=41)

LabelHargaTotal=Label(hargaFrame,text='TOTAL PRICE', font=('Krabby Patty',12,'bold'),bg='#ffeec2',fg='#461912')
LabelHargaTotal.grid(row=2,column=2)

textHargaTotal=Entry(hargaFrame,font=('Krabby Patty',14,'bold'),bd=6,width=16,state='readonly',textvariable=totalcostvar)
textHargaTotal.grid(row=2,column=3,padx=41)


# Membuat tampilan Buttons struk (Tombol-tombol pada frame kanan)
buttonTotal= Button(buttonFrame,text='Total',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonStruk= Button(buttonFrame,text='Receipt',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=struk)
buttonStruk.grid(row=0,column=1)

buttonSimpan= Button(buttonFrame,text='Save',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=save)
buttonSimpan.grid(row=0,column=2)

buttonReset= Button(buttonFrame,text='Reset',font=('arial',12,'bold'),fg='#fefefe',bg='red',bd=3,padx=12,
            command=reset)
buttonReset.grid(row=0,column=4)

# menentukan teks pada frame struk
textStruk=Text(strukFrame,font=('arial',12,'bold'),bd=3,width=36,height=26)
textStruk.grid(row=0,column=0)


root.mainloop()

# Stop the music when the program exits
mixer.music.stop()