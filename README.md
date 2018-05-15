云平台服务统一接口
===

<!-- TOC -->

- [1. 概述](#1-概述)
- [2. 接口分类](#2-接口分类)
    - [2.1. 服务器/云主机](#21-服务器云主机)
        - [2.1.1. 读取主机信息 (DescribeInstances)](#211-读取主机信息-describeinstances)
        - [2.1.2. 创建新主机 (CreateInstances)](#212-创建新主机-createinstances)
        - [2.1.3. 启动现有主机 (StartInstances)](#213-启动现有主机-startinstances)
        - [2.1.4. 关闭现有主机 (StopInstances)](#214-关闭现有主机-stopinstances)
        - [2.1.5. 销毁现有主机 (DestroyInstances)](#215-销毁现有主机-destroyinstances)
    - [2.2. 网络](#22-网络)
    - [2.3. 负载均衡器](#23-负载均衡器)
    - [2.4. 对象型存储](#24-对象型存储)

<!-- /TOC -->

# 1. 概述
使用一组统一的接口用于管理以下服务商提供的资源：
+ AWS
+ 腾讯云

# 2. 接口分类
## 2.1. 服务器/云主机
此模块中包含的接口对应以下服务：
* AWS: EC2
* 腾讯云: CVM

云服务器资源需要实现以下接口：
* 读取主机信息 - DescribeInstances
* 创建新主机 - CreateInstances
* 启动现有主机 - StartInstances
* 关闭现有主机 - StopInstances
* 销毁现有主机 - DestroyInstances

### 2.1.1. 读取主机信息 (DescribeInstances)
### 2.1.2. 创建新主机 (CreateInstances)
### 2.1.3. 启动现有主机 (StartInstances)
### 2.1.4. 关闭现有主机 (StopInstances)
### 2.1.5. 销毁现有主机 (DestroyInstances)

## 2.2. 网络
此模块中包含的接口对应以下服务：
* AWS: VPC
* 腾讯云: VPC

网络相关的接口包括：


## 2.3. 负载均衡器
此模块中包含的接口对应以下服务：
* AWS: ELB
* 腾讯云: CLB

## 2.4. 对象型存储
此模块中包含的接口对应以下服务：
* AWS: S3
* 腾讯云: COS
