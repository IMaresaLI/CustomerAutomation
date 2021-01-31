-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: stokotomasyon
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `kategori_bilgileri`
--

DROP TABLE IF EXISTS `kategori_bilgileri`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kategori_bilgileri` (
  `kategori` varchar(45) DEFAULT NULL,
  UNIQUE KEY `kategori_UNIQUE` (`kategori`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kategori_bilgileri`
--

LOCK TABLES `kategori_bilgileri` WRITE;
/*!40000 ALTER TABLE `kategori_bilgileri` DISABLE KEYS */;
INSERT INTO `kategori_bilgileri` VALUES ('Gıda'),('İçecekler'),('Teknoloji'),('Yiyecek');
/*!40000 ALTER TABLE `kategori_bilgileri` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marka_bilgileri`
--

DROP TABLE IF EXISTS `marka_bilgileri`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marka_bilgileri` (
  `kategori` varchar(45) DEFAULT NULL,
  `marka` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marka_bilgileri`
--

LOCK TABLES `marka_bilgileri` WRITE;
/*!40000 ALTER TABLE `marka_bilgileri` DISABLE KEYS */;
INSERT INTO `marka_bilgileri` VALUES ('Gıda','Eti'),('İçecekler','Coca-Cola'),('İçecekler','Fruko'),('Yiyecek','Pringles'),('İçecekler','Erikli');
/*!40000 ALTER TABLE `marka_bilgileri` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `musteriler`
--

DROP TABLE IF EXISTS `musteriler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `musteriler` (
  `idmusteriler` int NOT NULL AUTO_INCREMENT,
  `tc` varchar(11) NOT NULL,
  `adsoyad` varchar(45) NOT NULL,
  `tel` varchar(10) NOT NULL,
  `adres` varchar(100) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idmusteriler`),
  UNIQUE KEY `idmusteriler_UNIQUE` (`idmusteriler`),
  UNIQUE KEY `tc_UNIQUE` (`tc`),
  UNIQUE KEY `tel_UNIQUE` (`tel`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `musteriler`
--

LOCK TABLES `musteriler` WRITE;
/*!40000 ALTER TABLE `musteriler` DISABLE KEYS */;
INSERT INTO `musteriler` VALUES (13,'24558598488','Hakan Gate','5474115454','İstanbul','istanbul@hotmail.com'),(14,'11554887566','Leyla Dota1','4158589977','Balıkesir','balıkesir@hotmail.com'),(16,'14253678963','Mert Yatay','1234567898','Bursa','a@hotmail.com');
/*!40000 ALTER TABLE `musteriler` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `satislar`
--

DROP TABLE IF EXISTS `satislar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `satislar` (
  `idsatıslar` int NOT NULL AUTO_INCREMENT,
  `tc` varchar(45) DEFAULT NULL,
  `adsoyad` varchar(45) DEFAULT NULL,
  `barkodno` varchar(45) DEFAULT NULL,
  `urunadi` varchar(45) DEFAULT NULL,
  `miktari` int DEFAULT NULL,
  `satısfiyati` decimal(5,2) DEFAULT NULL,
  `toplamfiyati` decimal(5,2) DEFAULT NULL,
  `tarih` datetime DEFAULT NULL,
  PRIMARY KEY (`idsatıslar`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satislar`
--

LOCK TABLES `satislar` WRITE;
/*!40000 ALTER TABLE `satislar` DISABLE KEYS */;
INSERT INTO `satislar` VALUES (21,'24558598488','Hakan Gate','1','Browni Çikolata',51,2.15,109.65,'2021-01-02 23:31:34');
/*!40000 ALTER TABLE `satislar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sepet`
--

DROP TABLE IF EXISTS `sepet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sepet` (
  `tc` varchar(45) DEFAULT NULL,
  `adsoyad` varchar(45) DEFAULT NULL,
  `barkodno` varchar(45) DEFAULT NULL,
  `urunadi` varchar(45) DEFAULT NULL,
  `miktari` int DEFAULT NULL,
  `satısfiyati` decimal(5,2) DEFAULT NULL,
  `toplamfiyati` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sepet`
--

LOCK TABLES `sepet` WRITE;
/*!40000 ALTER TABLE `sepet` DISABLE KEYS */;
/*!40000 ALTER TABLE `sepet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `urunlistesi`
--

DROP TABLE IF EXISTS `urunlistesi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `urunlistesi` (
  `barkodno` int NOT NULL,
  `kategori` varchar(45) DEFAULT NULL,
  `marka` varchar(45) DEFAULT NULL,
  `urunadı` varchar(45) DEFAULT NULL,
  `miktari` int DEFAULT NULL,
  `alisfiyati` decimal(5,2) DEFAULT NULL,
  `satisfiyati` decimal(5,2) DEFAULT NULL,
  `tarih` datetime DEFAULT NULL,
  PRIMARY KEY (`barkodno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `urunlistesi`
--

LOCK TABLES `urunlistesi` WRITE;
/*!40000 ALTER TABLE `urunlistesi` DISABLE KEYS */;
INSERT INTO `urunlistesi` VALUES (1,'Gıda','Eti','Browni Çikolata',1149,0.75,2.15,'2020-11-19 01:53:13'),(2,'Gıda','Eti','Browni Intense',150,0.75,2.00,'2020-11-19 02:48:00'),(3,'Gıda','Eti','Benim O Çikolata',1500,0.75,1.50,'2020-11-19 01:40:37'),(4,'İçecekler','Erikli','Su 0.5 lt',1036,0.10,1.25,'2020-11-20 03:22:13'),(5,'İçecekler','Coca-Cola','Coca-Cola',1000,2.00,4.50,'2020-11-21 17:35:26');
/*!40000 ALTER TABLE `urunlistesi` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-31 17:51:20
