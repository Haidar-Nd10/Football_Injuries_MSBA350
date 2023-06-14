#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[218]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
#import seaborn as sns
#get_ipython().run_line_magic('matplotlib', 'inline')

#pd.set_option('notebook_repr_html', True)


# Read df file:
df=pd.read_csv(r'C:\Users\Haidar\Desktop\AUB\MSBA\Summer\MSBA 350\Projects\Individual project\Data\df.csv')

injury_groups = {
    'Group 1: Knee Injuries': ['Meniscal Injury', 'Torn muscle bundle', 'Torn Muscle Fibre', 'Ruptured intraarticular ligament initiation in knee', 'Knee Injury', 'Cruciate Ligament Rupture', 'Cruciate Ligament Injury', 'Patella problems', 'Patella tendon luxation', 'Partial damage to the cruciate ligament', 'Ruptured cruciate ligament', 'Partial demolition of the plantar fascia', 'Inflamed head of fibula', 'Strain of the patella'],
    'Group 2: Ankle and Foot Injuries': ['Achilles tendon rupture', 'Ankle Injury', 'Ankle problems', 'Sprained ankle', 'Distortion of the ankle', 'Torn ankle ligament', 'Fracture-dislocation of the ankle', 'Tarsal Rupture', 'Overstretching of the syndesmotic ligament', 'Capsular rupture in the ankle', 'Intraarticular ligament crack in the ankle', 'Ruptured ankle ligament', 'Intraarticular ligament fissure', 'Capsular tear in the ankle', 'Arthroscopy', 'Ruptured intraarticular ligament initiation in the ankle', 'Ankle Inflammation', 'Plantar fascia'],
    'Group 3: Leg and Calf Injuries': ['Disrupted Calf Muscle', 'Calf Injury', 'Calf Strain', 'Leg Injury', 'Calf Problems', 'Shinbone injury', 'Tibia Fracture', 'Hairline crack in calfbone', 'Shin bone bruise', 'Stress response of the bone', 'Muscle fiber tear', 'Calf muscle strain'],
    'Group 4: Groin and Hip Injuries': ['Tear in the abductor muscle', 'Groin Injury', 'Groin strain', 'Adductor problems', 'Pubitis', 'Problems with the hip flexor', 'Groin Surgery', 'Hip problems', 'Hip Injury', 'Edema in the knee', 'Sideband tear in the knee', 'Sideband strain in the knee'],
    'Group 5: Muscle Injuries': ['Muscle Injury', 'Muscular problems', 'Hamstring Injury', 'Muscle Fatigue', 'Biceps femoris muscle injury', 'Strain in the thigh and gluteal muscles', 'Muscle bruise', 'Muscle partial avulsion'],
    'Group 6: Arm and Shoulder Injuries': ['Fractured Arm', 'Shoulder Injury', 'Fractured Thumb', 'Bruised Acromioclavicular', 'Forearm Fracture', 'Elbow Injury', 'Hand Injury', 'Fractured Finger', 'Finger Injury', 'Wrist Injury', 'Hand fracture', 'Ulnar fracture', 'Midface fracture', 'Forearm Fracture', 'Scissure', 'Fractured Kneecap', 'Finger fracture', 'Fractured collarbone', 'Radius fracture', 'Broken shoulder', 'Fractured wrist'],
    'Group 7: Back and Neck Injuries': ['Back Injury', 'Back Pain', 'Spinal Injury', 'Back Strain', 'Vertebral fractures', 'Coccyx Problems', 'Spinal problems', 'Spinal Pain', 'Neck Pain', 'Sore Rib', 'Ruptured Rib', 'Fracture of the orbit', 'Lumbar Vertebra Fracture', 'Cervical spine injury', 'Cervical Fracture', 'Lumbar vertebrae problems', 'Blockade in the spinal', 'Inflammation in spine', 'Whiplash'],
    'Group 8: Other Injuries': ['Fibula Fracture', 'Nose Injury', 'Nose surgery', 'Facial Fracture', 'Facial Injury', 'Tooth Inflammation', 'Toothache', 'Cheekbone Fracture', 'Cheek bone contusion', 'Basal Skull Fracture', 'Nasal Bone Fracture', 'Forearm Fracture', 'Bruised Rib', 'Neck Injury', 'Neck bruise', 'Ruptured lateral collateral ligament', 'Ruptured sideband in the ankle', 'Bone chipping', 'Broken wrist', 'Patella rupture', 'Sideband injury', 'Lumbar vertebrae problems', 'Ruptured knee ligament', 'Vertebra injury', 'Ruptured ligaments', 'Bullet Wound', 'Kidney problems', 'Kidney stone surgery', 'Stroke']
}

# Streamlit
import streamlit as st

def show_home():
    # Image URL
    IMAGE_URL = "https://media.cnn.com/api/v1/images/stellar/prod/221125075457-01-neymar-injury-world-cup-1124.jpg?c=16x9&q=h_720,w_1280,c_fill/f_webp"
    
    # Display the image
    st.image(IMAGE_URL, width=700)
    # Header
    st.title('Football Injury Analysis')

    # Introduction
    st.markdown("""
        Injuries in football are a significant concern affecting players at all levels.
        This analysis explores injury statistics, injury distribution by club and country,
        and injury patterns based on player stats. Understanding the prevalence and patterns
        of football injuries can help develop strategies to prevent and manage them effectively.
    """)
    

## Injury Statistics tab
def show_Recovery_Time_statistics():
    # Display the injury statistics section
    st.markdown('<div class="header">Injury Recovery Time Statistics</div>', unsafe_allow_html=True)
    st.markdown('<div class="section">This section explores injury patterns with different recovery times.</div>', unsafe_allow_html=True)

    # Select top 20 injuries
    top_20_injuries = df['injury_type'].value_counts().head(20).index.tolist()

    # Create radio buttons to select the plot
    selected_plot = st.radio('Select a plot:', ('Recovery Time of Different Injuries', 'Recovery Time vs Player Age', 'Injury Recover Time Count'))

    if selected_plot == 'Recovery Time of Different Injuries':
        # Create a dropdown widget for the first plot (recovery time)
        selected_injury = st.selectbox('Select an injury type:', top_20_injuries)
        plot_recovery_time(selected_injury)
    elif selected_plot == 'Recovery Time vs Player Age':
        plot_recovery_time_vs_injury_age()
    elif selected_plot == 'Injury Recover Time Count':
        recovery_time_count_plot()

def plot_recovery_time(selected_injury):
    filtered_data = df[df['injury_type'] == selected_injury]
    recovery_count = filtered_data['recovery_time'].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(sorted(recovery_count.index), recovery_count.values, marker='o')
    ax.axvline(filtered_data['recovery_time'].mean(), color='red', linestyle='--', label='Mean Recovery Time')
    ax.set_xlabel('Recovery Time')
    ax.set_ylabel('Count')
    ax.set_title(f'Count of Recovery Time for {selected_injury}')
    ax.legend()

    # Customize x-axis tick labels to show every 20 recovery times
    x_ticks = sorted(recovery_count.index)[::20]  # Select every 20th recovery time
    ax.set_xticks(x_ticks)

    st.pyplot(fig)


def plot_recovery_time_vs_injury_age():
    group_names = list(injury_groups.keys())
    group_names.insert(0, "All Injuries")  # Add "All Injuries" option at the beginning of the group_names list
    selected_group = st.selectbox('Select an injury group', group_names)

    if selected_group == "All Injuries":
        filtered_data = df  # Select all data from df
    else:
        selected_injuries = injury_groups[selected_group]
        filtered_data = df[df['injury_type'].isin(selected_injuries)]
    
    mean_recovery_times = filtered_data.groupby('injury_age')['recovery_time'].mean()

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(mean_recovery_times.index, mean_recovery_times.values, color='blue', marker='o')
    ax.set_xlabel('Injury Age')
    ax.set_ylabel('Mean Recovery Time')
    ax.set_title('Mean Recovery Time vs Injury Age')
    ax.grid(True)

    # Add trend line
    z = np.polyfit(mean_recovery_times.index, mean_recovery_times.values, 1)
    p = np.poly1d(z)
    ax.plot(mean_recovery_times.index, p(mean_recovery_times.index), color='red', linestyle='--', label='Trend Line')

    ax.legend()

    st.pyplot(fig)



def recovery_time_count_plot():
    # Filter out non-integer values in 'recovery_time' column
    recovery_time_filtered = df['recovery_time'].loc[df['recovery_time'].astype(str).str.isdigit()]

    # Calculate the count of injuries by recovery time and sort in ascending order
    injury_count = recovery_time_filtered.value_counts().sort_index()

    # Convert recovery time values to integers
    injury_count.index = injury_count.index.astype(int)

    # Generate x and y coordinates for the scatter plot
    x = injury_count.index
    y = injury_count.values

    # Sort the x-axis values in ascending order
    x_sorted = sorted(x)

    # Plot the scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x_sorted, y)
    ax.set_xlabel('Recovery Time')
    ax.set_ylabel('Count')
    ax.set_title('Count of Injuries by Recovery Time')

    # Customize x-axis tick labels to show every 20 recovery times
    x_ticks = x_sorted[::20]  # Select every 20th recovery time from the sorted x-axis values
    ax.set_xticks(x_ticks)

    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot(fig)

## Injury player stat tab
def show_injury_by_player_stats():
    # Display the injury by player stats section
    st.markdown('<div class="header">Injury by Player Stats</div>', unsafe_allow_html=True)
    st.markdown('<div class="section">This section explores injury patterns based on player statistics.</div>', unsafe_allow_html=True)

    # Dropdown for player statistics
    statistic_type = st.selectbox('Select a player statistic:', ('Nationality', 'Age', 'Position', 'Height', 'Weight', 'Preferred Foot', 'Transfers'))

    if statistic_type == 'Nationality':
        plot_nationality()
    elif statistic_type == 'Age':
        plot_age()
    elif statistic_type == 'Position':
        plot_position()
    elif statistic_type == 'Height':
        plot_height()
    elif statistic_type == 'Weight':
        plot_weight()
    elif statistic_type == 'Preferred Foot':
        plot_preferred_foot()
    elif statistic_type == 'Transfers':
        plot_injuries_vs_transfers()


def plot_injuries_vs_transfers():
    # Group the data by 'id' and calculate the count of injuries per player
    count_per_id = df.groupby('id').size()
    num_of_transfers = df.groupby('id')['num_of_transfers'].first()
    
    # Calculate the trend line using numpy.polyfit
    slope, intercept = np.polyfit(num_of_transfers, count_per_id, 1)
    trend_line = slope * num_of_transfers + intercept
    
    # Plot the scatter plot and trend line
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(num_of_transfers, count_per_id)
    ax.plot(num_of_transfers, trend_line, color='red', label='Trend Line')
    ax.set_xlabel('Number of Transfers')
    ax.set_ylabel('Number of Injuries')
    ax.set_title('Number of Injuries vs Number of Transfers')
    ax.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Display the plot using Streamlit
    st.pyplot(fig)


def plot_nationality():
    # Assuming you have a DataFrame named df with 'country', 'injury_season', and 'role' columns

    # Add a slider to select the start and end years of the season
    start_year, end_year = st.slider('Select Season Range', 2000, 2022, (2000, 2022))

    # Add a multiselect box to select the player positions
    positions = ['All Positions'] + df['role'].unique().tolist()
    selected_positions = st.multiselect('Select Player Positions', positions)

    # Filter the DataFrame based on the selected season range and positions
    start_season = str(start_year)[-2:] + '/' + str(start_year + 1)[-2:]
    end_season = str(end_year)[-2:] + '/' + str(end_year + 1)[-2:]

    if 'All Positions' in selected_positions:
        filtered_data = df[(df['injury_season'] >= start_season) & (df['injury_season'] <= end_season)]
    elif selected_positions:
        filtered_data = df[(df['injury_season'] >= start_season) & (df['injury_season'] <= end_season) & (df['role'].isin(selected_positions))]
    else:
        filtered_data = df[(df['injury_season'] >= start_season) & (df['injury_season'] <= end_season)]

    # Check if filtered data is empty
    if filtered_data.empty:
        st.write("No data available for the selected filters.")
        return

    # Convert the season format to year format
    filtered_data['injury_year'] = filtered_data['injury_season'].apply(convert_season_to_year)

    # Calculate the count of injuries by nationality
    injury_count = filtered_data['country'].value_counts().head(20)

    # Plot the bar graph
    fig, ax = plt.subplots(figsize=(15, 8))
    injury_count.plot(kind='bar', ax=ax)
    ax.set_xlabel('Country')
    ax.set_ylabel('Count')
    ax.set_title('Count of Injuries by Nationality')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

def plot_age():
    # Assuming you have a DataFrame named df with 'injury_age' and 'role' columns

    # Add a multiselect box to select the player positions
    positions = ['All Positions'] + df['role'].unique().tolist()
    selected_positions = st.multiselect('Select Player Positions', positions)

    # Filter the DataFrame based on the selected positions
    if 'All Positions' in selected_positions:
        filtered_data = df
    elif selected_positions:
        filtered_data = df[df['role'].isin(selected_positions)]
    else:
        filtered_data = df

    # Calculate the count of injuries by age and sort in ascending order
    injury_count = filtered_data['injury_age'].value_counts().sort_index()

    # Generate x and y coordinates for the scatter plot
    x = injury_count.index
    y = injury_count.values

    # Plot the scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x, y)
    ax.set_xlabel('Age')
    ax.set_ylabel('Count')
    ax.set_title('Count of Injuries by Age')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

def plot_position():
    # Assuming you have a DataFrame named df with 'role' and 'injury_season' columns

    # Add a slider to select the start and end years of the season
    start_year, end_year = st.slider('Select Season Range', 2000, 2022, (2000, 2022))

    # Filter the DataFrame based on the selected season range
    start_season = str(start_year)[-2:] + '/' + str(start_year + 1)[-2:]
    end_season = str(end_year)[-2:] + '/' + str(end_year + 1)[-2:]
    filtered_data = df[(df['injury_season'] >= start_season) & (df['injury_season'] <= end_season)]

    # Calculate the count of injuries by position
    injury_count = filtered_data['role'].value_counts()

    # Plot the bar graph
    fig, ax = plt.subplots(figsize=(15, 8))
    injury_count.plot(kind='bar', ax=ax)
    ax.set_xlabel('Position')
    ax.set_ylabel('Count')
    ax.set_title('Count of Injuries by Position')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)


def plot_height():
    
    # Add a multiselect box to select the player positions
    positions = ['All Positions'] + df['role'].unique().tolist()
    selected_positions = st.multiselect('Select Player Positions', positions)

    # Filter the DataFrame based on the selected positions
    if 'All Positions' in selected_positions:
        filtered_data = df
    elif selected_positions:
        filtered_data = df[df['role'].isin(selected_positions)]
    else:
        filtered_data = df

    # Calculate the count of injuries by height and sort in ascending order
    injury_count = filtered_data['height'].value_counts().sort_index()

    # Generate x and y coordinates for the scatter plot
    x = injury_count.index
    y = injury_count.values

    # Plot the scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x, y)
    ax.set_xlabel('Height')
    ax.set_ylabel('Count')
    ax.set_title('Count of Injuries by Height')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)


def plot_weight():
    # Assuming you have a DataFrame named df with 'weight' and 'role' columns

    # Add a multiselect box to select the player positions
    positions = ['All Positions'] + df['role'].unique().tolist()
    selected_positions = st.multiselect('Select Player Positions', positions)

    # Filter the DataFrame based on the selected positions
    if 'All Positions' in selected_positions:
        filtered_data = df
    elif selected_positions:
        filtered_data = df[df['role'].isin(selected_positions)]
    else:
        filtered_data = df

    # Calculate the count of injuries by weight and sort in ascending order
    injury_count = filtered_data['weight'].value_counts().sort_index()

    # Generate x and y coordinates for the scatter plot
    x = injury_count.index
    y = injury_count.values

    # Plot the scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x, y)
    ax.set_xlabel('Weight')
    ax.set_ylabel('Count')
    ax.set_title('Count of Injuries by Weight')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)


def plot_preferred_foot():
    # Assuming you have a DataFrame named df with 'injury_club_country' column

    # Calculate the count of injuries by preferred foot
    injury_count = df['foot'].value_counts().head(3)

    # Plot the bar graph
    fig, ax = plt.subplots(figsize=(15, 8))
    injury_count.plot(kind='bar', ax=ax)
    ax.set_xlabel('Preferred Foot')
    ax.set_ylabel('Count')
    ax.set_title('Count of Injuries by Preferred Foot')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    
#Injury by club country tab
def show_injury_by_club_country():
    # Display the injury by club and country section
    st.markdown('<div class="header">Injury by Club and Country</div>', unsafe_allow_html=True)
    st.markdown('<div class="section">This section analyzes the distribution of injuries by club and country.</div>', unsafe_allow_html=True)

    # Dropdown for player statistics
    statistic_type = st.selectbox('Select a player statistic:', ('League', 'Club', 'Season', 'Latest Club'))

    if statistic_type == 'League':
        plot_league()
    elif statistic_type == 'Club':
        plot_club()
    elif statistic_type == 'Season':
        plot_season()
    elif statistic_type == 'Latest Club':
        plot_latest_club()

def convert_season_to_year(season):
    # Extract the start and end years from the season format
    start_year = int('20' + season[:2])
    end_year = int('20' + season[3:])
    return start_year, end_year
def plot_league():
    # Assuming you have a DataFrame named df with 'injury_club_country' and 'injury_season' columns

    # Add a slider to select the start and end years of the season
    start_year, end_year = st.slider('Select Season Range', 2000, 2022, (2000, 2022))

    # Filter the DataFrame based on the selected season range
    start_season = str(start_year)[-2:] + '/' + str(start_year + 1)[-2:]
    end_season = str(end_year)[-2:] + '/' + str(end_year + 1)[-2:]
    filtered_data = df[(df['injury_season'] >= start_season) & (df['injury_season'] <= end_season)]

    # Convert the season format to year format
    filtered_data['injury_year'] = filtered_data['injury_season'].apply(convert_season_to_year)

    # Calculate the count of injuries by country
    injury_count = filtered_data['injury_club_country'].value_counts()

    # Plot the bar graph
    fig, ax = plt.subplots(figsize=(15, 8))
    injury_count.plot(kind='bar', ax=ax)
    ax.set_xlabel('Country')
    ax.set_ylabel('Count')
    ax.set_title('Count of Injuries by Domestic Leagues')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

def plot_club():
    # Assuming you have a DataFrame named df with 'injury_club_country' and 'injury_season' columns

    # Add a slider to select the start and end years of the season
    start_year, end_year = st.slider('Select Season Range', 2000, 2022, (2000, 2022))

    # Filter the DataFrame based on the selected season range
    start_season = str(start_year)[-2:] + '/' + str(start_year + 1)[-2:]
    end_season = str(end_year)[-2:] + '/' + str(end_year + 1)[-2:]
    filtered_data = df[(df['injury_season'] >= start_season) & (df['injury_season'] <= end_season)]

    # Convert the season format to year format
    filtered_data['injury_year'] = filtered_data['injury_season'].apply(convert_season_to_year)

    # Calculate the count of injuries by club
    injury_count = filtered_data['injury_club'].value_counts().head(20)

    # Plot the bar graph
    fig, ax = plt.subplots(figsize=(15, 8))
    injury_count.plot(kind='bar', ax=ax)
    ax.set_xlabel('Club')
    ax.set_ylabel('Count')
    ax.set_title('Count of Injuries by Club')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

def plot_season():
    # Assuming you have a DataFrame named df with 'injury_season' column

    # Calculate the count of injuries by season and sort in ascending order
    injury_count = df['injury_season'].value_counts().sort_index()

    # Plot the line plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(injury_count.index, injury_count.values, marker='o', linestyle='-', linewidth=2)
    ax.set_xlabel('Season')
    ax.set_ylabel('Count')
    ax.set_title('Count of Injuries by Season')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

def plot_latest_club():
    # Assuming you have a DataFrame named df with 'latest_club' and 'injury_season' columns

    # Add a slider to select the start and end years of the season
    start_year, end_year = st.slider('Select Season Range', 2000, 2022, (2000, 2022))

    # Filter the DataFrame based on the selected season range
    start_season = str(start_year)[-2:] + '/' + str(start_year + 1)[-2:]
    end_season = str(end_year)[-2:] + '/' + str(end_year + 1)[-2:]
    filtered_data = df[(df['injury_season'] >= start_season) & (df['injury_season'] <= end_season)]

    # Convert the season format to year format
    filtered_data['injury_year'] = filtered_data['injury_season'].apply(convert_season_to_year)

    # Calculate the count of injuries by club
    injury_count = filtered_data['latest_club'].value_counts().head(20)

    # Plot the bar graph
    fig, ax = plt.subplots(figsize=(15, 8))
    injury_count.plot(kind='bar', ax=ax)
    ax.set_xlabel('Club')
    ax.set_ylabel('Count')
    ax.set_title('Number of injuries sustained by players in each Club')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    

def main():        
    # Set page title and favicon
    st.set_page_config(page_title='Football Injury Analysis', page_icon=':soccer:', layout='wide')


    # Set background color and font color using CSS classes
    st.markdown("""
        <style>
        body {
            background-color: #F5F5F5;
            color: #333333;
            font-family: Arial, sans-serif;
        }

        .header {
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .section {
            margin-bottom: 40px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Menu bar
    #menu_options = ['Home', 'Injury Statistics', 'Injury by Club and Country', 'Injury by Player Stats']
    #menu_choice = st.sidebar.selectbox('Menu', menu_options)

    #if menu_choice == 'Home':
     #   show_home()
    #elif menu_choice == 'Injury Statistics':
     #   show_injury_statistics()
    #elif menu_choice == 'Injury by Club and Country':
     #   show_injury_by_club_country()
    #elif menu_choice == 'Injury by Player Stats':
     #   show_injury_by_player_stats()

    # Navigation bar
    section = st.sidebar.selectbox('Navigation', ('Home','Injury Recovery Time Statistics', 'Injury by Club and Country', 'Injury by Player Stats'))

    # Display the selected section
    if section == 'Home':
        show_home()
    elif section == 'Injury Recovery Time Statistics':
        show_Recovery_Time_statistics()
    elif section == 'Injury by Club and Country':
        show_injury_by_club_country()
    elif section == 'Injury by Player Stats':
        show_injury_by_player_stats()

if __name__ == '__main__':
    main()
