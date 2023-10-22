const Model = require("./Model")

class Character extends Model {
    static get tableName() {
        return "characters"
    }

    static get relationMappings() {
        const {User} = require("./index.js")

        return {
            users: {
                relation: Model.BelongsToOneRelation,
                modelClass: User,
                join: {
                    from: "riffs.userId",
                    to: "users.id"
                }
            }
        }
    }

}

module.exports = Character