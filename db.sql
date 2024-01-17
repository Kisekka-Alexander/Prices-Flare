-- MariaDB dump 10.19  Distrib 10.6.12-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: price_flare
-- ------------------------------------------------------
-- Server version	10.6.12-MariaDB-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_items`
--

DROP TABLE IF EXISTS `tbl_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `item_name` varchar(255) NOT NULL,
  `unit_of_measure` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `item_name` (`item_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_items`
--

LOCK TABLES `tbl_items` WRITE;
/*!40000 ALTER TABLE `tbl_items` DISABLE KEYS */;
INSERT INTO `tbl_items` VALUES (1,'Tomato','Tomato','Box'),(2,'Cassava','Cassava','Sack'),(3,'Maize','Maize','Kg');
/*!40000 ALTER TABLE `tbl_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_markets`
--

DROP TABLE IF EXISTS `tbl_markets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_markets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `market` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `market` (`market`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_markets`
--

LOCK TABLES `tbl_markets` WRITE;
/*!40000 ALTER TABLE `tbl_markets` DISABLE KEYS */;
INSERT INTO `tbl_markets` VALUES (1,'Natete','Natete'),(2,'Owino','Owino'),(3,'Nakasero','Nakasero'),(4,'Kalerwe','Kalerwe'),(5,'Kisenyi','Kisenyi');
/*!40000 ALTER TABLE `tbl_markets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_prices`
--

DROP TABLE IF EXISTS `tbl_prices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_prices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` decimal(18,2) NOT NULL,
  `date` date NOT NULL,
  `created_on` datetime DEFAULT current_timestamp(),
  `item` int(11) NOT NULL,
  `market` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `item` (`item`),
  KEY `market` (`market`),
  CONSTRAINT `tbl_prices_ibfk_1` FOREIGN KEY (`item`) REFERENCES `tbl_items` (`id`),
  CONSTRAINT `tbl_prices_ibfk_2` FOREIGN KEY (`market`) REFERENCES `tbl_markets` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_prices`
--

LOCK TABLES `tbl_prices` WRITE;
/*!40000 ALTER TABLE `tbl_prices` DISABLE KEYS */;
INSERT INTO `tbl_prices` VALUES (1,5000.00,'2023-01-01',NULL,1,1),(2,300.00,'2023-06-01',NULL,3,5),(3,350.00,'2023-06-02',NULL,3,5),(4,350.00,'2023-06-02',NULL,3,5),(5,300.00,'2023-06-03',NULL,3,5),(6,300.00,'2023-06-04',NULL,3,5),(7,300.00,'2023-06-05',NULL,3,5),(8,350.00,'2023-06-06',NULL,3,5),(9,350.00,'2023-06-07',NULL,3,5),(10,350.00,'2023-06-08',NULL,3,5),(11,350.00,'2023-06-09',NULL,3,5),(12,350.00,'2023-06-10',NULL,3,5),(13,350.00,'2023-06-11',NULL,3,5),(14,350.00,'2023-06-12',NULL,3,5),(15,400.00,'2023-06-13',NULL,3,5),(16,400.00,'2023-06-14',NULL,3,5),(17,400.00,'2023-06-15',NULL,3,5),(18,400.00,'2023-06-16',NULL,3,5),(19,400.00,'2023-06-17',NULL,3,5),(20,400.00,'2023-06-18',NULL,3,5),(21,400.00,'2023-06-19',NULL,3,5),(22,400.00,'2023-06-20',NULL,3,5),(23,400.00,'2023-06-21',NULL,3,5),(24,400.00,'2023-06-22',NULL,3,5),(25,400.00,'2023-06-23',NULL,3,5),(26,400.00,'2023-06-24',NULL,3,5),(27,400.00,'2023-06-25',NULL,3,5),(28,400.00,'2023-06-26',NULL,3,5),(29,400.00,'2023-06-27',NULL,3,5),(30,400.00,'2023-06-28',NULL,3,5),(31,380.00,'2023-06-29',NULL,3,5),(32,380.00,'2023-06-30',NULL,3,5),(33,380.00,'2023-07-01',NULL,3,5),(34,500.00,'2023-07-02',NULL,3,5),(35,500.00,'2023-07-03',NULL,3,5),(36,500.00,'2023-07-04',NULL,3,5),(37,500.00,'2023-07-05',NULL,3,5),(38,500.00,'2023-07-06',NULL,3,5),(39,480.00,'2023-07-07',NULL,3,5),(40,480.00,'2023-07-08',NULL,3,5),(41,500.00,'2023-07-09',NULL,3,5),(42,510.00,'2023-07-10',NULL,3,5),(43,510.00,'2023-07-11',NULL,3,5),(44,510.00,'2023-07-12',NULL,3,5),(45,510.00,'2023-07-13',NULL,3,5),(46,510.00,'2023-07-14',NULL,3,5),(47,510.00,'2023-07-15',NULL,3,5),(48,510.00,'2023-07-16',NULL,3,5),(49,500.00,'2023-07-17',NULL,3,5),(50,500.00,'2023-07-18',NULL,3,5),(51,500.00,'2023-07-19',NULL,3,5),(52,500.00,'2023-07-20',NULL,3,5),(53,500.00,'2023-07-21',NULL,3,5),(54,500.00,'2023-07-22',NULL,3,5),(55,500.00,'2023-07-23',NULL,3,5),(56,500.00,'2023-07-24',NULL,3,5),(57,500.00,'2023-07-25',NULL,3,5),(58,500.00,'2023-07-26',NULL,3,5),(59,500.00,'2023-07-27',NULL,3,5),(60,500.00,'2023-07-28',NULL,3,5),(61,500.00,'2023-07-29',NULL,3,5),(62,500.00,'2023-07-30',NULL,3,5),(63,510.00,'2023-07-31',NULL,3,5);
/*!40000 ALTER TABLE `tbl_prices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_subscribers`
--

DROP TABLE IF EXISTS `tbl_subscribers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_subscribers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) NOT NULL,
  `location` varchar(255) DEFAULT NULL,
  `market` int(11) DEFAULT NULL,
  `active` tinyint(1) DEFAULT 0,
  `item` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `market` (`market`),
  KEY `item` (`item`),
  CONSTRAINT `tbl_subscribers_ibfk_1` FOREIGN KEY (`market`) REFERENCES `tbl_markets` (`id`),
  CONSTRAINT `tbl_subscribers_ibfk_2` FOREIGN KEY (`item`) REFERENCES `tbl_items` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_subscribers`
--

LOCK TABLES `tbl_subscribers` WRITE;
/*!40000 ALTER TABLE `tbl_subscribers` DISABLE KEYS */;
INSERT INTO `tbl_subscribers` VALUES (1,'alexander kisekka','+256752091697','kira',1,1,1);
/*!40000 ALTER TABLE `tbl_subscribers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbl_users`
--

DROP TABLE IF EXISTS `tbl_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_users`
--

LOCK TABLES `tbl_users` WRITE;
/*!40000 ALTER TABLE `tbl_users` DISABLE KEYS */;
INSERT INTO `tbl_users` VALUES (1,'admin','admin@gmail.com','pbkdf2:sha256:600000$3ykbixxXrg5uNVpJ$8b8f19d43c4b0bcaf09df444cad6ddd472ad2d3febd07aea534a098d7f09eade');
/*!40000 ALTER TABLE `tbl_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-17 15:46:17
