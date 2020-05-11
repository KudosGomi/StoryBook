from tkinter import  *
from Page import Page
import StartStory
import Fonts


def begin_p3(self):
    part = Part3Page(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p3pA(self):
    part = Part3PartAPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p3pALP(self):
    part = Part3PartALastPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p3pB(self):
    part = Part3PartBPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p3pBpX(self):
    part = Part3PartBPartXPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p3pBpY(self):
    part = Part3PartBPartYPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p3pBpX2(self):
    part = Part3PartBPartX2Page(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p3pBpY2(self):
    part = Part3PartBPartY2Page(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p3pBpY2LP1(self):
    part = Part3PartBPartY2LastPage1(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p3pBpY2_2LP(self):
    part = Part3PartBPartY2SecondLastPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p3pBpY2LP(self):
    part = Part3PartBPartY2LastPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p3pBpY3(self):
    part = Part3PartBPartY3(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p3pBpX2LP(self):
    part = Part3PartBPartX2LastPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p3pBpY3SecondLastPage(self):
    part = Part3PartBPartY3SecondLastPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p3pBpY3LP(self):
    part = Part3PartBPartY3LastPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()





class Part3Page(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text="He found his friends at the park down the street... ")

        StartStory.firstOptLbl.config(text="2.) They ran and played on the swings and the slides until they got tired and decided "
                                "to go home for lunch. ")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 19))

        StartStory.secOptLbl.config(text="2.) They began to play but then they found a puppy, stuck inside the slide. ")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 20))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 19))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 20))
        self.unbind("3")


class Part3PartAPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text=StartStory.storyText)

        StartStory.firstOptLbl.config(text="3.) They each parted ways and went home.")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 21))

        StartStory.secOptLbl.config(text="3.) They all went to Name’s house for lunch and continued to play and watch movies there!")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 21))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 21))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 21))
        self.unbind("3")


class Part3PartALastPage(Page):
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


class Part3PartBPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text=StartStory.storyText)

        StartStory.firstOptLbl.config(text="3.) They helped the puppy get out and began to play with him. ")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 22))

        StartStory.secOptLbl.config(text="3.) They got the puppy out and decided to him look for his owner. ")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 23))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 22))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 23))
        self.unbind("3")


class Part3PartBPartXPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text="They named the puppy Charlie and taught him a lot of new tricks, but at the end of the "
                             "day they could figure out what they would do with him or who would take him home. ")

        StartStory.firstOptLbl.config(text="3.) They decided that they would all take turns taking care of Charlie. The first one "
                                "to watch him would be " + StartStory.characterName + ". He took Charlie home and... ")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 24))

        StartStory.secOptLbl.config(text="3.) They flipped a coin and " + StartStory.characterName + " won! So, it will be his puppy, but he "
                                                                               "agreed to let his friends play and "
                                                                               "visit Charlie whenever they wanted. ")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 25))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 24))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 25))
        self.unbind("3")


class Part3PartBPartX2Page(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text=StartStory.storyText)

        StartStory.firstOptLbl.config(text="4.) Asked his mom to go to the pet store to buy puppy food and a bed!")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 26))

        StartStory.secOptLbl.config(text="4.) Gave Charlie a bath and got ready for bed! They’d go to the pet store for food and "
                              "a puppy bed first thing tomorrow morning!")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 26))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 26))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 26))
        self.unbind("3")


class Part3PartBPartX2LastPage(Page):
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


class Part3PartBPartYPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text=StartStory.storyText)

        StartStory.firstOptLbl.config(text="4.) They walked over to the vet’s office to see if he could help them find out where "
                                "he lived. " + StartStory.characterName + ". ")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 26))

        StartStory.secOptLbl.config(text="4.) They went to every house in the neighborhood and knocked on every door to see if "
                              "anybody would recognize the puppy. ")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 27))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 26))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 27))
        self.unbind("3")


class Part3PartBPartY2Page(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text=StartStory.storyText)

        StartStory.firstOptLbl.config(text="5.)  The vet was able to find the puppy’s address and gave it "
                                "to " + StartStory.characterName + " and his friends.")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 28))

        StartStory.secOptLbl.config(text="5.) They vet wasn’t able to find any record of the puppy anywhere, but told the children that... ")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 29))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 28))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 29))
        self.unbind("3")


class Part3PartBPartY2LastPage1(Page):
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
        endOfStory.insert(1.0, StartStory.storyText + "They went to the address and took the puppy back to his owner. The family "
                                           "was soo happy to see their puppy again that they thanked the children and "
                                           "promised them that they could come back and visit the puppy anytime they "
                                           "wanted to.")
        endOfStory.configure(state="disabled", wrap=WORD, highlightbackground="black")

        theEndLbl = Label(self, text="THE END! THANKS FOR PLAYING ~\n(You may exit and start another new story!)",
                          fg="red2", bg="black", font=Fonts.THEEND_FONT)
        theEndLbl.pack(fill=X, anchor=CENTER)


class Part3PartBPartY2SecondLastPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text=StartStory.storyText)

        StartStory.firstOptLbl.config(text="6.)  They could take him to the animal shelter. The children took the puppy to the "
                                "shelter, said goodbye and went home. “Surely, he’ll find a good home soon”,the "
                                "children said to themselves as theyall went back home.")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 30))

        StartStory.secOptLbl.config(text="6.) They could adopt the puppy themselves! They all adopted the puppy together and "
                              "agreed that they’d take turns taking care of him! They took the puppy home "
                              "to " + StartStory.characterName + "’s house first. They said goodbye and promised to be back "
                                                      "tomorrow morning to play.")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 30))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 30))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 30))
        self.unbind("3")


class Part3PartBPartY2LastPage(Page):
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


class Part3PartBPartY3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text=StartStory.storyText)

        StartStory.firstOptLbl.config(text="6.)  They went to 5 different houses until finally they found the puppy’s owner! ")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 28))

        StartStory.secOptLbl.config(text="6.) They went to every house they could but nobody wanted the puppy. So, the children "
                              "decided to... ")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 29))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 28))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 29))
        self.unbind("3")


class Part3PartBPartY3SecondLastPage(Page):
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
        endOfStory.insert(1.0, StartStory.storyText + " The owner was thrilled to see the puppy and thanked them for bringing her "
                                           "back! The children all went back home, exhausted from walking all day but "
                                           "happy that they were able help the puppy find his way back home.")
        endOfStory.configure(state="disabled", wrap=WORD, highlightbackground="black")

        theEndLbl = Label(self, text="THE END! THANKS FOR PLAYING ~\n(You may exit and start another new story!)",
                          fg="red2", bg="black", font=Fonts.THEEND_FONT)
        theEndLbl.pack(fill=X, anchor=CENTER)


class Part3PartBPartY3LastPage(Page):
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
        endOfStory.insert(1.0, StartStory.storyText + " ")
        endOfStory.configure(state="disabled", wrap=WORD, highlightbackground="black")

        theEndLbl = Label(self, text="THE END! THANKS FOR PLAYING ~\n(You may exit and start another new story!)",
                          fg="red2", bg="black", font=Fonts.THEEND_FONT)
        theEndLbl.pack(fill=X, anchor=CENTER)