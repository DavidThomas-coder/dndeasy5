/**
 * @typedef {import("knex")} Knex
 */

/**
 * @param {Knex} knex
 */
exports.up = async (knex) => {
    return knex.schema.alterTable("characters", (table) => {
        table.string("class").notNullable()
    }
}

/**
 * @param {Knex} knex
 */
exports.down = (knex) => {
    return knex.schema.alterTable("characters", (table) => {
        table.dropColumn("class").notNullable()
    }
}
