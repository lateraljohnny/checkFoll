# checkFoll

Prerequisites: {

Request your information from Instagram: 

    Settings >> Account Center >> Your information and permissions >> Export your information >> Create export 
    >> Export to Device >> Date range set to 'All time' >> Customize information 	
    >> Clear all for all sections then check 'Followers and following' under 'Connections' >> Save >> Start export
  
This will take about 30 minutes or longer so come back to the "Export your information" page later.

-- If you wish to check who unfollowed you, you need 2 instances of your following list (Before and After) from different dates. 

Ex: 'following.html' from Monday and 'following.html' from Friday but rename it to 'following2.html'

Once you have your information downloaded and extracted (it will download as a zip file), move the 'following.html' and 'followers.html' files into a folder with the program.

}


Follow these steps to run the program:
1. Open terminal (Win + R >> type cmd >> click enter OR Right-click windows icon on your taskbar >> terminal)
  
2. cd into the folder where your python file is (mine is called "checkfoll")
Ex: cd C:\Users\[my user]\Downloads\checkfoll
5. Run this code in the brackets:

{python3 FANORNAH.py -i following.html -i following2.html -e followers.html} - To check who unfollowed and who doesn't follow you back.
   
{python3 FANORNAH.py -i following.html -e followers.html} - To only check who doesn't follow you back.
