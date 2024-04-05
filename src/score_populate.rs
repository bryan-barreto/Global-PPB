use rand::Rng;
use sqlx::PgPool;

use crate::prelude::*;

pub async fn score_populate(db:&PgPool){
    let player_list = sqlx::query_as!(Player, "SELECT player_id FROM public.player")
        .fetch_all(db)
        .await
        .expect("Error");

    for player in player_list{
        let mut rng = rand::thread_rng();
        let player_id = player.player_id;
        let score = rng.gen_range(100..1000000);
        let stage = if rng.gen_range(0..2)==0{StageType::Ruby} else{StageType::Sapphire};

        let query = sqlx::query!(r#"
            INSERT INTO public.score
                VALUES(
                    gen_random_uuid(),
                    $1,
                    $2,
                    $3,
                    now()
                )
            "#,
            player_id, 
            score, 
            stage as i8);
        query.execute(db).await.expect("error");
    }    
}