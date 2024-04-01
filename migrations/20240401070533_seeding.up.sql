-- Add up migration script here

INSERT INTO public."Player"
VALUES(
    gen_random_uuid(),
    'Bryan',
    'email',
    NULL,
    NULL,
    now(),
    'password'
);