def take_magic_damage(health, resist, amp, spell_power):
    max_damage =spell_power * amp
    damage_dealt  = max_damage - resist
    new_health = health - damage_dealt
    return new_health