# Team Model

## 用途
定义战队在 OK赛事联盟中的角色、类型、生命周期与管理边界。

## 负责人
Team Operations Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 战队目录：[README.md](README.md)
- 内容模型：[../00-system/content-model.md](../00-system/content-model.md)
- 唯一可信来源地图：[../00-system/source-of-truth-map.md](../00-system/source-of-truth-map.md)
- 战队注册：[team-registration.md](team-registration.md)

## Source of Truth
本文档是 Team（战队）业务对象的唯一可信来源。

## Team 定义
Team 是玩家组织化参与 OK赛事联盟赛事、社群和成长体系的基本单位。

Team 不只是报名名单，而是可被识别、维护、成长和复盘的玩家组织。

## Team 核心属性
| 属性 | 含义 |
|---|---|
| Team Identity | 战队名称、标识和基础身份 |
| Captain | 队长或主要负责人 |
| Members | 队员集合 |
| Game Category | 主要参与项目 |
| Home Store | 关联门店，可为空 |
| Status | 战队状态 |
| Conduct Record | 行为和纪律记录 |
| Event History | 赛事参与历史 |

## Team 状态
L1 阶段定义 Team 的基础状态：

- Candidate：潜在战队。
- Registered：已注册战队。
- Verified：已认证战队。
- Active：活跃战队。
- Suspended：暂停权益战队。
- Archived：历史归档战队。

## Team 关系
- Team 由 Player 组成。
- Team 参加 Event。
- Team 可以关联 Store。
- Team 活跃在 Community 中。

## 边界
本文档只定义战队对象和知识边界。

战队认证流程属于 `19-sops/sop-team-verification.md`。

战队分级规则属于 `team-grading.md`。

战队数据口径属于 `09-data/metrics-definition.md`。

## 后续待完成内容
- L2 阶段补充战队相关执行剧本。
- L5 阶段补充战队数据指标口径。
- 后续确认战队类型和权益映射。
