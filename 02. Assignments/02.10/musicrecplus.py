'''
Created on Nov 15, 2017

@author: arusignu, csimonal

I pledge my honor that I have abided by the Stevens Honor System. arusignu, csimonal


'''

from cs115 import *

def readInData():
    """Reads in data"""
    database = {}
    try:
        handle = open("musicrecplus.txt","r")
        lines = handle.read().splitlines()
        #print(lines)
        handle.close()
        for line in lines:
            # print("line:" line)
            parts = line.split(":")
            name = parts[0]
            artists = parts[1]
            # print("name: '%s' artists: '%s'" % (name, artists))
            # print(sorted(artists.split(",")))
            database[name] = sorted(artists.split(","))
        # print(database)
    except:
        return database
    return database

def getUser():
    """Gets user."""
    print("Enter your name (put a $ after your name if you wish")
    print("your preferences to remain private):")
    username = input()
    return username

"""
def myMap(fn, iterable):
    ret = [0] * len(iterable)
    i = 0
    for thing in iterable:
        ret[i] = fn(thing)
        i += 1
    return ret
"""

def printOnePerLine(iterable):
    """Prints items in a list line after line."""
    for thing in iterable:
        print(thing)

def enterPrefs(user, database):
    """Allows user to enter preferences."""
    i = 0
    prefs = [] 
    while i == 0:
        print("Enter an artist that you like (Enter to finish):")
        pref = input()
        if pref == '':
            i = 1
        else:
            prefs.append(pref)
    database[user] = prefs
    return database
        
def getRecs(user,database):
    """Gets recommendations for the user."""
    def compare(userArtists, otherArtists, otherUName):
        """Compares the artist lists of other user from your own.
        Returns number of matches"""
        if otherUName[-1] == '$':
            return -1
        iUser = 0
        iOther = 0
        score = 0
        while iUser < len(userArtists) and iOther < len(otherArtists):
            aUser = userArtists[iUser]
            aOther = otherArtists[iOther]
            if aUser == aOther:
                score += 1
                iUser += 1
                iOther += 1
            elif aUser < aOther:
                iUser += 1
            else:
                iOther += 1
        if len(otherArtists) == score:
            return -1
        return score
    
    def diff(userArtists, otherArtists):
        """Returns list of different artists"""
        iUser = 0
        iOther = 0
        diffs = []
        while iUser < len(userArtists) and iOther < len(otherArtists):
            aUser = userArtists[iUser]
            aOther = otherArtists[iOther]
            if aUser == aOther:
                iUser += 1
                iOther += 1
            elif aUser < aOther:
                iUser += 1
            else:
                diffs.append(aOther)
                iOther += 1
        if iOther < len(otherArtists):
            diffs.extend(otherArtists[iOther:])
        return diffs
    
    userArtists = database[user]
    ranked = sorted(map(lambda uname: (compare(userArtists, \
        database[uname],uname), uname), database), reverse = True)\
    
    if len(ranked) == 0 or ranked[0][0] <= 0:
        print('No recommendations available at this time')
        return
    
    maxScore = ranked[0][0]
    iMax = 0
    for result in ranked:
        if maxScore != result[0]:
            break
        iMax += 1
    
    artists = []
    for i in range(iMax):
        artists.extend(diff(userArtists, database[ranked[i][1]]))
    artists = sorted(list(set(artists)))
    printOnePerLine(artists)

def popArt1(database):
    """Returns a dictionary of artists and their popularity"""
    artPop = {}
    """
    artRaw = map(lambda uname: database[uname], database)
    artPro = sorted(reduce(lambda i, j: i + j, artRaw))
    for i in artPro:
    """
    for user in database:
        if user[-1] =='$':
            continue
        for artist in database[user]:
            if artist in artPop:
                artPop[artist] += 1
            else:
                artPop[artist] = 1
    return artPop

def popArt2(database):
    """Returns the most popular artists"""
    ranked = sorted(list(popArt1(database).items()), key = lambda item: item[1], reverse = True)
    maxScore = ranked[0][1]
    popArts = []
    for i in range(len(ranked)):
        if ranked[i][1] == maxScore and ranked[i][0][-1] != '$':
            popArts.append(ranked[i][0])
    printOnePerLine(popArts)
    return ''
    
def popArt3(database):
    """Returns how popular the most popular artist is"""
    ranked = sorted(list(popArt1(database).items()), key = lambda item: item[1], reverse = True)
    print(ranked[0][1])
    
def activeUser(database):
    """Returns the most active user."""
    ranked = sorted(map(lambda i: (i,len(database[i])),database),key = lambda item: item[1], reverse = True)
    maxScore = ranked[0][1]
    actUse = []
    for i in range(len(ranked)):
        if ranked[i][1] == maxScore and ranked[i][0][-1] != '$':
            actUse.append(ranked[i][0])
    printOnePerLine(actUse)
    return ''

def save(database):
    """Saves the file."""
    handle = open("musicrecplus.txt", "w")
    for i in database:
        dbe = ''
        for j in sorted(database[i]):
            dbe += j + ','
        handle.write(i + ':' + dbe[0:-1] + '\n')
    handle.close()

def menu(user, database):
    """Creates a menu for the user."""
    i = 0
    while i == 0:    
        print("Enter a letter to choose an option:")
        print("e - Enter preferences")
        print("r - Get recommendations")
        print("p - Show most popular artists")
        print("h - How popular is the most popular")
        print("m - Which user has the most likes")
        print("q - Save and quit")
        choice = input()
        if choice == 'e':
            database = enterPrefs(user, database)
        elif choice == 'r':
            getRecs(user, database)
        elif choice == 'p':
            popArt2(database)
        elif choice == 'h':
            popArt3(database)
        elif choice == 'm':
            activeUser(database)
        elif choice == 'q':
            i = 1
        else:
            print("This is not a valid entry")
    return database
    
def main():
    """Does the thing."""
    database = readInData()
    user = getUser()
    if user not in database:
        enterPrefs(user,database)
    database = menu(user,database)
    save(database)    
    
main()