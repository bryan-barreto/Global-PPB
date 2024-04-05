-- Add up migration script here

INSERT INTO public.player
VALUES(
    gen_random_uuid(),
    'Player1',
    'email1',
    NULL,
    'R',
    now(),
    'password'
);
INSERT INTO public.player
VALUES(
    gen_random_uuid(),
    'Player2',
    'email2',
    NULL,
    'R',
    now(),
    'password'
);
INSERT INTO public.player
VALUES(
    gen_random_uuid(),
    'Player3',
    'email3',
    NULL,
    'S',
    now(),
    'password'
);
INSERT INTO public.player
VALUES(
    gen_random_uuid(),
    'Player4',
    'email4',
    NULL,
    'S',
    now(),
    'password'
);
INSERT INTO public.player
VALUES(
    gen_random_uuid(),
    'Player5',
    'email5',
    NULL,
    'S',
    now(),
    'password'
);