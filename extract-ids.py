import sqlparse

def process(sql):
  q = sqlparse.parse(sql)[0]

  mod_q = ''
  seen_from = False
  seen_where = False
  tables = False

  for t in q.tokens:
    if str(t).upper() == 'FROM':
      seen_from = True

    if str(t).upper() == 'WHERE':
      seen_where = True
    
    if seen_from:
      mod_q += str(t)

    if seen_from and not seen_where and isinstance(t, sqlparse.sql.IdentifierList):
      tables = t.get_identifiers()

  for tbl in tables:
    if tbl.get_real_name().lower().endswith('_type'):
      continue
    qq = "INSERT INTO ids_%s SELECT %s.id %s\n" % (tbl.get_real_name(), tbl.get_alias(), mod_q)
    print(qq)


import glob
files = glob.glob("[0-9]*.sql")
files.sort()

for f in files:
  with open(f, 'r') as file:
      print('-- %s' % f)
      data = file.read()
      process(data)


# some schema for ya
# CREATE TABLE IF NOT EXISTS ids_aka_name        (id INTEGER);
# CREATE TABLE IF NOT EXISTS ids_aka_title       (id INTEGER);
# CREATE TABLE IF NOT EXISTS ids_cast_info       (id INTEGER);
# CREATE TABLE IF NOT EXISTS ids_char_name       (id INTEGER);
# CREATE TABLE IF NOT EXISTS ids_company_name    (id INTEGER);
# CREATE TABLE IF NOT EXISTS ids_complete_cast   (id INTEGER);
# CREATE TABLE IF NOT EXISTS ids_keyword         (id INTEGER);
# CREATE TABLE IF NOT EXISTS ids_movie_companies (id INTEGER);
# CREATE TABLE IF NOT EXISTS ids_movie_info      (id INTEGER);
# CREATE TABLE IF NOT EXISTS ids_movie_info_idx  (id INTEGER);
# CREATE TABLE IF NOT EXISTS ids_movie_keyword   (id INTEGER);
# CREATE TABLE IF NOT EXISTS ids_movie_link      (id INTEGER);
# CREATE TABLE IF NOT EXISTS ids_name            (id INTEGER);
# CREATE TABLE IF NOT EXISTS ids_person_info     (id INTEGER);
# CREATE TABLE IF NOT EXISTS ids_title           (id INTEGER);

# DELETE FROM ids_aka_name       ;
# DELETE FROM ids_aka_title      ;
# DELETE FROM ids_cast_info      ;
# DELETE FROM ids_char_name      ;
# DELETE FROM ids_company_name   ;
# DELETE FROM ids_complete_cast  ;
# DELETE FROM ids_keyword        ;
# DELETE FROM ids_movie_companies;
# DELETE FROM ids_movie_info     ;
# DELETE FROM ids_movie_info_idx ;
# DELETE FROM ids_movie_keyword  ;
# DELETE FROM ids_movie_link     ;
# DELETE FROM ids_name           ;
# DELETE FROM ids_person_info    ;
# DELETE FROM ids_title          ;

# SELECT 'ids_aka_name       ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_aka_name       UNION ALL
# SELECT 'ids_aka_title      ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_aka_title      UNION ALL
# SELECT 'ids_cast_info      ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_cast_info      UNION ALL
# SELECT 'ids_char_name      ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_char_name      UNION ALL
# SELECT 'ids_company_name   ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_company_name   UNION ALL
# SELECT 'ids_complete_cast  ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_complete_cast  UNION ALL
# SELECT 'ids_keyword        ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_keyword        UNION ALL
# SELECT 'ids_movie_companies' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_movie_companies UNION ALL
# SELECT 'ids_movie_info     ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_movie_info     UNION ALL
# SELECT 'ids_movie_info_idx ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_movie_info_idx UNION ALL
# SELECT 'ids_movie_keyword  ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_movie_keyword  UNION ALL
# SELECT 'ids_movie_link     ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_movie_link     UNION ALL
# SELECT 'ids_name           ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_name           UNION ALL
# SELECT 'ids_person_info    ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_person_info    UNION ALL
# SELECT 'ids_title          ' AS n, COUNT(*),COUNT(DISTINCT id) FROM ids_title          ;



# COPY (SELECT * FROM aka_name         where id in (select id from ids_aka_name       )) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/aka_name.csv'        CSV DELIMITER ',' ESCAPE '\';
# COPY (SELECT * FROM aka_title        where id in (select id from ids_aka_title      )) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/aka_title.csv'       CSV DELIMITER ',' ESCAPE '\';
# COPY (SELECT * FROM cast_info        where id in (select id from ids_cast_info      )) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/cast_info.csv'       CSV DELIMITER ',' ESCAPE '\';
# COPY (SELECT * FROM char_name        where id in (select id from ids_char_name      )) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/char_name.csv'       CSV DELIMITER ',' ESCAPE '\';
# COPY (SELECT * FROM company_name     where id in (select id from ids_company_name   )) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/company_name.csv'    CSV DELIMITER ',' ESCAPE '\';
# COPY (SELECT * FROM complete_cast    where id in (select id from ids_complete_cast  )) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/complete_cast.csv'   CSV DELIMITER ',' ESCAPE '\';
# COPY (SELECT * FROM keyword          where id in (select id from ids_keyword        )) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/keyword.csv'         CSV DELIMITER ',' ESCAPE '\';
# COPY (SELECT * FROM movie_companies  where id in (select id from ids_movie_companies)) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/movie_companies.csv' CSV DELIMITER ',' ESCAPE '\';
# COPY (SELECT * FROM movie_info       where id in (select id from ids_movie_info     )) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/movie_info.csv'      CSV DELIMITER ',' ESCAPE '\';
# COPY (SELECT * FROM movie_info_idx   where id in (select id from ids_movie_info_idx )) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/movie_info_idx.csv'  CSV DELIMITER ',' ESCAPE '\';
# COPY (SELECT * FROM movie_keyword    where id in (select id from ids_movie_keyword  )) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/movie_keyword.csv'   CSV DELIMITER ',' ESCAPE '\';
# COPY (SELECT * FROM movie_link       where id in (select id from ids_movie_link     )) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/movie_link.csv'      CSV DELIMITER ',' ESCAPE '\';
# COPY (SELECT * FROM name             where id in (select id from ids_name           )) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/name.csv'            CSV DELIMITER ',' ESCAPE '\';
# COPY (SELECT * FROM person_info      where id in (select id from ids_person_info    )) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/person_info.csv'     CSV DELIMITER ',' ESCAPE '\';
# COPY (SELECT * FROM title            where id in (select id from ids_title          )) TO '/export/scratch2/home/hannes/duckdb/third_party/imdb/data_stripped/title.csv'           CSV DELIMITER ',' ESCAPE '\';



