from tkinter import *
from Page import Page
import StartStory
import Fonts


def begin_p1(self):
    part = Part1Page(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p1pA(self):
    part = Part1PartAPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p1pApX(self):
    part = Part1PartAPartXPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p1pApXLP(self):
    part = Part1PartAPartXLastPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p1pBpX(self):
    part = Part1PartBPartXPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p1pBpX2(self):
    part = Part1PartBPartX2Page(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p1pBpX2LP(self):
    part = Part1PartBPartX2LastPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p1pBpY(self):
    part = Part1PartBPartYPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p1pBpY2(self):
    part = Part1PartBPartY2Page(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p1pBpY2LP(self):
    part = Part1PartBPartY2LastPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p1pBpY3(self):
    part = Part1PartBPartY3Page(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()


def begin_p1pBpY3LP(self):
    part = Part1PartBPartY3LastPage(self)
    part.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
    part.lift()





class Part1Page(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)
        StartStory.titleLbl.config(text=StartStory.characterName + " got up and was really sleepy so he went back to sleep. He woke up "
                                             "several hours later and realized... ")

        StartStory.storyText = StartStory.storyText + StartStory.titleLbl.cget("text")

        StartStory.firstOptLbl.config(text="2.) He was late for school! ")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 4))

        StartStory.secOptLbl.config(text="2.) He only had 10 minutes to make it to school on time. He quickly ran downstairs to "
                              "get breakfast and get ready to leave. ")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 5))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 4))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 5))
        self.unbind("3")


class Part1PartAPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)
        StartStory.titleLbl.config(text="He decided not to go and stay home to play with his puppy instead! They had a lot of "
                             "time playing together and spending the day at home. But "
                             "then " + StartStory.characterName + "'s mom got home from work and ")

        StartStory.storyText = StartStory.storyText + StartStory.titleLbl.cget("text")

        StartStory.firstOptLbl.config(text="3.) She was very angry. ")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 6))

        StartStory.secOptLbl.config(text="3.) She said hello to them and made them lunch. ")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 7))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 6))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 7))
        self.unbind("3")


class Part1PartAPartXPage(Page):
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
        endOfStory.pack(fill=X, padx=50, pady=10)
        endOfStory.tag_configure("center", justify="center")
        endOfStory.insert(1.0, StartStory.storyText + "She told " + StartStory.characterName + " to go to his room and grounded him "
                                                                         "for the rest of the week. And that was the "
                                                                         "last time " + StartStory.characterName + " missed school.", "center")
        endOfStory.configure(state="disabled", wrap=WORD, highlightbackground="black")

        theEndLbl = Label(self, text="THE END! THANKS FOR PLAYING ~\n(You may exit and start another new stroy!)",
                          fg="red2", bg="black", font=Fonts.THEEND_FONT)
        theEndLbl.pack(fill=X, anchor=CENTER)


class Part1PartAPartXLastPage(Page):
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
        endOfStory.insert(1.0, StartStory.storyText + "4.) They had lunch and enjoyed the rest of their day. "
                                           "" + StartStory.characterName + "’s mom never even realized he overslept and missed "
                                                                "school until his teacher called the next day!", "center")
        endOfStory.configure(state="disabled", wrap=WORD, highlightbackground="black")

        theEndLbl = Label(self, text="THE END! THANKS FOR PLAYING ~\n(You may exit and start another new story!)",
                          fg="red2", bg="black", font=Fonts.THEEND_FONT)
        theEndLbl.pack(fill=X, anchor=CENTER)


class Part1PartBPartXPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text="He ran out of the house... ")

        StartStory.storyText = StartStory.storyText + StartStory.titleLbl.cget("text")

        StartStory.firstOptLbl.config(text="3.) And made it right on time to catch the bus to school! ")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 8))

        StartStory.secOptLbl.config(text="3.) But he got to the school bus stop only to realize it had just left! ")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 10))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 8))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 10))
        self.unbind("3")


class Part1PartBPartX2Page(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text="He went to school and learned a lot of new things! He even made a few never friends! "
                             "After class... ")

        StartStory.storyText = StartStory.storyText + StartStory.titleLbl.cget("text")

        StartStory.firstOptLbl.config(text="4.) He went back home, did some homework and then went to bed, excited to go back to "
                                "school tomorrow.")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 9))

        StartStory.secOptLbl.config(text="4.)  He went back home and told his mom about his day! “I can’t wait to go back "
                              "tomorrow!” He told her.")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 9))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 9))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 9))
        self.unbind("3")


class Part1PartBPartYPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text=StartStory.storyText)

        StartStory.firstOptLbl.config(text="4.) He panicked and started to run after it! He chased the bus all the way to the "
                                "school and got there right on time, but extremely tired and out of breath. ")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 11))

        StartStory.secOptLbl.config(text="4.)  He ran back home to look for his mom or sister (maybe they’d be able to take him). ")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 12))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 11))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 12))
        self.unbind("3")


class Part1PartBPartX2LastPage(Page):
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


class Part1PartBPartY2Page(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text="He was so tired that... ", wraplength=700)

        StartStory.storyText = StartStory.storyText + StartStory.titleLbl.cget("text")

        StartStory.firstOptLbl.config(text="5.) He slept throughout class until his mom went to pick him up at the end of the day!")
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 13))

        StartStory.secOptLbl.config(text="5.) He decided to walk back home and take a nap instead! He’ll be on time tomorrow for "
                              "sure he told himself as he laid back down in bed and dozed off.")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 13))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 13))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 13))
        self.unbind("3")


class Part1PartBPartY2LastPage(Page):
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


class Part1PartBPartY3Page(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.configure(bg="black")

        StartStory.createTitleAndOptLbls(self)

        StartStory.titleLbl.config(text=StartStory.storyText)

        StartStory.firstOptLbl.config(
            text="5.) When he got home, he realized nobody was there! What can he do? He thought to himself. "
                 "He decided to go outside and play with his puppy! He figured he’d have to wait until tomorrow. "
                 "Surely tomorrow he will wake up on time to go to class!", wraplength=500)
        StartStory.firstOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 14))

        StartStory.secOptLbl.config(text="5.) He got home in time to see his mom pulling out of the driveway! Thankfully she was "
                              "able to take him to school today!")
        StartStory.secOptLbl.bind("<Button-1>", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 14))

        StartStory.thirdOptLbl.pack_forget()

        self.bind("1", lambda event: StartStory.switchPlots(self, StartStory.firstOptLbl.cget("text"), 14))
        self.bind("2", lambda event: StartStory.switchPlots(self, StartStory.secOptLbl.cget("text"), 14))
        self.unbind("3")


class Part1PartBPartY3LastPage(Page):
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