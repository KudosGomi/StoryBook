from tkinter import *
from Page import Page
import Fonts


class MenuPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        outlineFrame = Frame(self, bg="light steel blue")
        outlineFrame.pack(fill=BOTH, expand=True)

        title = Label(outlineFrame, text="My Story Book", font=Fonts.TITLE_FONT, fg="IndianRed2", bg="light steel blue")
        title.pack(fill=X, expand=False, anchor=CENTER, pady=25)

        msg = Text(outlineFrame, height=2, fg="purple4", bg="light steel blue", font=Fonts.NORM_FONT)
        msg.pack(fill=X, padx=30, pady=0)
        msg.tag_configure("center", justify='center')
        msg.insert(1.0,"Hello! Welcome to your very own storybook. To begin, please select the"
                       " \"New Story\" option. Let's get started!", "center")
        msg.configure(state="disabled", wrap=WORD, highlightbackground="light steel blue")

        BookFrame = Frame(outlineFrame, bg="DarkOrange1", relief=RIDGE, bd=3)
        BookFrame.pack(fill=BOTH, expand=True, padx=150, pady=40)

        stemBookFrame = Frame(BookFrame, bg="brown", relief=RIDGE, bd=2)
        stemBookFrame.pack(side=LEFT, fill=Y)

        stemWidth = Label(stemBookFrame, text="                ", bg="brown")
        stemWidth.pack()

        def startNewStory(event):
            from StartStory import StartStory
            newStoryPage = StartStory(self)
            newStoryPage.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
            newStoryPage.lift()

        def newStoryBtnWhiteColor(event):
            newStoryLbl.config(fg="aquamarine2")
            canvas.pack()

        def newStoryBlackColor(event):
            newStoryLbl.config(fg="black")
            canvas.pack_forget()

        canvas = Canvas(stemBookFrame, width=50, bg="brown", highlightbackground="brown")
        canvas.create_oval(20, 85, 36, 95, fill="aquamarine2", width=0)
        canvas.pack(fill=X, expand=False)
        canvas.pack_forget()

        newStoryLbl = Label(BookFrame, font=Fonts.BUTTON_FONT, text="New Story", bg="DarkOrange1")
        newStoryLbl.pack(fill=X, anchor=CENTER, pady=90)
        newStoryLbl.bind("<Button-1>", startNewStory)
        newStoryLbl.bind("<Enter>", newStoryBtnWhiteColor)
        newStoryLbl.bind("<Leave>", newStoryBlackColor)