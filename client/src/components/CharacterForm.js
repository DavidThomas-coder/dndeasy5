import React from "react";

const CharacterForm = (props) => {
    return (
        <form onSubmit={onSubmit}>
            <label>
                Character Name:
                <input
                    type="text"
                    value={userAnswer}
                    onChange={onUserAnswerChange}
                />
            </label>
            <button type="submit">Submit</button>
        </form>
    );
};

export default CharacterForm;