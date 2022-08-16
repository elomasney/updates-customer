""" Reads json file data and filters this data
    for each customer type based on contract criteria.
    Saves filtered data as new json files.
"""
import json


class Update:
    # Class for update messages
    def __init__(self, fixture_id, competition, update_type,
                 selection_id, probability):
        self.fixture_id = fixture_id
        self.competition = competition
        self.update_type = update_type
        self.selection_id = selection_id
        self.probability = probability

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def __repr__(self):
        return f'<User { self.fixture_id }, {self.competition}, {self.update_type}, {self.selection_id}, {self.probability}>'


# Open and load json forwarder_updates file
with open('forwarder_updates.json', 'r', encoding='utf-8') as json_file:
    updates = json.loads(json_file.read())

fun_bet_updates = []
# Loop through all updates in forwarder_updates data.
for update in updates:
    # Exclude all updates for the 'PlayerProps' update type.
    if update['update_type'] != 'PlayerProps':
        # Append each matching update to the fun_bet_updates list
        fun_bet_updates.append(Update(**update))

print(fun_bet_updates)

crazy_bet_updates = []
# Loop through all updates in forwarder_updates data.
for update in updates:
    # Find updates from the SerieA competition only.
    if update['competition'] == 'SerieA':
        # Append each matching update to the crazy_bet_updates list
        crazy_bet_updates.append(update)

print(crazy_bet_updates)

lucky_bet_updates = []
# Loop through all updates in forwarder_updates data.
for update in updates:
    # Exclude all Premier League competition updates.
    if update['competition'] != 'PremierLeague':
        # Find updates within the filtered data
        # Where probability is higher than 0.25
        if update['probability'] >= 0.25:
            # Append each matching update to the lucky_bet_updates list.
            lucky_bet_updates.append(update)
            # Write filtered data list to new json file
            # with open("lucky_bet.json", "w", encoding='utf-8') as file:
            # json.dump(lucky_bet_updates, file, indent=4)

print(lucky_bet_updates)
