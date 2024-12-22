DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS users_answers;

CREATE TABLE questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question_text VARCHAR(255),
    option_a VARCHAR(100),
    option_b VARCHAR(100),
    option_c VARCHAR(100),
    option_d VARCHAR(100)
);

CREATE TABLE users_answers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    question_id INT NOT NULL,
    selected_option VARCHAR(1),
    FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
);

INSERT INTO questions (question_text, option_a, option_b, option_c, option_d) VALUES
(
    'What platform is the most often used for video game live streaming?',
    'Twitch',
    'YouTube',
    'Facebook Live',
    'Vimeo'
),
(
    'Which spice is known as "queen of spices"?',
    'Cinnamon',
    'Cardamom',
    'Nutmeg',
    'Black pepper'
),
(
    'What part of the brain is responsible for memory and learning?',
    'Cerebellum',
    'Hypothalamus',
    'Hippocampus',
    'Medulla oblongata'
),
(
    'How many bones are there in the adult human body?',
    '186',
    '206',
    '226',
    '246'
),
(
    'Which breed of dog is known for its excellent sense of smell and tracking abilities?',
    'Golden Retriever',
    'German Shepherd',
    'Bloodhound',
    'Bulldog'
);