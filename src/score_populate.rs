use chrono::Utc;
use rand::Rng;
use sqlx::PgPool;
use chrono::Datelike;

use crate::prelude::*;

pub async fn score_populate(db:&PgPool, cycles:i16){
    let player_list = sqlx::query_as!(Player, "SELECT player_id FROM public.player")
        .fetch_all(db)
        .await
        .expect("Error");

    let utc = Utc::now();
    let mut rng = rand::thread_rng();
    let mut change_day = 1;
    let mut day_timer = rng.gen_range(1..11);
    for _ in 0..cycles{
        if day_timer == 0{
            change_day+=1;
            if change_day > 30{
                change_day = 1;
            }
            day_timer=rng.gen_range(1..11);
        }else {
            day_timer-=1;
        }
        for player in &player_list{
            let player_id = player.player_id;
            let score = rng.gen_range(100..1000000);
            let stage = if rng.gen_range(0..2)==0{StageType::Ruby} else{StageType::Sapphire};
            let today = utc.with_day(change_day).unwrap().naive_utc();
            let query = sqlx::query!(r#"
                INSERT INTO public.score
                    VALUES(
                        gen_random_uuid(),
                        $1,
                        $2,
                        $3,
                        $4
                    )
                "#,
                player_id, 
                score, 
                stage as i8,
                today
            );
            query.execute(db).await.expect("error");
        }
    }    
}