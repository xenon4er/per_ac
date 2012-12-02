-- phpMyAdmin SQL Dump
-- version 3.4.10.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 19, 2012 at 09:47 PM
-- Server version: 5.5.28
-- PHP Version: 5.3.10-1ubuntu3.4

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `accounts_department`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_department_category`
--

CREATE TABLE IF NOT EXISTS `accounts_department_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(255) NOT NULL,
  `periodicity` int(11) NOT NULL,
  `FK_User_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_User_id` (`FK_User_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `accounts_department_category`
--

INSERT INTO `accounts_department_category` (`id`, `Title`, `periodicity`, `FK_User_id`) VALUES
(3, 'ww', 0, 13),
(6, 'wwdwd', 0, 13),
(7, 'Shop', 0, 13),
(8, 'Internet', 1, 13),
(9, 'New_cat', 0, 24),
(10, 'shop', 0, 24),
(11, 'vasya', 0, 24);

-- --------------------------------------------------------

--
-- Table structure for table `accounts_department_payment`
--

CREATE TABLE IF NOT EXISTS `accounts_department_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `FK_User_id` int(11) NOT NULL,
  `currency` varchar(10) NOT NULL,
  `Reason` varchar(255) NOT NULL,
  `Amount_of_payment` double NOT NULL,
  `date` date NOT NULL,
  `FK_Category_id` int(11) NOT NULL,
  `Fk_Safe_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Fk_Safe_id` (`Fk_Safe_id`),
  KEY `FK_User_id` (`FK_User_id`),
  KEY `FK_Category_id` (`FK_Category_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `accounts_department_payment`
--

INSERT INTO `accounts_department_payment` (`id`, `FK_User_id`, `currency`, `Reason`, `Amount_of_payment`, `date`, `FK_Category_id`, `Fk_Safe_id`) VALUES
(1, 24, 'hf', 'found', 123832, '2012-11-01', 11, 2);

-- --------------------------------------------------------

--
-- Table structure for table `accounts_department_safe`
--

CREATE TABLE IF NOT EXISTS `accounts_department_safe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(255) NOT NULL,
  `FK_User_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_User_id` (`FK_User_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `accounts_department_safe`
--

INSERT INTO `accounts_department_safe` (`id`, `Title`, `FK_User_id`) VALUES
(2, 'Test', 24);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_message`
--

CREATE TABLE IF NOT EXISTS `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_fbfc09f1` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=37 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add message', 4, 'add_message'),
(11, 'Can change message', 4, 'change_message'),
(12, 'Can delete message', 4, 'delete_message'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add site', 7, 'add_site'),
(20, 'Can change site', 7, 'change_site'),
(21, 'Can delete site', 7, 'delete_site'),
(25, 'Can add payment', 9, 'add_payment'),
(26, 'Can change payment', 9, 'change_payment'),
(27, 'Can delete payment', 9, 'delete_payment'),
(28, 'Can add category', 10, 'add_category'),
(29, 'Can change category', 10, 'change_category'),
(30, 'Can delete category', 10, 'delete_category'),
(31, 'Can add safe', 11, 'add_safe'),
(32, 'Can change safe', 11, 'change_safe'),
(33, 'Can delete safe', 11, 'delete_safe'),
(34, 'Can add user profile', 12, 'add_userprofile'),
(35, 'Can change user profile', 12, 'change_userprofile'),
(36, 'Can delete user profile', 12, 'delete_userprofile');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=25 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(13, '4', 'vasay', 'ivanof', '6', 'sha1$fc571$b172e2382204439fb6ef385c3d6253425edf228b', 0, 1, 0, '2012-11-19 00:34:04', '2012-11-18 14:11:48'),
(15, '434', '', '', '5', 'sha1$5b369$ca62232650b3291c97489229ede8670b07c4c190', 0, 1, 0, '2012-11-18 14:45:48', '2012-11-18 14:45:48'),
(24, 'alex', 'alex', 'al', '123', 'pbkdf2_sha256$10000$AZxXZmZmWbD7$4YMQqlP5342oaflu91WT+/T0VDjB+DOgx3hXfyRbDZM=', 0, 1, 0, '2012-11-19 18:22:51', '2012-11-19 00:56:48');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'message', 'auth', 'message'),
(5, 'content type', 'contenttypes', 'contenttype'),
(6, 'session', 'sessions', 'session'),
(7, 'site', 'sites', 'site'),
(9, 'payment', 'accounts_department', 'payment'),
(10, 'category', 'accounts_department', 'category'),
(11, 'safe', 'accounts_department', 'safe'),
(12, 'user profile', 'users', 'userprofile');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('18921f5476e78a58c6b80c92f1f4f1f2', 'NjUxNDZlMzM3MWNlMjQyZjA0ZjhlNDNiMWIyZDNkYWViNWVmYzhmNzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKARh1Lg==\n', '2012-12-03 18:22:51'),
('702e5bc08dd5def2a3aec42697bc36c2', 'NjUxNDZlMzM3MWNlMjQyZjA0ZjhlNDNiMWIyZDNkYWViNWVmYzhmNzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKARh1Lg==\n', '2012-12-03 00:57:48'),
('c9c604d9a118d8ba520a8b91518b5732', 'ZGZlMzQyZDJiYjhlMTM4Zjk0NDRhNTVjMWM0YTljOWJmMDY2ZWNjODqAAn1xAS4=\n', '2012-12-02 12:31:31'),
('d70edef8ba0598eb3bea25b826999b1c', 'ZGZlMzQyZDJiYjhlMTM4Zjk0NDRhNTVjMWM0YTljOWJmMDY2ZWNjODqAAn1xAS4=\n', '2012-11-16 14:00:22'),
('e35701cfcde1f3e71aaf1846c20809b8', 'ZGZlMzQyZDJiYjhlMTM4Zjk0NDRhNTVjMWM0YTljOWJmMDY2ZWNjODqAAn1xAS4=\n', '2012-12-03 21:43:24'),
('ed03636da2969596b43960dc194648e4', 'ZGZlMzQyZDJiYjhlMTM4Zjk0NDRhNTVjMWM0YTljOWJmMDY2ZWNjODqAAn1xAS4=\n', '2012-10-24 00:07:53');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Table structure for table `users_userprofile`
--

CREATE TABLE IF NOT EXISTS `users_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `balance` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `users_userprofile`
--

INSERT INTO `users_userprofile` (`id`, `user_id`, `balance`) VALUES
(3, 13, 0),
(4, 15, 0),
(11, 24, 0);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts_department_category`
--
ALTER TABLE `accounts_department_category`
  ADD CONSTRAINT `accounts_department_category_ibfk_1` FOREIGN KEY (`FK_User_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `accounts_department_payment`
--
ALTER TABLE `accounts_department_payment`
  ADD CONSTRAINT `accounts_department_payment_ibfk_1` FOREIGN KEY (`FK_User_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `accounts_department_payment_ibfk_2` FOREIGN KEY (`FK_Category_id`) REFERENCES `accounts_department_category` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `accounts_department_payment_ibfk_3` FOREIGN KEY (`Fk_Safe_id`) REFERENCES `accounts_department_safe` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `accounts_department_safe`
--
ALTER TABLE `accounts_department_safe`
  ADD CONSTRAINT `accounts_department_safe_ibfk_1` FOREIGN KEY (`FK_User_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_message`
--
ALTER TABLE `auth_message`
  ADD CONSTRAINT `user_id_refs_id_9af0b65a` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `users_userprofile`
--
ALTER TABLE `users_userprofile`
  ADD CONSTRAINT `users_userprofile_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
