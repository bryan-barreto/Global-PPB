-- Add up migration script here
CREATE TABLE IF NOT EXISTS public."Score"
(
    score_id uuid NOT NULL,
    player_id uuid NOT NULL,
    score_value integer NOT NULL,
    stage "char" NOT NULL,
    upload_date date NOT NULL,
    CONSTRAINT "Score_pkey" PRIMARY KEY (score_id, player_id),
    CONSTRAINT "Score_player_id_fkey" FOREIGN KEY (player_id)
        REFERENCES public."Player" (player_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Score"
    OWNER to postgres;