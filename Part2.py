from tkinter import *
from Page import Page
import StartStory
import Fonts


def begin_p2(self):
    part = Part2Page(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p2pA(self):
    part = Part2PartAPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p2pALP(self):
    part = Part2PartALastPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p2pB(self):
    part = Part2PartBPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p2pBLP(self):
    part = Part2PartBLastPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()




class Part2Page(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text=StartStory.storyText)

        StartStory.firstOptLbl.config(text="2.) " + StartStory.characterName + " then went over to his/her grandma's house to see family... ")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 15))

        StartStory.secOptLbl.config(text="2.) then went to go watch a movie at the theatre. ")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 16))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 15))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 16))
        self.unbind("3")


class Part2PartAPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text=StartStory.characterName + " played with his cousins and ran around the yard! He had so much fun! At "
                                             "the end of the day... ")

        StartStory.firstOptLbl.config(text="3.) They all went back home, exhausted and ready for bed. Name crawled into bed, and "
                                "before name knew it, he was fast asleep. ")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 17))

        StartStory.secOptLbl.config(text="3.) " + StartStory.characterName + " begged for his mom and dad to let him spend the night with "
                                                       "his cousins until they said yes! They all stayed up late "
                                                       "watching movies and playing games until finally, they fell "
                                                       "asleep. It was a good day! ")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 17))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 17))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 17))
        self.unbind("3")


class Part2PartALastPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)
        self.unbind("1")
        self.unbind("2")
        self.unbind("3")

        StartStory.titleLbl.pack_forget()
        StartStory.firstOptLbl.pack_forget()
        StartStory.secOptLbl.pack_forget()
        StartStory.thirdOptLbl.pack_forget()

        endOfStory = Text(self, height=12, fg="pink", bg="black", font=Fonts.NEWSTORY_FONT)
        endOfStory.pack(fill=X, padx=50, pady=0)
        endOfStory.tag_configure("center", justify="center")
        endOfStory.insert(1.0, StartStory.storyText)
        endOfStory.configure(state="disabled", wrap=WORD, highlightbackground="black")

        theEndLbl = Label(self, text="THE END! THANKS FOR PLAYING ~\n(You may exit and start another new story!)",
                          fg="red2", bg="black", font=Fonts.THEEND_FONT)
        theEndLbl.pack(fill=X, anchor=CENTER)


class Part2PartBPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text="They got lots of snacks and ate them while they waited for the movie to start. After "
                             "the movie was over... ")

        StartStory.firstOptLbl.config(text="4.) they all went back home.")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 18))

        StartStory.secOptLbl.config(text="4.) they went to the park and played until sundown!")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 18))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 18))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 18))
        self.unbind("3")


class Part2PartBLastPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)
        self.unbind("1")
        self.unbind("2")
        self.unbind("3")

        StartStory.titleLbl.pack_forget()
        StartStory.firstOptLbl.pack_forget()
        StartStory.secOptLbl.pack_forget()
        StartStory.thirdOptLbl.pack_forget()

        endOfStory = Text(self, height=12, fg="pink", bg="black", font=Fonts.NEWSTORY_FONT)
        endOfStory.pack(fill=X, padx=50, pady=0)
        endOfStory.tag_configure("center", justify="center")
        endOfStory.insert(1.0, StartStory.storyText)
        endOfStory.configure(state="disabled", wrap=WORD, highlightbackground="black")

        theEndLbl = Label(self, text="THE END! THANKS FOR PLAYING ~\n(You may exit and start another new story!)",
                          fg="red2", bg="black", font=Fonts.THEEND_FONT)
        theEndLbl.pack(fill=X, anchor=CENTER)