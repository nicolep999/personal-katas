ALTER TABLE countries_rivers
    ADD CONSTRAINT fk_countries_rivers_river_id FOREIGN KEY (river_id)
    REFERENCES rivers (id) ON UPDATE CASCADE;

ALTER TABLE countries_rivers
    ADD CONSTRAINT fk_country_code_rivers FOREIGN KEY (country_code)
    REFERENCES countries (country_code) ON UPDATE CASCADE;
