from tkinter import *
from Page import Page
from MenuPage import MenuPage
# from Part1Page import Part1Page
import Fonts


def liftMenu(event):
    menuPage.lift()


class PickNamePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        page = Frame(self, bg="black")
        page.pack(fill=BOTH, expand=TRUE)

        def returnToMenu(event):
            menuPage = MenuPage(self)
            menuPage.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
            menuPage.lift()

        exitBtn = Label(page, text="X", font=Fonts.EXIT_FONT, fg="green", bg="black")
        exitBtn.pack(side=TOP, expand=False, anchor=E, padx=7, pady=3)
        exitBtn.bind("<Button-1>", returnToMenu)

        global pickNameLbl
        pickNameLbl = Label(page, text="First pick a name for the main character of your story!", fg="green",
                              bg="black", font=Fonts.NEWSTORY_FONT, anchor=CENTER, wraplength=700)
        pickNameLbl.pack(fill=X, anchor=CENTER)

        global userInput
        userInput = Entry(page, fg="green", bg="black", font=Fonts.NEWSTORY_FONT, justify=CENTER)
        userInput.pack(side=TOP, anchor=CENTER, pady=25)
        userInput.bind("<Return>", )

        global optLblSelected
        optLblSelected = ""

        global answerLbl
        answerLbl = Label(page, text=optLblSelected)


class StartApplication(Frame):
    def __init__(self, master):
        outlineFrame = Frame(master, bd=3, relief=RIDGE, bg="light steel blue")
        outlineFrame.pack(fill=BOTH, expand=True, padx=125, pady=50)

        menuPage.place(in_=outlineFrame, x=0, y=0, relwidth=1, relheight=1)

        liftMenu(self)


book = Tk()
book.title("My Story Application")
book.minsize(1000, 600)

menuPage = MenuPage(book)

start = StartApplication(book)

book.lift()
book.mainloop()