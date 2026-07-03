# Data System

## 用途
定义 OKOS L5 Data 的数据治理体系、分层模型、权责边界和持续扩展规则。

## 负责人
Data Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 企业宪章：[../01-strategy/enterprise-charter.md](../01-strategy/enterprise-charter.md)
- 内容模型：[../00-system/content-model.md](../00-system/content-model.md)
- 数据字典：[data-dictionary.md](data-dictionary.md)
- 指标定义：[metrics-definition.md](metrics-definition.md)
- 数据质量：[data-quality.md](data-quality.md)
- 报表体系：[reporting-system.md](reporting-system.md)
- 隐私规则：[privacy-policy.md](privacy-policy.md)

## L5 Data 定义
L5 Data 将 L0-L4 中的业务对象、执行状态、产品行为和 AI 协作结果转化为可追溯、可比较、可治理的数据资产。

## 数据分层
1. Source：业务系统、审核记录和经批准的人工数据源。
2. Standard：按数据字典统一对象、字段、状态和时间。
3. Metric：依据唯一口径生成可复用指标。
4. Report：按固定周期与权限提供报表和看板。
5. Decision：为经营决策提供证据，不替代 Owner 决策。

## 治理原则
- 业务对象和标识必须统一，不以名称代替稳定 ID。
- 指标先定义后使用，禁止在报表中临时发明公式。
- 原始数据、修正记录和指标结果必须可追溯。
- 门店、战队、合作方和个人数据按组织及角色隔离。
- 缺失、延迟和异常必须显式呈现，不得用默认值掩盖。
- 自动分析必须引用指标版本和统计周期。

## 权责
Data Owner 负责字典、指标、质量和发布；Business Owner 负责业务状态真实性；Product Owner 负责采集设计；Compliance Owner 负责隐私与使用边界；报表使用者负责在授权范围内解释和决策。

## 变更规则
字段、状态、公式、时间窗口、去重键或数据源变化必须评估历史可比性。破坏可比性的变更需要 Decision Record、版本升级、迁移说明和生效日期。

## 扩展规则
新增业务域时，依次补充对象与字段、事件、质量规则、指标和报表。不得先建看板后补口径。

## 后续待完成内容
- 接入真实产品后登记物理表、接口和数据血缘。
- 建立自动质量监控与指标版本仓库。

