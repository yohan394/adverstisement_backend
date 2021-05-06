-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.3.9-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping data for table app_grouptango.auth_user: ~3 rows (approximately)
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
REPLACE INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(3, 'pbkdf2_sha256$180000$S1Y2LgstFpmY$Kw2ttFqnmgZFyz1DTAO72quutKt/PLhaWB8IBSTzXfY=', '2020-09-03 06:43:01.481645', 1, 'admin', 'dohyung', 'kim', 'dhyj777@gmail.com', 1, 1, '2020-08-28 13:40:41.999709'),
	(10, 'pbkdf2_sha256$180000$HBzOlVLkrNvW$/+UXRZyVvJUGA2jVjkkQFbfZ6f8LghTHXjy7cyfs/f0=', '2020-09-03 06:05:09.206224', 0, 'admin_yh', 'yohan', 'na', 'yohan394@naver.com', 0, 1, '2020-09-02 09:22:17.274810'),
	(11, 'pbkdf2_sha256$180000$E9oi6G6Tj51o$beMGSLspk34c0Zmj9X+CVGn8po7R2qrU4vmYM2YZV4I=', '2020-09-02 11:41:56.045826', 0, 'admin_jy', 'jiyoon', 'yoon', 'parassence@gmail.com', 0, 1, '2020-09-02 11:39:31.711766');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
