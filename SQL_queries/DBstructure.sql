
CREATE DATABASE OrangeDB
 Use OrangeDB

 CREATE TABLE location (
    LOC1_ID INT PRIMARY KEY,
	city VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    UNIQUE (Country, City)
);

CREATE TABLE Airbnb_Location (
    [city centre Distance] DECIMAL(6,2) CHECK ( [city centre Distance] >= 0),
	[metro Distance] DECIMAL(6,2) CHECK ( [metro Distance] >= 0),
	lng DECIMAL(9,6) ,
	lat DECIMAL(9,6) ,
    LOC1_ID INT ,
    FOREIGN KEY (LOC1_ID)
        REFERENCES location(LOC1_ID)
        ON DELETE CASCADE
);


CREATE TABLE Hotel (
    ID INT PRIMARY KEY,
    hotel_name VARCHAR(150) NOT NULL,
	Rating DECIMAL(2,2),
    Check_in nvarchar (20),
    Check_out nvarchar (20),
    Pets_allowance TINYINT NOT NULL,
    LOC1_ID INT NOT NULL,
    FOREIGN KEY (LOC1_ID)
        REFERENCES location(LOC1_ID)
        ON DELETE CASCADE
);

CREATE TABLE Attraction (
    ID INT PRIMARY KEY,
    Name VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE HotelAttraction (
    ID INT,
    AttractionID INT ,
    PRIMARY KEY (AttractionID, ID),
    FOREIGN KEY (AttractionID) REFERENCES Hotel(ID) ON DELETE CASCADE,
    FOREIGN KEY (ID) REFERENCES Attraction(ID) ON DELETE CASCADE
);


CREATE TABLE Facility(
	FacID INT PRIMARY KEY,
    fACilites VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE HotelFac (
    HotelID INT,
    FacID INT,
    PRIMARY KEY (HotelID, FacID),
    FOREIGN KEY (HotelID) REFERENCES Hotel(ID) ON DELETE CASCADE,
    FOREIGN KEY (FacID) REFERENCES Facility(FacID) ON DELETE CASCADE
);

CREATE TABLE PublicTransport (
    TransID INT PRIMARY KEY,
    Public_transit VARCHAR(150) NOT NULL UNIQUE,
	Distance_meter int 
);

CREATE TABLE HotelTransport (
    HotelID INT,
    PublicTransport_TransID INT,
    PRIMARY KEY (HotelID, PublicTransport_TransID),
    FOREIGN KEY (HotelID) REFERENCES Hotel(ID) ON DELETE CASCADE,
    FOREIGN KEY (PublicTransport_TransID) REFERENCES Transportation(ID) ON DELETE CASCADE
);

CREATE TABLE Resturant (
    RestID INT PRIMARY KEY,
    Resturants_cafes VARCHAR(150) NOT NULL UNIQUE,
	Distance_meter int

);
CREATE TABLE HotelResturant (
    HotelID INT,
    Resturant_RestID INT,
    PRIMARY KEY (HotelID, Resturant_RestID),
    FOREIGN KEY (HotelID) REFERENCES Hotel(ID) ON DELETE CASCADE,
    FOREIGN KEY (Resturant_RestID) REFERENCES Resturant(RestID) ON DELETE CASCADE
);

CREATE TABLE Airport (
    AirportID INT PRIMARY KEY,
    Closed_Airports VARCHAR(150) NOT NULL UNIQUE,
	Distance_KM int
);

CREATE TABLE HotelAirport (
    HotelID INT,
    Airport_AirportID INT,
    PRIMARY KEY (HotelID, Airport_AirportID),
    FOREIGN KEY (HotelID) REFERENCES Hotel(ID) ON DELETE CASCADE,
    FOREIGN KEY (Airport_AirportID) REFERENCES Airport(AirportID) ON DELETE CASCADE
);

CREATE TABLE Languages (
    LangID INT PRIMARY KEY,
    Lang_Spoken VARCHAR(100) NOT NULL UNIQUE
);
CREATE TABLE LanguageSpoken (
    ID INT,
    Language_LangID INT,
    PRIMARY KEY (ID, Language_LangID),
    FOREIGN KEY (ID) REFERENCES Hotel(ID) ON DELETE CASCADE,
    FOREIGN KEY (Language_LangID) REFERENCES Languages(LangID) ON DELETE CASCADE
);




