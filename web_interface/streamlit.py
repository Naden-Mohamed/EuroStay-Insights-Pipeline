import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from sklearn.neighbors import BallTree
import warnings

warnings.filterwarnings("ignore")

BLACK  = "black"
ORANGE = "orange"
GREY   = "grey"

sns.set_theme(style="darkgrid", rc={
    "axes.facecolor": BLACK,      # Background of the plot
    "figure.facecolor": BLACK,    # Background of the entire figure
    "axes.edgecolor": ORANGE,     # Border color
    "grid.color": GREY,           # Grid line color
    "text.color": "white",        # Text color
    "xtick.color": "white",       # X-axis tick color
    "ytick.color": "white",       # Y-axis tick color
    "axes.labelcolor": "white",   # Axis labels
    "axes.titlesize": 16
})

st.set_page_config(page_title="Travel Insights Dashboard", layout="wide")

@st.cache_data 
def load_data():
    df = pd.read_csv("Airbnb dataset/Airbnb.csv") 
    df['realSum'] = df['realSum'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False)
    df['realSum'] = pd.to_numeric(df['realSum'])
    return df

df = load_data()

st.title("🏨 European Hotel & Airbnb Analysis")

mean_weekday = df[df['Day_Type'] == 'weekday']['realSum'].mean()
mean_weekend = df[df['Day_Type'] == 'weekend']['realSum'].mean()

col_m1, col_m2 = st.columns(2)
col_m1.metric("Avg Weekday Price", f"${mean_weekday:.2f}")
col_m2.metric("Avg Weekend Price", f"${mean_weekend:.2f}")

st.markdown("---") 

plot_col1, plot_col2 = st.columns(2)

# --- Price Distribution Plot ---
with plot_col1:
    st.subheader("Price Distribution")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.histplot(df[df['realSum'] < 1000]['realSum'], kde=True, color=ORANGE, bins=30, ax=ax1)
    
    ax1.set_title('Price Distribution', color=ORANGE, fontsize=18, fontweight='bold', pad=20)
    ax1.set_xlabel('Price ($)', color='white', fontsize=12)
    ax1.set_ylabel('Frequency', color='white', fontsize=12)
    
    ax1.tick_params(axis='x', colors='lightgrey', labelsize=10)
    ax1.tick_params(axis='y', colors='lightgrey', labelsize=10)
    
    sns.despine()
    st.pyplot(fig1)

# --- Price by Country Plot ---
with plot_col2:
    st.subheader("Country Price Analysis")

    available_countries = sorted(df['Country'].unique())
    selected_country = st.selectbox("Select a Country to view price range:", options=available_countries)

    country_filtered_df = df[(df['Country'] == selected_country) & (df['realSum'] < 800)]

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    
    sns.boxplot(x='Country', y='realSum', data=country_filtered_df, color=ORANGE, ax=ax2)
    
    ax2.set_title(f'Price Distribution: {selected_country}', color=ORANGE, fontsize=16, fontweight='bold', pad=20)
    ax2.set_xlabel('Selected Country', color='white', fontsize=12)
    ax2.set_ylabel('Price ($)', color='white', fontsize=12)
    
    ax2.tick_params(axis='x', colors='white', labelsize=11)
    ax2.tick_params(axis='y', colors='white')
    
    ax2.set_facecolor('#1B1B1B')
    fig2.patch.set_facecolor('#1B1B1B')
    
    sns.despine()
    plt.tight_layout()
    
    st.pyplot(fig2)

# --- Correlation Matrix ---
st.subheader("Features Correlation Matrix")

fig, ax = plt.subplots(figsize=(10, 8)) 

corr_matrix = df.corr(numeric_only=True)

cmap_orange = LinearSegmentedColormap.from_list("BlackOrange", [BLACK, ORANGE, "white"])

sns.heatmap(
    corr_matrix, 
    annot=True,          
    fmt=".2f",           
    cmap=cmap_orange,
    linewidths=1, 
    linecolor=BLACK, 
    ax=ax,               
    annot_kws={"size": 10} 
)

plt.xticks(rotation=45, ha='right', color='white')
plt.yticks(rotation=0, color='white')

ax.set_title('Feature Correlation', color=ORANGE, fontweight='bold', fontsize=20, pad=20)

plt.tight_layout()

st.pyplot(fig)

# ------------------------------------------
plot_col1, plot_col2 = st.columns(2)

# --- Does Distance to Center Kill the Price? ---
with plot_col1:
    st.subheader("Does Distance to Center Kill the Price?")
    sns.set_theme(style="darkgrid", rc={"axes.facecolor": BLACK, "figure.facecolor": BLACK, "text.color": "white", "axes.labelcolor": "white", "xtick.color": "white", "ytick.color": "white"})

    fig, ax = plt.subplots(figsize=(10, 8)) 

    sns.regplot(x='city centre Distance', y='realSum', data=df.sample(2000), 
                scatter_kws={'alpha':0.3, 'color': ORANGE}, 
                line_kws={'color': 'white'})


    ax.set_title('Does Distance to Center Kill the Price?', color=ORANGE, fontweight='bold', fontsize=20, pad=20)
    ax.set_xlabel('Distance to City Center (km)', color='white', fontsize=12)
    ax.set_ylabel('Price (Euro)', color='white', fontsize=12)
    plt.tight_layout()

    st.pyplot(fig)

# --- Mutli vs Single Percentages ---
with plot_col2:
    st.subheader("Mutli vs Single Percentages")
    multi_counts = df['multi'].value_counts().sort_index()
    labels = ['Single', 'Multi']

    fig, ax = plt.subplots(figsize=(8, 6))

    fig.patch.set_facecolor("#000000") 
    ax.set_facecolor('#000000')

    wedges, texts, autotexts = ax.pie(
        multi_counts, 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=['#666666', ORANGE],       # Grey for Single, Orange for Multi
        pctdistance=0.82,                 # Position of the percentage labels
        explode=[0.05, 0.05],             # Gap between slices
        textprops={'color': 'white', 'fontsize': 12, 'weight': 'bold'},
        wedgeprops={'width': 0.3, 'edgecolor': '#1B1B1B', 'linewidth': 3} # Donut hole
    )

    for text in texts:
        text.set_color('white')
        text.set_fontsize(13)
        text.set_weight('bold')

    total_listings = multi_counts.sum() 
    ax.text(0, 0, f'TOTAL\n{total_listings:,}', ha='center', va='center', 
            color='white', fontsize=15, fontweight='bold')

    ax.set_title('Multi-listing Distribution', color=ORANGE, fontsize=18, pad=20)
    plt.tight_layout()

    st.pyplot(fig)


# ------------------------------------------
plot_col1, plot_col2 = st.columns(2)

with plot_col1:
    st.subheader("City Identity: Culture Capital vs. Foodie Heaven")
    fig, ax = plt.subplots(figsize=(10, 8))
    city_indices = df.groupby('City')[['attr_index', 'rest_index']].mean().reset_index()

    city_indices_melted = city_indices.melt(id_vars='City', var_name='Index_Type', value_name='Score')

    sns.barplot(
        x='City', 
        y='Score', 
        hue='Index_Type', 
        data=city_indices_melted, 
        palette=[ORANGE, 'grey']
    )

    ax.set_xlabel('City', color='white')
    ax.set_ylabel('Average Index Score', color='white')
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')

    legend = plt.legend(title='Index Type', facecolor='black', labelcolor='white')
    plt.setp(legend.get_title(), color='white')

    sns.despine()
    st.pyplot(fig)

with plot_col2:
    st.subheader('Attraction vs. Restaurant Dominance')

    available_cities = sorted(df['City'].unique())
    selected_city = st.selectbox("Select a City to analyze:", options=available_cities)

    city_indices = df.groupby('City')[['attr_index', 'rest_index']].mean()
    
    city_data = city_indices.loc[[selected_city]]

    fig, ax = plt.subplots(figsize=(6, 4)) # Adjusted size for a single bar
    
    city_data.plot(kind='bar', stacked=True, color=[ORANGE, 'grey'], ax=ax, width=0.5)

    for container in ax.containers:

        height = container.datavalues[0]
        total = city_data.sum(axis=1).values[0]
        percentage = (height / total) * 100
        
        label = f'{height:.1f}\n({percentage:.0f}%)'
        
        ax.bar_label(container, labels=[label], label_type='center', 
                     color='white', fontweight='bold', fontsize=12)

    ax.set_title(f'Attraction vs. Restaurant dominance in {selected_city}', color=ORANGE, fontsize=18, fontweight='bold', pad=20)
    ax.set_ylabel('Index Score', color='white', fontsize=12)
    
    plt.xticks(rotation=0, color='white', fontsize=14) 
    plt.yticks(color='white')
    
    ax.yaxis.set_visible(False)
    
    legend = ax.legend(title='Index Type', facecolor='black', edgecolor='white', loc='upper right')
    plt.setp(legend.get_title(), color='white')
    for text in legend.get_texts():
        text.set_color("white")

    ax.set_facecolor("#000000")
    fig.patch.set_facecolor('#000000')

    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    
    st.pyplot(fig)


#----------------------------------------
plot_col1, plot_col2 = st.columns(2)

with plot_col1:
    st.subheader("Do Tourists Pay More for Sights or Food?")
    fig, ax = plt.subplots(figsize=(8, 6))

    subset = df[df['realSum'] < 800]
    sns.regplot(x='attr_index', y='realSum', data=subset, 
                scatter=False, label='Attraction Index Effect', color=ORANGE)

    sns.regplot(x='rest_index', y='realSum', data=subset, 
                scatter=False, label='Restaurant Index Effect', color='white', line_kws={'linestyle':'--'})

    ax.set_xlabel('Index Score', color='white')
    ax.set_ylabel('Price (Euro)', color='white')
    ax.legend(facecolor='black', labelcolor='white')
    ax.grid(True, alpha=0.1)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    
    st.pyplot(fig)

#---Which cities are oversaturated with 'Shared Rooms' and
#   where do we need more 'Entire Homes'?---
with plot_col2:
    st.subheader('Market Supply: Room Type Distribution by City')
    fig, ax = plt.subplots(figsize=(8, 6))

    order = df['City'].value_counts().index
    sns.countplot(x='City', hue='room_type', data=df, order=order, palette=[ORANGE, 'grey', 'white'])
    
    ax.set_xlabel('City', color='white')
    ax.set_ylabel('Number of Listings', color='white')
    ax.legend(title='Room Type')
    plt.xticks(rotation=45, color='white')
    plt.yticks(color='white')
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    
    st.pyplot(fig)





plot1, plot2 = st.columns(2)

# --- 'Does High Price = High Satisfaction?' ---
with plot1:
    st.subheader('Does High Price = High Satisfaction?')
    guest_data = df[df['realSum'] < 400]

    fig, ax = plt.subplots(figsize=(8, 6))
    
    sns.regplot(
        x='realSum', 
        y='guest_satisfaction_overall', 
        data=guest_data,
        scatter_kws={'alpha': 0.1, 'color': 'grey'},
        line_kws={'color': ORANGE},
        ax=ax  
    )
    
    ax.set_ylabel('Guest Satisfaction (0-100)', color='white')
    ax.set_xlabel('Price Paid', color='white')
    ax.set_ylim(60, 105) 
    
    ax.set_facecolor('#1B1B1B')
    fig.patch.set_facecolor('#1B1B1B')
    
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    
    st.pyplot(fig)

# --- 'Cleanliness vs. Satisfaction' ---
with plot2:
    st.subheader('Cleanliness vs. Satisfaction')
    
    df['Quality_Ratio'] = df['guest_satisfaction_overall'] / (df['cleanliness_rating'] * 10)
    bubble_data = df.groupby(['cleanliness_rating', 'guest_satisfaction_overall']).agg(
        count=('realSum', 'count'),
        quality_ratio=('Quality_Ratio', 'mean')
    ).reset_index()
    bubble_data = bubble_data[bubble_data['count'] > 5]

    fig, ax = plt.subplots(figsize=(8, 6))

    sns.scatterplot(
        data=bubble_data, 
        x='cleanliness_rating', 
        y='guest_satisfaction_overall', 
        size='count', 
        hue='quality_ratio',
        sizes=(20, 1000), 
        palette='inferno', 
        alpha=0.7,
        edgecolor='white',
        legend='brief',
        ax=ax 
    )
    
    sns.regplot(
        data=df, 
        x='cleanliness_rating', 
        y='guest_satisfaction_overall',
        scatter=False,      
        color='white',      
        line_kws={'linewidth': 3, 'linestyle': '--'},
        ax=ax 
    )   

    ax.set_ylabel('Overall Satisfaction (0-100)', color='white')
    ax.set_xlabel('Cleanliness Rating (2-10)', color='white')
    
    legend = ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., 
                       title='Size & Charm', facecolor='black', labelcolor='white')
    plt.setp(legend.get_title(), color='white')

    ax.set_facecolor('#1B1B1B')
    fig.patch.set_facecolor('#1B1B1B')
    ax.grid(True, alpha=0.1)
    
    plt.tight_layout()
    st.pyplot(fig)

    _ = """
    plot1, plot2 = st.columns(2)
    # --- Average Price by Location (Nearness to Metro)---
    with plot1:
        conditions = [
        (df['metro Distance'] <= 0.5),
        (df['metro Distance'] > 0.5) & (df['metro Distance'] <= 2.0),
        (df['metro Distance'] > 2.0)
        ]
        choices = ['Prime Location', 'Walkable', 'Remote']

        df['Distance_Score'] = np.select(conditions, choices, default='Remote')
        fig, ax = plt.subplots(figsize= (8,6))
        order = ['Prime Location', 'Walkable', 'Remote']

        ax = sns.barplot(
            x='Distance_Score', 
            y='realSum', 
            data=df, 
            order=order, 
            palette=['#FF9F1C', 'grey', 'white'],
        )

        for i in ax.containers:
            ax.bar_label(i, fmt='%.0f', color='white', padding=3, fontweight='bold')

            
        ax.set_title('Average Price by Location (Nearness to Metro)', color=ORANGE, fontsize=16)
        ax.set_ylabel('Average Price', color='white')
        ax.set_xlabel('Proximity to Metro', color='white')
        plt.xticks(color='white')
        plt.yticks(color='white')
        sns.despine(left=True, bottom=True)
        plt.tight_layout()
        
        st.pyplot(fig)

    # ----The Density Effect: Does Competition Lower Prices? ---
    coords = np.radians(df[['lat', 'lng']].values)
    tree = BallTree(coords, metric='haversine')
    radius = 0.5 / 6371

    # عدد الجيران في دايرة 500 متر
    df['Density_500m'] = tree.query_radius(coords, r=radius, count_only=True)

    df['Density_500m'] = df['Density_500m'] - 1

    with plot2:
        subset = df[df['realSum'] < 800]

        sns.regplot(
            x='Density_500m', 
            y='realSum', 
            data=subset, 
            scatter_kws={'alpha': 0.3, 'color': 'grey', 's': 10},
            line_kws={'color': ORANGE, 'linewidth': 3}            
        )

        fig,ax = sns.subplots(figsize = (8,6))
        sns.subheader('The Density Effect: Does Competition Lower Prices?')
        ax.set_ylabel('Average Price', color='white')
        ax.set_xlabel('Proximity to Metro', color='white')
        ax.grid(True, alpha=0.1)
        sns.despine(left=True, bottom=True)
        plt.tight_layout()
        
        st.pyplot(fig)


    # --- ----
    with plot2:
        df['Density_Bin'] = pd.cut(df['Density_500m'], bins=10)

        sns.lineplot(
            x='Density_500m', 
            y='guest_satisfaction_overall', 
            data=df, 
            color=ORANGE,
            errorbar=None 
        )

        fig,ax = sns.subplots(figsize = (8,6))
        sns.subheader('Are Crowded Areas Rated Lower?')
        ax.set_ylabel('Average Guest Satisfaction', color='white')
        ax.set_xlabel('Neighborhood Density', color='white')
        ax.grid(True, alpha=0.1)
        sns.despine(left=True, bottom=True)
        plt.tight_layout()
        
        st.pyplot(fig)

    """
