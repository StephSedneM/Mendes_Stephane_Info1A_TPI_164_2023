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


-- Listage de la structure de la base pour module_164
DROP DATABASE IF EXISTS `module_164`;
CREATE DATABASE IF NOT EXISTS `module_164` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `module_164`;

-- Listage de la structure de table module_164. t_documentation
DROP TABLE IF EXISTS `t_documentation`;
CREATE TABLE IF NOT EXISTS `t_documentation` (
  `id_doc` int NOT NULL,
  `Nom_doc` varchar(50) NOT NULL DEFAULT '',
  `Ext_doc` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id_doc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164.t_documentation : ~0 rows (environ)

-- Listage de la structure de table module_164. t_interview
DROP TABLE IF EXISTS `t_interview`;
CREATE TABLE IF NOT EXISTS `t_interview` (
  `id_interview` int NOT NULL,
  `Nom_Inter` int NOT NULL,
  `Date_Inter` date NOT NULL,
  PRIMARY KEY (`id_interview`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164.t_interview : ~0 rows (environ)

-- Listage de la structure de table module_164. t_inter_avoir_sujet
DROP TABLE IF EXISTS `t_inter_avoir_sujet`;
CREATE TABLE IF NOT EXISTS `t_inter_avoir_sujet` (
  `id_inter_avoir_sujet` int NOT NULL,
  `Fk_Inter` int DEFAULT NULL,
  `Fk_sujet` int DEFAULT NULL,
  PRIMARY KEY (`id_inter_avoir_sujet`),
  KEY `Fk_interview_avoir_sujet` (`Fk_Inter`),
  KEY `Fk_sujet_avoir_interview` (`Fk_sujet`),
  CONSTRAINT `Fk_interview_avoir_sujet` FOREIGN KEY (`Fk_Inter`) REFERENCES `t_sujet` (`id_sujet`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Fk_sujet_avoir_interview` FOREIGN KEY (`Fk_sujet`) REFERENCES `t_interview` (`id_interview`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164.t_inter_avoir_sujet : ~0 rows (environ)

-- Listage de la structure de table module_164. t_inter_avoir_theme
DROP TABLE IF EXISTS `t_inter_avoir_theme`;
CREATE TABLE IF NOT EXISTS `t_inter_avoir_theme` (
  `id_inter_avoir_theme` int NOT NULL,
  `Fk_Inter` int NOT NULL,
  `Fk_theme` int NOT NULL,
  PRIMARY KEY (`id_inter_avoir_theme`),
  KEY `Fk_interview_avoir_theme_interview` (`Fk_Inter`),
  KEY `Fk_theme_avoir_interview` (`Fk_theme`),
  CONSTRAINT `Fk_interview_avoir_theme_interview` FOREIGN KEY (`Fk_Inter`) REFERENCES `t_interview` (`id_interview`) ON UPDATE RESTRICT,
  CONSTRAINT `Fk_theme_avoir_interview` FOREIGN KEY (`Fk_theme`) REFERENCES `t_sujet` (`id_sujet`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164.t_inter_avoir_theme : ~0 rows (environ)

-- Listage de la structure de table module_164. t_mail
DROP TABLE IF EXISTS `t_mail`;
CREATE TABLE IF NOT EXISTS `t_mail` (
  `id_mail` int NOT NULL,
  `Adresse_mail` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id_mail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164.t_mail : ~7 rows (environ)
INSERT INTO `t_mail` (`id_mail`, `Adresse_mail`) VALUES
	(1, 'Local@local.com'),
	(2, 'Nautilus@local.com'),
	(3, 'Draven@local.com'),
	(4, 'Ashe@local.com'),
	(5, 'Xayah@local.com'),
	(6, 'samthekid@local.com'),
	(7, 'Canal115@local.com');

-- Listage de la structure de table module_164. t_pays
DROP TABLE IF EXISTS `t_pays`;
CREATE TABLE IF NOT EXISTS `t_pays` (
  `id_pays` int NOT NULL,
  `Pays` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`id_pays`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164.t_pays : ~0 rows (environ)

-- Listage de la structure de table module_164. t_personnes
DROP TABLE IF EXISTS `t_personnes`;
CREATE TABLE IF NOT EXISTS `t_personnes` (
  `id_pers` int NOT NULL,
  `Prenom_pers` varchar(50) NOT NULL DEFAULT '',
  `Nom_pers` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `Date_Nais` date NOT NULL,
  PRIMARY KEY (`id_pers`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164.t_personnes : ~6 rows (environ)
INSERT INTO `t_personnes` (`id_pers`, `Prenom_pers`, `Nom_pers`, `Date_Nais`) VALUES
	(1, 'Caytlin', 'Fortune', '2023-05-10'),
	(2, 'Aurelion', 'Garen', '2019-05-10'),
	(3, 'Warwick', 'Malphite', '1987-05-17'),
	(4, 'Anivia', 'Leona', '1985-12-20'),
	(5, 'Dr.', 'Mundo', '1543-09-23'),
	(6, 'Tresh', 'Veigar', '1997-03-04');

-- Listage de la structure de table module_164. t_pers_avoir_mail
DROP TABLE IF EXISTS `t_pers_avoir_mail`;
CREATE TABLE IF NOT EXISTS `t_pers_avoir_mail` (
  `id_pers_avoir_mail` int NOT NULL,
  `Fk_personnes` int DEFAULT NULL,
  `Fk_mail` int DEFAULT NULL,
  PRIMARY KEY (`id_pers_avoir_mail`),
  KEY `FK_pers_avoir_mail` (`Fk_mail`),
  KEY `FK_pers` (`Fk_personnes`),
  CONSTRAINT `FK_pers` FOREIGN KEY (`Fk_personnes`) REFERENCES `t_personnes` (`id_pers`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_pers_avoir_mail` FOREIGN KEY (`Fk_mail`) REFERENCES `t_mail` (`id_mail`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164.t_pers_avoir_mail : ~1 rows (environ)
INSERT INTO `t_pers_avoir_mail` (`id_pers_avoir_mail`, `Fk_personnes`, `Fk_mail`) VALUES
	(1, 1, 4);

-- Listage de la structure de table module_164. t_pers_inter_pers
DROP TABLE IF EXISTS `t_pers_inter_pers`;
CREATE TABLE IF NOT EXISTS `t_pers_inter_pers` (
  `id_pers_inter_pers` int NOT NULL,
  `Date_inter` timestamp NULL DEFAULT NULL,
  `Fk_pers_quest` int DEFAULT NULL,
  `FK_pers_rep` int DEFAULT NULL,
  PRIMARY KEY (`id_pers_inter_pers`),
  KEY `FK_t_pers_inter_pers_t_personnes` (`Fk_pers_quest`),
  KEY `FK_t_pers_inter_pers_t_personnes_2` (`FK_pers_rep`),
  CONSTRAINT `FK_t_pers_inter_pers_t_personnes` FOREIGN KEY (`Fk_pers_quest`) REFERENCES `t_personnes` (`id_pers`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_t_pers_inter_pers_t_personnes_2` FOREIGN KEY (`FK_pers_rep`) REFERENCES `t_personnes` (`id_pers`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164.t_pers_inter_pers : ~0 rows (environ)

-- Listage de la structure de table module_164. t_sujet
DROP TABLE IF EXISTS `t_sujet`;
CREATE TABLE IF NOT EXISTS `t_sujet` (
  `id_sujet` int NOT NULL,
  `Nom_Sujet` int DEFAULT NULL,
  PRIMARY KEY (`id_sujet`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164.t_sujet : ~0 rows (environ)

-- Listage de la structure de table module_164. t_tel
DROP TABLE IF EXISTS `t_tel`;
CREATE TABLE IF NOT EXISTS `t_tel` (
  `id_tel` int NOT NULL,
  `Nume_tel` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '',
  PRIMARY KEY (`id_tel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164.t_tel : ~0 rows (environ)

-- Listage de la structure de table module_164. t_theme
DROP TABLE IF EXISTS `t_theme`;
CREATE TABLE IF NOT EXISTS `t_theme` (
  `id_theme` int NOT NULL,
  `Nom_Theme` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id_theme`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164.t_theme : ~4 rows (environ)
INSERT INTO `t_theme` (`id_theme`, `Nom_Theme`) VALUES
	(1, 'Technologie'),
	(2, 'Social'),
	(3, 'Culturelle'),
	(4, 'Sport'),
	(5, 'Environment '),
	(6, 'Droit');

-- Listage de la structure de table module_164. t_theme_avoir_sujet
DROP TABLE IF EXISTS `t_theme_avoir_sujet`;
CREATE TABLE IF NOT EXISTS `t_theme_avoir_sujet` (
  `theme_avoir_sujet` int NOT NULL,
  `Fk_theme` int DEFAULT NULL,
  `Fk_sujet` int DEFAULT NULL,
  PRIMARY KEY (`theme_avoir_sujet`),
  KEY `FK_t_theme_avoir_sujet_t_sujet` (`Fk_theme`),
  KEY `Fk_sujet_avoir_theme` (`Fk_sujet`),
  CONSTRAINT `Fk_sujet_avoir_theme` FOREIGN KEY (`Fk_sujet`) REFERENCES `t_theme` (`id_theme`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_t_theme_avoir_sujet_t_sujet` FOREIGN KEY (`Fk_theme`) REFERENCES `t_sujet` (`id_sujet`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table module_164.t_theme_avoir_sujet : ~0 rows (environ)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
