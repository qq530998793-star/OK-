# Partnership Model

## 用途
定义 OK赛事联盟合作伙伴体系的整体模型。

## 负责人
Partnership Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 合作伙伴目录：[README.md](README.md)
- 内容模型：[../00-system/content-model.md](../00-system/content-model.md)
- 唯一可信来源地图：[../00-system/source-of-truth-map.md](../00-system/source-of-truth-map.md)
- 合作伙伴类型：[partner-types.md](partner-types.md)

## Source of Truth
本文档是 Partner（合作伙伴）业务对象的唯一可信来源。

## Partner 定义
Partner 是与 OK赛事联盟进行资源、渠道、场地、品牌、内容、商业或技术协作的外部组织。

Partner 的价值不只来自一次合作，而来自可复用、可交付、可复盘的长期合作关系。

## Partner 核心属性
| 属性 | 含义 |
|---|---|
| Partner Identity | 合作伙伴名称、类型和基础身份 |
| Partner Type | 合作伙伴类型 |
| Contact Ownership | 对接人与维护责任 |
| Cooperation Scope | 合作范围 |
| Related Events | 关联赛事 |
| Related Stores | 关联门店 |
| Rights And Benefits | 权益与交付边界 |
| Review Record | 合作复盘记录 |

## Partner 类型
L1 阶段定义基础类型：

- Store Partner：门店合作伙伴。
- Brand Partner：品牌合作伙伴。
- Sponsor：赞助商。
- Channel Partner：渠道合作伙伴。
- City Partner：城市合作伙伴。
- Technology Partner：技术合作伙伴。

## Partner 关系
- Partner 可以支持 Event。
- Partner 可以连接 Store。
- Sponsor 是 Partner 的一种商业合作类型。
- Partner 合作结果需要被复盘和归档。

## 边界
本文档只定义合作伙伴对象和知识边界。

赞助销售打法属于 `18-playbooks/sponsorship-sales-playbook.md`。

合同和合规要求属于 `14-legal-compliance/contract-standards.md`。

合作结算规则属于 `15-finance/sponsorship-settlement.md`。

## 后续待完成内容
- L2 阶段补充合作伙伴相关 Playbook。
- L5 阶段补充合作效果指标口径。
- 后续确认合作伙伴分级和权益模型。
