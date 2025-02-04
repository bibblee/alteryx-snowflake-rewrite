
  create or replace   view TEST_DATABASE.PUBLIC.extract_dbt_model
  
   as (
    SELECT *
FROM SOURCES_FOR_FUZZY
  );

