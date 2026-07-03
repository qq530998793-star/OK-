# Product System

## 用途
定义 OKOS L3 Product 的产品治理体系、产品边界、文档关系和持续演进规则。

## 负责人
Product Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 企业宪章：[../01-strategy/enterprise-charter.md](../01-strategy/enterprise-charter.md)
- 内容模型：[../00-system/content-model.md](../00-system/content-model.md)
- 产品愿景：[product-vision.md](product-vision.md)
- 产品需求：[product-requirements.md](product-requirements.md)
- 功能地图：[feature-map.md](feature-map.md)
- 用户路径：[user-journeys.md](user-journeys.md)
- 发布策略：[release-policy.md](release-policy.md)

## L3 Product 定义
L3 Product 是 OKOS 的数字产品层，负责把 L0 原则、L1 业务对象和 L2 执行方式转化为可交付、可验收、可迭代的产品能力。

产品层描述“系统需要支持什么”和“用户如何完成目标”，不替代业务规则、执行剧本、AI Prompt 或数据指标口径。

## 产品边界
L3 可以定义：
- 产品愿景、目标用户和价值主张。
- 用户旅程、产品能力和功能依赖。
- 需求准入、优先级、验收和发布机制。
- 产品状态、权限原则和异常体验原则。

L3 不定义：
- 业务对象的权威含义，引用 L1 Knowledge。
- 线下执行步骤，引用 L2 Playbooks 和 SOP。
- AI 员工角色、Prompt 与评测，留在 L4 AI。
- 指标公式、数据表和看板口径，留在 L5 Data。

## 产品文档关系
1. `product-vision.md` 定义为什么建设。
2. `user-journeys.md` 定义谁在什么场景完成什么目标。
3. `feature-map.md` 定义产品提供哪些能力。
4. `product-requirements.md` 定义需求如何进入、评审和验收。
5. `release-policy.md` 定义能力如何发布和退出。
6. `product-faq.md` 只解释上述权威文档，不创建新规则。

## 产品治理原则
- 业务对象先于页面：功能必须关联 L1 中的权威对象。
- 用户目标先于功能数量：需求必须说明用户问题和预期结果。
- 全链路可追溯：需求应能追溯到来源、旅程、能力、验收和发布记录。
- 多组织可隔离：门店、城市和合作方数据与权限必须具备组织边界。
- 规模化优先：设计需支持 100+ 门店、1000+ 战队和 10万+ 玩家。
- 人工可接管：自动化能力必须保留人工审核、异常处理和回退路径。
- 单一可信来源：产品规则只在对应产品主文档中定义。

## 产品状态
产品需求与能力统一使用以下状态：
- Proposed：已提出，尚未准入。
- Discovery：正在验证问题与方案。
- Approved：已评审并进入计划。
- In Delivery：正在交付。
- Released：已发布并可使用。
- Deprecated：已声明弃用。
- Retired：已停止使用并完成迁移。

## 扩展机制
未来新增独立产品或管理后台时，应在 `08-product/` 下建立子目录，并至少包含 README、愿景、能力地图、用户旅程和发布说明。跨产品共享规则继续由本目录主文档维护，禁止复制。

## 后续待完成内容
- L3 确认后，以真实用户研究和业务优先级形成首批需求条目。
- L5 阶段为产品目标补充正式指标口径。

