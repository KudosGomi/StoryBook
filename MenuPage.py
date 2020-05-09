from tkinter import *
from Page import Page
import Fonts


class MenuPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        outlineFrame = Frame(self, bg="light steel blue") # IndianRed2 # light steel blue
        outlineFrame.pack(fill=BOTH, expand=True)

        title = Label(outlineFrame, text="My Story Book", font=Fonts.TITLE_FONT, fg="IndianRed2", bg="light steel blue")
        title.pack(fill=X, expand=False, anchor=CENTER, pady=25)

        msg = Text(outlineFrame, height=2, fg="purple4", bg="light steel blue", font=Fonts.MENU_FONT)
        msg.pack(fill=X, padx=30, pady=0)
        msg.tag_configure("center", justify='center')
        msg.insert(1.0,"Hello! Welcome to your very own storybook. To begin, please select the"
                       " \"New Story\" option. Let's get started!", "center")
        msg.configure(state="disabled", wrap=WORD, highlightbackground="light steel blue")

        bookFrame = Frame(outlineFrame, bg="light steel blue", relief=RAISED, bd=1)
        bookFrame.pack(fill=BOTH, expand=True, padx=150, pady=40)

        bookFrame.grid_rowconfigure(0, weight=1)
        # bookFrame.grid_rowconfigure(1, weight=1)
        bookFrame.grid_columnconfigure(0, weight=1)
        bookFrame.grid_columnconfigure(1, weight=25)

        coverFrame = Frame(bookFrame, bg="olive drab")
        coverFrame.grid(row=0, column=1, sticky=NSEW)

        coverFrame.grid_rowconfigure(0, weight=1)
        coverFrame.grid_rowconfigure(1, weight=1)
        coverFrame.grid_columnconfigure(0, weight=2)

        topSqFrame = Frame(coverFrame, bg="DarkOrange3",  relief=RIDGE, bd=3)
        topSqFrame.grid(sticky=NSEW, row=0, padx=94, pady=25)

        bottomSqFrame = Frame(coverFrame, bg="DarkOrange2", relief=RIDGE, bd=3)
        bottomSqFrame.grid(sticky=NSEW, row=1, padx=38, pady=19)

        bottomSqFrame.grid_rowconfigure(0, weight=1)
        bottomSqFrame.grid_columnconfigure(0, weight=1)

        byWhoLbl = Label(bottomSqFrame, text="Author by: YOU ~", font='ComicSansMS 17 bold', bg="DarkOrange2", fg="blue")
        byWhoLbl.grid(sticky=NSEW, row=0, padx=0, pady=0)

        def startNewStory(event):
            from StartStory import StartStory
            newStoryPage = StartStory(self)
            newStoryPage.place(in_=self, x=0, y=0, relwidth=1, relheight=1)
            newStoryPage.lift()

        def newStoryBtnWhiteColor(event):
            newStoryLbl.config(fg="yellow")
            canvas.grid(row=1, column=0)
            # canvas.pack()

        def newStoryBlackColor(event):
            newStoryLbl.config(fg="black")
            canvas.grid_forget()

        topSqFrame.grid_rowconfigure(0, weight=1)
        topSqFrame.grid_columnconfigure(0, weight=1)

        newStoryLbl = Label(topSqFrame, font='ComicSansMS 22 bold', text="New Story", bg="DarkOrange3")
        newStoryLbl.grid(sticky=NSEW, row=0, padx=0, pady=0, ipadx=35)
        newStoryLbl.bind("<Button-1>", startNewStory)
        newStoryLbl.bind("<Enter>", newStoryBtnWhiteColor)
        newStoryLbl.bind("<Leave>", newStoryBlackColor)

        stemBookFrame = Frame(bookFrame, bg="brown", relief=RAISED, bd=2)
        stemBookFrame.grid(row=0, column=0, sticky=NSEW)

        stemBookFrame.grid_rowconfigure(0, weight=0)
        stemBookFrame.grid_rowconfigure(1, weight=1)
        stemBookFrame.grid_rowconfigure(2, weight=1)
        stemBookFrame.grid_columnconfigure(0, weight=1)

        stemWidth = Label(stemBookFrame, text="               ", bg="brown")
        stemWidth.grid(row=0, column=0, sticky=NSEW)

        canvas = Canvas(stemBookFrame, width=50, bg="brown", highlightbackground="brown")
        canvas.create_oval(20, 35, 36, 45, fill="yellow", width=0)
        canvas.pack_forget()