SELECT 'ids_aka_name       ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_aka_name       UNION ALL
SELECT 'ids_aka_title      ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_aka_title      UNION ALL
SELECT 'ids_cast_info      ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_cast_info      UNION ALL
SELECT 'ids_char_name      ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_char_name      UNION ALL
SELECT 'ids_company_name   ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_company_name   UNION ALL
SELECT 'ids_complete_cast  ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_complete_cast  UNION ALL
SELECT 'ids_keyword        ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_keyword        UNION ALL
SELECT 'ids_movie_companies' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_movie_companies UNION ALL
SELECT 'ids_movie_info     ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_movie_info     UNION ALL
SELECT 'ids_movie_info_idx ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_movie_info_idx UNION ALL
SELECT 'ids_movie_keyword  ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_movie_keyword  UNION ALL
SELECT 'ids_movie_link     ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_movie_link     UNION ALL
SELECT 'ids_name           ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_name           UNION ALL
SELECT 'ids_person_info    ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_person_info    UNION ALL
SELECT 'ids_title          ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_title          ;



COPY (SELECT * FROM aka_name         where id in (select id from ids_aka_name       )) TO '/Users/hannes/source/join-order-benchmark/data-stripped/aka_name.csv'        CSV DELIMITER ',' ESCAPE '\';
COPY (SELECT * FROM aka_title        where id in (select id from ids_aka_title      )) TO '/Users/hannes/source/join-order-benchmark/data-stripped/aka_title.csv'       CSV DELIMITER ',' ESCAPE '\';
COPY (SELECT * FROM cast_info        where id in (select id from ids_cast_info      )) TO '/Users/hannes/source/join-order-benchmark/data-stripped/cast_info.csv'       CSV DELIMITER ',' ESCAPE '\';
COPY (SELECT * FROM char_name        where id in (select id from ids_char_name      )) TO '/Users/hannes/source/join-order-benchmark/data-stripped/char_name.csv'       CSV DELIMITER ',' ESCAPE '\';
COPY (SELECT * FROM company_name     where id in (select id from ids_company_name   )) TO '/Users/hannes/source/join-order-benchmark/data-stripped/company_name.csv'    CSV DELIMITER ',' ESCAPE '\';
COPY (SELECT * FROM complete_cast    where id in (select id from ids_complete_cast  )) TO '/Users/hannes/source/join-order-benchmark/data-stripped/complete_cast.csv'   CSV DELIMITER ',' ESCAPE '\';
COPY (SELECT * FROM keyword          where id in (select id from ids_keyword        )) TO '/Users/hannes/source/join-order-benchmark/data-stripped/keyword.csv'         CSV DELIMITER ',' ESCAPE '\';
COPY (SELECT * FROM movie_companies  where id in (select id from ids_movie_companies)) TO '/Users/hannes/source/join-order-benchmark/data-stripped/movie_companies.csv' CSV DELIMITER ',' ESCAPE '\';
COPY (SELECT * FROM movie_info       where id in (select id from ids_movie_info     )) TO '/Users/hannes/source/join-order-benchmark/data-stripped/movie_info.csv'      CSV DELIMITER ',' ESCAPE '\';
COPY (SELECT * FROM movie_info_idx   where id in (select id from ids_movie_info_idx )) TO '/Users/hannes/source/join-order-benchmark/data-stripped/movie_info_idx.csv'  CSV DELIMITER ',' ESCAPE '\';
COPY (SELECT * FROM movie_keyword    where id in (select id from ids_movie_keyword  )) TO '/Users/hannes/source/join-order-benchmark/data-stripped/movie_keyword.csv'   CSV DELIMITER ',' ESCAPE '\';
COPY (SELECT * FROM movie_link       where id in (select id from ids_movie_link     )) TO '/Users/hannes/source/join-order-benchmark/data-stripped/movie_link.csv'      CSV DELIMITER ',' ESCAPE '\';
COPY (SELECT * FROM name             where id in (select id from ids_name           )) TO '/Users/hannes/source/join-order-benchmark/data-stripped/name.csv'            CSV DELIMITER ',' ESCAPE '\';
COPY (SELECT * FROM person_info      where id in (select id from ids_person_info    )) TO '/Users/hannes/source/join-order-benchmark/data-stripped/person_info.csv'     CSV DELIMITER ',' ESCAPE '\';
COPY (SELECT * FROM title            where id in (select id from ids_title          )) TO '/Users/hannes/source/join-order-benchmark/data-stripped/title.csv'           CSV DELIMITER ',' ESCAPE '\';


