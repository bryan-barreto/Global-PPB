use std::sync::Arc;

use handlebars::Handlebars;
use sqlx::PgPool;

#[derive(Clone)]
pub (crate) struct AppState<'a>{
    pub (crate) database:Arc<PgPool>,
    pub (crate) handlebars:Arc<Handlebars<'a>>
}

impl AppState<'static>{
    pub (crate) fn new(database:Arc<PgPool>, handlebars:Arc<Handlebars<'static>>) -> Self{
        Self { database, handlebars }
    }
}