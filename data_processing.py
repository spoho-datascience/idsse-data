import os
import pandas as pd
from floodlight.io.dfl import read_position_data_xml, read_event_data_xml, read_teamsheets_from_mat_info_xml

# Define the path to the dataset
path = "C:\\Users\\ke6564\\Desktop\\Studium\\Promotion\\floodlight\\Benchmark_Dataset\\Data\\"

# Load Team Sheets
def load_team_sheets(path):
    info_files = [x for x in os.listdir(path) if "matchinformation" in x]
    team_sheets_all = pd.DataFrame()
    for file in info_files:
        team_sheets = read_teamsheets_from_mat_info_xml(os.path.join(path, file))
        team_sheets_combined = pd.concat([team_sheets["Home"].teamsheet, team_sheets["Away"].teamsheet])
        team_sheets_all = pd.concat([team_sheets_all, team_sheets_combined])
    return team_sheets_all

# Load Event Data
def load_event_data(path):
    info_files = [x for x in os.listdir(path) if "matchinformation" in x]
    event_files = [x for x in os.listdir(path) if "events_raw" in x]
    all_events = pd.DataFrame()
    for events_file, info_file in zip(event_files, info_files):
        events, _, _ = read_event_data_xml(os.path.join(path, events_file), os.path.join(path, info_file))
        events_fullmatch = pd.DataFrame()
        for half in events:
            for team in events[half]:
                events_fullmatch = pd.concat([events_fullmatch, events[half][team].events])
        all_events = pd.concat([all_events, events_fullmatch])
    return all_events

# Load Position Data
def load_position_data(path):
    info_files = [x for x in os.listdir(path) if "matchinformation" in x]
    position_files = [x for x in os.listdir(path) if "positions_raw" in x]
    n_frames = 0
    for position_file, info_file in zip(position_files, info_files):
        positions, _, _, _, _ = read_position_data_xml(os.path.join(path, position_file), os.path.join(path, info_file))
        n_frames += len(positions["firstHalf"]["Home"]) + len(positions["secondHalf"]["Home"])
    return n_frames

# Display Data Summary
def display_data_summary(path):
    team_sheets_all = load_team_sheets(path)
    all_events = load_event_data(path)
    n_frames = load_position_data(path)

    print("Unique player IDs:", team_sheets_all["pID"].nunique())
    print("Unique teams:", team_sheets_all["team"].nunique())
    print("Total number of events:", len(all_events))
    print("Unique event ID counts:\n", all_events["eID"].value_counts())
    print("Total number of position frames:", n_frames)