-- Add up migration script here

INSERT INTO public.player
VALUES(
    gen_random_uuid(),
    'Player1',
    'email1',
    NULL,
    'R',
    now(),
    'USA',
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
    'USA',
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
    'USA',
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
    'USA',
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
    'Japan',
    'password'
);
INSERT INTO public.business
VALUES(
    gen_random_uuid(),
    'business1',
    'business_email1'
);
INSERT INTO public.business
VALUES(
    gen_random_uuid(),
    'business2',
    'business_email2'
);
INSERT INTO public.business
VALUES(
    gen_random_uuid(),
    'business3',
    'business_email3'
);