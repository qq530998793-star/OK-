# Store Model

## 用途
定义合作门店在 OK赛事联盟中的业务角色、合作边界与基础模型。

## 负责人
Store Operations Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 门店目录：[README.md](README.md)
- 内容模型：[../00-system/content-model.md](../00-system/content-model.md)
- 唯一可信来源地图：[../00-system/source-of-truth-map.md](../00-system/source-of-truth-map.md)
- 门店分级：[store-grading.md](store-grading.md)
- 合作伙伴模型：[../13-partnerships/partnership-model.md](../13-partnerships/partnership-model.md)

## Source of Truth
本文档是 Store（合作门店）业务对象的唯一可信来源。

## Store 定义
Store 是 OK赛事联盟的合作门店，是线下赛事、玩家触点、战队活动、社群运营和品牌合作的本地节点。

Store 不是普通场地记录，而是 OK赛事联盟线下网络的基础单位。

## Store 核心属性
Store 在 L1 阶段至少包含以下知识属性：

| 属性 | 含义 |
|---|---|
| Store Identity | 门店身份与基础识别信息 |
| Location | 城市、区域与线下服务范围 |
| Cooperation Status | 合作状态 |
| Operation Capacity | 赛事、社群和活动承载能力 |
| Contact Ownership | 对接人与维护责任 |
| Related Community | 关联社群 |
| Related Events | 关联赛事 |

## Store 状态
L1 阶段定义 Store 的基础状态：

- Candidate：潜在合作门店。
- Onboarding：接入中门店。
- Active：正式合作门店。
- Suspended：暂停合作门店。
- Archived：历史归档门店。

## Store 关系
- Store 可以承载 Event。
- Store 可以连接本地 Player 和 Team。
- Store 可以拥有或参与 Community。
- Store 可以参与 Partner 或 Sponsor 的线下交付。

## 边界
本文档只定义门店对象和知识边界。

门店接入流程属于 `19-sops/sop-store-onboarding.md`。

门店启动打法属于 `18-playbooks/store-launch-playbook.md`。

门店指标口径属于 `09-data/metrics-definition.md`。

## 后续待完成内容
- L2 阶段补充门店启动 Playbook。
- L5 阶段补充门店数据指标口径。
- 后续确认门店类型与合作等级。
