# Knowledge Taxonomy

## 用途
定义 OKOS L1 Knowledge 的企业知识分类法，说明哪些知识属于标准、模型、术语、规则、模板、记录或归档。

## 负责人
OKOS Chief System Architect

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 企业宪章：[../01-strategy/enterprise-charter.md](../01-strategy/enterprise-charter.md)
- 内容模型：[content-model.md](content-model.md)
- 唯一可信来源地图：[source-of-truth-map.md](source-of-truth-map.md)
- 术语表：[../GLOSSARY.md](../GLOSSARY.md)

## L1 Knowledge 定义
L1 Knowledge 是 OKOS 的企业知识层，负责定义公司长期复用的业务对象、概念、标准边界和知识来源。

L1 解决的问题是：公司说的每个核心名词到底是什么意思，归谁维护，权威文档在哪里，与其他对象有什么关系。

## 知识分类
OKOS 的企业知识分为以下类型：

| 类型 | 含义 | 主要位置 |
|---|---|---|
| Charter | 企业最高原则 | `01-strategy/enterprise-charter.md` |
| Domain Model | 业务域模型 | 各业务域 `*-model.md` 或 overview 文档 |
| Glossary Term | 统一术语 | `GLOSSARY.md` |
| Standard | 正式标准 | 对应业务域标准文档 |
| Policy | 规则与边界 | 合规、财务、AI、安全等 policy 文档 |
| Template | 可复用格式 | `17-templates/` |
| Decision Record | 决策记录 | `20-decision-records/` |
| Archive | 历史资料 | `22-archive/` |

## 知识边界
L1 不定义具体执行步骤。具体执行步骤属于 L2 Playbooks 或 SOP。

L1 不定义产品功能优先级。产品功能属于 L3 Product。

L1 不定义 AI Prompt。Prompt 属于 L4 AI。

L1 不定义指标公式和看板。指标公式和看板属于 L5 Data。

## 知识维护原则
1. 一个概念只能有一个权威定义。
2. 一个业务对象只能有一个主文档。
3. 其他文档可以引用权威定义，但不能复制并改写。
4. 业务对象变更必须检查下游 SOP、Playbook、产品、AI 和数据影响。
5. 跨业务域概念优先进入 `GLOSSARY.md`。

## 后续待完成内容
- L1 确认后进入 L2 Playbooks。
- 后续为每个业务对象补充更完整的字段与状态流转。

