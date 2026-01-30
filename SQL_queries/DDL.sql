CREATE DATABASE OrangeDB

USE OrangeDB

CREATE TABLE location (
    LOC1_ID INT PRIMARY KEY,
	city VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    UNIQUE (Country, City)
); 

CREATE TABLE Airbnb_Location (
    ID INT PRIMARY KEY,
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
    Check_in nvarchar (20),
    Check_out nvarchar (20),
    Rating DECIMAL(4,2),
    LOC1_ID INT NOT NULL,
	Pets_allowance NVARCHAR(10) NOT NULL,
    FOREIGN KEY (LOC1_ID)
        REFERENCES location(LOC1_ID)
        ON DELETE CASCADE
);
drop table Attraction

CREATE TABLE Attraction (
    AttrID INT PRIMARY KEY,
    top_attractions VARCHAR(500) NOT NULL ,
	Distance FLOAT
);

CREATE TABLE HotelAttraction (
    HotelID INT,
    AttractionID INT ,
    PRIMARY KEY (AttractionID, HotelID),
    FOREIGN KEY (AttractionID) REFERENCES Hotel(ID) ON DELETE CASCADE,
    FOREIGN KEY (HotelID) REFERENCES Attraction(AttrID) ON DELETE CASCADE
);

CREATE TABLE Facility(
	FacID INT PRIMARY KEY,
    fACilites VARCHAR(150) NOT NULL 
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
    FOREIGN KEY (PublicTransport_TransID) REFERENCES PublicTransport(TransID) ON DELETE CASCADE
);

CREATE TABLE Resturant (
    RestID INT PRIMARY KEY,
    Resturants_cafes VARCHAR(150) NOT NULL ,
	Distance_meter int

);
CREATE TABLE HotelResturant (
    HotelID INT,
    Resturant_RestID INT,
    PRIMARY KEY (HotelID, Resturant_RestID),
    FOREIGN KEY (HotelID) REFERENCES Hotel(ID) ON DELETE CASCADE,
    FOREIGN KEY (Resturant_RestID) REFERENCES Resturant(RestID) ON DELETE CASCADE
);

DROP TABLE Airport
CREATE TABLE Airport (
    AirportID INT PRIMARY KEY,
    Closed_Airports VARCHAR(150) NOT NULL ,
	Distance_KM Float
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
    Lang_Spoken VARCHAR(100) NOT NULL 
);
CREATE TABLE LanguageSpoken (
    ID INT,
    Language_LangID INT,
    PRIMARY KEY (ID, Language_LangID),
    FOREIGN KEY (ID) REFERENCES Hotel(ID) ON DELETE CASCADE,
    FOREIGN KEY (Language_LangID) REFERENCES Languages(LangID) ON DELETE CASCADE
);


CREATE TABLE Airbnb_Rating (
    cleanliness_rating FLOAT,
    guest_satisfaction_overall FLOAT,
    attr_index FLOAT,
    attr_index_norm FLOAT,
    rest_index FLOAT ,
    rest_index_norm FLOAT ,
	RatintID INT PRIMARY KEY,
);

CREATE TABLE ListRoom (
    ID INT PRIMARY KEY,
	room_type VARCHAR(100) NOT NULL,
	person_capacity INT CHECK (person_capacity > 0),
	Multi Nvarchar(50) NOT NULL,
	biz nvarchar(50) NOT NULL,
    bedrooms INT CHECK (bedrooms >= 0),
);



CREATE TABLE Host (
    HostID INT PRIMARY KEY,
    host_is_suprthost VARCHAR(50) NOT NULL
);



CREATE TABLE Airbnb_List_Fact (
    ID INT PRIMARY KEY,
    realSum FLOAT CHECK (Realsum >= 0),
	Day_Type NVARCHAR(10),
	LocID INT ,
    RateID INT NOT NULL,
    HostID INT NOT NULL,
	ListRoomsID INT NOT NULL,
    FOREIGN KEY (HostID) REFERENCES Host(HostID),
    FOREIGN KEY (RateID) REFERENCES Airbnb_Rating(RatintID),
    FOREIGN KEY (ListRoomsID) REFERENCES ListRoom(ID),
	FOREIGN KEY (LocID) REFERENCES Airbnb_Location(ID),
);
DROP TABLE Airbnb_List_Fact