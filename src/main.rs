use std::borrow::Borrow;
use std::env;

use axum::Extension;
use axum::{
    routing::get,
    // http::StatusCode,
    // Json, 
    Router
};
// use serde::{Deserialize, Serialize};
use axum::response::Html;
use handlebars::Handlebars;
use serde_json::json;
use sqlx::{PgPool, Pool, Postgres};


#[tokio::main]
async fn main() {
    dotenv::dotenv().unwrap();
    let db = PgPool::connect_lazy(&env::var("DATABASE_URL").expect("Database environment variable missing"))
        .expect("Could not connect to database");
    let app = Router::new()
        .route("/", get(handler))
        .layer(Extension(db));
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    

    //Last line in code
    axum::serve(listener, app).await.unwrap();
}

async fn handler(db:Extension<PgPool>) -> Html<String> {
    let player_name = sqlx::query!("SELECT username FROM public.\"Player\"")
        .fetch_one(&*db)
        .await
        .expect("No Player found")
        .username;

    let html_file = "../index.html";
    let html_site = include_str!("../index.html");
    let mut reg = Handlebars::new();
    let html_out = reg.render_template(html_site, &json!({"name": player_name})).expect("Idk, error");

    Html(html_out)
}