x = int(2.5) # x will be 2
y = int("5") # y will be 5

#print(x, y)
#print(6.5 // 2)
x1 = float(2)
#print(x1)
x2 = str(2.5)
#print(x2)
lst = [5, 4, 3, 2, 1]

def get_min(lst):   
    minimum = float('inf')
    for num in lst:
        if num < minimum:
            minimum = num

    return minimum
#EX!: 
def lineup(artists, set_times):
    return dict(zip(artists, set_times))

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

#EX2:
def get_artist_info(artist, festival_schedule):
    if artist in festival_schedule:
        return festival_schedule[artist]
    return {"message": "The artist not found"}

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))

#EX3:
def total_sales(ticket_sales):

    total = 0
    for key in ticket_sales:
        total += ticket_sales[key]
    return total

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))
#output: 4500

#EX4:
def identify_conflicts(venue1_schedule, venue2_schedule):

    conflicts = {}
    for artist in venue1_schedule:
        if artist in venue2_schedule and venue1_schedule[artist] == venue2_schedule[artist]:
            conflicts[artist] = venue1_schedule[artist]

    return conflicts

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}


print(identify_conflicts(venue1_schedule, venue2_schedule))

#output:{"Stromae": "9:00 PM", "HARDY": "7:00 PM"} 

#EX5:
#for v in my_dict.values():
#freq[v] = freq.get(v, 0) + 1
def best_set(votes):
    vote_count = {}
    for i in votes:
        artist = votes[i]
        if artist in vote_count:
            vote_count[artist] += 1
        else:
            vote_count[artist] = 1
    max_votes = max(vote_count.values())
    for artist, count in vote_count.items():
        if count == max_votes:
            return artist 

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
#output: SZA
#Ethel Cain
#Note: SZA and Ethel Cain would both be acceptable answers for the second example

#EX6:
def max_audience_performances(audiences):
    max_aud = max(audiences)
    count = audiences.count(max_aud)  
    return max_aud * count

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))

#output: 250
#440
#EX8:
def num_popular_pairs(popularity_scores):
    pass

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3)) 

#output: 4  6  0