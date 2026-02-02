# EuroStay Insights: An End-to-End Data Analysis Pipeline
## Project Overview
This project was developed during a 4-day intensive Data Analysis Hackathon hosted by Instant Software Solutions in collaboration with Orange Egypt.

The goal was to move beyond static datasets by enriching the "Airbnb Prices in European Cities" dataset with real-time external data. We built a full-scale pipeline that handles everything from raw web scraping to relational database architecture and interactive business intelligence dashboards.

## Technical Workflow
### Phase 1: Data Acquisition & Enrichment
**Web Scraping:** Developed a custom crawler using **Python & Selenium** to extract hotel details, room types, and amenities from Booking.com across major European cities.

**Data Cleaning:** Leveraged Pandas to handle missing values, normalize pricing currencies, and sanitize text data (removing hidden characters and newlines).

### Phase 2: Database Engineering
**Relational Modeling:** Designed a comprehensive **Entity Relationship Diagram (ERD)** to structure the relationship between Airbnb listings and Booking.com hotel data.

**SQL Architecture:** Implemented a structured schema with primary/foreign key constraints. Used **CTEs** and **Views** to create complex analytical joins for deeper insights.

### Phase 3: Analytics & Visualization
**Interactive Web App:** Built a **Streamlit** dashboard featuring a "Dark Theme" UI, allowing users to filter data by city and explore correlations between price, cleanliness, and satisfaction.

**Business Intelligence:** Developed **Power BI** reports to track high-level KPIs and answer critical business questions regarding market dominance and price-to-quality ratios.

<img width="1154" height="664" alt="image" src="https://github.com/user-attachments/assets/571bfb99-86cd-4b69-a662-d4c8ed665dd2" />

## Tech Stack
**Languages:** Python (Pandas, Selenium, Matplotlib, Seaborn), SQL

**Tools:** Streamlit, Power BI, SQL Server/PostgreSQL

**Design:** Lucidchart (ERD)

## Key Business Questions Answered
- Does a higher price point guarantee higher guest satisfaction across European markets?

- What is the ratio of "Attraction Dominance" vs. "Restaurant Dominance" in major tourist hubs?

- How does cleanliness rating directly impact the overall "Quality Ratio" of a listing?
