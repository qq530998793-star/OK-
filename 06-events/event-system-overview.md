# Event System Overview

## 用途
定义 OK赛事联盟赛事体系的整体结构与适用范围。

## 负责人
Event Operations Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 赛事目录：[README.md](README.md)
- 内容模型：[../00-system/content-model.md](../00-system/content-model.md)
- 唯一可信来源地图：[../00-system/source-of-truth-map.md](../00-system/source-of-truth-map.md)
- 赛事类型：[event-types.md](event-types.md)
- 赛事生命周期：[event-lifecycle.md](event-lifecycle.md)

## Source of Truth
本文档是 Event（赛事）体系对象的唯一可信来源。

## Event 定义
Event 是 OK赛事联盟连接玩家、战队、门店、社群、品牌和合作伙伴的核心运营载体。

Event 不只是一次比赛，而是包含报名、组织、执行、结果、内容、社群传播和复盘沉淀的业务对象。

## Event 核心属性
| 属性 | 含义 |
|---|---|
| Event Identity | 赛事名称、编号和基础身份 |
| Event Type | 赛事类型 |
| Game Category | 游戏项目 |
| Host Store | 承办或关联门店 |
| Participants | 参赛玩家或战队 |
| Schedule | 时间安排 |
| Ruleset | 规则来源 |
| Result | 结果记录 |
| Review | 复盘记录 |

## Event 状态
L1 阶段定义 Event 的基础状态：

- Concept：概念中。
- Planned：已计划。
- Registration Open：报名中。
- Running：执行中。
- Completed：已完成。
- Reviewed：已复盘。
- Archived：已归档。

## Event 关系
- Event 由 Store 承载或协作。
- Event 由 Player 或 Team 参与。
- Event 在 Community 中传播和沉淀。
- Event 可服务 Partner 和 Sponsor 的合作交付。
- Event 产生后续 Product、AI 和 Data 的业务输入。

## 边界
本文档只定义赛事体系对象和知识边界。

赛事执行流程属于 `event-lifecycle.md` 和后续 SOP。

城市赛启动打法属于 `18-playbooks/city-event-launch-playbook.md`。

赛事指标口径属于 `09-data/metrics-definition.md`。

## 后续待完成内容
- L1 后续确认赛事类型分类。
- L2 阶段补充赛事启动 Playbook。
- L5 阶段补充赛事数据指标口径。
