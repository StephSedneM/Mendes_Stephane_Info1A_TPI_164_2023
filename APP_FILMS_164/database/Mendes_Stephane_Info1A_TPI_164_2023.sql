-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.31 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour mendes_stephane_info1a_tpi_164_2023
CREATE DATABASE IF NOT EXISTS `mendes_stephane_info1a_tpi_164_2023` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mendes_stephane_info1a_tpi_164_2023`;

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_documentation
CREATE TABLE IF NOT EXISTS `t_documentation` (
  `id_doc` int NOT NULL AUTO_INCREMENT,
  `Nom_doc` varchar(50) NOT NULL DEFAULT '',
  `Type_doc` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`id_doc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_documentation : ~0 rows (environ)

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_doc_avoir_theme
CREATE TABLE IF NOT EXISTS `t_doc_avoir_theme` (
  `id_doc_avoir_theme` int NOT NULL AUTO_INCREMENT,
  `Fk_Doc` int DEFAULT NULL,
  `Fk_theme` int DEFAULT NULL,
  PRIMARY KEY (`id_doc_avoir_theme`),
  KEY `Fk_DocumentAvoirTheme` (`Fk_Doc`),
  KEY `FK_ThemeAvoir_Document` (`Fk_theme`),
  CONSTRAINT `Fk_DocumentAvoirTheme` FOREIGN KEY (`Fk_Doc`) REFERENCES `t_documentation` (`id_doc`),
  CONSTRAINT `FK_ThemeAvoir_Document` FOREIGN KEY (`Fk_theme`) REFERENCES `t_theme` (`id_theme`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_doc_avoir_theme : ~0 rows (environ)

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_interview
CREATE TABLE IF NOT EXISTS `t_interview` (
  `id_interview` int NOT NULL AUTO_INCREMENT,
  `Nom_Inter` int NOT NULL,
  `Date_Inter` date NOT NULL,
  PRIMARY KEY (`id_interview`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_interview : ~0 rows (environ)

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_inter_avoir_sujet
CREATE TABLE IF NOT EXISTS `t_inter_avoir_sujet` (
  `id_inter_avoir_sujet` int NOT NULL AUTO_INCREMENT,
  `Fk_inter` int DEFAULT NULL,
  `Fk_sujet` int DEFAULT NULL,
  PRIMARY KEY (`id_inter_avoir_sujet`),
  KEY `Fk_inter` (`Fk_inter`),
  KEY `Fk_interview_avoir_sujet` (`Fk_sujet`),
  CONSTRAINT `Fk_interview_avoir_sujet` FOREIGN KEY (`Fk_sujet`) REFERENCES `t_sujet` (`id_sujet`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Fk_sujet_avoir_interview` FOREIGN KEY (`Fk_inter`) REFERENCES `t_interview` (`id_interview`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_inter_avoir_sujet : ~0 rows (environ)

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_inter_avoir_theme
CREATE TABLE IF NOT EXISTS `t_inter_avoir_theme` (
  `id_inter_avoir_theme` int NOT NULL AUTO_INCREMENT,
  `Fk_inter` int DEFAULT NULL,
  `Fk_theme` int DEFAULT NULL,
  PRIMARY KEY (`id_inter_avoir_theme`),
  KEY `Fk_interview_avoir_theme` (`Fk_inter`),
  KEY `Fk_therm_avoir_interview` (`Fk_theme`),
  CONSTRAINT `Fk_interview_avoir_theme` FOREIGN KEY (`Fk_inter`) REFERENCES `t_interview` (`id_interview`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Fk_therm_avoir_interview` FOREIGN KEY (`Fk_theme`) REFERENCES `t_sujet` (`id_sujet`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_inter_avoir_theme : ~0 rows (environ)

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_mail
CREATE TABLE IF NOT EXISTS `t_mail` (
  `id_mail` int NOT NULL AUTO_INCREMENT,
  `Adresse_mail` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id_mail`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_mail : ~7 rows (environ)
INSERT INTO `t_mail` (`id_mail`, `Adresse_mail`) VALUES
	(1, 'Local@local.com'),
	(2, 'Nautilus@local.com'),
	(3, 'Draven@local.com'),
	(4, 'Ashe@local.com'),
	(5, 'Xayah@local.com'),
	(6, 'samthekid@local.com'),
	(7, 'Canal115@local.com');

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_pays
CREATE TABLE IF NOT EXISTS `t_pays` (
  `id_pays` int NOT NULL AUTO_INCREMENT,
  `Pays` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id_pays`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_pays : ~0 rows (environ)

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_personnes
CREATE TABLE IF NOT EXISTS `t_personnes` (
  `id_personne` int NOT NULL AUTO_INCREMENT,
  `Prenom_personne` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `Nom_personne` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`id_personne`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_personnes : ~5 rows (environ)
INSERT INTO `t_personnes` (`id_personne`, `Prenom_personne`, `Nom_personne`) VALUES
	(1, 'Stéphane', 'Mendes '),
	(2, 'Hermione', 'Granger'),
	(3, 'Warwick', 'Malphite'),
	(4, 'Ron', 'Wealsley'),
	(20, 'Harry', 'Potter');

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_personne_avoir_mail
CREATE TABLE IF NOT EXISTS `t_personne_avoir_mail` (
  `id_personne_avoir_mail` int NOT NULL AUTO_INCREMENT,
  `Fk_personne` int DEFAULT NULL,
  `Fk_mail` int DEFAULT NULL,
  PRIMARY KEY (`id_personne_avoir_mail`),
  KEY `Fk_mail` (`Fk_mail`),
  KEY `Fk_personnemail` (`Fk_personne`),
  CONSTRAINT `Fk_mail` FOREIGN KEY (`Fk_mail`) REFERENCES `t_mail` (`id_mail`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Fk_personnemail` FOREIGN KEY (`Fk_personne`) REFERENCES `t_personnes` (`id_personne`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_personne_avoir_mail : ~0 rows (environ)

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_personne_avoir_pays
CREATE TABLE IF NOT EXISTS `t_personne_avoir_pays` (
  `id_personne_avoir_pays` int NOT NULL AUTO_INCREMENT,
  `Fk_personne` int DEFAULT NULL,
  `Fk_pays` int DEFAULT NULL,
  PRIMARY KEY (`id_personne_avoir_pays`),
  KEY `FkPersonneAvoirPays` (`Fk_personne`),
  KEY `FkPaysAvoirPersonne` (`Fk_pays`),
  CONSTRAINT `FkPaysAvoirPersonne` FOREIGN KEY (`Fk_pays`) REFERENCES `t_pays` (`id_pays`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FkPersonneAvoirPays` FOREIGN KEY (`Fk_personne`) REFERENCES `t_personnes` (`id_personne`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_personne_avoir_pays : ~0 rows (environ)

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_personne_avoir_telephone
CREATE TABLE IF NOT EXISTS `t_personne_avoir_telephone` (
  `id_personne_avoir_telephone` int NOT NULL AUTO_INCREMENT,
  `Fk_personne` int DEFAULT NULL,
  `FK_telephone` int DEFAULT NULL,
  PRIMARY KEY (`id_personne_avoir_telephone`),
  KEY `Fk_personnetelephone` (`Fk_personne`),
  KEY `Fk_telephone` (`FK_telephone`),
  CONSTRAINT `Fk_personnetelephone` FOREIGN KEY (`Fk_personne`) REFERENCES `t_personnes` (`id_personne`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Fk_telephone` FOREIGN KEY (`FK_telephone`) REFERENCES `t_tel` (`id_tel`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_personne_avoir_telephone : ~0 rows (environ)

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_sujet
CREATE TABLE IF NOT EXISTS `t_sujet` (
  `id_sujet` int NOT NULL AUTO_INCREMENT,
  `Nom_sujet` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_sujet`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_sujet : ~5 rows (environ)
INSERT INTO `t_sujet` (`id_sujet`, `Nom_sujet`) VALUES
	(1, 'Le monde du futur passé'),
	(2, 'Contract Apprentis'),
	(3, 'Le l\'enfant et la famille'),
	(9, 'Les apprentis deviennent fous avec ce module'),
	(11, 'Norwood Scale');

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_tel
CREATE TABLE IF NOT EXISTS `t_tel` (
  `id_tel` int NOT NULL AUTO_INCREMENT,
  `Nume_tel` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '',
  PRIMARY KEY (`id_tel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_tel : ~0 rows (environ)

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_theme
CREATE TABLE IF NOT EXISTS `t_theme` (
  `id_theme` int NOT NULL AUTO_INCREMENT,
  `Nom_Theme` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id_theme`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_theme : ~6 rows (environ)
INSERT INTO `t_theme` (`id_theme`, `Nom_Theme`) VALUES
	(1, 'Technologie'),
	(2, 'Social'),
	(3, 'Culturelle'),
	(4, 'Sport'),
	(5, 'Environment '),
	(6, 'Droit');

-- Listage de la structure de table mendes_stephane_info1a_tpi_164_2023. t_theme_avoir_sujet
CREATE TABLE IF NOT EXISTS `t_theme_avoir_sujet` (
  `id_theme_avoir_sujet` int NOT NULL AUTO_INCREMENT,
  `Fk_theme` int DEFAULT NULL,
  `Fk_sujet` int DEFAULT NULL,
  PRIMARY KEY (`id_theme_avoir_sujet`),
  KEY `Fk_theme_avoir_sujet` (`Fk_theme`),
  KEY `Fk_sujet_avoir_theme` (`Fk_sujet`),
  CONSTRAINT `Fk_sujet_avoir_theme` FOREIGN KEY (`Fk_sujet`) REFERENCES `t_sujet` (`id_sujet`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Fk_theme_avoir_sujet` FOREIGN KEY (`Fk_theme`) REFERENCES `t_theme` (`id_theme`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table mendes_stephane_info1a_tpi_164_2023.t_theme_avoir_sujet : ~0 rows (environ)
INSERT INTO `t_theme_avoir_sujet` (`id_theme_avoir_sujet`, `Fk_theme`, `Fk_sujet`) VALUES
	(1, 6, 2),
	(2, 5, 3),
	(3, 4, 9);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
