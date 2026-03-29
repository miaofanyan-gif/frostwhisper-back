-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: frostwhisper_hanfu
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `frostwhisper_hanfu`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `frostwhisper_hanfu` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `frostwhisper_hanfu`;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '分类ID',
  `name` varchar(64) NOT NULL COMMENT '分类名称',
  `parent_id` bigint unsigned NOT NULL DEFAULT '0' COMMENT '父分类ID',
  `status` tinyint NOT NULL DEFAULT '1' COMMENT '状态 1=正常 0=禁用',
  `sort` int NOT NULL DEFAULT '0' COMMENT '排序',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `type` varchar(20) NOT NULL,
  `name_cn` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_parent_id` (`parent_id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='商品分类表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (5,'shape_system',0,1,1,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','形制体系'),(6,'dynasty_style',0,1,2,'2026-03-25 08:57:02','2026-03-25 08:57:02','dynasty','朝代风格'),(7,'gender',0,1,3,'2026-03-25 08:57:02','2026-03-25 08:57:02','gender','穿着性别'),(8,'usage_scene',0,1,4,'2026-03-25 08:57:02','2026-03-25 08:57:02','scene','用途场景'),(9,'structure',0,1,5,'2026-03-25 08:57:02','2026-03-25 08:57:02','structure','款式结构'),(10,'quju',1,1,1,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','曲裾'),(11,'zhiju',1,1,2,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','直裾'),(12,'qixiong_ruqun',1,1,3,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','齐胸襦裙'),(13,'qiyao_ruqun',1,1,4,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','齐腰襦裙'),(14,'duijin_ruqun',1,1,5,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','对襟襦裙'),(15,'jiaoling_ruqun',1,1,6,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','交领襦裙'),(16,'aoqun',1,1,7,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','袄裙'),(17,'mamian_qun',1,1,8,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','马面裙'),(18,'pifeng',1,1,9,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','披风'),(19,'bijia',1,1,10,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','比甲'),(20,'beizi',1,1,11,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','褙子'),(21,'banbi',1,1,12,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','半臂'),(22,'yuanling_pao',1,1,13,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','圆领袍'),(23,'zhiduo',1,1,14,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','直裰/直身'),(24,'daopao',1,1,15,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','道袍'),(25,'yesan',1,1,16,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','曳撒'),(26,'tieli',1,1,17,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','贴里'),(27,'daxiu_shan',1,1,18,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','大袖衫'),(28,'hezi_qun',1,1,19,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','诃子裙'),(29,'song_ku',1,1,20,'2026-03-25 08:57:02','2026-03-25 08:57:02','shape','宋裤'),(30,'qin_han',2,1,1,'2026-03-25 08:57:02','2026-03-25 08:57:02','dynasty','秦汉风'),(31,'wei_jin',2,1,2,'2026-03-25 08:57:02','2026-03-25 08:57:02','dynasty','魏晋风'),(32,'tang',2,1,3,'2026-03-25 08:57:02','2026-03-25 08:57:02','dynasty','唐制'),(33,'song',2,1,4,'2026-03-25 08:57:02','2026-03-25 08:57:02','dynasty','宋制'),(34,'ming',2,1,5,'2026-03-25 08:57:02','2026-03-25 08:57:02','dynasty','明制'),(35,'female',3,1,1,'2026-03-25 08:57:02','2026-03-25 08:57:02','gender','女装汉服'),(36,'male',3,1,2,'2026-03-25 08:57:02','2026-03-25 08:57:02','gender','男装汉服'),(37,'unisex',3,1,3,'2026-03-25 08:57:02','2026-03-25 08:57:02','gender','男女通款汉服'),(38,'daily',4,1,1,'2026-03-25 08:57:02','2026-03-25 08:57:02','scene','日常汉服'),(39,'formal',4,1,2,'2026-03-25 08:57:02','2026-03-25 08:57:02','scene','礼服汉服'),(40,'wedding',4,1,3,'2026-03-25 08:57:02','2026-03-25 08:57:02','scene','婚服汉服'),(41,'ritual',4,1,4,'2026-03-25 08:57:02','2026-03-25 08:57:02','scene','祭祀/礼仪汉服'),(42,'performance',4,1,5,'2026-03-25 08:57:02','2026-03-25 08:57:02','scene','舞台表演汉服'),(43,'shangyi_xiachang',5,1,1,'2026-03-25 08:57:02','2026-03-25 08:57:02','structure','上衣下裳（襦裙类）'),(44,'shenyi',5,1,2,'2026-03-25 08:57:02','2026-03-25 08:57:02','structure','深衣制'),(45,'pao',5,1,3,'2026-03-25 08:57:02','2026-03-25 08:57:02','structure','袍制'),(46,'yiku',5,1,4,'2026-03-25 08:57:02','2026-03-25 08:57:02','structure','衣裤制');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_item`
--

DROP TABLE IF EXISTS `order_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_item` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '订单项ID',
  `order_id` bigint NOT NULL COMMENT '订单主表ID',
  `order_no` varchar(32) NOT NULL COMMENT '订单编号',
  `product_id` bigint NOT NULL COMMENT '商品ID',
  `product_name` varchar(255) NOT NULL COMMENT '商品名称（快照）',
  `product_image` varchar(255) DEFAULT NULL COMMENT '商品主图',
  `price` decimal(10,2) NOT NULL COMMENT '下单时单价',
  `quantity` int NOT NULL COMMENT '购买数量',
  `total_price` decimal(10,2) NOT NULL COMMENT '商品小计',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `is_rent` int DEFAULT '0',
  `rent_date` int DEFAULT '0',
  `deposit` float(12,4) DEFAULT '0.0000',
  PRIMARY KEY (`id`),
  KEY `idx_order_id` (`order_id`),
  KEY `idx_order_no` (`order_no`),
  KEY `idx_product_id` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='订单商品明细表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_item`
--

LOCK TABLES `order_item` WRITE;
/*!40000 ALTER TABLE `order_item` DISABLE KEYS */;
INSERT INTO `order_item` VALUES (1,11,'2719897470',7,'明制圆领袍',NULL,279.00,1,279.00,'2026-03-26 04:18:15',0,0,0.0000),(2,14,'2356788176',9,'Drunken Beauty Hanfu Set','/statics/product/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-26 04:34:05',0,0,0.0000),(7,19,'1509348099',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,10,3054.00,'2026-03-28 04:04:14',0,0,0.0000),(8,20,'2609240115',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:06:18',0,0,0.0000),(9,21,'2140362191',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:06:58',0,0,0.0000),(10,22,'5360712970',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:11:14',0,0,0.0000),(11,23,'2068481733',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,2,610.80,'2026-03-28 04:11:38',0,0,0.0000),(12,24,'2621186652',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:12:28',0,0,0.0000),(13,25,'2447606540',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:13:06',0,0,0.0000),(14,26,'2772832838',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:13:37',0,0,0.0000),(15,27,'2976336908',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:15:42',0,0,0.0000),(16,28,'3121514950',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:15:54',0,0,0.0000),(17,29,'1672140526',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:18:08',0,0,0.0000),(18,30,'1314207233',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:19:57',0,0,0.0000),(19,31,'1138598963',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:20:07',0,0,0.0000),(20,32,'2502029573',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:21:44',0,0,0.0000),(21,33,'2869087927',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:22:02',0,0,0.0000),(22,34,'1667895151',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:22:52',0,0,0.0000),(23,35,'1774262511',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:23:45',0,0,0.0000),(24,36,'3490541932',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:24:02',0,0,0.0000),(25,37,'2547973170',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:27:42',0,0,0.0000),(26,38,'2200237111',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,4,1221.60,'2026-03-28 04:29:46',0,0,0.0000),(27,39,'2494786004',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 04:41:22',0,0,0.0000),(28,39,'2494786004',8,'儿童唐制襦裙',NULL,129.00,1,129.00,'2026-03-28 04:41:22',0,0,0.0000),(29,39,'2494786004',6,'晋制大袖男装',NULL,259.00,1,259.00,'2026-03-28 04:41:22',0,0,0.0000),(30,39,'2494786004',7,'明制圆领袍',NULL,279.00,1,279.00,'2026-03-28 04:41:22',0,0,0.0000),(31,40,'1395027520',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,4,1221.60,'2026-03-28 12:43:22',0,0,0.0000),(32,41,'3237494432',6,'晋制大袖男装',NULL,259.00,1,259.00,'2026-03-28 12:54:02',0,0,0.0000),(33,42,'2937738782',7,'明制圆领袍',NULL,279.00,1,279.00,'2026-03-28 12:56:15',0,0,0.0000),(34,43,'3019883033',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,2,610.80,'2026-03-28 12:58:26',0,0,0.0000),(35,44,'1189873975',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,2,610.80,'2026-03-28 12:59:30',0,0,0.0000),(36,45,'1082983276',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 13:00:39',0,0,0.0000),(37,46,'3139914022',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,8,2443.20,'2026-03-28 13:41:52',0,0,0.0000),(38,47,'1798938246',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 13:42:16',0,0,0.0000),(39,48,'1510090234',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,1,305.40,'2026-03-28 14:18:33',0,0,0.0000),(40,48,'1510090234',8,'儿童唐制襦裙',NULL,129.00,1,129.00,'2026-03-28 14:18:33',0,0,0.0000),(41,49,'3613510105',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,2,610.80,'2026-03-29 09:24:47',0,0,0.0000),(42,50,'3053369142',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,2,610.80,'2026-03-29 09:33:41',0,0,0.0000),(43,51,'1916546116',9,'Drunken Beauty Hanfu Set','/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',305.40,10,3054.00,'2026-03-29 09:39:45',0,0,0.0000),(44,52,'1727420489',11,'Chinese Style Vintage Sweet Fairy Hanfu Dress Ancient Trad','/static/products/3.webp',184.96,1,184.96,'2026-03-29 10:07:03',0,0,0.0000),(45,53,'1481881367',18,'Men\'s Wuxia Style Hanfu for COS Performance','/static/products/10.webp',198.00,2,396.00,'2026-03-29 10:58:10',0,0,0.0000),(46,54,'1151985337',18,'Men\'s Wuxia Style Hanfu for COS Performance','/static/products/10.webp',198.00,1,198.00,'2026-03-29 11:00:03',0,0,0.0000),(47,55,'4403861468',18,'Men\'s Wuxia Style Hanfu for COS Performance','/static/products/10.webp',198.00,1,198.00,'2026-03-29 11:03:54',0,0,0.0000),(48,58,'3395913630',18,'Men\'s Wuxia Style Hanfu for COS Performance','/static/products/10.webp',198.00,5,990.00,'2026-03-30 05:45:06',0,NULL,0.0000),(49,59,'9230845121',21,'Ming-Style Hanfu Wedding Gown (Male)','/static/products/12.webp',799.00,5,3995.00,'2026-03-30 05:45:29',1,5,100.0000),(50,60,'2564268142',21,'Ming-Style Hanfu Wedding Gown (Male)','/static/products/12.webp',799.00,1,799.00,'2026-03-30 06:33:05',1,7,0.0000),(51,61,'8884827572',21,'Ming-Style Hanfu Wedding Gown (Male)','/static/products/12.webp',799.00,3,2397.00,'2026-03-30 06:33:24',1,7,0.0000),(52,62,'1011630483',21,'Ming-Style Hanfu Wedding Gown (Male)','/static/products/12.webp',799.00,2,1598.00,'2026-03-30 06:34:09',1,11,0.0000),(53,63,'1928121300',21,'Ming-Style Hanfu Wedding Gown (Male)','/static/products/12.webp',799.00,2,1598.00,'2026-03-30 06:37:07',1,7,100.0000),(54,64,'7736120239',21,'Ming-Style Hanfu Wedding Gown (Male)','/static/products/12.webp',799.00,1,799.00,'2026-03-30 06:41:09',1,7,100.0000),(55,64,'7736120239',20,'Hanfu Product','/static/products/13.webp',199.00,1,199.00,'2026-03-30 06:41:09',1,7,100.0000),(56,64,'7736120239',19,'Oil Paper Umbrella - Red','/static/products/11.webp',88.00,1,88.00,'2026-03-30 06:41:09',0,7,100.0000);
/*!40000 ALTER TABLE `order_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_main`
--

DROP TABLE IF EXISTS `order_main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_main` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '订单ID',
  `order_no` varchar(32) NOT NULL COMMENT '订单编号（唯一）',
  `user_id` bigint NOT NULL COMMENT '用户ID',
  `total_amount` decimal(10,2) NOT NULL COMMENT '订单总金额',
  `pay_amount` decimal(10,2) NOT NULL COMMENT '实付金额',
  `freight_amount` decimal(10,2) DEFAULT '0.00' COMMENT '运费',
  `discount_amount` decimal(10,2) DEFAULT '0.00' COMMENT '优惠金额',
  `order_status` tinyint NOT NULL DEFAULT '0' COMMENT '订单状态：0待付款 1待发货 2待收货 3已完成 4已关闭',
  `pay_status` tinyint NOT NULL DEFAULT '0' COMMENT '支付状态：0未支付 1已支付',
  `pay_type` tinyint DEFAULT NULL COMMENT '支付方式：1微信 2支付宝',
  `pay_time` datetime DEFAULT NULL COMMENT '支付时间',
  `delivery_time` datetime DEFAULT NULL COMMENT '发货时间',
  `receive_time` datetime DEFAULT NULL COMMENT '确认收货时间',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  `is_deleted` tinyint NOT NULL DEFAULT '0' COMMENT '是否删除：0正常 1删除',
  `currency` varchar(10) DEFAULT 'USD',
  `consignee` varchar(64) DEFAULT NULL COMMENT '收件人姓名',
  `address` varchar(255) DEFAULT NULL COMMENT '详细地址',
  `country_code` varchar(20) DEFAULT NULL COMMENT '国家代码',
  `state` varchar(64) DEFAULT NULL COMMENT '州/省',
  `city` varchar(64) DEFAULT NULL COMMENT '城市',
  `zip_code` varchar(20) DEFAULT NULL COMMENT '邮编',
  `is_commented` tinyint DEFAULT '0' COMMENT '是否已评论 0未评论 1已评论',
  `is_rent` int DEFAULT NULL,
  `deposit` float(12,4) DEFAULT '0.0000',
  PRIMARY KEY (`id`),
  KEY `idx_user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='订单主表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_main`
--

LOCK TABLES `order_main` WRITE;
/*!40000 ALTER TABLE `order_main` DISABLE KEYS */;
INSERT INTO `order_main` VALUES (11,'2719897470',8,279.00,279.00,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-26 04:18:15','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(14,'2356788176',8,305.40,305.40,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-26 04:34:05','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(19,'1509348099',8,3054.00,3054.00,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 04:04:14','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(20,'2609240115',8,305.40,305.40,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 04:06:18','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(21,'2140362191',8,305.40,305.40,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 04:06:58','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(22,'5360712970',8,305.40,305.40,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 04:11:14','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(23,'2068481733',8,610.80,610.80,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 04:11:38','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(24,'2621186652',8,305.40,305.40,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 04:12:28','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(25,'2447606540',8,305.40,305.40,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 04:13:06','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(26,'2772832838',8,305.40,305.40,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 04:13:37','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(27,'2976336908',8,305.40,305.40,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 04:15:42','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(28,'3121514950',8,305.40,305.40,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 04:15:54','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(29,'1672140526',8,305.40,305.40,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 04:18:08','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(30,'1314207233',8,305.40,305.40,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 04:19:57','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(31,'1138598963',8,305.40,305.40,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 04:20:07','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(32,'2502029573',8,305.40,305.40,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 04:21:44','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(33,'2869087927',8,305.40,305.40,0.00,0.00,1,2,1,NULL,NULL,NULL,'2026-03-28 04:22:02','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(34,'1667895151',8,305.40,305.40,0.00,0.00,1,2,1,NULL,NULL,NULL,'2026-03-28 04:22:52','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(35,'1774262511',8,305.40,305.40,0.00,0.00,1,2,1,NULL,NULL,NULL,'2026-03-28 04:23:45','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(36,'3490541932',8,305.40,305.40,0.00,0.00,3,2,1,NULL,NULL,NULL,'2026-03-28 04:24:02','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(37,'2547973170',8,305.40,305.40,0.00,0.00,3,2,1,NULL,NULL,NULL,'2026-03-28 04:27:42','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(38,'2200237111',8,1221.60,1221.60,0.00,0.00,3,2,1,NULL,NULL,NULL,'2026-03-28 04:29:45','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(39,'2494786004',8,972.40,972.40,0.00,0.00,3,2,1,NULL,NULL,NULL,'2026-03-28 04:41:22','2026-03-30 04:53:18',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(40,'1395027520',8,1221.60,1221.60,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 12:43:22','2026-03-30 04:51:52',0,'USD',NULL,NULL,NULL,NULL,NULL,NULL,0,0,0.0000),(41,'3237494432',8,259.00,259.00,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 12:54:02','2026-03-30 04:51:51',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,0.0000),(42,'2937738782',8,279.00,279.00,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 12:56:15','2026-03-30 04:51:51',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,0.0000),(43,'3019883033',8,610.80,610.80,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 12:58:26','2026-03-30 04:51:51',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,0.0000),(44,'1189873975',8,610.80,610.80,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 12:59:30','2026-03-30 04:51:51',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,0.0000),(45,'1082983276',8,305.40,305.40,0.00,0.00,3,2,1,NULL,NULL,NULL,'2026-03-28 13:00:39','2026-03-30 04:51:51',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',1,0,0.0000),(46,'3139914022',8,2443.20,2443.20,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-28 13:41:52','2026-03-30 04:51:51',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,0.0000),(47,'1798938246',8,305.40,305.40,0.00,0.00,3,2,1,NULL,NULL,NULL,'2026-03-28 13:42:16','2026-03-30 04:51:51',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',1,0,0.0000),(48,'1510090234',8,434.40,434.40,0.00,0.00,3,2,1,NULL,NULL,NULL,'2026-03-28 14:18:33','2026-03-30 04:51:51',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',1,0,0.0000),(49,'3613510105',8,610.80,610.80,0.00,0.00,1,2,1,NULL,NULL,NULL,'2026-03-29 09:24:47','2026-03-30 04:51:51',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,0.0000),(50,'3053369142',8,610.80,610.80,0.00,0.00,1,2,1,NULL,NULL,NULL,'2026-03-29 09:33:40','2026-03-30 04:51:51',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,0.0000),(51,'1916546116',8,3054.00,3054.00,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-29 09:39:45','2026-03-30 04:51:51',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,0.0000),(52,'1727420489',8,184.96,184.96,0.00,0.00,1,2,1,NULL,NULL,NULL,'2026-03-29 10:07:03','2026-03-30 04:52:06',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,90.0000),(53,'1481881367',8,396.00,396.00,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-29 10:58:09','2026-03-30 04:51:52',0,'USD','adfa','adsf','adf','afadf','asdf','adf',0,0,0.0000),(54,'1151985337',8,198.00,198.00,0.00,0.00,3,2,1,NULL,NULL,NULL,'2026-03-29 11:00:03','2026-03-30 05:00:05',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,0.0000),(55,'4403861468',8,198.00,198.00,0.00,0.00,3,2,1,NULL,NULL,NULL,'2026-03-29 11:03:54','2026-03-30 04:52:06',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',1,1,80.0000),(58,'3395913630',8,2180.00,2180.00,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-30 05:45:06','2026-03-30 05:45:06',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,0.0000),(59,'9230845121',8,4495.00,4495.00,0.00,0.00,3,2,1,NULL,NULL,NULL,'2026-03-30 05:45:29','2026-03-30 06:22:21',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',1,0,500.0000),(60,'2564268142',8,899.00,899.00,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-30 06:33:05','2026-03-30 06:33:05',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,0.0000),(61,'8884827572',8,2697.00,2697.00,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-30 06:33:24','2026-03-30 06:33:24',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,0.0000),(62,'1011630483',8,1798.00,1798.00,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-30 06:34:09','2026-03-30 06:34:09',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,0.0000),(63,'1928121300',8,1798.00,1798.00,0.00,0.00,0,0,NULL,NULL,NULL,NULL,'2026-03-30 06:37:07','2026-03-30 06:37:07',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,200.0000),(64,'7736120239',8,1386.00,1386.00,0.00,0.00,1,2,1,NULL,NULL,NULL,'2026-03-30 06:41:09','2026-03-30 06:41:30',0,'USD','fanyan','10 rd, swalmail rd','8','az','flag','86001',0,0,300.0000);
/*!40000 ALTER TABLE `order_main` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_comment`
--

DROP TABLE IF EXISTS `product_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_comment` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '评价ID',
  `product_id` bigint unsigned NOT NULL COMMENT '商品ID',
  `user_id` bigint unsigned NOT NULL COMMENT '用户ID',
  `order_item_id` bigint unsigned DEFAULT NULL COMMENT '订单项ID',
  `score` tinyint NOT NULL COMMENT '评分 1-5',
  `content` text NOT NULL COMMENT '评价内容',
  `image_list` varchar(1024) DEFAULT NULL COMMENT '图片地址,逗号分隔',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `username` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_product_id` (`product_id`),
  KEY `idx_user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='商品评价表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_comment`
--

LOCK TABLES `product_comment` WRITE;
/*!40000 ALTER TABLE `product_comment` DISABLE KEYS */;
INSERT INTO `product_comment` VALUES (1,1,1,1,5,'衣服非常好看！',NULL,'2026-03-25 07:38:04',''),(2,2,2,2,4,'质量不错',NULL,'2026-03-25 07:38:04',''),(3,9,8,NULL,1,'haode ',NULL,'2026-03-24 21:28:12',''),(4,9,8,NULL,1,'haode ',NULL,'2026-03-24 21:30:28',''),(5,9,8,NULL,1,'haode ',NULL,'2026-03-24 21:31:10','aa'),(6,9,8,NULL,1,'haode ',NULL,'2026-03-24 21:31:24','aa'),(7,9,8,NULL,1,'haode ',NULL,'2026-03-24 21:33:41','miaomiao'),(8,9,8,NULL,5,'adadfadfadfaf',NULL,'2026-03-27 22:32:32','miaomiao'),(9,9,8,NULL,5,'dadfadfas',NULL,'2026-03-27 22:33:01','miaomiao'),(10,9,8,NULL,5,'adfadfa',NULL,'2026-03-27 22:33:50','miaomiao'),(11,9,8,NULL,5,'aafd',NULL,'2026-03-27 22:41:34','miaomiao'),(12,9,8,NULL,5,'河东时候',NULL,'2026-03-27 22:42:33','miaomiao'),(13,9,8,NULL,5,'wo juede tinghaode ',NULL,'2026-03-27 23:20:19','miaomiao'),(14,18,8,NULL,5,'good',NULL,'2026-03-28 20:04:32','miaomiao'),(15,21,8,NULL,5,'1234',NULL,'2026-03-29 15:22:22','miaomiao');
/*!40000 ALTER TABLE `product_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_image`
--

DROP TABLE IF EXISTS `product_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_image` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '图片ID',
  `product_id` bigint unsigned NOT NULL COMMENT '商品ID',
  `url` varchar(512) NOT NULL COMMENT '图片地址',
  `sort` int NOT NULL DEFAULT '0' COMMENT '排序',
  `is_cover` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否封面 1=是',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_product_id` (`product_id`),
  CONSTRAINT `product_image_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product_main` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='商品图片表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_image`
--

LOCK TABLES `product_image` WRITE;
/*!40000 ALTER TABLE `product_image` DISABLE KEYS */;
INSERT INTO `product_image` VALUES (6,9,'/static/products/O1CN01FvJPjA2Kw0z4lzSvh_!!2215738439620.jpg_.webp',2,1,'2026-03-25 09:11:26'),(7,9,'/static/products/O1CN01RPFMfR2Kw0ysH2McN_!!2215738439620.jpg_.webp',1,0,'2026-03-25 09:16:22'),(9,9,'/static/products/O1CN01Y2Q0aD2Kw0z6Plu2n_!!2215738439620.jpg_.webp',3,0,'2026-03-25 09:17:16'),(10,9,'/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',4,0,'2026-03-25 09:17:16'),(11,10,'/static/products/O1CN01bvJdNL1bQGwIdjlum_!!2215546883459.jpg_.webp',0,1,'2026-03-29 09:54:45'),(12,10,'/static/products/O1CN01jDWOWW1bQGwIdjR7L_!!2215546883459.jpg_.webp',1,0,'2026-03-29 09:54:45'),(13,10,'/static/products/O1CN01MD7fOf1bQGwDmM5rZ_!!2215546883459.jpg_.webp',2,0,'2026-03-29 09:54:45'),(14,10,'/static/products/O1CN01POFLtx1bQGwIdk2hz_!!2215546883459.jpg_.webp',3,0,'2026-03-29 09:54:45'),(19,11,'/static/products/3.webp',0,1,'2026-03-29 10:05:49'),(20,11,'/static/products/3.1.webp',1,0,'2026-03-29 10:05:49'),(21,11,'/static/products/3.2.webp',2,0,'2026-03-29 10:05:49'),(22,11,'/static/products/3.3.webp',3,0,'2026-03-29 10:05:49'),(23,12,'/static/products/4.1.webp',0,1,'2026-03-29 10:13:34'),(24,12,'/static/products/4.2.webp',1,0,'2026-03-29 10:13:34'),(25,12,'/static/products/4.3.webp',2,0,'2026-03-29 10:13:34'),(26,12,'/static/products/4.5.webp',3,0,'2026-03-29 10:13:34'),(27,13,'/static/products/5.1.webp',0,1,'2026-03-29 10:20:08'),(28,14,'/static/products/6.1.webp',0,1,'2026-03-29 10:24:03'),(29,14,'/static/products/6.2.webp',1,0,'2026-03-29 10:24:03'),(30,14,'/static/products/6.3.webp',2,0,'2026-03-29 10:24:03'),(32,15,'/static/products/7.webp',2,1,'2026-03-29 10:27:11'),(33,15,'/static/products/7.3.webp',3,0,'2026-03-29 10:27:11'),(34,15,'/static/products/7.4.webp',4,0,'2026-03-29 10:27:11'),(35,15,'/static/products/7.1.webp',1,0,'2026-03-29 10:27:11'),(36,16,'/static/products/8.webp',0,1,'2026-03-29 10:40:36'),(38,17,'/static/products/9.webp',0,1,'2026-03-29 10:45:45'),(39,17,'/static/products/9.1.webp',1,0,'2026-03-29 10:45:45'),(40,17,'/static/products/9.2.webp',2,0,'2026-03-29 10:45:45'),(41,17,'/static/products/9.3.webp',3,0,'2026-03-29 10:45:45'),(42,18,'/static/products/10.webp',0,1,'2026-03-29 10:50:14'),(43,18,'/static/products/10.1.webp',1,0,'2026-03-29 10:50:14'),(44,19,'/static/products/11.webp',0,1,'2026-03-29 10:40:36'),(45,19,'/static/products/11.1.webp',0,1,'2026-03-29 10:40:36'),(48,20,'/static/products/13.webp',3,0,'2026-03-30 01:48:48'),(49,20,'/static/products/13.1.jpg',2,0,'2026-03-30 01:48:48'),(50,20,'/static/products/13.2.webp',1,1,'2026-03-30 01:48:48'),(51,21,'/static/products/12.webp',0,1,'2026-03-30 01:52:50'),(52,21,'/static/products/12.1.webp',1,0,'2026-03-30 01:52:50');
/*!40000 ALTER TABLE `product_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_main`
--

DROP TABLE IF EXISTS `product_main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_main` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '商品ID',
  `product_sn` varchar(64) NOT NULL COMMENT '商品编号',
  `name` varchar(255) NOT NULL COMMENT '服装名称',
  `category_id` bigint unsigned NOT NULL COMMENT '分类ID',
  `brand` varchar(64) DEFAULT NULL COMMENT '品牌',
  `price` decimal(12,2) NOT NULL COMMENT '售价',
  `deposit` decimal(12,2) DEFAULT NULL COMMENT 'deposit',
  `cost_price` decimal(12,2) DEFAULT NULL COMMENT '成本价',
  `status` tinyint NOT NULL DEFAULT '1' COMMENT '1=上架 0=下架',
  `is_deleted` tinyint(1) NOT NULL DEFAULT '0' COMMENT '逻辑删除',
  `sort` int NOT NULL DEFAULT '0' COMMENT '排序',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `scene_id` bigint unsigned DEFAULT NULL COMMENT '场景ID',
  `name_cn` varchar(200) DEFAULT NULL COMMENT '中文名称',
  `name_en` varchar(200) DEFAULT NULL COMMENT '英文名称',
  `dynasty_style` varchar(50) DEFAULT NULL COMMENT '朝代风格',
  `gender` varchar(100) DEFAULT NULL COMMENT 'xingbie',
  `shape_system` varchar(100) DEFAULT NULL COMMENT '形制体系',
  `base_price` decimal(12,2) DEFAULT NULL COMMENT '基础价格(默认结算币种)',
  `is_rental_available` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否可租赁 1=是',
  `is_customizable` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否可定制 1=是',
  `content` text COMMENT 'text',
  `cover` varchar(150) DEFAULT NULL,
  `stock` int NOT NULL DEFAULT '0',
  `structure` varchar(100) DEFAULT NULL,
  `usage_scene` varchar(100) DEFAULT NULL COMMENT 'yongtu',
  `warehouse` varchar(100) DEFAULT NULL,
  `body_fit` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_sn` (`product_sn`),
  KEY `idx_category_id` (`category_id`),
  KEY `idx_status` (`status`),
  KEY `idx_is_deleted` (`is_deleted`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='商品主表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_main`
--

LOCK TABLES `product_main` WRITE;
/*!40000 ALTER TABLE `product_main` DISABLE KEYS */;
INSERT INTO `product_main` VALUES (9,'HF20250325001','Drunken Beauty Hanfu Set',28,'0',305.40,368.00,158.00,1,0,0,'2026-03-25 09:09:51','2026-03-28 18:33:44',35,'醉美人汉服大袖衫襦裙套装','Drunken Beauty Hanfu with Large Sleeves & Ruqun','tang','unisex','Traditional Embroidery, Handmade Edges',305.40,0,0,NULL,'/static/products/O1CN017hUtwr2Kw0z8tQcYx_!!2215738439620.jpg_.webp',8,NULL,'daily','asia','usa_robust'),(10,'HF-PURPLE-001','Hanfu Dress Women Ancient Chinese Hanfu 3pcs Sets Female Fai',1,'BECKHAM 32',490.32,590.00,245.16,1,0,0,'2026-03-29 09:51:41','2026-03-29 10:15:54',1,'紫色三件套女士汉服','Purple 3pcs Set Women\'s Hanfu','wei_jin','female','qiyao_ruqun',490.32,0,0,'紫色三件套女士汉服，包含上衣、下裙与披帛，魏晋风格，宽袖交领设计，适合日常及表演穿着','/static/products/O1CN01MD7fOf1bQGwDmM5rZ_!!2215546883459.jpg_.webp',100,'shenyi','performance','asia','asia_normal'),(11,'HF-BEIGE-001','Chinese Style Vintage Sweet Fairy Hanfu Dress Ancient Trad',1,'Voostac',184.96,210.96,92.48,1,0,0,'2026-03-29 10:01:57','2026-03-29 10:15:54',1,'米色仙气流苏汉服','Beige Sweet Fairy Hanfu Dress','tang','female','quju',184.96,0,0,'米色仙气流苏汉服，重工刺绣，大袖飘逸，适合婚礼、表演及日常穿着','/static/products/3.webp',99,'shangyi_xiachang','wedding','asia','euro_normal'),(12,'HF-EUR-0011','Chinese Style Vintage Sweet Fairy Hanfu Dress',5,'Voostac',184.96,210.96,92.48,1,0,0,'2026-03-29 10:12:45','2026-03-29 10:27:49',1,'复古仙气流苏汉服女款','Vintage Sweet Fairy Hanfu Dress for Women','tang','female','jiaoling_ruqun',184.96,0,0,'European size Hanfu, elegant embroidery, soft fabric, suitable for daily wear, party and performance.','/static/products/4.1.webp',100,'shangyi_xiachang','daily','europe','euro_normal'),(13,'HF-HAIRPIN-001','2023 New Chinese Hair Girls Vintage Wedding Hanfu Decor Hair Pin',1,NULL,22.57,28.00,11.29,1,0,0,'2026-03-29 10:19:36','2026-03-30 01:23:09',1,'复古中式汉服发簪 婚礼头饰','Vintage Chinese Hanfu Hairpin for Wedding & Daily Wear','ming','female','toushi',22.57,0,0,'琉璃花瓣+珍珠设计，古风发簪，适配汉服造型，适合婚礼、日常及表演佩戴，发货地北京，亚洲仓储存货。','/static/products/5.1.webp',100,NULL,'wedding','asia','asia_normal'),(14,'HF-TANG-0014','Sui Chang An Tang Style Round Collar Printed Hanfu Robe',5,'诗野原创汉服',138.00,168.00,69.00,1,0,0,'2026-03-29 10:23:28','2026-03-29 10:27:49',1,'岁长安 唐制圆领袍印花汉服','Sui Chang An Tang Style Round Collar Printed Hanfu','tang','female','yuanling_pao',138.00,0,0,'唐制圆领袍，印花大放量设计，春秋款，复原蓝色灯笼裤，含腰带，适合日常及汉服活动，山东菏泽发货，亚洲仓储存货。','/static/products/6.1.webp',200,'pao','daily','asia','asia_normal'),(15,'HF-TANG-M-015','Bi Cheng Tang Style Men\'s Round Collar Robe Linen Hanfu',5,'池夏',68.00,88.00,34.00,1,0,0,'2026-03-29 10:27:11','2026-03-29 10:27:49',1,'【碧城】唐制人棉圆领袍亚麻灯笼裤改良汉服','Bi Cheng Tang Style Men\'s Round Collar Robe & Linen Lantern Pants','tang','male','yuanling_pao',68.00,0,0,'唐制改良汉服，人棉圆领袍+亚麻灯笼裤，大放量设计，适合春秋日常穿着，美洲仓发货，适配美洲男性身材。','/static/products/7.1.webp',200,'pao','daily','north_america','usa_regular'),(16,'HF-QING-016','Qing Style Changyi Mamian Qun Hanfu for Women',5,'曼工坊',218.00,368.00,109.00,1,0,0,'2026-03-29 10:39:39','2026-03-29 10:39:39',1,'清朝圆领斜襟氅衣马面裙全套汉服','Qing Style Round Collar Changyi & Mamian Qun Full Set Hanfu','ming','female','aoqun',218.00,0,0,'原创清朝风格汉服，圆领斜襟氅衣+马面裙，重工刺绣，适合正式场合、表演及汉服活动，山东菏泽发货，亚洲仓储存货。','/static/products/8.webp',100,'shangyi_xiachang','formal','asia','asia_normal'),(17,'HF-TANG-WED-017','Ru Yi Jin Cha Tang Style Hezi Qun Hanfu for Wedding',5,'月梳茼',223.00,268.00,111.50,1,0,0,'2026-03-29 10:45:45','2026-03-29 10:45:45',1,'【如意金钗】唐制诃子裙重工刺绣汉服婚礼套装','Ru Yi Jin Cha Tang Style Hezi Qun Hanfu with Heavy Embroidery for Wedding','tang','female','qixiong_ruqun',223.00,0,0,'唐制改良齐胸诃子裙，重工刺绣大袖衫+裙子+披帛+腰链全套，适合婚礼、正式场合及汉服婚服穿着，山东菏泽发货，亚洲仓储存货。','/static/products/9.webp',300,'shangyi_xiachang','wedding','asia','asia_normal'),(18,'HF-MALE-WUXIA-017','Men\'s Wuxia Style Hanfu for COS Performance',5,'柒小爱汉服居',198.00,238.00,99.00,1,0,0,'2026-03-29 10:50:14','2026-03-29 14:00:02',1,'侠骨伞影男士武侠风汉服COS剧服','Men\'s Wuxia Style Hanfu for Drama & COS','wei_jin','male','daopao',198.00,0,0,'白色武侠风男士汉服，道袍形制，飘逸大袖，适合COS、表演及古风拍摄，亚洲仓发货，适配亚洲男性身材。','/static/products/10.webp',198,'pao','performance','asia','asia_normal'),(19,'PRD202603300019','Oil Paper Umbrella - Red',10,'蜀泸印象',88.00,100.00,45.00,1,0,0,'2026-03-30 01:33:41','2026-03-29 15:41:30',40,'非遗油纸伞（枣红/中国红）','Intangible Cultural Heritage Oil Paper Umbrella','ming','unisex','yesan',88.00,0,1,'非遗油纸伞，纯手工制作，传统桐油工艺，可防雨防晒，适用于中式结婚、摄影等场景，提供枣红与中国红两种颜色选择。','/static/products/11.webp',199,'yiku','wedding','north_america','unisex_relaxed'),(20,'PRD19001','Hanfu Product',10,'Hanfu Brand',199.00,100.00,99.00,1,0,0,'2026-03-30 01:48:25','2026-03-29 15:41:30',38,'汉服款式','Hanfu Style','ming','female','quju',199.00,1,0,'汉服商品详情描述','/static/products/13.webp',99,'shenyi','wedding','asia','asia_normal'),(21,'PRD202603300021','Ming-Style Hanfu Wedding Gown (Male)',16,'十一时',799.00,100.00,450.00,1,0,0,'2026-03-30 01:52:31','2026-03-29 15:41:30',40,'明制汉服婚服重工礼服（良缘男款）','Ming-Style Hanfu Wedding Attire (Male Version)','ming','male','aoqun',799.00,1,0,'明制汉服婚服，重工刺绣，传统中式婚礼礼服，适合新郎穿着，搭配官帽与精致纹样，尽显庄重华贵。','/static/products/12.webp',144,'pao','wedding','north_america','usa_regular');
/*!40000 ALTER TABLE `product_main` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_related`
--

DROP TABLE IF EXISTS `product_related`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_related` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `product_id` bigint unsigned NOT NULL COMMENT '主商品ID',
  `related_id` bigint unsigned NOT NULL COMMENT '关联商品ID',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_product_related` (`product_id`,`related_id`),
  KEY `idx_product_id` (`product_id`),
  KEY `idx_related_id` (`related_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='商品关联表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_related`
--

LOCK TABLES `product_related` WRITE;
/*!40000 ALTER TABLE `product_related` DISABLE KEYS */;
INSERT INTO `product_related` VALUES (1,17,13,'2026-03-30 00:51:36'),(3,17,19,'2026-03-30 01:19:01'),(4,20,21,'2026-03-30 01:53:47'),(5,20,13,'2026-03-30 01:53:47'),(6,20,19,'2026-03-30 01:53:47'),(7,21,19,'2026-03-30 01:55:45'),(8,21,20,'2026-03-30 01:55:45'),(9,21,13,'2026-03-30 01:55:45');
/*!40000 ALTER TABLE `product_related` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_size_stock`
--

DROP TABLE IF EXISTS `product_size_stock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_size_stock` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `product_id` bigint unsigned NOT NULL,
  `size_id` bigint unsigned NOT NULL COMMENT '关联size_standard表',
  `stock_quantity` int DEFAULT '0' COMMENT '当前库存',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_deleted` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  KEY `size_id` (`size_id`),
  CONSTRAINT `product_size_stock_ibfk_2` FOREIGN KEY (`size_id`) REFERENCES `size_standard` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='商品尺码库存映射表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_size_stock`
--

LOCK TABLES `product_size_stock` WRITE;
/*!40000 ALTER TABLE `product_size_stock` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_size_stock` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_sku`
--

DROP TABLE IF EXISTS `product_sku`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_sku` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT 'SKU ID',
  `product_id` bigint unsigned NOT NULL COMMENT '商品ID',
  `sku_sn` varchar(64) NOT NULL COMMENT 'SKU编码',
  `color` varchar(32) NOT NULL COMMENT '颜色',
  `size` varchar(32) NOT NULL COMMENT '尺码 S/M/L/XL',
  `barcode` varchar(64) DEFAULT NULL COMMENT '条形码',
  `price` decimal(12,2) NOT NULL COMMENT 'SKU售价',
  `stock` int NOT NULL DEFAULT '0' COMMENT '库存',
  `lock_stock` int NOT NULL DEFAULT '0' COMMENT '锁定库存',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sku_sn` (`sku_sn`),
  KEY `idx_product_id` (`product_id`),
  CONSTRAINT `product_sku_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product_main` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='商品SKU表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_sku`
--

LOCK TABLES `product_sku` WRITE;
/*!40000 ALTER TABLE `product_sku` DISABLE KEYS */;
INSERT INTO `product_sku` VALUES (8,9,'sky-S','normal','S','BC2345 ',305.40,90,0,'2026-03-25 11:47:03','2026-03-25 11:47:03');
/*!40000 ALTER TABLE `product_sku` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shopping_cart`
--

DROP TABLE IF EXISTS `shopping_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shopping_cart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL COMMENT '用户ID',
  `product_id` bigint DEFAULT NULL COMMENT '普通商品ID',
  `quantity` int NOT NULL DEFAULT '1' COMMENT '购买数量',
  `selected` tinyint DEFAULT '1' COMMENT '是否选中 1=选中 0=未选中',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_deleted` tinyint DEFAULT '0',
  `is_rent` int DEFAULT NULL,
  `rent_date` int DEFAULT '0',
  `deposit` float(12,4) DEFAULT '0.0000',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='购物车';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shopping_cart`
--

LOCK TABLES `shopping_cart` WRITE;
/*!40000 ALTER TABLE `shopping_cart` DISABLE KEYS */;
INSERT INTO `shopping_cart` VALUES (1,8,90,18,1,'2026-03-25 12:55:43','2026-03-26 04:29:46',1,NULL,0,0.0000),(2,8,8,2,1,'2026-03-25 13:17:37','2026-03-25 13:23:55',1,NULL,0,0.0000),(3,8,7,1,1,'2026-03-25 13:19:28','2026-03-26 04:18:15',1,NULL,0,0.0000),(10,8,9,1,1,'2026-03-26 04:34:05','2026-03-26 04:34:05',1,NULL,0,0.0000),(17,8,9,10,1,'2026-03-28 04:04:14','2026-03-28 04:04:14',1,NULL,0,0.0000),(18,8,9,1,1,'2026-03-28 04:06:18','2026-03-28 04:06:18',1,NULL,0,0.0000),(19,8,9,1,1,'2026-03-28 04:06:59','2026-03-28 04:06:59',1,NULL,0,0.0000),(20,8,9,1,1,'2026-03-28 04:11:14','2026-03-28 04:11:14',1,NULL,0,0.0000),(21,8,9,2,1,'2026-03-28 04:11:38','2026-03-28 04:11:38',1,NULL,0,0.0000),(22,8,9,1,1,'2026-03-28 04:12:28','2026-03-28 04:12:28',1,NULL,0,0.0000),(23,8,9,1,1,'2026-03-28 04:13:06','2026-03-28 04:13:06',1,NULL,0,0.0000),(24,8,9,1,1,'2026-03-28 04:13:37','2026-03-28 04:13:37',1,NULL,0,0.0000),(25,8,9,1,1,'2026-03-28 04:15:42','2026-03-28 04:15:42',1,NULL,0,0.0000),(26,8,9,1,1,'2026-03-28 04:15:54','2026-03-28 04:15:54',1,NULL,0,0.0000),(27,8,9,1,1,'2026-03-28 04:18:08','2026-03-28 04:18:08',1,NULL,0,0.0000),(28,8,9,1,1,'2026-03-28 04:19:57','2026-03-28 04:19:57',1,NULL,0,0.0000),(29,8,9,1,1,'2026-03-28 04:20:07','2026-03-28 04:20:07',1,NULL,0,0.0000),(30,8,9,1,1,'2026-03-28 04:21:44','2026-03-28 04:21:44',1,NULL,0,0.0000),(31,8,9,1,1,'2026-03-28 04:22:02','2026-03-28 04:22:02',1,NULL,0,0.0000),(32,8,9,1,1,'2026-03-28 04:22:52','2026-03-28 04:22:52',1,NULL,0,0.0000),(33,8,9,1,1,'2026-03-28 04:23:45','2026-03-28 04:23:45',1,NULL,0,0.0000),(34,8,9,1,1,'2026-03-28 04:24:02','2026-03-28 04:24:02',1,NULL,0,0.0000),(35,8,9,1,1,'2026-03-28 04:27:42','2026-03-28 04:27:42',1,NULL,0,0.0000),(36,8,9,4,1,'2026-03-28 04:29:46','2026-03-28 04:29:46',1,NULL,0,0.0000),(37,8,9,1,1,'2026-03-28 04:41:22','2026-03-28 04:41:22',1,NULL,0,0.0000),(38,8,8,1,1,'2026-03-28 04:41:22','2026-03-28 04:41:22',1,NULL,0,0.0000),(39,8,6,1,1,'2026-03-28 04:41:22','2026-03-28 04:41:22',1,NULL,0,0.0000),(40,8,7,1,1,'2026-03-28 04:41:22','2026-03-28 04:41:22',1,NULL,0,0.0000),(41,8,9,4,1,'2026-03-28 12:43:22','2026-03-28 12:43:22',1,NULL,0,0.0000),(42,8,2,1,1,'2026-03-28 10:56:24','2026-03-28 10:56:24',1,NULL,0,0.0000),(43,8,7,1,1,'2026-03-28 12:56:15','2026-03-28 12:56:15',1,NULL,0,0.0000),(44,8,6,1,1,'2026-03-28 12:54:02','2026-03-28 12:54:02',1,NULL,0,0.0000),(45,8,9,2,1,'2026-03-28 12:58:26','2026-03-28 12:58:26',1,NULL,0,0.0000),(46,8,9,2,1,'2026-03-28 12:59:30','2026-03-28 12:59:30',1,NULL,0,0.0000),(47,8,9,1,1,'2026-03-28 13:00:39','2026-03-28 13:00:39',1,NULL,0,0.0000),(48,8,9,8,1,'2026-03-28 13:41:52','2026-03-28 13:41:52',1,NULL,0,0.0000),(49,8,8,1,1,'2026-03-28 13:02:19','2026-03-28 13:02:19',1,NULL,0,0.0000),(50,8,9,1,1,'2026-03-28 13:42:16','2026-03-28 13:42:16',1,NULL,0,0.0000),(51,8,9,1,1,'2026-03-28 14:18:33','2026-03-28 14:18:33',1,NULL,0,0.0000),(52,8,8,1,1,'2026-03-28 14:18:33','2026-03-28 14:18:33',1,NULL,0,0.0000),(53,8,9,2,1,'2026-03-29 09:24:47','2026-03-29 09:24:47',1,NULL,0,0.0000),(54,8,9,2,1,'2026-03-29 09:33:41','2026-03-29 09:33:41',1,NULL,0,0.0000),(55,8,9,10,1,'2026-03-29 09:39:45','2026-03-29 09:39:45',1,NULL,0,0.0000),(56,8,11,1,1,'2026-03-29 10:07:03','2026-03-29 10:07:03',1,NULL,0,0.0000),(57,8,18,2,1,'2026-03-29 10:58:10','2026-03-29 10:58:10',1,NULL,0,0.0000),(58,8,18,1,1,'2026-03-29 11:00:03','2026-03-29 11:00:03',1,NULL,0,0.0000),(59,8,18,1,1,'2026-03-29 11:03:54','2026-03-29 11:03:54',1,NULL,0,0.0000),(60,19,18,1,1,'2026-03-30 01:19:16','2026-03-30 01:19:16',0,NULL,0,0.0000),(61,19,13,1,1,'2026-03-30 01:23:27','2026-03-30 01:23:27',0,NULL,0,0.0000),(62,19,21,2,1,'2026-03-30 02:52:06','2026-03-30 02:52:06',0,NULL,0,0.0000),(63,8,21,5,1,'2026-03-30 05:45:29','2026-03-30 05:45:29',1,1,5,100.0000),(64,8,18,5,1,'2026-03-30 05:45:06','2026-03-30 05:45:06',1,0,NULL,0.0000),(65,8,20,1,1,'2026-03-30 06:32:06','2026-03-30 06:32:06',1,0,NULL,0.0000),(66,8,21,1,1,'2026-03-30 06:32:05','2026-03-30 06:32:05',1,0,NULL,0.0000),(67,8,21,1,1,'2026-03-30 06:33:05','2026-03-30 06:33:05',1,1,7,0.0000),(68,8,21,3,1,'2026-03-30 06:33:24','2026-03-30 06:33:24',1,1,7,0.0000),(69,8,21,2,1,'2026-03-30 06:34:09','2026-03-30 06:34:09',1,1,11,0.0000),(70,8,21,2,1,'2026-03-30 06:37:07','2026-03-30 06:37:07',1,1,7,100.0000),(71,8,21,1,1,'2026-03-30 06:41:09','2026-03-30 06:41:09',1,1,7,100.0000),(72,8,20,1,1,'2026-03-30 06:41:09','2026-03-30 06:41:09',1,1,7,100.0000),(73,8,19,1,1,'2026-03-30 06:41:09','2026-03-30 06:41:09',1,0,7,100.0000);
/*!40000 ALTER TABLE `shopping_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `size_standard`
--

DROP TABLE IF EXISTS `size_standard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `size_standard` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `region_type` enum('Asia','Europe','America') COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '地区类型: 亚洲/欧洲/美洲',
  `size_code` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '尺码代码: S/M/L/XL/定制',
  `height_range` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '适用身高范围(cm)',
  `bust_range` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '适用胸围范围(cm)',
  `waist_range` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '适用腰围范围(cm)',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_by` bigint unsigned DEFAULT '0',
  `update_by` bigint unsigned DEFAULT '0',
  `is_deleted` tinyint(1) DEFAULT '0' COMMENT '逻辑删除: 0未删, 1已删',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='尺码标准配置表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `size_standard`
--

LOCK TABLES `size_standard` WRITE;
/*!40000 ALTER TABLE `size_standard` DISABLE KEYS */;
INSERT INTO `size_standard` VALUES (1,'Asia','S','155-160','80-84','62-66','2026-03-23 12:37:42','2026-03-23 12:37:42',0,0,0),(2,'Asia','M','160-165','84-88','66-70','2026-03-23 12:37:42','2026-03-23 12:37:42',0,0,0),(3,'Europe','M','165-175','90-94','72-76','2026-03-23 12:37:42','2026-03-23 12:37:42',0,0,0),(4,'Europe','L','170-180','96-100','78-82','2026-03-23 12:37:42','2026-03-23 12:37:42',0,0,0),(5,'America','XL','170-185','104-108','86-90','2026-03-23 12:37:42','2026-03-23 12:37:42',0,0,0);
/*!40000 ALTER TABLE `size_standard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_addresses`
--

DROP TABLE IF EXISTS `user_addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_addresses` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `consignee` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `country_code` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT 'US',
  `state` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `city` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `zip_code` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_default` tinyint(1) DEFAULT '0',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `idx_user_addresses_user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_addresses`
--

LOCK TABLES `user_addresses` WRITE;
/*!40000 ALTER TABLE `user_addresses` DISABLE KEYS */;
INSERT INTO `user_addresses` VALUES (1,8,'string','string','string','string','1adadfa','string',0,'2026-03-23 17:35:19','2026-03-23 17:35:19'),(3,8,'string','string','string','string','1adadfa','string',0,'2026-03-23 17:42:22','2026-03-23 17:42:22'),(8,8,'string','string','string','string','1adadfa','string',0,'2026-03-24 17:34:07','2026-03-24 17:34:07'),(9,8,'string','86001','string','string','1adadfa','string',0,'2026-03-24 17:34:32','2026-03-24 17:34:32'),(10,8,'adfa','adf','afadf','asdf','adsf','adf',0,'2026-03-28 03:52:49','2026-03-28 03:52:49'),(11,8,'fanyan','8','az','flag','10 rd, swalmail rd','86001',1,'2026-03-28 04:24:05','2026-03-28 04:24:05');
/*!40000 ALTER TABLE `user_addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_main`
--

DROP TABLE IF EXISTS `user_main`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_main` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '用户名/账号',
  `password_hash` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Passlib加密后的密码',
  `phone` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '手机号',
  `email` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '邮箱(全球通行)',
  `member_level` enum('Normal','Silver','Gold','Diamond') COLLATE utf8mb4_unicode_ci DEFAULT 'Normal' COMMENT '会员等级',
  `points` int DEFAULT '0' COMMENT '会员积分',
  `preferred_currency` char(3) COLLATE utf8mb4_unicode_ci DEFAULT 'USD' COMMENT '偏好币种: CNY/USD/EUR',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `create_by` bigint unsigned DEFAULT '0',
  `update_by` bigint unsigned DEFAULT '0',
  `is_deleted` tinyint(1) DEFAULT '0',
  `user_tag` enum('1','2','3','4') COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '1',
  `growth_value` int DEFAULT '0',
  `is_active` int NOT NULL DEFAULT '0',
  `column_name` datetime DEFAULT NULL COMMENT 'last_login',
  `last_login` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `idx_phone_member` (`phone`,`member_level`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='用户主表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_main`
--

LOCK TABLES `user_main` WRITE;
/*!40000 ALTER TABLE `user_main` DISABLE KEYS */;
INSERT INTO `user_main` VALUES (1,'hanfu_lover_01','hash_pw_1','13800000001','user1@example.com','Gold',5000,'CNY','2026-03-23 12:38:11','2026-03-23 12:38:11',0,0,0,'1',0,0,NULL,NULL),(2,'global_atlas','hash_pw_2',NULL,'atlas@euro.com','Silver',1200,'EUR','2026-03-23 12:38:11','2026-03-23 12:38:11',0,0,0,'1',0,0,NULL,NULL),(3,'ny_tester','hash_pw_3','12125550199','test@us.com','Normal',0,'USD','2026-03-23 12:38:11','2026-03-23 12:38:11',0,0,0,'1',0,0,NULL,NULL),(4,'string','12345678','123123','user@example.com',NULL,0,'USD','2026-03-23 15:31:44','2026-03-23 15:31:44',0,0,0,'2',0,1,NULL,NULL),(6,'string1','$argon2id$v=19$m=65536,t=3,p=4$WkuJce7dmzMGIITQOqeUcg$YVSFYOsU5ciUkYUBAWuUSj/tGmL+YiFx22zdQfTT74c','123123','user@example.com',NULL,0,'USD','2026-03-23 15:50:44','2026-03-23 15:50:44',0,0,0,'2',0,1,NULL,NULL),(7,'miao','$argon2id$v=19$m=65536,t=3,p=4$Q+gd4/yfU+r9f89ZixEC4A$sauvvi3FV3QcafkhDFCfrXO3vHzmwT4A6JeczoJbXXc','123123','user@example.com',NULL,0,'USD','2026-03-23 15:50:51','2026-03-23 15:50:51',0,0,0,'2',0,1,NULL,NULL),(8,'miaomiao','$argon2id$v=19$m=65536,t=3,p=4$SMlZ611LiRGidG7N+R8D4A$aQI38A11iErsJlore9JgTK+zzj+WxoSnKRfTXp1e+98','12345678954','user@example.com','Normal',0,'USD','2026-03-24 00:36:31','2026-03-24 00:36:31',0,0,0,'2',0,1,NULL,NULL),(10,'miaomiao1','$argon2id$v=19$m=65536,t=3,p=4$hlAKYQzBeC9lTAnBeK9VSg$+n880KgurSq+VBqCWjRcFHYcHBj+3afA3aXp+7P2KaM','12345678954','user@example.com','Normal',0,'USD','2026-03-24 06:42:46','2026-03-24 06:42:46',0,0,0,'2',0,1,NULL,NULL),(12,'miaomiao3','$argon2id$v=19$m=65536,t=3,p=4$wRgD4FzrfW/NmfP+XwvhnA$S5o86i6CKtgpffd+BSRAJbfwm50mIv1tKD+jlNt5w9k','12345678954','user@example.com','Normal',0,'USD','2026-03-24 06:45:03','2026-03-24 06:45:03',0,0,0,'2',0,1,NULL,NULL),(15,'miaomiao4','$argon2id$v=19$m=65536,t=3,p=4$dW5NKWUsJSTkHGPsPef8Hw$wAalNaNaENmDyS1otY2UjKfxYdECheBSdN3IimVIiBE','12345678954','user@example.com','Normal',0,'USD','2026-03-24 06:49:38','2026-03-24 06:49:38',0,0,0,'2',0,1,NULL,NULL),(16,'miaomiao5','$argon2id$v=19$m=65536,t=3,p=4$0pqTUqrVOkeodU6JUcr5Hw$Lc/8x7LonXclgw8vBwsrP7dgNDoSiGamsbiYc8aBAiE','12345678954','user@example.com','Normal',0,'USD','2026-03-25 01:33:03','2026-03-25 01:33:03',0,0,0,'2',0,1,NULL,NULL),(17,'miaomiao15','$argon2id$v=19$m=65536,t=3,p=4$EEIo5fzf2zsnJKS0ltJ6bw$MqdN48Flu5omzV0ynOLlOKhNfPEm4lQ8esVi9pi17tI',NULL,'user@example.com','Normal',0,'USD','2026-03-26 06:10:05','2026-03-26 06:10:05',0,0,0,'2',0,1,NULL,NULL),(18,'miaomiao11','$argon2id$v=19$m=65536,t=3,p=4$YWwNAeCcM4ZwrpUSAqBUqg$J86EFY9dGqQ8MXJCG8nIPVFNrEnCh9V0mXnc4ZDuum0',NULL,'miaofanyan@gmail.com','Normal',0,'USD','2026-03-26 06:11:33','2026-03-26 06:11:33',0,0,0,'2',0,1,NULL,NULL),(19,'hengliu','$argon2id$v=19$m=65536,t=3,p=4$hTBGiFFK6b137v0fA+D8/w$8aU/hZEHEUKkLmshMMqgOU1K/bIBOJuAHEFY4pybGyA',NULL,'124214lk@gmai.com','Normal',0,'USD','2026-03-29 11:08:51','2026-03-29 11:08:51',0,0,0,'2',0,1,NULL,NULL);
/*!40000 ALTER TABLE `user_main` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-30  7:26:24
