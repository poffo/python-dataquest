
# In this guided project, we'll extend the work we did in the last two missions on visualizing the gender gap across college degrees. So far, we mostly focused on the STEM degrees but now we will generate line charts to compare across all degree categories. In the last step of this guided project, we'll explore how to export the final diagram we create as an image file. You can download the solutions for this guided project here.


# %matplotlib inline
#import pandas as pd
#import matplotlib.pyplot as plt
#
#women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
#cb_dark_blue = (0/255,107/255,164/255)
#cb_orange = (255/255, 128/255, 14/255)
#stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']
#
#fig = plt.figure(figsize=(18, 3))
#
#for sp in range(0,6):
#    ax = fig.add_subplot(1,6,sp+1)
#    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
#    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
#    ax.spines["right"].set_visible(False)    
#    ax.spines["left"].set_visible(False)
#    ax.spines["top"].set_visible(False)    
#    ax.spines["bottom"].set_visible(False)
#    ax.set_xlim(1968, 2011)
#    ax.set_ylim(0,100)
#    ax.set_title(stem_cats[sp])
#    ax.tick_params(bottom="off", top="off", left="off", right="off")
#    
#    if sp == 0:
#        ax.text(2005, 87, 'Men')
#        ax.text(2002, 8, 'Women')
#    elif sp == 5:
#        ax.text(2005, 62, 'Men')
#        ax.text(2001, 35, 'Women')
#plt.show()
#
##############################################################################

# - Generate a 6 row by 3 column grid of subplots.
# - In the first column:
#   - Generate line charts for both male and female percentages for every degree in stem_cats.
#   - Add text annotations for Women and Men in the topmost and bottommost plots.
# - In the second column:
#   - Generate line charts for both male and female percentages for every degree in lib_arts_cats.
#   - Add text annotations for Women and Men for only the topmost plot (since the lines overlap at the end in the bottommost plot).
# - In the third column:
#   - Generate line charts for both male and female percentages for every degree in other_cats.
#   - Add text annotations for Women and Men in the topmost and bottommost plots.

#import pandas as pd
#import matplotlib.pyplot as plt
#
#women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
#cb_dark_blue = (0/255,107/255,164/255)
#cb_orange = (255/255, 128/255, 14/255)
#
#stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering', 'Computer Science']
#lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
#other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']
#
#fig = plt.figure(figsize=(18, 3))
#col = 0
#
#for varList in ['stem_cats','lib_arts_cats','other_cats']:
#    print(varList)
#    size = len(eval(varList))
#
#    if(size > 6):
#        size = 6
#
#    data = eval(varList)
#
#    for sp in range(0,size):
#        print((((sp+1)*(col+1))+(sp*2)-(col*sp)))
#        ax = fig.add_subplot(6,3,(((sp+1)*(col+1))+(sp*2)-(col*sp)))
#        ax.plot(women_degrees['Year'], women_degrees[data[sp]], c=cb_dark_blue, label='Women', linewidth=3)
#        ax.plot(women_degrees['Year'], 100-women_degrees[data[sp]], c=cb_orange, label='Men', linewidth=3)
#        ax.spines["right"].set_visible(False)    
#        ax.spines["left"].set_visible(False)
#        ax.spines["top"].set_visible(False)    
#        ax.spines["bottom"].set_visible(False)
#        ax.set_xlim(1968, 2011)
#        ax.set_ylim(0,100)
#        ax.set_title(data[sp])
#        ax.tick_params(bottom="off", top="off", left="off", right="off")
#
#        if sp == 0:
#            ax.text(2005, 87, 'Men')
#            ax.text(2002, 8, 'Women')
#        elif sp == 5:
#            ax.text(2005, 62, 'Men')
#            ax.text(2001, 35, 'Women')
#
#    col = col + 1
#
#plt.show()


#######################################################################


# Disable the x-axis labels for all line charts except the bottommost line charts in each column.
# Click here to see what the diagram should look like.

#import pandas as pd
#import matplotlib.pyplot as plt
#
#women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
#cb_dark_blue = (0/255,107/255,164/255)
#cb_orange = (255/255, 128/255, 14/255)
#
#stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering', 'Computer Science']
#lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
#other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']
#
#fig = plt.figure(figsize=(18, 3))
#col = 0
#
#for varList in ['stem_cats','lib_arts_cats','other_cats']:
#    print(varList)
#    size = len(eval(varList))
#
#    if(size > 6):
#        size = 6
#
#    data = eval(varList)
#
#    for sp in range(0,size):
#        print((((sp+1)*(col+1))+(sp*2)-(col*sp)))
#        ax = fig.add_subplot(6,3,(((sp+1)*(col+1))+(sp*2)-(col*sp)))
#        ax.plot(women_degrees['Year'], women_degrees[data[sp]], c=cb_dark_blue, label='Women', linewidth=3)
#        ax.plot(women_degrees['Year'], 100-women_degrees[data[sp]], c=cb_orange, label='Men', linewidth=3)
#        ax.spines["right"].set_visible(False)    
#        ax.spines["left"].set_visible(False)
#        ax.spines["top"].set_visible(False)    
#        ax.spines["bottom"].set_visible(False)
#        ax.set_xlim(1968, 2011)
#        ax.set_ylim(0,100)
#        ax.set_title(data[sp])
#        
#        if sp == 0:
#            ax.text(2005, 87, 'Men')
#            ax.text(2002, 8, 'Women')
#        elif sp == 5:
#            ax.text(2005, 62, 'Men')
#            ax.text(2001, 35, 'Women')
#
#        if sp == (size-1):
#            ax.tick_params(labelbottom="on", bottom="off", top="off", left="off", right="off")
#        else:
#            ax.tick_params(labelbottom="off", bottom="off", top="off", left="off", right="off")
#
#
#    col = col + 1
#
#plt.show()


#######################################################################

# For all plots:
# Enable just the y-axis labels at 0 and 100.

#import pandas as pd
#import matplotlib.pyplot as plt
#
#women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
#cb_dark_blue = (0/255,107/255,164/255)
#cb_orange = (255/255, 128/255, 14/255)
#
#stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering', 'Computer Science']
#lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
#other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']
#
#fig = plt.figure(figsize=(18, 3))
#col = 0
#
#for varList in ['stem_cats','lib_arts_cats','other_cats']:
#    print(varList)
#    size = len(eval(varList))
#
#    if(size > 6):
#        size = 6
#
#    data = eval(varList)
#
#    for sp in range(0,size):
#        print((((sp+1)*(col+1))+(sp*2)-(col*sp)))
#        ax = fig.add_subplot(6,3,(((sp+1)*(col+1))+(sp*2)-(col*sp)))
#        ax.plot(women_degrees['Year'], women_degrees[data[sp]], c=cb_dark_blue, label='Women', linewidth=3)
#        ax.plot(women_degrees['Year'], 100-women_degrees[data[sp]], c=cb_orange, label='Men', linewidth=3)
#        ax.spines["right"].set_visible(False)    
#        ax.spines["left"].set_visible(False)
#        ax.spines["top"].set_visible(False)    
#        ax.spines["bottom"].set_visible(False)
#        ax.set_yticks([0,100])
#        ax.set_xlim(1968, 2011)
#        ax.set_ylim(0,100)
#        ax.set_title(data[sp])
#        
#        if sp == 0:
#            ax.text(2005, 87, 'Men')
#            ax.text(2002, 8, 'Women')
#        elif sp == 5:
#            ax.text(2005, 62, 'Men')
#            ax.text(2001, 35, 'Women')
#
#        if sp == (size-1):
#            ax.tick_params(labelbottom="on", bottom="off", top="off", left="off", right="off")
#        else:
#            ax.tick_params(labelbottom="off", bottom="off", top="off", left="off", right="off")
#
#
#    col = col + 1
#
#plt.show()


######################################################################

# - For all plots:
#   - Generate a horizontal line with the following properties:
#   - Starts at the y-axis position 50
#   - Set to the third color (light gray) in the Color Blind 10 palette
#   - Has a transparency of 0.3


import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)

stem_cats = ['Psychology', 'Biology', 'Math and Statistics', 'Physical Sciences', 'Computer Science', 'Engineering', 'Computer Science']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

fig = plt.figure(figsize=(18, 3))
col = 0

for varList in ['stem_cats','lib_arts_cats','other_cats']:
    print(varList)
    size = len(eval(varList))

    if(size > 6):
        size = 6

    data = eval(varList)

    for sp in range(0,size):
        print((((sp+1)*(col+1))+(sp*2)-(col*sp)))
        ax = fig.add_subplot(6,3,(((sp+1)*(col+1))+(sp*2)-(col*sp)))
        ax.plot(women_degrees['Year'], women_degrees[data[sp]], c=cb_dark_blue, label='Women', linewidth=3)
        ax.plot(women_degrees['Year'], 100-women_degrees[data[sp]], c=cb_orange, label='Men', linewidth=3)
        ax.spines["right"].set_visible(False)    
        ax.spines["left"].set_visible(False)
        ax.spines["top"].set_visible(False)    
        ax.spines["bottom"].set_visible(False)
        ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
        ax.set_yticks([0,100])
        ax.set_xlim(1968, 2011)
        ax.set_ylim(0,100)
        ax.set_title(data[sp])
        
        if sp == 0:
            ax.text(2005, 87, 'Men')
            ax.text(2002, 8, 'Women')
        elif sp == 5:
            ax.text(2005, 62, 'Men')
            ax.text(2001, 35, 'Women')

        if sp == (size-1):
            ax.tick_params(labelbottom="on", bottom="off", top="off", left="off", right="off")
        else:
            ax.tick_params(labelbottom="off", bottom="off", top="off", left="off", right="off")


    col = col + 1

# If I want to save the figure, first I should call the savefig method.
# plt.show()


######################################################################

# Export the figure containing all of the line charts to "gender_degrees.png".

plt.savefig('biology_degrees.png')

plt.show()
