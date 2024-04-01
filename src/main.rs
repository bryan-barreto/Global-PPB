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
use std::error::Error;

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(handler));
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}

async fn handler() -> Html<String> {
    let html_file = "../index.html";
    let html_site = include_str!("../index.html");
    let mut reg = Handlebars::new();
    let html_out = reg.render_template(html_site, &json!({"name": "foo"})).expect("Idk, error");

    Html(html_out)
}