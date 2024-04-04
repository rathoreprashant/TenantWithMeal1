CREATE DATABASE  IF NOT EXISTS `tenantapp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `tenantapp`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tenantapp
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight` (
  `fl_id` int NOT NULL AUTO_INCREMENT,
  `airline_serv` text NOT NULL,
  `from_city` text NOT NULL,
  `to_city` text NOT NULL,
  `avail_seats` int NOT NULL,
  PRIMARY KEY (`fl_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
INSERT INTO `flight` VALUES (1,'indigo','indore','goa',50),(2,'air india','indore','delhi',30),(18,'indogo','goa','bhopal',55),(29,'indogo','ratlam','banglore',22),(30,'air india','ratlam','banglore',55),(31,'fly emirates','bhopal','dubai',1),(33,'air india','ratlam','bhopal',20);
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotel`
--

DROP TABLE IF EXISTS `hotel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hotel` (
  `ht_id` int NOT NULL AUTO_INCREMENT,
  `hotel_name` text NOT NULL,
  `city` text NOT NULL,
  `avail_rooms` int NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`ht_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotel`
--

LOCK TABLES `hotel` WRITE;
/*!40000 ALTER TABLE `hotel` DISABLE KEYS */;
INSERT INTO `hotel` VALUES (1,'wow','indore',5,4000),(2,'sayaji','indore',6,3500),(4,'indogo','Bhopal',55,55),(5,'air india','Bhopal',55,1100),(6,'air india','Bhopal',55,123),(7,'indogo','Bhopal',55,123),(9,'indogo','bhopal',55,123),(11,'indogo','Bhopal',55,56);
/*!40000 ALTER TABLE `hotel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `meal`
--

DROP TABLE IF EXISTS `meal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `meal` (
  `meal_id` int NOT NULL AUTO_INCREMENT,
  `meal_name` varchar(45) NOT NULL,
  `meal_price` double NOT NULL,
  PRIMARY KEY (`meal_id`),
  UNIQUE KEY `meal_id_UNIQUE` (`meal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meal`
--

LOCK TABLES `meal` WRITE;
/*!40000 ALTER TABLE `meal` DISABLE KEYS */;
INSERT INTO `meal` VALUES (1,'chinese Platter',200),(2,'Rajasthani Platter',300),(3,'Gujarati Platter',400),(4,'mexican Platter',500),(5,'South Indian Platter',100);
/*!40000 ALTER TABLE `meal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taxi`
--

DROP TABLE IF EXISTS `taxi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taxi` (
  `tx_id` int NOT NULL AUTO_INCREMENT,
  `taxi_number` varchar(20) NOT NULL,
  `oper_city` varchar(20) NOT NULL,
  `rate_km` int NOT NULL,
  PRIMARY KEY (`tx_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taxi`
--

LOCK TABLES `taxi` WRITE;
/*!40000 ALTER TABLE `taxi` DISABLE KEYS */;
INSERT INTO `taxi` VALUES (1,'t01','indore',12),(2,'t02','delhi',15),(6,'indogo','1232',11),(7,'0000000000','abc',11),(8,'1111','indore',22),(9,'air india','Bhopal',50);
/*!40000 ALTER TABLE `taxi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tenant`
--

DROP TABLE IF EXISTS `tenant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tenant` (
  `t_id` int NOT NULL AUTO_INCREMENT,
  `tname` text NOT NULL,
  `userId` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`t_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tenant`
--

LOCK TABLES `tenant` WRITE;
/*!40000 ALTER TABLE `tenant` DISABLE KEYS */;
INSERT INTO `tenant` VALUES (8,'aditya69','aditya69','666'),(9,'aditya95','aditya95','333'),(10,'aditya1111','aditya1111','1111'),(11,'aditya70','aditya70','777'),(12,'aditya101','aditya101','101'),(13,'manish','manish','000'),(14,'manish1','manish1','111'),(15,'manish2','manish2','222'),(16,'aditya22','aditya22','111'),(17,'adityasonale89@gmail.com','aditya89','89'),(18,'aditya000','aditya000','000'),(19,'mmt','mmt','mmt');
/*!40000 ALTER TABLE `tenant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tenant_service`
--

DROP TABLE IF EXISTS `tenant_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tenant_service` (
  `t_id` int NOT NULL,
  `service_type` varchar(20) NOT NULL,
  PRIMARY KEY (`t_id`,`service_type`),
  CONSTRAINT `fk_tenant` FOREIGN KEY (`t_id`) REFERENCES `tenant` (`t_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tenant_service`
--

LOCK TABLES `tenant_service` WRITE;
/*!40000 ALTER TABLE `tenant_service` DISABLE KEYS */;
INSERT INTO `tenant_service` VALUES (8,'flight'),(8,'hotel'),(8,'taxi'),(8,'train'),(9,'flight'),(9,'hotel'),(9,'taxi'),(9,'train'),(10,'flight'),(10,'hotel'),(10,'taxi'),(10,'train'),(11,'flight'),(11,'hotel'),(11,'taxi'),(11,'train'),(12,'train'),(13,'train'),(14,'taxi'),(15,'flight'),(15,'hotel'),(15,'taxi'),(15,'train'),(16,'flight'),(16,'hotel'),(16,'taxi'),(16,'train'),(17,'flight'),(17,'hotel'),(17,'taxi'),(17,'train'),(18,'flight'),(18,'hotel'),(18,'taxi'),(18,'train'),(19,'flight'),(19,'hotel'),(19,'taxi'),(19,'train');
/*!40000 ALTER TABLE `tenant_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `train`
--

DROP TABLE IF EXISTS `train`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `train` (
  `tr_id` int NOT NULL AUTO_INCREMENT,
  `train_name` text NOT NULL,
  `from_city` text NOT NULL,
  `to_city` text NOT NULL,
  `price` int NOT NULL,
  `avail_seats` int NOT NULL,
  PRIMARY KEY (`tr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `train`
--

LOCK TABLES `train` WRITE;
/*!40000 ALTER TABLE `train` DISABLE KEYS */;
INSERT INTO `train` VALUES (1,'avantika','indore','delhi',1500,15),(2,'duranto','indore','mumbai',1200,10),(3,'mptourism','indore','mandav',1000,14),(6,'indogo','ratlam','banglore',1100,22),(8,'air india','goa','banglore',1100,55),(9,'ajshdasd','lkjl','qw',56,0),(10,'avantika','goa','banglore',123,22),(11,'avantika','goa','banglore',123,22),(12,'indogo','goa','banglore',55,1),(13,'indogo','goa','banglore',123,11);
/*!40000 ALTER TABLE `train` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_flight`
--

DROP TABLE IF EXISTS `user_flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_flight` (
  `t_id` int NOT NULL,
  `username` varchar(100) NOT NULL,
  `fl_id` int NOT NULL,
  `from_city` text NOT NULL,
  `to_city` text NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `fk_idx` (`fl_id`),
  CONSTRAINT `fk` FOREIGN KEY (`fl_id`) REFERENCES `flight` (`fl_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_flight`
--

LOCK TABLES `user_flight` WRITE;
/*!40000 ALTER TABLE `user_flight` DISABLE KEYS */;
INSERT INTO `user_flight` VALUES (10,'hhh111',1,'indore','goa',18),(10,'hhh112',1,'indore','goa',19),(10,'hhh113',1,'indore','goa',20),(10,'hhh114',2,'indore','delhi',21),(10,'hhh115',2,'indore','delhi',22),(10,'hhh116',1,'indore','goa',23),(10,'hhh117',1,'indore','goa',24),(10,'hhh118',1,'indore','goa',25),(10,'hhh119',1,'indore','goa',26),(10,'hhh120',2,'indore','delhi',27),(11,'adityasonale01@gmail.com',1,'indore','goa',28),(11,'adityasonale333',1,'indore','goa',29),(11,'rishi@1',1,'indore','goa',30),(11,'rishi@11',1,'indore','goa',31),(11,'rishi@13',1,'indore','goa',32),(11,'rishi@14',2,'indore','delhi',33),(11,'rishi@15',1,'indore','goa',34),(11,'rishi@16',1,'indore','goa',35),(11,'rishi@17',1,'indore','goa',36),(11,'rishi@18',1,'indore','goa',37),(11,'rishi@19',1,'indore','goa',38),(11,'rishi@2',2,'indore','delhi',39),(11,'rishi@20',1,'indore','goa',40),(11,'rishi@21',1,'indore','goa',41),(11,'rishi@22',2,'indore','delhi',42),(11,'rishi@23',2,'indore','delhi',43),(11,'rishi@24',1,'indore','goa',44),(11,'rishi@25',2,'indore','delhi',45),(11,'rishi@26',1,'indore','goa',46),(11,'rishi@27',1,'indore','goa',47),(11,'rishi@3',1,'indore','goa',48),(11,'rishi@30',1,'indore','goa',49),(11,'rishi@35',2,'indore','delhi',50),(11,'rishi@36',2,'indore','delhi',51),(11,'rishi@4',1,'indore','goa',52),(11,'rishi@40',2,'indore','delhi',53),(11,'rishi@41',2,'indore','delhi',54),(11,'rishi@42',1,'indore','goa',55),(11,'rishi@43',1,'indore','goa',56),(11,'rishi@5',1,'indore','goa',57),(11,'rishi@51',1,'indore','goa',58),(11,'rishi@55',1,'indore','goa',59),(11,'rishi@57',1,'indore','goa',60),(11,'rishi@58',2,'indore','delhi',61),(11,'rishi@6',1,'indore','goa',62),(11,'rishi@63',1,'indore','goa',63),(11,'rishi@65',1,'indore','goa',64),(11,'rishi@7',1,'indore','goa',65),(11,'rishi@70',1,'indore','goa',66),(11,'rishi@71',1,'indore','goa',67),(11,'rishi@73',1,'indore','goa',68),(11,'rishi@8',1,'indore','goa',69),(11,'rishi@80',1,'indore','goa',70),(11,'rishi@81',1,'indore','goa',71),(11,'rishi@85',1,'indore','goa',72),(11,'rishi@89',2,'indore','delhi',73),(11,'rishi@90',30,'ratlam','banglore',74),(11,'rohit@45',1,'indore','goa',76),(17,'rishi@33',1,'indore','goa',77),(17,'rishi@34',2,'indore','delhi',78),(11,'rishi@90',2,'indore','delhi',79),(11,'rishi@90',1,'indore','goa',80),(11,'rishi@90',18,'goa','bhopal',81),(11,'rishi@90',29,'ratlam','banglore',82),(11,'rishi@90',31,'bhopal','dubai',83),(11,'rishi@90',1,'indore','goa',84),(11,'rishi@90',1,'indore','goa',85),(19,'mmt1@gmail.com',1,'indore','goa',86);
/*!40000 ALTER TABLE `user_flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_flight_meal`
--

DROP TABLE IF EXISTS `user_flight_meal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_flight_meal` (
  `username` varchar(100) NOT NULL,
  `fl_id` int NOT NULL,
  `meal_id` int NOT NULL,
  PRIMARY KEY (`fl_id`,`username`),
  KEY `fk_idx` (`fl_id`),
  KEY `mk_idx` (`meal_id`),
  CONSTRAINT `flight_key` FOREIGN KEY (`fl_id`) REFERENCES `flight` (`fl_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `meal_key` FOREIGN KEY (`meal_id`) REFERENCES `meal` (`meal_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_flight_meal`
--

LOCK TABLES `user_flight_meal` WRITE;
/*!40000 ALTER TABLE `user_flight_meal` DISABLE KEYS */;
INSERT INTO `user_flight_meal` VALUES ('rishi@43',1,1),('rishi@6',1,1),('rishi@8',1,1),('rishi@81',1,1),('rishi@90',1,1),('rishi517',1,1),('rishi@90',30,1),('Meal Confirmed',1,2),('rishi@1',1,2),('rishi@4',1,2),('rishi@42',1,2),('rishi@5',1,2),('rishi@7',1,2),('rishi@80',1,2),('rishi@85',1,2),('rishi512',1,2),('rishi523',1,2),('rishi@2',2,2),('rishi@34',2,2),('rishi@89',2,2),('user@gmail.com',2,2),('adityasonale01@gmail.com',1,3),('rishi@3',1,3),('rishi@33',1,3),('rishi@51',1,3),('rishi@55',1,3),('rishi@63',1,3),('rishi@71',1,3),('rishi@73',1,3),('rishi500',1,3),('rishi503',1,3),('rishi518',1,3),('rishi520',1,3),('rohit@45',1,3),('user1',1,3),('xyz1000',1,3),('hhh114',2,3),('rishi@58',2,3),('rishi600',2,3),('r',1,4),('rishi@57',1,4),('rishi226',1,4),('rishi519',1,4),('abc101',2,4),('rishi522',2,4),('rishi524',2,4),('rishi501',2,5);
/*!40000 ALTER TABLE `user_flight_meal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_hotel`
--

DROP TABLE IF EXISTS `user_hotel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_hotel` (
  `t_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `ht_id` int NOT NULL,
  `city` text NOT NULL,
  PRIMARY KEY (`t_id`,`username`),
  KEY `fk_hotel_idx` (`ht_id`),
  CONSTRAINT `fk_hotel` FOREIGN KEY (`ht_id`) REFERENCES `hotel` (`ht_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_hotel`
--

LOCK TABLES `user_hotel` WRITE;
/*!40000 ALTER TABLE `user_hotel` DISABLE KEYS */;
INSERT INTO `user_hotel` VALUES (8,'user1',1,'indore'),(11,'rishi@100',2,'indore'),(11,'rishi@70',2,'indore'),(11,'rishi@72',1,'indore'),(11,'rishi@80',1,'indore'),(11,'rishi@81',1,'indore'),(11,'rishi@85',5,'Bhopal'),(11,'rishi@90',4,'Bhopal'),(19,'mmt1@gmail.com',1,'indore');
/*!40000 ALTER TABLE `user_hotel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_taxi`
--

DROP TABLE IF EXISTS `user_taxi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_taxi` (
  `t_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `tx_id` int NOT NULL,
  `taxi_number` varchar(20) NOT NULL,
  `oper_city` text NOT NULL,
  `rate_km` int NOT NULL,
  PRIMARY KEY (`t_id`,`username`),
  KEY `fk_taxi_idx` (`tx_id`),
  CONSTRAINT `fk_taxi` FOREIGN KEY (`tx_id`) REFERENCES `taxi` (`tx_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_taxi`
--

LOCK TABLES `user_taxi` WRITE;
/*!40000 ALTER TABLE `user_taxi` DISABLE KEYS */;
INSERT INTO `user_taxi` VALUES (8,'user1',2,'t02','delhi',15),(11,'rishi@63',1,'t01','indore',12),(11,'rishi@70',1,'t01','indore',12),(11,'rishi@71',1,'t01','indore',12),(11,'rishi@80',2,'t02','delhi',15),(11,'rishi@81',2,'t02','delhi',15),(11,'rishi@90',6,'indogo','1232',11),(11,'user1',2,'t02','delhi',15),(16,'user1',1,'t01','indore',12);
/*!40000 ALTER TABLE `user_taxi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_train`
--

DROP TABLE IF EXISTS `user_train`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_train` (
  `t_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `tr_id` int NOT NULL,
  `from_city` text NOT NULL,
  `to_city` text NOT NULL,
  PRIMARY KEY (`t_id`,`username`),
  KEY `fk_train_idx` (`tr_id`),
  CONSTRAINT `fk_train` FOREIGN KEY (`tr_id`) REFERENCES `train` (`tr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_train`
--

LOCK TABLES `user_train` WRITE;
/*!40000 ALTER TABLE `user_train` DISABLE KEYS */;
INSERT INTO `user_train` VALUES (8,'user1',1,'indore','delhi'),(11,'rishi@63',2,'indore','mumbai'),(11,'rishi@70',3,'indore','mandav'),(11,'rishi@71',3,'indore','mandav'),(11,'rishi@80',2,'indore','mumbai'),(11,'rishi@81',2,'indore','mumbai'),(11,'rishi@85',8,'goa','banglore'),(11,'user1',2,'indore','mumbai'),(12,'user1',3,'indore','mandav'),(13,'user1',2,'indore','mumbai'),(15,'user1',2,'indore','mumbai');
/*!40000 ALTER TABLE `user_train` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `t_id` int NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `fk_user_idx` (`t_id`),
  CONSTRAINT `fk_user` FOREIGN KEY (`t_id`) REFERENCES `tenant` (`t_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,8,'rishi45','444'),(2,9,'rishi23','222'),(3,8,'aditya222','222'),(4,8,'aditya44','444'),(5,8,'aditya23','333'),(6,11,'rishi99','999'),(7,11,'rishi100','100'),(8,11,'rishi101','101'),(9,12,'rishi103','103'),(10,13,'aayush','111'),(11,15,'aayush2','222'),(12,16,'hemant101','000'),(13,10,'hhh111','111'),(14,10,'hhh112','112'),(15,10,'hhh113','113'),(16,10,'hhh114','114'),(17,10,'hhh115','115'),(18,10,'hhh116','116'),(19,10,'hhh117','117'),(20,10,'hhh118','118'),(21,10,'hhh119','119'),(22,10,'hhh120','120'),(23,11,'adityasonale01@gmail.com','123'),(24,11,'adityasonale333','333'),(25,11,'rishi@1','111'),(26,11,'rishi@2','222'),(27,11,'rishi@3','333'),(28,11,'rishi@4','444'),(29,11,'rishi@5','555'),(30,11,'rishi@6','666'),(31,11,'rishi@7','777'),(32,11,'rishi@8','888'),(33,11,'rishi@10','111'),(34,11,'rishi@11','111'),(35,11,'rishi@13','333'),(36,11,'rishi@14','444'),(37,11,'rishi@15','555'),(38,11,'rishi@16','666'),(39,11,'rishi@17','777'),(40,11,'rohit@45','45'),(41,11,'rishi@18','888'),(42,11,'rishi@19','999'),(43,11,'rishi@20','20'),(44,11,'rishi@21','21'),(45,11,'rishi@22','22'),(46,11,'rishi@23','23'),(47,11,'rishi@24','24'),(48,11,'rishi@25','25'),(49,11,'rishi@26','26'),(50,11,'rishi@27','27'),(51,11,'rishi@30','30'),(52,12,'rishi@31','31'),(53,10,'rishisonalemwc24@gmail.com','24'),(54,17,'rishi@33','33'),(55,17,'rishi@34','34'),(56,11,'rishi@35','35'),(57,11,'rishi@36','36'),(58,11,'rishi@40','40'),(59,11,'rishi@50','50'),(60,11,'rishi@41','41'),(61,11,'rishi@42','42'),(62,11,'rishi@43','43'),(63,11,'rishi@51','51'),(64,11,'rishi@52','52'),(65,11,'rishi@55','55'),(66,11,'rishi@56','56'),(67,11,'rishi@57','57'),(68,11,'rishi@58','58'),(69,11,'rishi@59','59'),(70,11,'rishi@60','60'),(71,11,'rishi@61','61'),(72,11,'rishi@62','62'),(73,11,'rishi@63','63'),(74,11,'rishi@70','70'),(75,11,'rishi@71','71'),(76,11,'rishi@72','72'),(77,11,'rishi@73','73'),(78,11,'rishi@65','65'),(79,11,'rishi@80','80'),(80,11,'rishi@81','81'),(81,11,'rishi@85','85'),(82,11,'rishi@89','89'),(83,11,'rishi@90','90'),(84,11,'rishi@91','91'),(85,11,'rishi@100','100'),(86,11,'rishi@101','101'),(87,11,'rishi@102','102'),(88,11,'rishi@103','103'),(89,19,'mmt1@gmail.com','mmt1');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-02 13:12:48
