ALTER TABLE countries
ADD CONSTRAINT fk_continent_code FOREIGN KEY (continent_code)
    REFERENCES continents (continent_code) ON DELETE CASCADE;

ALTER TABLE countries
ADD CONSTRAINT fk_currency_code FOREIGN KEY (currency_code)
    REFERENCES currencies (currency_code) ON DELETE CASCADE;