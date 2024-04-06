use std::env;

use axum::Extension;
use axum::{
    routing::get,
    Router
};
use axum::response::Html;
use handlebars::Handlebars;
use serde_json::json;
use sqlx::PgPool;

mod prelude;
mod score_populate;

#[tokio::main]
async fn main() {
    dotenv::dotenv().unwrap();
    let db = PgPool::connect_lazy(&env::var("DATABASE_URL").expect("Database environment variable missing"))
        .expect("Could not connect to database");
    
    score_populate::score_populate(&db, 250).await;
    
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
    let html_out = reg.render(html_site, &json!({})).expect("Error");

    Html(html_out)
}

async fn business_handler() -> Html<String>{
    let html_site = include_str!("../index.html");
    let reg = Handlebars::new();
    let html_out = reg.render(html_site, &json!({})).expect("Error");

    Html(html_out)
}