from breezypythongui import EasyFrame
from tkinter import PhotoImage
import pytest

"""
Program: Chipotle Online Ordering Platform
Author: Evan Sorrell
Purpose: To simulate the experience of adding various items available for sale to a 
cart and then displaying the total cost all within a GUI program."""


class ChipotleMenu(EasyFrame):

  # With the init i set the title and size of the window and set up a start menu with the chipotle logo
  def __init__(self):
    EasyFrame.__init__(self, title = "Chipotle Ordering Platform")
    self.setResizable(True);
    self.setSize(450, 800)
    self.imageLabel = self.addLabel(text="",row=1,column=2,sticky="NSEW")
    self.image = PhotoImage(file = "chipotleLogo.png")
    self.imageLabel["image"] = self.image
    self.Start = self.addButton(text="Start",row=2,column=2,command=self.mainMenu)
    self.cart = {} # the "cart" will be a dictionary of items and prices

  def mainMenu(self):
    # print("Main-Menu")  ### Print statement for debugging, these are in nearly all of the different function in the program and are there to help me test it. I've commented them out but they can be useful for showing a button is working or the progress of tests
    self.textLabel = self.addLabel(text = "Select a type of item to add to your cart",row=2,column=2,sticky="NSEW")
    buttonPanel = self.addPanel(row=3, column=2, rowspan=2, columnspan=2)  # Here a button panel is used to keep the buttons organized and to make it look a bit nicer.
    Entrees = buttonPanel.addButton(text="Entrees",row=0,column=0,command=self.EntreeMenu)  # go to entree menu
    Sides = buttonPanel.addButton(text="Sides",row=0,column=1,command=self.SidesMenu)  # go to sides menu
    Drinks = buttonPanel.addButton(text="Drinks",row=1,column=0,command=self.DrinksMenu)  # go to drink menu
    Exit = buttonPanel.addButton(text="Exit",row=1,column=1,command=self.QuitApp)  # quits out of the program
    Checkout = self.addButton(text="Proceed to Checkout",row=4,column=2,command=self.Checkout)  # runs checkout
    # Back = buttonPanel.addButton(text="Back",row=1,column=1,command=self.mainMenu)  # returns to main menu

  def QuitApp(self): # simple exit program function
    # print("End of Program")
    exit()

  def EntreeMenu(self):
    # print("Entree-Menu")
    self.imageLabel = self.addLabel(text="",row=1,column=2,sticky="NSEW")  # With these three lines I reset the image to the logo in case it has been changed
    self.image = PhotoImage(file = "chipotleLogo.png")
    self.imageLabel["image"] = self.image
    self.entree = []  # here I set entree to be empty so that the user doen't have leftover inputs from previous entries
    self.textLabel['text'] = "Select a type of entree to add to your cart"
    buttonPanel = self.addPanel(row=3, column=2, rowspan=4, columnspan=2)  
    # Added these buttons to a button panel to keep them from the edge of the window and keep them organized
    # I added extra spacing in the text fields of some of the buttons in an effort to try and keep them about the same size
    Burrito = buttonPanel.addButton(text="      Burrito      ",row=0,column=0,command=self.BurritoMenu)
    Bowl = buttonPanel.addButton(text="       Bowl        ",row=0,column=1,command=self.BowlMenu)
    Quesadilla = buttonPanel.addButton(text="     Quesadilla    ",row=1,column=0,command=self.QuesaMenu)
    Salad = buttonPanel.addButton(text="       Salad       ",row=1,column=1,command=self.SaladMenu)
    Kids_Quesadilla = buttonPanel.addButton(text="  Kids Quesadilla  ",row=2,column=0,command=self.Kids_QuesaMenu)
    Kids_BYO = buttonPanel.addButton(text="Kids Build Your Own",row=2,column=1,command=self.Kids_BYOMenu)
    Back = buttonPanel.addButton(text="Back",row=3,column=0,command=self.mainMenu)  # returns to main menu
    Exit = buttonPanel.addButton(text="Exit",row=3,column=1,command=self.QuitApp)  # Exits program

######## Entree menu buttons
  def BurritoMenu(self):
    # print("Burrito-Menu")
    self.imageLabel = self.addLabel(text="",row=1,column=2,sticky="NSEW") # With these three lines I set the image to burrito to show the user what to expect
    self.image = PhotoImage(file = "burrito.png")
    self.imageLabel["image"] = self.image
    self.entree = [] # sets entree to be empty as additional protection from error
    self.entree.append("Burrito") # this sets the entree type as a burrito
    self.textLabel['text'] = "Select ingredients to add to your burrito."
    # User can add one choice of protein and can add one serving of each other ingredient to a burrito
    # Here a button panel is used to keep the buttons organized and to make it look a bit nicer since there are so many buttons here
    ingredientPanel = self.addPanel(row=3, column=2, rowspan=7, columnspan=3)
    self.WhiteRice = ingredientPanel.addButton(text="White Rice",row=0,column=0,command=self.AddWhiteRice)
    self.BrownRice = ingredientPanel.addButton(text="Brown Rice",row=0,column=1,command=self.AddBrownRice)
    self.BlackBeans = ingredientPanel.addButton(text="Black Beans",row=0,column=2,command=self.AddBlackBeans)
    self.PintoBeans = ingredientPanel.addButton(text="Pinto Beans",row=1,column=0,command=self.AddPintoBeans)
    self.Steak = ingredientPanel.addButton(text="Steak",row=1,column=1,command=self.AddSteak)
    self.Chicken = ingredientPanel.addButton(text="Chicken",row=1,column=2,command=self.AddChicken)
    self.Carnitas = ingredientPanel.addButton(text="Carnitas",row=2,column=0,command=self.AddCarnitas)
    self.Barbacoa = ingredientPanel.addButton(text="Barbacoa",row=2,column=1,command=self.AddBarbacoa)
    self.Queso = ingredientPanel.addButton(text="Queso Blanco",row=2,column=2,command=self.AddQueso)
    self.Guacamole = ingredientPanel.addButton(text="Guacamole",row=3,column=0,command=self.AddGuacamole)
    self.MildSalsa = ingredientPanel.addButton(text="Mild Salsa",row=3,column=1,command=self.AddMildSalsa)
    self.MediumSalsa = ingredientPanel.addButton(text="Meduim Salsa",row=3,column=2,command=self.AddMediumSalsa)
    self.HotSalsa = ingredientPanel.addButton(text="Hot Salsa",row=4,column=0,command=self.AddHotSalsa)
    self.CornSalsa = ingredientPanel.addButton(text="Corn Salsa",row=4,column=1,command=self.AddCornSalsa)
    self.SourCream = ingredientPanel.addButton(text="Sour Cream",row=4,column=2,command=self.AddSourCream)
    self.ShreddedCheese = ingredientPanel.addButton(text="Shredded Cheese",row=5,column=0,command=self.AddShreddedCheese)
    self.TacoLettuce = ingredientPanel.addButton(text="Lettuce",row=5,column=1,command=self.AddTacoLettuce)
    Back = ingredientPanel.addButton(text="Back",row=5,column=2,command=self.EntreeMenu)  # returns to entree menu
    AddToCart = ingredientPanel.addButton(text="Add to Cart",row=6,column=0,command=self.AddToCart)  # adds entree to cart
    Exit = ingredientPanel.addButton(text="Exit",row=6,column=2,command=self.QuitApp)  # Exits program

  def BowlMenu(self):
    # print("Bowl-Menu")
    self.imageLabel = self.addLabel(text="",row=1,column=2,sticky="NSEW")  # With these three lines I set the image to bowl to show the user what to expect
    self.image = PhotoImage(file = "bowl.png")
    self.imageLabel["image"] = self.image
    self.entree = []  # sets entree to be empty as additional protection from error
    self.entree.append("Bowl")  # this sets the entree type as a bowl
    self.textLabel['text'] = "Select ingredients to add to your bowl."
    # User can add one choice of protein and can add one serving of each other ingredient to a bowl
    # Here a button panel is used to keep the buttons organized and to make it look a bit nicer since there are so many buttons here
    ingredientPanel = self.addPanel(row=3, column=2, rowspan=7, columnspan=3)
    self.WhiteRice = ingredientPanel.addButton(text="White Rice",row=0,column=0,command=self.AddWhiteRice)
    self.BrownRice = ingredientPanel.addButton(text="Brown Rice",row=0,column=1,command=self.AddBrownRice)
    self.BlackBeans = ingredientPanel.addButton(text="Black Beans",row=0,column=2,command=self.AddBlackBeans)
    self.PintoBeans = ingredientPanel.addButton(text="Pinto Beans",row=1,column=0,command=self.AddPintoBeans)
    self.Steak = ingredientPanel.addButton(text="Steak",row=1,column=1,command=self.AddSteak)
    self.Chicken = ingredientPanel.addButton(text="Chicken",row=1,column=2,command=self.AddChicken)
    self.Carnitas = ingredientPanel.addButton(text="Carnitas",row=2,column=0,command=self.AddCarnitas)
    self.Barbacoa = ingredientPanel.addButton(text="Barbacoa",row=2,column=1,command=self.AddBarbacoa)
    self.Queso = ingredientPanel.addButton(text="Queso Blanco",row=2,column=2,command=self.AddQueso)
    self.Guacamole = ingredientPanel.addButton(text="Guacamole",row=3,column=0,command=self.AddGuacamole)
    self.MildSalsa = ingredientPanel.addButton(text="Mild Salsa",row=3,column=1,command=self.AddMildSalsa)
    self.MediumSalsa = ingredientPanel.addButton(text="Meduim Salsa",row=3,column=2,command=self.AddMediumSalsa)
    self.HotSalsa = ingredientPanel.addButton(text="Hot Salsa",row=4,column=0,command=self.AddHotSalsa)
    self.CornSalsa = ingredientPanel.addButton(text="Corn Salsa",row=4,column=1,command=self.AddCornSalsa)
    self.SourCream = ingredientPanel.addButton(text="Sour Cream",row=4,column=2,command=self.AddSourCream)
    self.ShreddedCheese = ingredientPanel.addButton(text="Shredded Cheese",row=5,column=0,command=self.AddShreddedCheese)
    self.TacoLettuce = ingredientPanel.addButton(text="Lettuce",row=5,column=1,command=self.AddTacoLettuce)
    Back = ingredientPanel.addButton(text="Back",row=5,column=2,command=self.EntreeMenu)  # returns to entree menu
    AddToCart = ingredientPanel.addButton(text="Add to Cart",row=6,column=0,command=self.AddToCart)  # adds entree to cart
    Exit = ingredientPanel.addButton(text="Exit",row=6,column=2,command=self.QuitApp)  # Exits program
  
  def SaladMenu(self):
    # print("Salad-Menu")
    self.imageLabel = self.addLabel(text="",row=1,column=2,sticky="NSEW")  # With these three lines I set the image to salad to show the user what to expect
    self.image = PhotoImage(file = "salad.png")
    self.imageLabel["image"] = self.image
    self.entree = []  # sets entree to be empty as additional protection from error
    self.entree.append("Salad")  # this sets the entree type as a salad
    self.textLabel['text'] = "Select ingredients to add to your salad."
    # User can add one choice of protein and can add one serving of each other ingredient to a salad"
    # Here a button panel is used to keep the buttons organized and to make it look a bit nicer since there are so many buttons here
    ingredientPanel = self.addPanel(row=3, column=2, rowspan=7, columnspan=3)
    self.WhiteRice = ingredientPanel.addButton(text="White Rice",row=0,column=0,command=self.AddWhiteRice)
    self.BrownRice = ingredientPanel.addButton(text="Brown Rice",row=0,column=1,command=self.AddBrownRice)
    self.BlackBeans = ingredientPanel.addButton(text="Black Beans",row=0,column=2,command=self.AddBlackBeans)
    self.PintoBeans = ingredientPanel.addButton(text="Pinto Beans",row=1,column=0,command=self.AddPintoBeans)
    self.Steak = ingredientPanel.addButton(text="Steak",row=1,column=1,command=self.AddSteak)
    self.Chicken = ingredientPanel.addButton(text="Chicken",row=1,column=2,command=self.AddChicken)
    self.Carnitas = ingredientPanel.addButton(text="Carnitas",row=2,column=0,command=self.AddCarnitas)
    self.Barbacoa = ingredientPanel.addButton(text="Barbacoa",row=2,column=1,command=self.AddBarbacoa)
    self.Queso = ingredientPanel.addButton(text="Queso Blanco",row=2,column=2,command=self.AddQueso)
    self.Guacamole = ingredientPanel.addButton(text="Guacamole",row=3,column=0,command=self.AddGuacamole)
    self.MildSalsa = ingredientPanel.addButton(text="Mild Salsa",row=3,column=1,command=self.AddMildSalsa)
    self.MediumSalsa = ingredientPanel.addButton(text="Meduim Salsa",row=3,column=2,command=self.AddMediumSalsa)
    self.HotSalsa = ingredientPanel.addButton(text="Hot Salsa",row=4,column=0,command=self.AddHotSalsa)
    self.CornSalsa = ingredientPanel.addButton(text="Corn Salsa",row=4,column=1,command=self.AddCornSalsa)
    self.SourCream = ingredientPanel.addButton(text="Sour Cream",row=4,column=2,command=self.AddSourCream)
    self.ShreddedCheese = ingredientPanel.addButton(text="Shredded Cheese",row=5,column=0,command=self.AddShreddedCheese)
    self.TacoLettuce = ingredientPanel.addButton(text="Lettuce",row=5,column=1,command=self.AddTacoLettuce)
    Back = ingredientPanel.addButton(text="Back",row=5,column=2,command=self.EntreeMenu)  # returns to entree menu
    AddToCart = ingredientPanel.addButton(text="Add to Cart",row=6,column=0,command=self.AddToCart)  # adds entree to cart
    Exit = ingredientPanel.addButton(text="Exit",row=6,column=2,command=self.QuitApp)  # Exits program
    
###### Entree Ingredients Buttons | Each of these buttons adds their respective ingredient to the entree and disables itself so only one serving can be added
  def AddWhiteRice(self):
    # print("add white rice to entree")
    self.entree.append("white rice")
    self.WhiteRice['state'] = 'disabled'

  def AddBrownRice(self):
    # print("add brown rice to entree")
    self.entree.append("brown rice")
    self.BrownRice['state'] = 'disabled'

  def AddBlackBeans(self):
    # print("add black beans to entree")
    self.entree.append("black beans")
    self.BlackBeans['state'] = 'disabled'

  def AddPintoBeans(self):
    # print("add pinto beans to entree")
    self.entree.append("pinto beans")
    self.PintoBeans['state'] = 'disabled'

  def AddSteak(self):  # Each protein button also disables each other protein option to limit each entree to one protein
    # print("add steak to entree")
    self.entree.append("steak")
    self.Steak['state'] = 'disabled'
    self.Chicken['state'] = 'disabled'
    self.Carnitas['state'] = 'disabled'
    self.Barbacoa['state'] = 'disabled'

  def AddChicken(self):
    # print("add chicken to entree")
    self.entree.append("chicken")
    self.Steak['state'] = 'disabled'
    self.Chicken['state'] = 'disabled'
    self.Carnitas['state'] = 'disabled'
    self.Barbacoa['state'] = 'disabled'

  def AddCarnitas(self):
    # print("add carnitas to entree")
    self.entree.append("carnitas")
    self.Steak['state'] = 'disabled'
    self.Chicken['state'] = 'disabled'
    self.Carnitas['state'] = 'disabled'
    self.Barbacoa['state'] = 'disabled'

  def AddBarbacoa(self):
    # print("add barbacoa to entree")
    self.entree.append("barbacoa")
    self.Steak['state'] = 'disabled'
    self.Chicken['state'] = 'disabled'
    self.Carnitas['state'] = 'disabled'
    self.Barbacoa['state'] = 'disabled'

  def AddQueso(self):
    # print("add queso to entree")
    self.entree.append("queso blanco")
    self.Queso['state'] = 'disabled'

  def AddGuacamole(self):
    # print("add guacamole to entree")
    self.entree.append("guacamole")
    self.Guacamole['state'] = 'disabled'

  def AddMildSalsa(self):
    # print("add mild salsa to entree")
    self.entree.append("mild salsa")
    self.MildSalsa['state'] = 'disabled'

  def AddMediumSalsa(self):
    # print("add medium salsa to entree")
    self.entree.append("medium salsa")
    self.MediumSalsa['state'] = 'disabled'

  def AddHotSalsa(self):
    # print("add hot salsa to entree")
    self.entree.append("hot salsa")
    self.HotSalsa['state'] = 'disabled'

  def AddCornSalsa(self):
    # print("add corn salsa to entree")
    self.entree.append("corn salsa")
    self.CornSalsa['state'] = 'disabled'

  def AddSourCream(self):
    # print("add sour cream to entree")
    self.entree.append("sour cream")
    self.SourCream['state'] = 'disabled'

  def AddShreddedCheese(self):
    # print("add shredded cheese to entree")
    self.entree.append("shredded cheese")
    self.ShreddedCheese['state'] = 'disabled'

  def AddTacoLettuce(self):
    # print("add lettuce to entree")
    self.entree.append("lettuce")
    self.TacoLettuce['state'] = 'disabled'
  
####### End of Entree Ingredients Buttons

  
  def QuesaMenu(self):
    # print("Quesadilla-Menu")
    self.imageLabel = self.addLabel(text="",row=1,column=2,sticky="NSEW")  # With these three lines I set the image to a quessadilla to show the user what to expect
    self.image = PhotoImage(file = "quessadilla.png")
    self.imageLabel["image"] = self.image
    self.entree = []  # sets entree to be empty as additional protection from error
    self.entree.append("Quesadilla")  # this sets the entree type as a quesadilla
    self.ingredientCount = 0  # this entree has a limited number of sides so this variable is created to track the number
    self.textLabel['text'] = "Select a protein and sides to add to your quessadilla."
    # User can add one choice of protein and can add one serving of each other ingredient with a mox of three non protein items. Queso and Guac are counted as proteins for this logic"
    # Here a button panel is used to keep the buttons organized and to make it look a bit nicer since there are so many buttons here
    ingredientPanel = self.addPanel(row=3, column=2, rowspan=7, columnspan=3)
    self.WhiteRiceLimit3 = ingredientPanel.addButton(text="White Rice",row=0,column=0,command=self.AddWhiteRiceLimit3)
    self.BrownRiceLimit3 = ingredientPanel.addButton(text="Brown Rice",row=0,column=1,command=self.AddBrownRiceLimit3)
    self.BlackBeansLimit3 = ingredientPanel.addButton(text="Black Beans",row=0,column=2,command=self.AddBlackBeansLimit3)
    self.PintoBeansLimit3 = ingredientPanel.addButton(text="Pinto Beans",row=1,column=0,command=self.AddPintoBeansLimit3)
    self.SteakLimit3 = ingredientPanel.addButton(text="Steak",row=1,column=1,command=self.AddSteakLimit3)
    self.ChickenLimit3 = ingredientPanel.addButton(text="Chicken",row=1,column=2,command=self.AddChickenLimit3)
    self.CarnitasLimit3 = ingredientPanel.addButton(text="Carnitas",row=2,column=0,command=self.AddCarnitasLimit3)
    self.BarbacoaLimit3 = ingredientPanel.addButton(text="Barbacoa",row=2,column=1,command=self.AddBarbacoaLimit3)
    self.QuesoLimit3 = ingredientPanel.addButton(text="Queso Blanco",row=2,column=2,command=self.AddQuesoLimit3)
    self.GuacamoleLimit3 = ingredientPanel.addButton(text="Guacamole",row=3,column=0,command=self.AddGuacamoleLimit3)
    self.MildSalsaLimit3 = ingredientPanel.addButton(text="Mild Salsa",row=3,column=1,command=self.AddMildSalsaLimit3)
    self.MediumSalsaLimit3 = ingredientPanel.addButton(text="Meduim Salsa",row=3,column=2,command=self.AddMediumSalsaLimit3)
    self.HotSalsaLimit3 = ingredientPanel.addButton(text="Hot Salsa",row=4,column=0,command=self.AddHotSalsaLimit3)
    self.CornSalsaLimit3 = ingredientPanel.addButton(text="Corn Salsa",row=4,column=1,command=self.AddCornSalsaLimit3)
    self.SourCreamLimit3 = ingredientPanel.addButton(text="Sour Cream",row=4,column=2,command=self.AddSourCreamLimit3)
    self.ShreddedCheeseLimit3 = ingredientPanel.addButton(text="Shredded Cheese",row=5,column=0,command=self.AddShreddedCheeseLimit3)
    self.TacoLettuceLimit3 = ingredientPanel.addButton(text="Lettuce",row=5,column=1,command=self.AddTacoLettuceLimit3)
    Back = ingredientPanel.addButton(text="Back",row=5,column=2,command=self.EntreeMenu)  # returns to entree menu
    AddToCart = ingredientPanel.addButton(text="Add to Cart",row=6,column=0,command=self.AddToCart)  # adds entree to cart
    Exit = ingredientPanel.addButton(text="Exit",row=6,column=2,command=self.QuitApp)  # Exits program

  def Kids_QuesaMenu(self):
    # print("Kids-Quesadilla-Menu")
    self.imageLabel = self.addLabel(text="",row=1,column=2,sticky="NSEW")  # With these three lines I set the image to a kids quessadilla to show the user what to expect
    self.image = PhotoImage(file = "kidsquesa.png")
    self.imageLabel["image"] = self.image
    self.entree = []  # sets entree to be empty as additional protection from error
    self.entree.append("Kids Quesadilla")  # this sets the entree type as a kids quesadilla
    self.ingredientCount = 0  # this entree has a limited number of sides so this variable is created to track the number
    self.textLabel['text'] = "Select a protein and sides to add to your quessadilla."
    # User can add one choice of protein and can add one serving of each other ingredient with a mox of three non protein items. Queso and Guac are counted as proteins for this logic"
    # Here a button panel is used to keep the buttons organized and to make it look a bit nicer since there are so many buttons here
    ingredientPanel = self.addPanel(row=3, column=2, rowspan=7, columnspan=3)
    self.WhiteRiceLimit3 = ingredientPanel.addButton(text="White Rice",row=0,column=0,command=self.AddWhiteRiceLimit3)
    self.BrownRiceLimit3 = ingredientPanel.addButton(text="Brown Rice",row=0,column=1,command=self.AddBrownRiceLimit3)
    self.BlackBeansLimit3 = ingredientPanel.addButton(text="Black Beans",row=0,column=2,command=self.AddBlackBeansLimit3)
    self.PintoBeansLimit3 = ingredientPanel.addButton(text="Pinto Beans",row=1,column=0,command=self.AddPintoBeansLimit3)
    self.SteakLimit3 = ingredientPanel.addButton(text="Steak",row=1,column=1,command=self.AddSteakLimit3)
    self.ChickenLimit3 = ingredientPanel.addButton(text="Chicken",row=1,column=2,command=self.AddChickenLimit3)
    self.CarnitasLimit3 = ingredientPanel.addButton(text="Carnitas",row=2,column=0,command=self.AddCarnitasLimit3)
    self.BarbacoaLimit3 = ingredientPanel.addButton(text="Barbacoa",row=2,column=1,command=self.AddBarbacoaLimit3)
    self.QuesoLimit3 = ingredientPanel.addButton(text="Queso Blanco",row=2,column=2,command=self.AddQuesoLimit3)
    self.GuacamoleLimit3 = ingredientPanel.addButton(text="Guacamole",row=3,column=0,command=self.AddGuacamoleLimit3)
    self.MildSalsaLimit3 = ingredientPanel.addButton(text="Mild Salsa",row=3,column=1,command=self.AddMildSalsaLimit3)
    self.MediumSalsaLimit3 = ingredientPanel.addButton(text="Meduim Salsa",row=3,column=2,command=self.AddMediumSalsaLimit3)
    self.HotSalsaLimit3 = ingredientPanel.addButton(text="Hot Salsa",row=4,column=0,command=self.AddHotSalsaLimit3)
    self.CornSalsaLimit3 = ingredientPanel.addButton(text="Corn Salsa",row=4,column=1,command=self.AddCornSalsaLimit3)
    self.SourCreamLimit3 = ingredientPanel.addButton(text="Sour Cream",row=4,column=2,command=self.AddSourCreamLimit3)
    self.ShreddedCheeseLimit3 = ingredientPanel.addButton(text="Shredded Cheese",row=5,column=0,command=self.AddShreddedCheeseLimit3)
    self.TacoLettuceLimit3 = ingredientPanel.addButton(text="Lettuce",row=5,column=1,command=self.AddTacoLettuceLimit3)
    Back = ingredientPanel.addButton(text="Back",row=5,column=2,command=self.EntreeMenu)  # returns to entree menu
    AddToCart = ingredientPanel.addButton(text="Add to Cart",row=6,column=0,command=self.AddToCart)  # adds entree to cart
    Exit = ingredientPanel.addButton(text="Exit",row=6,column=2,command=self.QuitApp)  # Exits program
    
  def Kids_BYOMenu(self):
    # print("Kids-BYO-Menu")
    self.imageLabel = self.addLabel(text="",row=1,column=2,sticky="NSEW")  # With these three lines I set the image to a kids BYO to show the user what to expect
    self.image = PhotoImage(file = "kidsbyo.png")
    self.imageLabel["image"] = self.image
    self.entree = []  # sets entree to be empty as additional protection from error
    self.entree.append("Kids BYO")  # this sets the entree type as a kids BYO
    self.ingredientCount = 0  # this entree has a limited number of sides so this variable is created to track the number
    self.textLabel['text'] = "Select 3 ingredients to add to your entree."
    # User can add one choice of protein and can add one serving of each other ingredient with a mox of three non protein items. Queso and Guac are counted as proteins for this logic"
    # Here a button panel is used to keep the buttons organized and to make it look a bit nicer since there are so many buttons here
    ingredientPanel = self.addPanel(row=3, column=2, rowspan=7, columnspan=3)
    self.WhiteRiceKBYO = ingredientPanel.addButton(text="White Rice",row=0,column=0,command=self.AddWhiteRiceKBYO)
    self.BrownRiceKBYO = ingredientPanel.addButton(text="Brown Rice",row=0,column=1,command=self.AddBrownRiceKBYO)
    self.BlackBeansKBYO = ingredientPanel.addButton(text="Black Beans",row=0,column=2,command=self.AddBlackBeansKBYO)
    self.PintoBeansKBYO = ingredientPanel.addButton(text="Pinto Beans",row=1,column=0,command=self.AddPintoBeansKBYO)
    self.SteakKBYO = ingredientPanel.addButton(text="Steak",row=1,column=1,command=self.AddSteakKBYO)
    self.ChickenKBYO = ingredientPanel.addButton(text="Chicken",row=1,column=2,command=self.AddChickenKBYO)
    self.CarnitasKBYO = ingredientPanel.addButton(text="Carnitas",row=2,column=0,command=self.AddCarnitasKBYO)
    self.BarbacoaKBYO = ingredientPanel.addButton(text="Barbacoa",row=2,column=1,command=self.AddBarbacoaKBYO)
    self.QuesoKBYO = ingredientPanel.addButton(text="Queso Blanco",row=2,column=2,command=self.AddQuesoKBYO)
    self.GuacamoleKBYO = ingredientPanel.addButton(text="Guacamole",row=3,column=0,command=self.AddGuacamoleKBYO)
    self.MildSalsaKBYO = ingredientPanel.addButton(text="Mild Salsa",row=3,column=1,command=self.AddMildSalsaKBYO)
    self.MediumSalsaKBYO = ingredientPanel.addButton(text="Meduim Salsa",row=3,column=2,command=self.AddMediumSalsaKBYO)
    self.HotSalsaKBYO = ingredientPanel.addButton(text="Hot Salsa",row=4,column=0,command=self.AddHotSalsaKBYO)
    self.CornSalsaKBYO = ingredientPanel.addButton(text="Corn Salsa",row=4,column=1,command=self.AddCornSalsaKBYO)
    self.SourCreamKBYO = ingredientPanel.addButton(text="Sour Cream",row=4,column=2,command=self.AddSourCreamKBYO)
    self.ShreddedCheeseKBYO = ingredientPanel.addButton(text="Shredded Cheese",row=5,column=0,command=self.AddShreddedCheeseKBYO)
    self.TacoLettuceKBYO = ingredientPanel.addButton(text="Lettuce",row=5,column=1,command=self.AddTacoLettuceKBYO)
    Back = ingredientPanel.addButton(text="Back",row=5,column=2,command=self.EntreeMenu)  # returns to entree menu
    AddToCart = ingredientPanel.addButton(text="Add to Cart",row=6,column=0,command=self.AddToCart)  # adds entree to cart
    Exit = ingredientPanel.addButton(text="Exit",row=6,column=2,command=self.QuitApp)  # Exits program
    
#### Entree Ingredients Buttons for entrees that have a limit of three ingredients
  def AddWhiteRiceLimit3(self):
    # print("add white rice to entree")
    self.entree.append("white rice")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3 function
      self.limit3()

  def AddBrownRiceLimit3(self):
    # print("add brown rice to entree")
    self.entree.append("brown rice")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3 function
      self.limit3()

  def AddBlackBeansLimit3(self):
    # print("add black beans to entree")
    self.entree.append("black beans")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3 function
      self.limit3()

  def AddPintoBeansLimit3(self):
    # print("add pinto beans to entree")
    self.entree.append("pinto beans")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3 function
      self.limit3()

  def AddSteakLimit3(self):  # Each protein button also disables each other protein option to limit each entree to one protein, this is also true for the queso and guac buttons
    # print("add steak to entree")
    self.entree.append("steak")  # adds ingredient to entree
    self.SteakLimit3['state'] = 'disabled'
    self.ChickenLimit3['state'] = 'disabled'
    self.CarnitasLimit3['state'] = 'disabled'
    self.BarbacoaLimit3['state'] = 'disabled'
    self.GuacamoleLimit3['state'] = 'disabled'
    self.QuesoLimit3['state'] = 'disabled'

  def AddChickenLimit3(self):
    # print("add chicken to entree")
    self.entree.append("chicken")  # adds ingredient to entree
    self.SteakLimit3['state'] = 'disabled'
    self.ChickenLimit3['state'] = 'disabled'
    self.CarnitasLimit3['state'] = 'disabled'
    self.BarbacoaLimit3['state'] = 'disabled'
    self.GuacamoleLimit3['state'] = 'disabled'
    self.QuesoLimit3['state'] = 'disabled'

  def AddCarnitasLimit3(self):
    # print("add carnitas to entree")
    self.entree.append("carnitas")  # adds ingredient to entree
    self.SteakLimit3['state'] = 'disabled'
    self.ChickenLimit3['state'] = 'disabled'
    self.CarnitasLimit3['state'] = 'disabled'
    self.BarbacoaLimit3['state'] = 'disabled'
    self.GuacamoleLimit3['state'] = 'disabled'
    self.QuesoLimit3['state'] = 'disabled'

  def AddBarbacoaLimit3(self):
    # print("add barbacoa to entree")
    self.entree.append("barbacoa")  # adds ingredient to entree
    self.SteakLimit3['state'] = 'disabled'
    self.ChickenLimit3['state'] = 'disabled'
    self.CarnitasLimit3['state'] = 'disabled'
    self.GuacamoleLimit3['state'] = 'disabled'
    self.QuesoLimit3['state'] = 'disabled'

  def AddQuesoLimit3(self):
    # print("add queso to entree")
    self.entree.append("queso blanco")  # adds ingredient to entree
    self.SteakLimit3['state'] = 'disabled'
    self.ChickenLimit3['state'] = 'disabled'
    self.CarnitasLimit3['state'] = 'disabled'
    self.BarbacoaLimit3['state'] = 'disabled'
    self.GuacamoleLimit3['state'] = 'disabled'
    self.QuesoLimit3['state'] = 'disabled'
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3 function
      self.limit3()

  def AddGuacamoleLimit3(self):
    # print("add guacamole to entree")
    self.entree.append("guacamole")  # adds ingredient to entree
    self.SteakLimit3['state'] = 'disabled'
    self.ChickenLimit3['state'] = 'disabled'
    self.CarnitasLimit3['state'] = 'disabled'
    self.BarbacoaLimit3['state'] = 'disabled'
    self.GuacamoleLimit3['state'] = 'disabled'
    self.QuesoLimit3['state'] = 'disabled'
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3 function
      self.limit3()

  def AddMildSalsaLimit3(self):
    # print("add mild salsa to entree")
    self.entree.append("mild salsa")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3 function
      self.limit3()

  def AddMediumSalsaLimit3(self):
    # print("add medium salsa to entree")
    self.entree.append("medium salsa")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3 function
      self.limit3()

  def AddHotSalsaLimit3(self):
    # print("add hot salsa to entree")
    self.entree.append("hot salsa")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3 function
      self.limit3()

  def AddCornSalsaLimit3(self):
    # print("add corn salsa to entree")
    self.entree.append("corn salsa")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3 function
      self.limit3()

  def AddSourCreamLimit3(self):
    # print("add sour cream to entree")
    self.entree.append("sour cream")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3 function
      self.limit3()

  def AddShreddedCheeseLimit3(self):
    # print("add shredded cheese to entree")
    self.entree.append("shredded cheese")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3 function
      self.limit3()

  def AddTacoLettuceLimit3(self):
    # print("add lettuce to entree")
    self.entree.append("lettuce")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3 function
      self.limit3()
      
  def limit3(self): # this is a helper function that disables all the ingredient buttons when the entree has 3 sides (not including proteins)
    # each of these lines disables one of the buttons on screen
    self.WhiteRiceLimit3['state'] = 'disabled'
    self.BrownRiceLimit3['state'] = 'disabled'
    self.BlackBeansLimit3['state'] = 'disabled'
    self.PintoBeansLimit3['state'] = 'disabled'
    self.QuesoLimit3['state'] = 'disabled'
    self.GuacamoleLimit3['state'] = 'disabled'
    self.MildSalsaLimit3['state'] = 'disabled'
    self.MediumSalsaLimit3['state'] = 'disabled'
    self.HotSalsaLimit3['state'] = 'disabled'
    self.CornSalsaLimit3['state'] = 'disabled'
    self.SourCreamLimit3['state'] = 'disabled'
    self.ShreddedCheeseLimit3['state'] = 'disabled'
    self.TacoLettuceLimit3['state'] = 'disabled'
#### end of entree ingredient buttons that have a limit of three ingredients
## Kids BYO Specific Buttons
  def AddWhiteRiceKBYO(self):
    # print("add white rice to entree")
    self.entree.append("white rice")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()

  def AddBrownRiceKBYO(self):
    # print("add brown rice to entree")
    self.entree.append("brown rice")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()

  def AddBlackBeansKBYO(self):
    # print("add black beans to entree")
    self.entree.append("black beans")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()

  def AddPintoBeansKBYO(self):
    # print("add pinto beans to entree")
    self.entree.append("pinto beans")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()

  def AddQuesoKBYO(self):
    # print("add queso to entree")
    self.entree.append("queso blanco")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYOlimit3BYO
    self.SteakKBYO['state'] = 'disabled'
    self.ChickenKBYO['state'] = 'disabled'
    self.CarnitasKBYO['state'] = 'disabled'
    self.BarbacoaKBYO['state'] = 'disabled'
    self.QuesoKBYO['state'] = 'disabled'
    self.GuacamoleKBYO['state'] = 'disabled'

  def AddGuacamoleKBYO(self):
    # print("add guacamole to entree")
    self.entree.append("guacamole")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()
    self.SteakKBYO['state'] = 'disabled'
    self.ChickenKBYO['state'] = 'disabled'
    self.CarnitasKBYO['state'] = 'disabled'
    self.BarbacoaKBYO['state'] = 'disabled'
    self.QuesoKBYO['state'] = 'disabled'
    self.GuacamoleKBYO['state'] = 'disabled'

  def AddMildSalsaKBYO(self):
    # print("add mild salsa to entree")
    self.entree.append("mild salsa")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()

  def AddMediumSalsaKBYO(self):
    # print("add medium salsa to entree")
    self.entree.append("medium salsa")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()

  def AddHotSalsaKBYO(self):
    # print("add hot salsa to entree")
    self.entree.append("hot salsa")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()

  def AddCornSalsaKBYO(self):
    # print("add corn salsa to entree")
    self.entree.append("corn salsa")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()

  def AddSourCreamKBYO(self):
    # print("add sour cream to entree")
    self.entree.append("sour cream")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()

  def AddShreddedCheeseKBYO(self):
    # print("add shredded cheese to entree")
    self.entree.append("shredded cheese")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()

  def AddTacoLettuceKBYO(self):
    # print("add lettuce to entree")
    self.entree.append("lettuce")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()
  def AddSteakKBYO(self):  # Each protein button also disables each other protein option to limit each entree to one protein, this is also true for the queso and guac buttons
    # print("add steak to entree")
    self.entree.append("steak")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()
    self.SteakKBYO['state'] = 'disabled'
    self.ChickenKBYO['state'] = 'disabled'
    self.CarnitasKBYO['state'] = 'disabled'
    self.BarbacoaKBYO['state'] = 'disabled'
    self.QuesoKBYO['state'] = 'disabled'
    self.GuacamoleKBYO['state'] = 'disabled'

  def AddChickenKBYO(self):
    # print("add chicken to entree")
    self.entree.append("chicken")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()
    self.SteakKBYO['state'] = 'disabled'
    self.ChickenKBYO['state'] = 'disabled'
    self.CarnitasKBYO['state'] = 'disabled'
    self.BarbacoaKBYO['state'] = 'disabled'
    self.QuesoKBYO['state'] = 'disabled'
    self.GuacamoleKBYO['state'] = 'disabled'

  def AddCarnitasKBYO(self):
    # print("add carnitas to entree")
    self.entree.append("carnitas")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()
    self.SteakKBYO['state'] = 'disabled'
    self.ChickenKBYO['state'] = 'disabled'
    self.CarnitasKBYO['state'] = 'disabled'
    self.BarbacoaKBYO['state'] = 'disabled'
    self.QuesoKBYO['state'] = 'disabled'
    self.GuacamoleKBYO['state'] = 'disabled'

  def AddBarbacoaKBYO(self):
    # print("add barbacoa to entree")
    self.entree.append("barbacoa")  # adds ingredient to entree
    self.ingredientCount += 1  # increments ingredient count
    if self.ingredientCount == 3:  # checks if ingredient count is 3 and if true, runs the limit3BYO function
      self.limit3KBYO()
    self.SteakKBYO['state'] = 'disabled'
    self.ChickenKBYO['state'] = 'disabled'
    self.CarnitasKBYO['state'] = 'disabled'
    self.BarbacoaKBYO['state'] = 'disabled'
    self.QuesoKBYO['state'] = 'disabled'
    self.GuacamoleKBYO['state'] = 'disabled'

  def limit3KBYO(self): # this is a helper function that disables all the ingredient buttons when the entree has 3 sides (including proteins)
    # each of these lines disables one of the buttons on screen
    self.WhiteRiceKBYO['state'] = 'disabled'
    self.BrownRiceKBYO['state'] = 'disabled'
    self.BlackBeansKBYO['state'] = 'disabled'
    self.PintoBeansKBYO['state'] = 'disabled'
    self.SteakKBYO['state'] = 'disabled'
    self.ChickenKBYO['state'] = 'disabled'
    self.CarnitasKBYO['state'] = 'disabled'
    self.BarbacoaKBYO['state'] = 'disabled'
    self.QuesoKBYO['state'] = 'disabled'
    self.GuacamoleKBYO['state'] = 'disabled'
    self.MildSalsaKBYO['state'] = 'disabled'
    self.MediumSalsaKBYO['state'] = 'disabled'
    self.HotSalsaKBYO['state'] = 'disabled'
    self.CornSalsaKBYO['state'] = 'disabled'
    self.SourCreamKBYO['state'] = 'disabled'
    self.ShreddedCheeseKBYO['state'] = 'disabled'
    self.TacoLettuceKBYO['state'] = 'disabled'
    
## end of Kids BYO specific menu buttons

  def AddToCart(self):  # This function determines the price of the entree before adding it to the cart
    price = 0  # init price as 0
    if "Burrito" in self.entree or "Bowl" in self.entree or "Salad" in self.entree:
      price = 7.85  # price for veggie or chicken entree
      if "steak" in self.entree or "barbacoa" in self.entree:
        price = 9.60  # price for steak or barbacoa entree
      if "carnitas" in self.entree:
        price = 8.50  # price for carnitas entree
      if "guacamole" in self.entree:
        price += 2.40  # price for adding guac
      if "queso blanco" in self.entree:
        price += 1.40  # price for adding queso
      
      if "Burrito" in self.cart and "Burrito" in self.entree:  # These next three if statements determine if entree is a bowl, burrito, or salad, and will update the price of that type of item in the cart 
        self.cart.update({"Burrito": self.cart["Burrito"] + price})
        self.messageBox(title = "Success", message = self.entree[0] + " added to cart")
        return
      if "Bowl" in self.cart and "Bowl" in self.entree:
        self.cart.update({"Bowl": self.cart["Bowl"] + price})
        self.messageBox(title = "Success", message = self.entree[0] + " added to cart")
        return
      if "Salad" in self.cart and "Salad" in self.entree:
        self.cart.update({"Salad": self.cart["Salad"] + price})
        self.messageBox(title = "Success", message = self.entree[0] + " added to cart")
        return
      else:  # if they were not already in the cart, the lines within this else statement add the entree into the cart
        self.cart.update({self.entree[0]: price})
        print("This entree was added to cart: " + self.entree[0])
        self.messageBox(title = "Success", message = self.entree[0] + " added to cart")
      return
    if "Quesadilla" in self.entree:
      price = 8.40  # price for veggie or chicken entree
      if "steak" in self.entree or "barbacoa" in self.entree or "queso blanco" in self.entree or "guacamole" in self.entree:
        price = 10.15  # price for steak, barbacoa entree, or cheese entree with queso or guac side
      if "carnitas" in self.entree:
        price = 9.05  # price for carnitas entree
      if "Quesadilla" in self.cart:  # This if statement determines if entree is a Quesadilla and will update the price of that type of item in the cart 
        self.cart.update({"Quesadilla": self.cart["Quesadilla"] + price})
        self.messageBox(title = "Success", message = self.entree[0] + " added to cart")
        return
      else:  # if is was not already in the cart, the lines within this else statement add the entree into the cart
        self.cart.update({self.entree[0]: price})
        self.messageBox(title = "Success", message = self.entree[0] + " added to cart")
        return
    if "Kids Quesadilla" in self.entree:
      price = 3.95  # price for veggie entree
      if "steak" in self.entree or "barbacoa" in self.entree or "chicken" in self.entree or "carnitas" in self.entree or "guacamole" in self.entree or "queso blanco" in self.entree:
        price = 4.50  # price for steak, barbacoa, chicken, or carnitas entree, or cheese entree with queso or guac side
      if "Kids Quesadilla" in self.cart:  # This if statement determines if entree is a kids Quesadilla and will update the price of that type of item in the cart 
        self.cart.update({"Kids Quesadilla": self.cart["Kids Quesadilla"] + price})
        self.messageBox(title = "Success", message = self.entree[0] + " added to cart")
        return
      else:  # if is was not already in the cart, the lines within this else statement add the entree into the cart
        self.cart.update({self.entree[0]: price})
        self.messageBox(title = "Success", message = self.entree[0] + " added to cart")
        return
    if "Kids BYO" in self.entree:
      price = 4.95  # price for entree
      if "Kids BYO" in self.cart:  # This if statement determines if entree is a kids byo and will update the price of that type of item in the cart 
        self.cart.update({"Kids BYO": self.cart["Kids BYO"] + price})
        self.messageBox(title = "Success", message = self.entree[0] + " added to cart")
        return
      else:  # if is was not already in the cart, the lines within this else statement add the entree into the cart
        self.cart.update({self.entree[0]: price})
        self.messageBox(title = "Success", message = self.entree[0] + " added to cart") 
        return
######## end of entree menu buttons
  def SidesMenu(self):
    # print("Sides-Menu")
    # User can add any number of sides individually to their cart
    # Here a button panel is used to keep the buttons organized and to make it look a bit nicer since there are so many buttons here
    textLabel = self.addLabel(text = "Select a side to add to your cart",row=2,column=2,sticky="NSEW")
    buttonPanel = self.addPanel(row=3, column=2, rowspan=8, columnspan=2)
    Guacamole = buttonPanel.addButton(text="  Guacamole  ",row=0,column=0,command=self.AddSideGuac)
    Queso = buttonPanel.addButton(text="Queso Blanco",row=0,column=1,command=self.AddSideQueso)
    WhiteRice = buttonPanel.addButton(text="White Rice",row=1,column=0,command=self.AddSideWhite)
    BrownRice = buttonPanel.addButton(text="Brown Rice",row=1,column=1,command=self.AddSideBrown)
    BlackBeans = buttonPanel.addButton(text="Black Beans",row=2,column=0,command=self.AddSideBlack)
    PintoBeans = buttonPanel.addButton(text="Pinto Beans",row=2,column=1,command=self.AddSidePinto)
    MildSalsa = buttonPanel.addButton(text="Mild Salsa",row=3,column=0,command=self.AddSideMild)
    MediumSalsa = buttonPanel.addButton(text="Meduim Salsa",row=3,column=1,command=self.AddSideMedium)
    HotSalsa = buttonPanel.addButton(text="Hot Salsa",row=4,column=0,command=self.AddSideHot)
    CornSalsa = buttonPanel.addButton(text="Corn Salsa",row=4,column=1,command=self.AddSideCorn)
    SourCream = buttonPanel.addButton(text="Sour Cream",row=5,column=0,command=self.AddSideSourCream)
    ShreddedCheese = buttonPanel.addButton(text="Shredded Cheese",row=5,column=1,command=self.AddSideShredCheese)
    TacoLettuce = buttonPanel.addButton(text="Lettuce",row=6,column=0,command=self.AddSideTacoLet)
    SideTortilla = buttonPanel.addButton(text="Side Tortilla", row=6, column=1, command=self.AddSideTort)
    Back = buttonPanel.addButton(text="Back",row=7,column=0,command=self.mainMenu)  # returns to main menu
    Exit = buttonPanel.addButton(text="Exit",row=7,column=1,command=self.QuitApp)  # quits the program

### Side Menu Buttons 
  def AddSideGuac(self):
    # print("add a side of guacamole")
    if "Side of Guacamole" in self.cart:  # this if else clause determines if the side was already in the cart and updates the entry's price to reflect an additional side
      self.cart.update({"Side of Guacamole": self.cart["Side of Guacamole"] + 2.40})
    else:
      self.cart.update({"Side of Guacamole": 2.40})
    self.messageBox(title = "Success", message = "Side of Guacamole added to cart")  # This messagebox is used to show the user that the item has been added to their cart
  def AddSideQueso(self):
    # print("add a side of queso")
    if "Side of Queso Blanco" in self.cart:  # this if else clause determines if the side was already in the cart and updates the entry's price to reflect an additional side
      self.cart.update({"Side of Queso Blanco": self.cart["Side of Queso Blanco"] + 2.40})
    else:
      self.cart.update({"Side of Queso Blanco": 2.40})
    self.messageBox(title = "Success", message = "Side of Queso Blanco added to cart")  # This messagebox is used to show the user that the item has been added to their cart
    
  def AddSideWhite(self):
    # print("add a side of white rice")
    if "Side of White Rice" in self.cart:  # this if else clause determines if the side was already in the cart and updates the entry's price to reflect an additional side
      self.cart.update({"Side of White Rice": self.cart["Side of White Rice"] + 0.30})
    else:
      self.cart.update({"Side of White Rice": 0.30})
    self.messageBox(title = "Success", message = "Side of White Rice added to cart")  # This messagebox is used to show the user that the item has been added to their cart
    
  def AddSideBrown(self):
    # print("add a side of brown rice")
    if "Side of Brown Rice" in self.cart:  # this if else clause determines if the side was already in the cart and updates the entry's price to reflect an additional side
      self.cart.update({"Side of Brown Rice": self.cart["Side of Brown Rice"] + 0.30})
    else:
      self.cart.update({"Side of Brown Rice": 0.30})
    self.messageBox(title = "Success", message = "Side of Brown Rice added to cart")  # This messagebox is used to show the user that the item has been added to their cart

  def AddSideBlack(self):
    # print("add a side of black beans")
    if "Side of Black Beans" in self.cart:  # this if else clause determines if the side was already in the cart and updates the entry's price to reflect an additional side
      self.cart.update({"Side of Black Beans": self.cart["Side of Black Beans"] + 0.30})
    else:
      self.cart.update({"Side of Black Beans": 0.30})
    self.messageBox(title = "Success", message = "Side of Black Beans added to cart")  # This messagebox is used to show the user that the item has been added to their cart
    
  def AddSidePinto(self):
    # print("add a side of pinto beans")
    if "Side of Pinto Beans" in self.cart:  # this if else clause determines if the side was already in the cart and updates the entry's price to reflect an additional side
      self.cart.update({"Side of Pinto Beans": self.cart["Side of Pinto Beans"] + 0.30})
    else:
      self.cart.update({"Side of Pinto Beans": 0.30})
    self.messageBox(title = "Success", message = "Side of Pinto Beans added to cart")  # This messagebox is used to show the user that the item has been added to their cart

  def AddSideMild(self):
    # print("add a side of mild salsa")
    if "Side of Mild Salsa" in self.cart:  # this if else clause determines if the side was already in the cart and updates the entry's price to reflect an additional side
      self.cart.update({"Side of Mild Salsa": self.cart["Side of Mild Salsa"] + 0.30})
    else:
      self.cart.update({"Side of Mild Salsa": 0.30})
    self.messageBox(title = "Success", message = "Side of Mild Salsa added to cart")  # This messagebox is used to show the user that the item has been added to their cart
    
  def AddSideMedium(self):
    # print("add a side of medium salsa")
    if "Side of Medium Salsa" in self.cart:  # this if else clause determines if the side was already in the cart and updates the entry's price to reflect an additional side
      self.cart.update({"Side of Medium Salsa": self.cart["Side of Medium Salsa"] + 0.30})
    else:
      self.cart.update({"Side of Medium Salsa": 0.30})
    self.messageBox(title = "Success", message = "Side of Medium Salsa added to cart")  # This messagebox is used to show the user that the item has been added to their cart

  def AddSideHot(self):
    # print("add a side of hot salsa")
    if "Side of Hot Salsa" in self.cart:  # this if else clause determines if the side was already in the cart and updates the entry's price to reflect an additional side
      self.cart.update({"Side of Hot Salsa": self.cart["Side of Hot Salsa"] + 0.30})
    else:
      self.cart.update({"Side of Hot Salsa": 0.30})
    self.messageBox(title = "Success", message = "Side of Hot Salsa added to cart")  # This messagebox is used to show the user that the item has been added to their cart
    
  def AddSideCorn(self):
    print("add a side of corn salsa")
    if "Side of Corn Salsa" in self.cart:
      self.cart.update({"Side of Corn Salsa": self.cart["Side of Corn Salsa"] + 0.30})
    else:
      self.cart.update({"Side of Corn Salsa": 0.30})
    self.messageBox(title = "Success",
                    message = "Side of Corn Salsa added to cart")
    
  def AddSideSourCream(self):
    # print("add a side of sour cream")
    if "Side of Sour Cream" in self.cart:  # this if else clause determines if the side was already in the cart and updates the entry's price to reflect an additional side
      self.cart.update({"Side of Sour Cream": self.cart["Side of Sour Cream"] + 0.30})
    else:
      self.cart.update({"Side of Sour Cream": 0.30})
    self.messageBox(title = "Success", message = "Side of Sour Cream added to cart")  # This messagebox is used to show the user that the item has been added to their cart
    
  def AddSideShredCheese(self):
    # print("add a side of shredded cheese")
    if "Side of Shredded Cheese" in self.cart:  # this if else clause determines if the side was already in the cart and updates the entry's price to reflect an additional side
      self.cart.update({"Side of Shredded Cheese": self.cart["Side of Shredded Cheese"] + 0.30})
    else:
      self.cart.update({"Side of Shredded Cheese": 0.30})
    self.messageBox(title = "Success", message = "Side of Shredded Cheese added to cart")  # This messagebox is used to show the user that the item has been added to their cart

  def AddSideTacoLet(self):
    # print("add a side of lettuce")
    if "Side of Lettuce" in self.cart:  # this if else clause determines if the side was already in the cart and updates the entry's price to reflect an additional side
      self.cart.update({"Side of Lettuce": self.cart["Side of Lettuce"] + 0.30})
    else:
      self.cart.update({"Side of Lettuce": 0.30})
    self.messageBox(title = "Success", message = "Side of Lettuce added to cart")  # This messagebox is used to show the user that the item has been added to their cart
    
  def AddSideTort(self):
    # print("add a side tortilla")
    if "Side Tortilla" in self.cart:  # this if else clause determines if the side was already in the cart and updates the entry's price to reflect an additional side
      self.cart.update({"Side Tortilla": self.cart["Side Tortilla"] + 0.50})
    else:
      self.cart.update({"Side Tortilla": 0.50})
    self.messageBox(title = "Success", message = "Side Tortilla added to cart")  # This messagebox is used to show the user that the item has been added to their cart
    
### end of side menu buttons
  def DrinksMenu(self):
    # print("Drinks-Menu")
    textLabel = self.addLabel(text = "Select a drink size to add to your cart",row=2,column=2,sticky="NSEW")
    buttonPanel = self.addPanel(row=3, column=2, rowspan=2, columnspan=2) # added button panel to remain consistent and keep formatting neat for the following buttons
    small = buttonPanel.addButton(text="Small",row=0,column=0,command=self.AddSmallDrink)
    large = buttonPanel.addButton(text="Large",row=0,column=1,command=self.AddLargeDrink)
    Back = buttonPanel.addButton(text="Back",row=1,column=0,command=self.mainMenu)  # returns to main menu
    Exit = buttonPanel.addButton(text="Exit",row=1,column=1,command=self.QuitApp)

### Drink Menu Buttons
  def AddSmallDrink(self):
    # print("add a small drink")
    if "Small Drink" in self.cart:  # this if else clause determines if the item was already in the cart and updates the entry's price to reflect an additional item
      self.cart.update({"Small Drink": self.cart["Small Drink"] + 2.65})
    else:
      self.cart.update({"Small Drink": 2.65})
    self.messageBox(title = "Success", message = "Small Drink added to cart")  # This messagebox is used to show the user that the item has been added to their cart
    
  def AddLargeDrink(self):
    # print("add a large drink")
    if "Large Drink" in self.cart:  # this if else clause determines if the item was already in the cart and updates the entry's price to reflect an additional item
      self.cart.update({"Large Drink": self.cart["Large Drink"] + 2.95})
    else:
      self.cart.update({"Large Drink": 2.95})
    self.messageBox(title = "Success", message = "Large Drink added to cart")  # This messagebox is used to show the user that the item has been added to their cart

### end of drink menu buttons

  def Checkout(self):
    total = 0  # set total to 0
    checkoutMessage = "Your order is ${:.2f}"  # format to 2 decimal places so the message does not contain the result of a floating-point representation error
    for price in self.cart.values():
      total += price
    self.messageBox(title = "Order Confirmed", message = checkoutMessage.format(total))  # This messagebox is used to show the user their cart's total
    
def main():
  ChipotleMenu().mainloop()

# main()  # uncomment this line to run the program as intended

"""Valdidation Tests"""
c = ChipotleMenu()
# c.mainloop()  # starts up the program
# c.mainMenu()  # simulates pressing start button
# c.EntreeMenu()  # simulates pressing entrees button
# c.SidesMenu()  # simulates pressing sides button
# c.DrinksMenu()  # simulates pressing drinks button
# c.QuitApp() # simulates pressing exit button

### This test adds a burrito with a price of 7.85 to the cart then adds a second burrito with steak in to the cart
## This tests that the price for a steak burrito is 9.60 and that the dictionary value for burrito in the cart is changed to reflect
# the price of both burritos.
c.cart = {"Burrito": 7.85}
c.entree = ["Burrito", "steak", "brown rice", "black beans", "mild salsa", "sour cream", "shredded cheese"]
c.AddToCart()
assert c.cart.get("Burrito") == 17.45  # 7.85 + 9.60

### This test simply if a side tortilla is added to the cart and that its price is 0.50
c.AddSideTort()
assert c.cart.get("Side Tortilla") == 0.5

### This test adds a side of queso to the cart and checks the price after the second and third are added
## I got a floating-point representation error after adding the third side of queso to the cart
# As a result of this error I have the message in the checkout formatted to the first two decimal places
c.AddSideQueso()
c.AddSideQueso()
assert c.cart.get("Side of Queso Blanco") == 4.80
c.AddSideQueso()
assert c.cart.get("Side of Queso Blanco") == pytest.approx(7.20, 0.001)

### These tests if the drinks are added to the cart and that their prices are correct for the number of each
## size of drink within the cart
c.AddSmallDrink()
c.AddLargeDrink()
assert c.cart.get("Small Drink") == 2.65
assert c.cart.get("Large Drink") == 2.95
c.AddSmallDrink()
c.AddLargeDrink()
assert c.cart.get("Small Drink") == 5.30
assert c.cart.get("Large Drink") == 5.90