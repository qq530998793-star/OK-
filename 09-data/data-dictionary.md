# Data Dictionary

## 用途
定义 OKOS 中核心数据字段、业务对象字段和数据来源。

## 负责人
Data Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 数据目录：[README.md](README.md)
- 内容模型：[../00-system/content-model.md](../00-system/content-model.md)
- 指标定义：[metrics-definition.md](metrics-definition.md)

## 通用字段
| 字段 | 类型 | 定义 |
|---|---|---|
| `*_id` | string | 对象稳定唯一标识，不复用 |
| `status` | enum | 对象当前标准状态 |
| `created_at` | datetime | 创建时间，保存时区信息 |
| `updated_at` | datetime | 最后更新时间 |
| `organization_id` | string | 数据所属组织 |
| `source_system` | string | 数据产生系统 |
| `is_test` | boolean | 是否测试数据 |
| `invalidated_at` | datetime/null | 作废时间 |

## 核心对象
| 对象 | 主键 | 必填业务字段 | Owner |
|---|---|---|---|
| Player | `player_id` | 身份状态、授权状态、所属组织范围 | Community Owner |
| Store | `store_id` | 门店状态、组织、城市、接入日期 | Store Operations Owner |
| Team | `team_id` | 认证状态、负责人、组织范围 | Team Operations Owner |
| Event | `event_id` | 类型、状态、主办组织、门店、计划与完成时间 | Event Operations Owner |
| Registration | `registration_id` | 赛事、玩家或战队、审核状态、报名时间 | Event Operations Owner |
| Participation | `participation_id` | 赛事、玩家、确认状态、确认时间 | Event Operations Owner |
| Partner | `partner_id` | 类型、状态、授权范围 | Partnership Owner |

## 标准事件
| 事件 | 触发条件 | 必备字段 |
|---|---|---|
| `registration_submitted` | 报名提交成功 | registration_id、event_id、subject_id、occurred_at |
| `registration_approved` | 报名审核通过 | registration_id、reviewer_id、occurred_at |
| `participation_confirmed` | 到场或参赛事实被授权人员确认 | participation_id、player_id、event_id、confirmed_by |
| `event_completed` | 赛事完成并确认结果 | event_id、completed_at、confirmed_by |
| `team_verified` | 战队认证通过 | team_id、verified_at、reviewer_id |
| `store_activated` | 门店完成接入并激活 | store_id、activated_at、reviewer_id |

## 字段治理
新增字段必须有定义、类型、允许值、Owner、来源和敏感等级。同义字段必须合并或建立明确映射。

## 后续待完成内容
- 接入系统后补充物理字段、枚举值和数据血缘。
- 建立机器可读 Schema。
