-- Add up migration script here
CREATE TABLE IF NOT EXISTS public."Player"
(
    player_id uuid NOT NULL,
    username character varying(16) COLLATE pg_catalog."default" NOT NULL,
    email character varying(320) COLLATE pg_catalog."default" NOT NULL,
    birth_date date,
    favorite_stage "char",
    account_created date NOT NULL,
    password_hash character varying(80) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Player_pkey" PRIMARY KEY (player_id),
    CONSTRAINT "Player_username_key" UNIQUE (username)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Player"
    OWNER to postgres;