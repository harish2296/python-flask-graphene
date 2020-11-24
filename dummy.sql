-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.26 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             10.1.0.5464
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for db_test_graphene
CREATE DATABASE IF NOT EXISTS `db_test_graphene` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `db_test_graphene`;

-- Dumping structure for table db_test_graphene.student
CREATE TABLE IF NOT EXISTS `student` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table db_test_graphene.student: ~0 rows (approximately)
DELETE FROM `student`;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` (`id`, `name`, `email`) VALUES
	(1, 'Harish Vijayakumar', 'vijiharishv96@gmail.com'),
	(2, 'Karan Sharma', 'vijiharishv1996@gmail.com');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;

-- Dumping structure for table db_test_graphene.student_meta
CREATE TABLE IF NOT EXISTS `student_meta` (
  `id` int(11) NOT NULL,
  `student_id` int(11) DEFAULT NULL,
  `course` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_student_meta_student` (`student_id`),
  CONSTRAINT `FK_student_meta_student` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table db_test_graphene.student_meta: ~0 rows (approximately)
DELETE FROM `student_meta`;
/*!40000 ALTER TABLE `student_meta` DISABLE KEYS */;
INSERT INTO `student_meta` (`id`, `student_id`, `course`) VALUES
	(1, 1, 'Python Programming'),
	(2, 2, 'Java Programming');
/*!40000 ALTER TABLE `student_meta` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
