# User Lifecycle

## 用途
定义玩家从触达到注册、参与、活跃、留存和召回的生命周期。

## 负责人
Community Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 社群模型：[community-model.md](community-model.md)
- 内容模型：[../00-system/content-model.md](../00-system/content-model.md)
- 唯一可信来源地图：[../00-system/source-of-truth-map.md](../00-system/source-of-truth-map.md)
- 玩家活跃：[player-engagement.md](player-engagement.md)
- 数据指标：[../09-data/metrics-definition.md](../09-data/metrics-definition.md)

## Source of Truth
本文档是 Player（玩家）业务对象和玩家生命周期知识的唯一可信来源。

## Player 定义
Player 是 OK赛事联盟服务的核心用户对象，可以通过赛事、门店、社群、战队、内容或产品与 OK赛事联盟产生关系。

Player 不只是一次报名记录，而是可被识别、服务、运营和长期维护的用户对象。

## Player 核心属性
| 属性 | 含义 |
|---|---|
| Player Identity | 玩家基础身份 |
| Contact Channel | 可触达渠道 |
| Related Store | 关联门店 |
| Related Team | 关联战队 |
| Related Community | 关联社群 |
| Event Participation | 赛事参与记录 |
| Lifecycle Stage | 生命周期阶段 |

## 生命周期阶段
L1 阶段定义 Player 的基础生命周期：

- Visitor：被触达但未建立稳定身份。
- Registered：已注册或留下可识别信息。
- Participant：参与过赛事、活动或社群互动。
- Active：持续参与赛事、社群或门店活动。
- Core：高频参与并对社群或战队有贡献。
- Dormant：一段时间未活跃。
- Archived：历史归档用户。

## 边界
本文档只定义玩家对象和生命周期知识边界。

玩家运营动作属于 L2 Playbooks。

玩家产品路径属于 L3 Product。

玩家指标口径属于 L5 Data。

## 后续待完成内容
- L2 阶段补充玩家活跃和社群增长 Playbook。
- L3 阶段补充玩家产品路径。
- L5 阶段补充玩家指标口径。
