/*
 Navicat Premium Data Transfer

 Source Server         : uwork
 Source Server Type    : MySQL
 Source Server Version : 80025
 Source Host           : rm-2zenjcndt98hc2cz17o.mysql.rds.aliyuncs.com:3306
 Source Schema         : uwork

 Target Server Type    : MySQL
 Target Server Version : 80025
 File Encoding         : 65001

 Date: 20/04/2023 11:10:54
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for api_infor_call_record
-- ----------------------------
DROP TABLE IF EXISTS `api_infor_call_record`;
CREATE TABLE `api_infor_call_record` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `api_id` int DEFAULT '0' COMMENT '接口id',
  `ip` varchar(255) COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '调用ip',
  `uuid` varchar(255) COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '接口调用人ID',
  `create_at` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间/接口调用时间',
  `update_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `index_oci_id` (`api_id`) USING BTREE,
  KEY `index_uuid` (`uuid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='api调用记录表';

-- ----------------------------
-- Table structure for api_infor_change_record
-- ----------------------------
DROP TABLE IF EXISTS `api_infor_change_record`;
CREATE TABLE `api_infor_change_record` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `api_id` int DEFAULT '0' COMMENT '接口id',
  `edit_mark` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '变更口描述',
  `edit_uuid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '接口修改人uuid',
  `new_info` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '接口修改前信息',
  `old_info` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '接口修改后信息',
  `create_at` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `index_api_id` (`api_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='api变更记录表';

-- ----------------------------
-- Table structure for api_information
-- ----------------------------
DROP TABLE IF EXISTS `api_information`;
CREATE TABLE `api_information` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `host` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '接口地址',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '接口名称',
  `api_mark` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci COMMENT '接口描述',
  `api_doc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '接口文档地址',
  `integral` bigint DEFAULT '0' COMMENT '每次调用积分',
  `deleted` tinyint DEFAULT '1' COMMENT '逻辑删除 1 未删除 2 已删除',
  `create_at` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `index_host` (`host`) USING BTREE,
  KEY `index_name` (`name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='api信息发布管理表';

-- ----------------------------
-- Table structure for api_points_change
-- ----------------------------
DROP TABLE IF EXISTS `api_points_change`;
CREATE TABLE `api_points_change` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `api_id` int DEFAULT '0' COMMENT '接口id',
  `member_points_change_id` int DEFAULT '0' COMMENT '积分变更记录id',
  `create_at` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间/接口调用时间',
  `update_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `index_api_id` (`api_id`) USING BTREE,
  KEY `index_member_points_change_id` (`member_points_change_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='api积分消费记录表';

-- ----------------------------
-- Table structure for demo
-- ----------------------------
DROP TABLE IF EXISTS `demo`;
CREATE TABLE `demo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL COMMENT '测试描述',
  `status` tinyint DEFAULT '1' COMMENT '状态 1 开启 2 关闭',
  `create_at` datetime DEFAULT NULL COMMENT '创建时间',
  `update_at` datetime DEFAULT NULL COMMENT '变更时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for log
-- ----------------------------
DROP TABLE IF EXISTS `log`;
CREATE TABLE `log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `method` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `uid` int DEFAULT NULL,
  `url` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `desc` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `ip` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_agent` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `create_time` datetime DEFAULT NULL,
  `success` int DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1485 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for member_points_account
-- ----------------------------
DROP TABLE IF EXISTS `member_points_account`;
CREATE TABLE `member_points_account` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `uuid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '用户唯一id',
  `historical_points` bigint DEFAULT '0' COMMENT '历史充值积分',
  `current_points` bigint DEFAULT '0' COMMENT '当前积分余额',
  `status` tinyint DEFAULT '1' COMMENT '账户状态 1 正常 2 锁定',
  `create_at` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `index_uuid` (`uuid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='用户积分账户表';

-- ----------------------------
-- Table structure for member_points_change_record
-- ----------------------------
DROP TABLE IF EXISTS `member_points_change_record`;
CREATE TABLE `member_points_change_record` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `uuid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '用户uuid',
  `account_id` int DEFAULT '0' COMMENT '账户id',
  `points` bigint DEFAULT '0' COMMENT '积分额度',
  `type` tinyint DEFAULT '1' COMMENT '积分类型 1 增-充值积分 2 减-消费积分 3 增-赠送积分',
  `create_at` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `idx_uuid` (`uuid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='用户账户积分变更记录表';

-- ----------------------------
-- Table structure for member_user
-- ----------------------------
DROP TABLE IF EXISTS `member_user`;
CREATE TABLE `member_user` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `username` char(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '用户姓名',
  `uuid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '用户唯一id',
  `token` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '' COMMENT '用户token（不对外）',
  `deleted` tinyint DEFAULT '1' COMMENT '逻辑删除 1 未删除 2 已删除',
  `status` tinyint DEFAULT '1' COMMENT '用户状态 1 正常 2 锁定',
  `create_at` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `index_uuid` (`uuid`) USING BTREE,
  KEY `index_token` (`token`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='外部用户表';

SET FOREIGN_KEY_CHECKS = 1;
