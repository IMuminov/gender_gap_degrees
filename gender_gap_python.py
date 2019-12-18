%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt


women_degrees = pd.read_csv('gender_gap_study.csv')
women_degrees.head()

%matplotlib inline
#degree categories
stem_degrees = ['Psychology', 'Biology', 
             'Math and Statistics', 'Physical Sciences', 
             'Computer Science', 'Engineering']
lib_arts = ['Foreign Languages', 'English', 
            'Communications and Journalism', 
            'Art and Performance', 'Social Sciences and History']
others = ['Health Professions', 'Public Administration', 
          'Education', 'Agriculture',
          'Business', 'Architecture']

spine_list = ['top','bottom','right','left']

#color blind RGB values
cb_blue = (0/255, 107/255, 164/255)
cb_orange = (255/255, 128/255, 14/255)

#setting the grid environment
fig = plt.figure(figsize=(18,15))
count = 0

#stem Categories
for i in range(0,18,3):
    if count < 6:
        ax = fig.add_subplot(6,3,i+1)
        ax.plot(women_degrees.Year, women_degrees[stem_degrees[count]], c=cb_blue, linewidth=3)
        ax.plot(women_degrees.Year, 100-women_degrees[stem_degrees[count]], c=cb_orange, linewidth=3)
        ax.set_title(stem_degrees[count])

        #removing spines from charts
        for x in range(0,4):
            ax.spines[spine_list[x]].set_visible(False)

        ax.set_xlim(1968, 2011)
        ax.set_ylim(0,100)

        ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.5)
        ax.set_yticks([0,100])
        ax.tick_params(bottom=False,top=False,left=False,right=False)
        if count!=5:
            ax.tick_params(labelbottom=False)
            
        if count==0:
            ax.text(2008, 92, 'Men')
            ax.text(2006, 1, 'Women')
        if count==5:
            ax.text(2006, 65, 'Women')
            ax.text(2008, 26, 'Men')
    count += 1

    
count = 0
for i in range(2,18,3):
    if count < 5:
        ax = fig.add_subplot(6,3,i)
        ax.plot(women_degrees.Year, women_degrees[lib_arts[count]], c=cb_blue, linewidth=3)
        ax.plot(women_degrees.Year, 100-women_degrees[lib_arts[count]], c=cb_orange, linewidth=3)
        ax.set_title(lib_arts[count])

        #removing spines from charts
        for x in range(0,4):
            ax.spines[spine_list[x]].set_visible(False)

        ax.set_xlim(1968, 2011)
        ax.set_ylim(0,100)
        
        ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.5)
        ax.set_yticks([0,100])
        ax.tick_params(bottom=False,top=False,left=False,right=False)
        if count!=4:
            ax.tick_params(labelbottom=False)
        if count==0:
            ax.text(2008, 80, 'Men')
            ax.text(2006, 15, 'Women')
        if count==4:
            ax.text(2006, 65, 'Women')
            ax.text(2008, 26, 'Men')
    count += 1

    
count = 0    
for i in range(3,19,3):
    if count < 6:
        ax = fig.add_subplot(6,3,i)
        ax.plot(women_degrees.Year, women_degrees[others[count]], c=cb_blue, linewidth=3)
        ax.plot(women_degrees.Year, 100-women_degrees[others[count]], c=cb_orange, linewidth=3)
        ax.set_title(others[count])

        #removing spines from charts
        for x in range(0,4):
            ax.spines[spine_list[x]].set_visible(False)

        ax.set_xlim(1968, 2011)
        ax.set_ylim(0,100)

        ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.5)
        ax.set_yticks([0,100])
        ax.tick_params(bottom=False,top=False,left=False,right=False)
        if count!=5:
            ax.tick_params(labelbottom=False)
        
        if count==0:
            ax.text(2008, 92, 'Men')
            ax.text(2006, 1, 'Women')
        if count==5:
            ax.text(2006, 65, 'Women')
            ax.text(2008, 26, 'Men')
    count += 1
fig.savefig('gender_gap_degrees.png')
plt.show() 
