-- Active: 1664349630889@@192.168.1.168@3306@Principale
CREATE TABLE ShortRangeRadar(  

    TIMED VARCHAR(255) NOT NULL,
    INDEXD int,
    HeartRate FLOAT(15),
    HR_Quality BOOL,
    RespirationRate FLOAT(15),
    RR_Quality BOOL,
    IE FLOAT(15),
    RAbin INT,
    STATED VARCHAR(255)
) COMMENT '';

ALTER TABLE ShortRangeRadar
ADD CONSTRAINT pk_sales PRIMARY KEY(TIMED, INDEXD);