-- Add up migration script here
CREATE TABLE IF NOT EXISTS public.business
(
    business_id uuid NOT NULL,
    business_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    email character varying(320) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT business_pkey PRIMARY KEY (business_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.business
    OWNER to postgres;