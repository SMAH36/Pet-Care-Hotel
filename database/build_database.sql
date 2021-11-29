-- psql postgres://pywbvbgjjkfnyv:50ffacc2606337e3c9d652c87509a725a515a6856fd93c9c77966995c9e05a4b@ec2-54-195-246-55.eu-west-1.compute.amazonaws.com:5432/dfl389q97gd8c6

BEGIN;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP TABLE IF EXISTS "user_auth" CASCADE;
DROP TABLE IF EXISTS "user_info" CASCADE;
DROP TABLE IF EXISTS "user_status" CASCADE;

SET CLIENT_ENCODING TO 'utf8';
SET timezone = 'Israel';

CREATE TABLE "user_auth" (
"id" uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
"email" varchar(255) NOT NULL UNIQUE,
"phone_number" varchar(255) NOT NULL UNIQUE,
"password" varchar(255) NOT NULL
);

CREATE TABLE "user_info" (
  "id" SERIAL PRIMARY KEY,
  "user_id" uuid NOT NULL UNIQUE,
  "first_name" varchar(255) NOT NULL,
  "last_name" varchar(255) NOT NULL,
  "age" varchar(255) NOT NULL,
  "gender" varchar(255) NOT NULL,
  "personal_id" varchar(255) NOT NULL,
  "rank" varchar(255) DEFAULT 'customer',
  "created_at" timestamptz NOT NULL DEFAULT NOW()
);

COMMIT;