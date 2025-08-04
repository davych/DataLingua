-- Artist definition

CREATE TABLE [Artist]
(
    [ArtistId] INTEGER  NOT NULL, -- Unique ID for each artist
    [Name] NVARCHAR(120),         -- Name of the artist
    CONSTRAINT [PK_Artist] PRIMARY KEY  ([ArtistId])
);


-- Genre definition

CREATE TABLE [Genre]
(
    [GenreId] INTEGER  NOT NULL, -- Unique ID for each genre
    [Name] NVARCHAR(120),        -- Name of the genre
    CONSTRAINT [PK_Genre] PRIMARY KEY  ([GenreId])
);


-- MediaType definition

CREATE TABLE [MediaType]
(
    [MediaTypeId] INTEGER  NOT NULL, -- Unique ID for each media type
    [Name] NVARCHAR(120),           -- Name of the media type
    CONSTRAINT [PK_MediaType] PRIMARY KEY  ([MediaTypeId])
);


-- Playlist definition

CREATE TABLE [Playlist]
(
    [PlaylistId] INTEGER  NOT NULL, -- Unique ID for each playlist
    [Name] NVARCHAR(120),           -- Name of the playlist
    CONSTRAINT [PK_Playlist] PRIMARY KEY  ([PlaylistId])
);


-- Album definition

CREATE TABLE [Album]
(
    [AlbumId] INTEGER  NOT NULL,      -- Unique ID for each album
    [Title] NVARCHAR(160)  NOT NULL,  -- Title of the album
    [ArtistId] INTEGER  NOT NULL,     -- ID of the artist (foreign key)
    CONSTRAINT [PK_Album] PRIMARY KEY  ([AlbumId]),
    FOREIGN KEY ([ArtistId]) REFERENCES [Artist] ([ArtistId]) 
    ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE INDEX [IFK_AlbumArtistId] ON [Album] ([ArtistId]);


-- Employee definition

CREATE TABLE [Employee]
(
    [EmployeeId] INTEGER  NOT NULL,    -- Unique ID for each employee
    [LastName] NVARCHAR(20)  NOT NULL, -- Last name of the employee
    [FirstName] NVARCHAR(20)  NOT NULL,-- First name of the employee
    [Title] NVARCHAR(30),              -- Job title
    [ReportsTo] INTEGER,               -- Manager's employee ID
    [BirthDate] DATETIME,              -- Date of birth
    [HireDate] DATETIME,               -- Date of hire
    [Address] NVARCHAR(70),            -- Address
    [City] NVARCHAR(40),               -- City
    [State] NVARCHAR(40),              -- State or province
    [Country] NVARCHAR(40),            -- Country
    [PostalCode] NVARCHAR(10),         -- Postal code
    [Phone] NVARCHAR(24),              -- Phone number
    [Fax] NVARCHAR(24),                -- Fax number
    [Email] NVARCHAR(60),              -- Email address
    CONSTRAINT [PK_Employee] PRIMARY KEY  ([EmployeeId]),
    FOREIGN KEY ([ReportsTo]) REFERENCES [Employee] ([EmployeeId]) 
    ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE INDEX [IFK_EmployeeReportsTo] ON [Employee] ([ReportsTo]);


-- Track definition

CREATE TABLE [Track]
(
    [TrackId] INTEGER  NOT NULL,         -- Unique ID for each track
    [Name] NVARCHAR(200)  NOT NULL,      -- Name of the track
    [AlbumId] INTEGER,                   -- Album ID (foreign key)
    [MediaTypeId] INTEGER  NOT NULL,     -- Media type ID (foreign key)
    [GenreId] INTEGER,                   -- Genre ID (foreign key)
    [Composer] NVARCHAR(220),            -- Composer of the track
    [Milliseconds] INTEGER  NOT NULL,    -- Duration in milliseconds
    [Bytes] INTEGER,                     -- File size in bytes
    [UnitPrice] NUMERIC(10,2)  NOT NULL, -- Price per unit
    CONSTRAINT [PK_Track] PRIMARY KEY  ([TrackId]),
    FOREIGN KEY ([AlbumId]) REFERENCES [Album] ([AlbumId]) 
    ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([GenreId]) REFERENCES [Genre] ([GenreId]) 
    ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([MediaTypeId]) REFERENCES [MediaType] ([MediaTypeId]) 
    ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE INDEX [IFK_TrackAlbumId] ON [Track] ([AlbumId]);
CREATE INDEX [IFK_TrackGenreId] ON [Track] ([GenreId]);
CREATE INDEX [IFK_TrackMediaTypeId] ON [Track] ([MediaTypeId]);


-- Customer definition

CREATE TABLE [Customer]
(
    [CustomerId] INTEGER  NOT NULL,      -- Unique ID for each customer
    [FirstName] NVARCHAR(40)  NOT NULL,  -- First name of the customer
    [LastName] NVARCHAR(20)  NOT NULL,   -- Last name of the customer
    [Company] NVARCHAR(80),              -- Company name
    [Address] NVARCHAR(70),              -- Address
    [City] NVARCHAR(40),                 -- City
    [State] NVARCHAR(40),                -- State or province
    [Country] NVARCHAR(40),              -- Country
    [PostalCode] NVARCHAR(10),           -- Postal code
    [Phone] NVARCHAR(24),                -- Phone number
    [Fax] NVARCHAR(24),                  -- Fax number
    [Email] NVARCHAR(60)  NOT NULL,      -- Email address
    [SupportRepId] INTEGER,              -- Employee ID of support representative (foreign key)
    CONSTRAINT [PK_Customer] PRIMARY KEY  ([CustomerId]),
    FOREIGN KEY ([SupportRepId]) REFERENCES [Employee] ([EmployeeId]) 
    ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE INDEX [IFK_CustomerSupportRepId] ON [Customer] ([SupportRepId]);


-- Invoice definition

CREATE TABLE [Invoice]
(
    [InvoiceId] INTEGER  NOT NULL,         -- Unique ID for each invoice
    [CustomerId] INTEGER  NOT NULL,        -- Customer ID (foreign key)
    [InvoiceDate] DATETIME  NOT NULL,      -- Date of the invoice
    [BillingAddress] NVARCHAR(70),         -- Billing address
    [BillingCity] NVARCHAR(40),            -- Billing city
    [BillingState] NVARCHAR(40),           -- Billing state or province
    [BillingCountry] NVARCHAR(40),         -- Billing country
    [BillingPostalCode] NVARCHAR(10),      -- Billing postal code
    [Total] NUMERIC(10,2)  NOT NULL,       -- Total amount
    CONSTRAINT [PK_Invoice] PRIMARY KEY  ([InvoiceId]),
    FOREIGN KEY ([CustomerId]) REFERENCES [Customer] ([CustomerId]) 
    ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE INDEX [IFK_InvoiceCustomerId] ON [Invoice] ([CustomerId]);


-- InvoiceLine definition

CREATE TABLE [InvoiceLine]
(
    [InvoiceLineId] INTEGER  NOT NULL,      -- Unique ID for each invoice line
    [InvoiceId] INTEGER  NOT NULL,          -- Invoice ID (foreign key)
    [TrackId] INTEGER  NOT NULL,            -- Track ID (foreign key)
    [UnitPrice] NUMERIC(10,2)  NOT NULL,    -- Price per unit
    [Quantity] INTEGER  NOT NULL,           -- Quantity sold
    CONSTRAINT [PK_InvoiceLine] PRIMARY KEY  ([InvoiceLineId]),
    FOREIGN KEY ([InvoiceId]) REFERENCES [Invoice] ([InvoiceId]) 
    ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([TrackId]) REFERENCES [Track] ([TrackId]) 
    ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE INDEX [IFK_InvoiceLineInvoiceId] ON [InvoiceLine] ([InvoiceId]);
CREATE INDEX [IFK_InvoiceLineTrackId] ON [InvoiceLine] ([TrackId]);


-- PlaylistTrack definition

CREATE TABLE [PlaylistTrack]
(
    [PlaylistId] INTEGER  NOT NULL, -- Playlist ID (foreign key)
    [TrackId] INTEGER  NOT NULL,    -- Track ID (foreign key)
    CONSTRAINT [PK_PlaylistTrack] PRIMARY KEY  ([PlaylistId], [TrackId]),
    FOREIGN KEY ([PlaylistId]) REFERENCES [Playlist] ([PlaylistId]) 
    ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([TrackId]) REFERENCES [Track] ([TrackId]) 
    ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE INDEX [IFK_PlaylistTrackPlaylistId] ON [PlaylistTrack] ([PlaylistId]);
CREATE INDEX [IFK_PlaylistTrackTrackId] ON [PlaylistTrack] ([TrackId]);