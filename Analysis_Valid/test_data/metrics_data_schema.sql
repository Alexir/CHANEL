-- [20201014] (air) Data layout for Metrics AMT collections
--
--     should suffice for Validity and subsequent metrics
--     built for the data in: CHANEL/ChatEval-AMT-Interface/data/original
--     note that this blows away any existing table
--


CREATE TABLE IF NOT EXISTS Validity (

       item_id     text NOT NULL PRIMARY KEY,
       participant text NOT NULL,
       turn        text NOT NULL

);


CREATE TABLE IF NOT EXISTS Session (

       HITId       text NOT NULL,
       WorkerId    text NOT NULL,
       AssignID    text NOT NULL,
       AcceptTime  text NOT NULL,
       SubmitTime  text NOT NULL,
       Duration    text NOT NULL,
       Catch       text,
       Comment     text
);

--
--
