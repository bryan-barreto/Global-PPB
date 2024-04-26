use std::{env, vec};

use axum::Extension;
use axum::{
    routing::get,
    Router
};
use axum::response::Html;
use handlebars::Handlebars;
use serde_json::json;
use sqlx::PgPool;
use std::process::Command;
use std::str;

mod prelude;
mod score_populate;



#[tokio::main]
async fn main() {
    dotenv::dotenv().unwrap();
    let db = PgPool::connect_lazy(&env::var("DATABASE_URL").expect("Database environment variable missing"))
        .expect("Could not connect to database");
    
    // score_populate::score_populate(&db, 250).await; // Comment out to prevent addition of sample data
    
    
    let app = Router::new()
        .route("/", get(handler))
        .route("/playerdash", get(player_handler))
        .route("/businessdash", get(business_handler))
        .layer(Extension(db));
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    

    //Last line in code
    axum::serve(listener, app).await.unwrap();
}

async fn handler(db:Extension<PgPool>) -> Html<String> {
    let player_name = sqlx::query!("SELECT username FROM public.player")
        .fetch_one(&*db)
        .await
        .expect("No Player found")
        .username;

    // let html_file = "../index.html";
    let html_site = include_str!("../index.html");
    let reg = Handlebars::new();
    let html_out = reg.render_template(html_site, &json!({"name": player_name})).expect("Idk, error");

    Html(html_out)
}

async fn player_handler() -> Html<String>{
    let html_site = include_str!("../index.html");
    let reg = Handlebars::new();
    let html_out = reg.render_template(html_site, &json!({})).expect("Error");

    Html(html_out)
}

async fn business_handler() -> Html<String>{
    let chart_list = vec!["daily_uploads_chart", "average_player_improvement", "total_players", "favorite_stage_graph", "players_by_country"];


    let html_site = include_str!("../index.html");
    let reg = Handlebars::new();
    let out_string= "Business Intelligence Dashboard".to_string();
    let html_out = reg.render_template(html_site, &json!({"name": out_string})).expect("Error");
    for chart in chart_list{
        let command =  "./src/graphs.py";
        let output = Command::new("python")
            .args([command,chart])
            .output()
            .expect("Failed to get {chart}")
            .stdout
        ;
        let out_vector = str::from_utf8(&output)
            .unwrap()
            .to_string()
            .split("")
        ;

        // println!("{}", out_to_string);
        // html_out += 
    }

    Html(html_out)
}

