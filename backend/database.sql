CREATE DATABASE IF NOT EXISTS `quizo` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `quizo`;

DROP TABLE IF EXISTS `sign_up`;
CREATE TABLE `sign_up` (
  `email` varchar(45) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(15) NOT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `sign_up` VALUES 
('mridhul@gmail.com','Mridhul','Mridhul'),
('divyansh01@gmail.com','Divya23','DivyaTiwari'),
('hemant56@gmail.com','Hemant329','Hemant123'),
('kumar1166@gmail.com','kris6','Krishna1'),
('parth529@gmail.com','Parth2839','Parth@456'),
('quizo_admin@gmail.com','ExamPortalTeam','Admin');
