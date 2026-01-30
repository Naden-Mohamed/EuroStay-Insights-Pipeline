
BULK INSERT Location
FROM 'D:\Orange\Hotel\Location.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);

BULK INSERT Airbnb_Location
FROM 'D:\Orange\Airbnb\AirbnbLoc_1.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);

BULK INSERT Hotel
FROM 'D:\Orange\Hotel\hotel_final.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);

BULK INSERT Attraction
FROM 'D:\Orange\Hotel\Attraction.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);

BULK INSERT HotelAttraction
FROM 'D:\Orange\Hotel\Hotel_Attraction.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);

BULK INSERT Facility
FROM 'D:\Orange\Hotel\Facility.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);


BULK INSERT HotelFac
FROM 'D:\Orange\Hotel\HotelFac.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);


BULK INSERT PublicTransport
FROM 'D:\Orange\Hotel\PublicTransport.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);

BULK INSERT HotelTransport
FROM 'D:\Orange\Hotel\HotelTransport.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);

BULK INSERT Resturant
FROM 'D:\Orange\Hotel\Resturant.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);

BULK INSERT HotelResturant
FROM 'D:\Orange\Hotel\Hotel_Resturant.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);

BULK INSERT Airport
FROM 'D:\Orange\Hotel\Airport.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);

BULK INSERT HotelAirport
FROM 'D:\Orange\Hotel\HotelAirport.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);

BULK INSERT Languages
FROM 'D:\Orange\Hotel\Language.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);

BULK INSERT LanguageSpoken
FROM 'D:\Orange\Hotel\LanguageSpoken .csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);

BULK INSERT Airbnb_Rating
FROM 'D:\Orange\Airbnb\AirbnbRate.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);


BULK INSERT ListRoom
FROM 'D:\Orange\Airbnb\ListRooms.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);


BULK INSERT Host
FROM 'D:\Orange\Airbnb\Host.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);

BULK INSERT Host
FROM 'D:\Orange\Airbnb\Host.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);


BULK INSERT Airbnb_List_Fact
FROM 'D:\Orange\Airbnb\AirbnbFact.csv'
WITH (
    FIRSTROW = 2, 
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n',  
    CODEPAGE = '65001',    
    TABLOCK
);
