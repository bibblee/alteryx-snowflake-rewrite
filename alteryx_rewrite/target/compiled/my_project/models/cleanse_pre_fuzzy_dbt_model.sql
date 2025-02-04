

SELECT
    "Account CSN",
    "Account UUID",
    "Clearance Reason",
    "Country Name",
    "Lead Number",
    "Opportunity Close Date",
    "Opportunity Number",
    "Opportunity Owner",
    "Opportunity Stage",
    "Parent CSN",
    "SFDC Lead CreatedDate",
    "SFDC Lead LastActivityDate",
    "SFDC Lead Status",
    "SFDC Lead Status Reason",
    "SFDC Licence Compliance Flag",
    "SFDC Oppty CreatedDate",
    "SFDC Oppty LastActivityDate",
    "Parent Name",
    "Site Name",
    UPPER(REGEXP_REPLACE("Parent Name", '[^a-zA-Z0-9_ ]', '')) AS "Parent Account Name Cleansed",
    UPPER(REGEXP_REPLACE("Site Name", '[^a-zA-Z0-9_ ]', '')) AS "Site Name Cleansed"
FROM SOURCES_FOR_FUZZY