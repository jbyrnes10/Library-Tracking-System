# Library-Tracking-System
CIS 627 Midterm Project

Here are the tables needed for the project:

CREATE TABLE `library`.`project_user` (
  `id` INT NOT NULL,
  `user_id` VARCHAR(20) NOT NULL,
  `first_name` VARCHAR(20) NOT NULL,
  `last_name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `library`.`project_topics` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `topic` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `library`.`project_mediaitem` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(100) NOT NULL,
  `title` VARCHAR(100) NOT NULL,
  `isbn` VARCHAR(17),
  `author` VARCHAR(100) NOT NULL,
  `image_file` VARCHAR(100),
  `checked_out` TINYINT(1) DEFAULT 0,
  `topic_id` INT(11),
  `subtopic_id` INT(11),
  PRIMARY KEY (`id`),
  FOREIGN KEY (topic_id) REFERENCES project_topics(id),
  FOREIGN KEY (subtopic_id) REFERENCES project_topics(id)
);

CREATE TABLE `library`.`project_mediahistory` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `media_item_id` INT(11),
  `date_out` DATE NOT NULL,
  `date_due` DATE NOT NULL,
  `date_returned` DATE,
  `borrower_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (borrower_id) REFERENCES project_user(id),
  FOREIGN KEY (media_item_id) REFERENCES project_mediaitem(id)
);


Run "python populate_library.py" to add data to the tables.