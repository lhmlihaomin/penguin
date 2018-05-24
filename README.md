云平台服务统一接口 - Python
===

<!-- TOC -->

- [云平台服务统一接口 - Python](#python)
- [1. 概述](#1)
- [2. 基础接口](#2)
    - [2.1. 身份验证](#21)
    - [2.2. API Key 管理](#22-api-key)
- [3. 接口分类](#3)
    - [3.1. 服务器/云主机](#31)
        - [3.1.1. 读取主机信息](#311)
        - [3.1.2. 创建新主机](#312)
        - [3.1.3. 启动现有主机](#313)
        - [3.1.4. 关闭现有主机](#314)
        - [3.1.5. 销毁现有主机](#315)
        - [3.1.6. 修改主机安全组](#316)
    - [3.2. 网络](#32)
        - [3.2.1. 读取路由条目](#321)
        - [3.2.2. 设置路由条目](#322)
    - [3.3. 负载均衡器](#33)
        - [3.3.1. 读取负载均衡器后端健康状况](#331)
        - [3.3.2. 将主机注册到负载均衡器后端](#332)
        - [3.3.3. 将主机从负载均衡器后端移除](#333)
    - [3.4. 对象型存储](#34)
        - [3.4.1. 上传文件](#341)

<!-- /TOC -->

# 1. 概述
使用一组统一的接口用于管理以下服务商提供的资源：
+ AWS
+ 腾讯云

本文中定义的接口均为当前运维和测试系统中使用到的接口，并会根据实际开发中的需求不断更新完善。

鉴于当前的运维测试等系统均基于AWS的API所开发，封装时，接口的参数与返回值结构应当尽量与AWS接近，以求降低移植的成本。



# 2. 基础接口
## 2.1. 身份验证
目前，需要支持的云服务提供商都拥有API Key的机制，使用一对key & secret key来对API调用进行身份验证。因此身份验证可以使用相同的参数进行处理。

由于AWS提供了IAM Role/Instance Profile等机制，可以在不提供任何API Key的情况下完成身份认证，这两个参数不是必选的。

## 2.2. API Key 管理
使用类似 AWSCLI 的方式从磁盘特定位置（~/.aws/credentials）自动读取指定的 API Key 。

# 3. 接口分类
## 3.1. 服务器/云主机
此模块中包含的接口对应以下服务：
* AWS: EC2
* 腾讯云: CVM

云服务器资源需要实现以下接口：
1. 读取主机信息 - describe_instances
2. 创建新主机 - create_instances
3. 启动现有主机 - start_instances
4. 关闭现有主机 - stop_instances
5. 销毁现有主机 - terminate_instances
6. 修改主机安全组 - modify_instance_groups

### 3.1.1. 读取主机信息
describe_instances

__参数__

|Argument|Type|Description|
|---|---|---|
|instance_ids|list|List of instance ids|
|filters|list|List of filters|

```
# Filters 结构:
filters = [
    {
        'Filter1': 'Value1',
        'Filter2': ['Value2', 'Value3'],
        ...
    }
]

# 支持的过滤属性：
{
    'Name': '主机名称 (tag:Name/name)',
    'State': '运行状态',
}
```

__返回值__

```
RetVal = [
    {
        'InstanceId': 'str',
        'State': 'str',
        'PrivateIpAddress': 'str',
        'VpcId': 'str',
        'ImageId': 'str',
        'KeyName': 'str',
        'SecurityGroups': [list],
        'SubnetId': 'str',
        'InstanceType': 'str,
    },
    {
        'InstanceId': '',
        ...
    },
    ...
]
```

### 3.1.2. 创建新主机
create_instances

__参数__

|Argument|Type|Description|
|---|---|---|
|image_id|str||


### 3.1.3. 启动现有主机
start_instances

__参数__

|Argument|Type|Description|
|---|---|---|
|instance_ids|list||

### 3.1.4. 关闭现有主机
stop_instances

__参数__

|Argument|Type|Description|
|---|---|---|
|instance_ids|list||

### 3.1.5. 销毁现有主机
terminate_instances

__参数__

|Argument|Type|Description|
|---|---|---|
|instance_ids|list||

### 3.1.6. 修改主机安全组
modify_instance_groups

__参数__

|Argument|Type|Description|
|---|---|---|
|instance_ids|list||
|group_ids|list||

## 3.2. 网络
此模块中包含的接口对应以下服务：
* AWS: VPC
* 腾讯云: VPC

网络相关的接口包括：
1. 读取路由条目 - describe_route_tables
2. 设置路由条目 - replace_routes

### 3.2.1. 读取路由条目
describe_route_tables

__参数__

|Argument|Type|Description|
|---|---|---|
|vpc_id|str||

### 3.2.2. 设置路由条目
replace_routes

__参数__

|Argument|Type|Description|
|---|---|---|
|vpc_id|str||


## 3.3. 负载均衡器
此模块中包含的接口对应以下服务：
* AWS: ELB
* 腾讯云: CLB

接口列表：
1. 读取负载均衡器后端健康状况 - describe_lb_health
2. 将主机注册到负载均衡器后端 - register_instances_with_lb
3. 将主机从负载均衡器后端移除 - deregister_instances_from_lb

### 3.3.1. 读取负载均衡器后端健康状况
describe_lb_health

__参数__

|Argument|Type|Description|
|---|---|---|


### 3.3.2. 将主机注册到负载均衡器后端
register_instances_with_lb

### 3.3.3. 将主机从负载均衡器后端移除
deregister_instances_from_lb

## 3.4. 对象型存储
此模块中包含的接口对应以下服务：
* AWS: S3
* 腾讯云: COS

接口列表：
1. 上传文件 - upload_file

### 3.4.1. 上传文件
upload_file
