use sqlx::types::Uuid;

pub struct Player{
    pub player_id : Uuid,
}

#[repr(i8)]
pub enum StageType{
    Ruby = 0x52,
    Sapphire = 0x53
}
