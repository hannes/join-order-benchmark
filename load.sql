COPY aka_name        FROM '/Users/hannes/source/join-order-benchmark/data-org/aka_name.csv'        WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY aka_title       FROM '/Users/hannes/source/join-order-benchmark/data-org/aka_title.csv'       WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY cast_info       FROM '/Users/hannes/source/join-order-benchmark/data-org/cast_info.csv'       WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY char_name       FROM '/Users/hannes/source/join-order-benchmark/data-org/char_name.csv'       WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY comp_cast_type  FROM '/Users/hannes/source/join-order-benchmark/data-org/comp_cast_type.csv'  WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY company_name    FROM '/Users/hannes/source/join-order-benchmark/data-org/company_name.csv'    WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY company_type    FROM '/Users/hannes/source/join-order-benchmark/data-org/company_type.csv'    WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY complete_cast   FROM '/Users/hannes/source/join-order-benchmark/data-org/complete_cast.csv'   WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY info_type       FROM '/Users/hannes/source/join-order-benchmark/data-org/info_type.csv'       WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY keyword         FROM '/Users/hannes/source/join-order-benchmark/data-org/keyword.csv'         WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY kind_type       FROM '/Users/hannes/source/join-order-benchmark/data-org/kind_type.csv'       WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY link_type       FROM '/Users/hannes/source/join-order-benchmark/data-org/link_type.csv'       WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY movie_companies FROM '/Users/hannes/source/join-order-benchmark/data-org/movie_companies.csv' WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY movie_info      FROM '/Users/hannes/source/join-order-benchmark/data-org/movie_info.csv'      WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY movie_info_idx  FROM '/Users/hannes/source/join-order-benchmark/data-org/movie_info_idx.csv'  WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY movie_keyword   FROM '/Users/hannes/source/join-order-benchmark/data-org/movie_keyword.csv'   WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY movie_link      FROM '/Users/hannes/source/join-order-benchmark/data-org/movie_link.csv'      WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY name            FROM '/Users/hannes/source/join-order-benchmark/data-org/name.csv'            WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY person_info     FROM '/Users/hannes/source/join-order-benchmark/data-org/person_info.csv'     WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY role_type       FROM '/Users/hannes/source/join-order-benchmark/data-org/role_type.csv'       WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');
COPY title           FROM '/Users/hannes/source/join-order-benchmark/data-org/title.csv'           WITH (FORMAT CSV, QUOTE '"', DELIMITER ',', NULL '', ESCAPE '\');

ANALYZE aka_name;
ANALYZE aka_title;
ANALYZE cast_info;
ANALYZE char_name;
ANALYZE comp_cast_type;
ANALYZE company_name;
ANALYZE company_type;
ANALYZE complete_cast;
ANALYZE info_type; 
ANALYZE keyword;
ANALYZE kind_type; 
ANALYZE link_type; 
ANALYZE movie_companies;
ANALYZE movie_info;
ANALYZE movie_info_idx;
ANALYZE movie_keyword;
ANALYZE movie_link;
ANALYZE name;
ANALYZE person_info;
ANALYZE role_type; 
ANALYZE title;

CHECKPOINT;