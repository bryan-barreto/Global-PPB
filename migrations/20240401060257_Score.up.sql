-- Add up migration script here
CREATE TABLE IF NOT EXISTS public.score
(
    score_id uuid NOT NULL,
    player_id uuid NOT NULL,
    score_value integer NOT NULL,
    stage "char" NOT NULL,
    upload_date date NOT NULL,
    CONSTRAINT score_pkey PRIMARY KEY (score_id, player_id),
    CONSTRAINT score_player_id_fkey FOREIGN KEY (player_id)
        REFERENCES public.player (player_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.score
    OWNER to postgres;