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

-- Dumping data for table app_grouptango.auth_group: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

-- Dumping data for table app_grouptango.auth_group_permissions: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

-- Dumping data for table app_grouptango.auth_permission: ~40 rows (approximately)
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
REPLACE INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add room', 7, 'add_room'),
	(26, 'Can change room', 7, 'change_room'),
	(27, 'Can delete room', 7, 'delete_room'),
	(28, 'Can view room', 7, 'view_room'),
	(29, 'Can add conversation', 8, 'add_conversation'),
	(30, 'Can change conversation', 8, 'change_conversation'),
	(31, 'Can delete conversation', 8, 'delete_conversation'),
	(32, 'Can view conversation', 8, 'view_conversation'),
	(33, 'Can add viewed', 9, 'add_viewed'),
	(34, 'Can change viewed', 9, 'change_viewed'),
	(35, 'Can delete viewed', 9, 'delete_viewed'),
	(36, 'Can view viewed', 9, 'view_viewed'),
	(37, 'Can add profile', 10, 'add_profile'),
	(38, 'Can change profile', 10, 'change_profile'),
	(39, 'Can delete profile', 10, 'delete_profile'),
	(40, 'Can view profile', 10, 'view_profile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

-- Dumping data for table app_grouptango.auth_user: ~3 rows (approximately)
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
REPLACE INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(3, 'pbkdf2_sha256$180000$S1Y2LgstFpmY$Kw2ttFqnmgZFyz1DTAO72quutKt/PLhaWB8IBSTzXfY=', '2020-09-04 07:10:21.114956', 1, 'admin', 'dohyung', 'kim', 'dhyj777@gmail.com', 1, 1, '2020-08-28 13:40:41.999709'),
	(10, 'pbkdf2_sha256$180000$HBzOlVLkrNvW$/+UXRZyVvJUGA2jVjkkQFbfZ6f8LghTHXjy7cyfs/f0=', '2020-09-03 06:05:09.206224', 0, 'admin_yh', 'yohan', 'na', 'yohan394@naver.com', 0, 1, '2020-09-02 09:22:17.274810'),
	(11, 'pbkdf2_sha256$180000$E9oi6G6Tj51o$beMGSLspk34c0Zmj9X+CVGn8po7R2qrU4vmYM2YZV4I=', '2020-09-04 07:27:58.367338', 0, 'admin_jy', 'jiyoon', 'yoon', 'parassence@gmail.com', 0, 1, '2020-09-02 11:39:31.711766');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

-- Dumping data for table app_grouptango.auth_user_groups: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;

-- Dumping data for table app_grouptango.auth_user_user_permissions: ~0 rows (approximately)
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;

-- Dumping data for table app_grouptango.chat_conversation: ~0 rows (approximately)
/*!40000 ALTER TABLE `chat_conversation` DISABLE KEYS */;
/*!40000 ALTER TABLE `chat_conversation` ENABLE KEYS */;

-- Dumping data for table app_grouptango.chat_room: ~0 rows (approximately)
/*!40000 ALTER TABLE `chat_room` DISABLE KEYS */;
/*!40000 ALTER TABLE `chat_room` ENABLE KEYS */;

-- Dumping data for table app_grouptango.chat_viewed: ~0 rows (approximately)
/*!40000 ALTER TABLE `chat_viewed` DISABLE KEYS */;
/*!40000 ALTER TABLE `chat_viewed` ENABLE KEYS */;

-- Dumping data for table app_grouptango.django_admin_log: ~0 rows (approximately)
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

-- Dumping data for table app_grouptango.django_content_type: ~10 rows (approximately)
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
REPLACE INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(8, 'chat', 'conversation'),
	(7, 'chat', 'room'),
	(9, 'chat', 'viewed'),
	(5, 'contenttypes', 'contenttype'),
	(10, 'index', 'profile'),
	(6, 'sessions', 'session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

-- Dumping data for table app_grouptango.django_migrations: ~23 rows (approximately)
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
REPLACE INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2020-08-28 10:43:16.345893'),
	(2, 'auth', '0001_initial', '2020-08-28 10:43:16.565284'),
	(3, 'admin', '0001_initial', '2020-08-28 10:43:17.054980'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2020-08-28 10:43:17.165872'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-08-28 10:43:17.175018'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2020-08-28 10:43:17.289157'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2020-08-28 10:43:17.350197'),
	(8, 'auth', '0003_alter_user_email_max_length', '2020-08-28 10:43:17.411584'),
	(9, 'auth', '0004_alter_user_username_opts', '2020-08-28 10:43:17.421521'),
	(10, 'auth', '0005_alter_user_last_login_null', '2020-08-28 10:43:17.474754'),
	(11, 'auth', '0006_require_contenttypes_0002', '2020-08-28 10:43:17.477746'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2020-08-28 10:43:17.486722'),
	(13, 'auth', '0008_alter_user_username_max_length', '2020-08-28 10:43:17.571705'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2020-08-28 10:43:17.645814'),
	(15, 'auth', '0010_alter_group_name_max_length', '2020-08-28 10:43:17.704788'),
	(16, 'auth', '0011_update_proxy_permissions', '2020-08-28 10:43:17.714157'),
	(17, 'sessions', '0001_initial', '2020-08-28 10:43:17.749113'),
	(18, 'chat', '0001_initial', '2020-08-28 11:10:37.565535'),
	(19, 'index', '0001_initial', '2020-09-02 01:49:28.351965'),
	(20, 'index', '0002_auto_20200902_1105', '2020-09-02 02:05:13.917031'),
	(21, 'index', '0003_auto_20200902_1710', '2020-09-02 08:10:16.916386'),
	(22, 'index', '0004_auto_20200903_1252', '2020-09-03 03:52:50.790931'),
	(23, 'index', '0005_auto_20200904_1551', '2020-09-04 06:51:51.754238');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;

-- Dumping data for table app_grouptango.django_session: ~7 rows (approximately)
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
REPLACE INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('8dsdrn70qc3mgn7fe9bf38sj82eoni26', 'NzJmM2RmOTBiMzVjMmEwMWFiMDA0YTIxOWM1YTA1MTZlZjBhYTI0OTp7fQ==', '2020-09-15 04:23:39.215181'),
	('a37yz96btiilx4574fvcrv809jlefokt', 'NzJmM2RmOTBiMzVjMmEwMWFiMDA0YTIxOWM1YTA1MTZlZjBhYTI0OTp7fQ==', '2020-09-17 05:18:38.062676'),
	('a8aj2t2am9geqwweff2unpicy8to5vgu', 'MTk1ZTQ4YTE5YzJkNWU1NzU4N2Q3MzY3Zjc5MThhOGRkYWEzMTk0MDp7Il9hdXRoX3VzZXJfaWQiOiIxMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZDdhZWE3NGIxYjY2YzEzMDA1OTM2Njg0YmY5MGFhYWExMGFkMDc0OCIsImZ1bGxuYW1lIjoiaml5b29uIHlvb24ifQ==', '2020-09-18 07:27:58.371243'),
	('bssvlywwbg8lt6bcrq3f1t4shozhbvqt', 'NzJmM2RmOTBiMzVjMmEwMWFiMDA0YTIxOWM1YTA1MTZlZjBhYTI0OTp7fQ==', '2020-09-17 05:08:17.548630'),
	('hs0r3rcjgqt5urb0o37a58g0xi240eh9', 'NzJmM2RmOTBiMzVjMmEwMWFiMDA0YTIxOWM1YTA1MTZlZjBhYTI0OTp7fQ==', '2020-09-17 05:12:10.331698'),
	('nxsfdrk2vp7gn88jtbndvoatg3438yrd', 'NzJmM2RmOTBiMzVjMmEwMWFiMDA0YTIxOWM1YTA1MTZlZjBhYTI0OTp7fQ==', '2020-09-14 20:07:13.875106'),
	('z31n64wlsp2yftzhn4ikkihgj7ppw6oj', 'NzJmM2RmOTBiMzVjMmEwMWFiMDA0YTIxOWM1YTA1MTZlZjBhYTI0OTp7fQ==', '2020-09-16 01:55:40.942260');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

-- Dumping data for table app_grouptango.index_profile: ~3 rows (approximately)
/*!40000 ALTER TABLE `index_profile` DISABLE KEYS */;
REPLACE INTO `index_profile` (`id`, `bio`, `location`, `birth_date`, `profile_pic`, `user_id`) VALUES
	(1, '', '', '1989-07-28', '', 3),
	(2, 'test bio 2', 'test loc 2', '1989-01-20', '', 10),
	(3, NULL, NULL, NULL, '', 11);
/*!40000 ALTER TABLE `index_profile` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
