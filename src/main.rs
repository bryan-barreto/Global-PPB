use std::sync::Arc;
use std::{env, vec};

use appstate::AppState;
use axum::Extension;
use axum::{
    routing::get,
    Router
};
use axum::response::Html;
use handlebars::Handlebars;
use serde::{Deserialize, Serialize};
use serde_json::json;
use sqlx::PgPool;
use std::process::Command;
use std::str;
use tower_http::services::ServeDir;

mod prelude;
mod score_populate;
mod appstate;

#[derive(Serialize, Deserialize, Debug)]
struct Graph{
    filename: String,
    title: String
}

#[tokio::main]
async fn main() {
    const SITE_URL:&str = "0.0.0.0:3000";

    dotenv::dotenv().expect(".env does not exist");

    let database_url = env::var("DATABASE_URL")
        .expect("Database environment variable missing");

    let db = PgPool::connect_lazy(&database_url)
        .expect("Could not connect to database");

    let arc_db = Arc::new(db);

    let mut hb = Handlebars::new();
    hb.register_template_file("index", "./templates/index.hbs");
    let arc_hb = Arc::new(hb);
    let appstate = AppState::new(arc_db, arc_hb);
    
    // score_populate::score_populate(&db, 250).await; // Comment out to prevent addition of sample data
    
    
    let app = Router::new()
        .route("/", get(handler))
        .route("/playerdash", get(player_handler))
        .route("/businessdash", get(business_handler))
        .nest_service(
            "/images",
            ServeDir::new("./images")
        )
        .layer(Extension(appstate));
    
    let listener = tokio::net::TcpListener::bind(SITE_URL).await.unwrap();
    

    //Last line in code
    axum::serve(listener, app).await.unwrap();
}

async fn handler(appstate:Extension<AppState<'_>>) -> Html<String> {
    let player_name = sqlx::query!(r#"

SELECT 
    username 
FROM 
    public.player

        "#)
        .fetch_one(&*appstate.database)
        .await
        .expect("No Player found")
        .username;

    let html_out = appstate.handlebars.render("index", &json!({"name": player_name})).expect("Idk, error");

    Html(html_out)
}

async fn player_handler() -> Html<String>{


    Html("Hello World".to_string())
}

async fn business_handler() -> Html<String>{
    let chart_list = vec!["daily_uploads_chart", "average_player_improvement", "total_players", "favorite_stage_graph", "players_by_country"];

    

    let html_site = include_str!("../bi.html");
    let reg = Handlebars::new();
    let out_string= "Business Intelligence Dashboard".to_string();
    let mut graph_vec: Vec<Graph> = vec![]; 

    for chart in chart_list{
        let command =  "./src/graphs.py";
        let output = Command::new("python")
            .args([command,chart])
            .output()
            .expect("Failed to get {chart}")
            .stdout
        ;
        let mut out_vector = str::from_utf8(&output)
            .unwrap()
            .lines()
        ;
        
        
        while let (Some(filename), Some(title)) = (out_vector.next(), out_vector.next()){
            graph_vec.push(Graph{filename:filename.to_string(),title:title.to_string()});
        }



        // println!("{}", out_to_string);
        // html_out += 
    }

    let out_json = &json!({"page_title": out_string,
                            "graph": graph_vec
                            });

    let html_out = reg.render_template(html_site, out_json).expect("Error");
    Html(html_out)
}

