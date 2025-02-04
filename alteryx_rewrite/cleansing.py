WITH TEST_DATABASE AS (
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
        "Parent Name",
        "SFDC Lead CreatedDate",
        "SFDC Lead LastActivityDate",
        "SFDC Lead Status",
        "SFDC Lead Status Reason",
        "SFDC Licence Compliance Flag",
        "SFDC Oppty CreatedDate",
        "SFDC Oppty LastActivityDate",
        "Site Name"
    FROM SOURCES_FOR_FUZZY
),

cleansed_data AS (
    SELECT
        "Account UUID",
        UPPER(TRIM("Site Name")) AS site_name_cleansed,
        REGEXP_REPLACE(TRIM("Parent Name"), '[^\w\s]', '') AS parent_name_cleansed,
        COUNT(*) AS record_count
    FROM source_data
    GROUP BY "Account UUID", site_name_cleansed, parent_name_cleansed
)

SELECT * FROM cleansed_data;