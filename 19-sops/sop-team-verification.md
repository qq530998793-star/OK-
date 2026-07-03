# SOP Team Verification

## 用途
定义战队认证和资料审核的标准作业流程。

## 负责人
Team Operations Owner

## 更新时间
2026-07-03

## 版本号
v1.0.0

## 引用关系
- 战队注册：[../05-teams/team-registration.md](../05-teams/team-registration.md)
- 战队模型：[../05-teams/team-model.md](../05-teams/team-model.md)
- SOP 模板：[../17-templates/sop-template.md](../17-templates/sop-template.md)

## Trigger
战队提交注册、认证或资料更新请求时启动本 SOP。

## Inputs
- 战队名称。
- 队长信息。
- 队员信息。
- 参与项目。
- 关联门店或社群。
- 行为准则确认。

## Steps
1. 确认 Team 对象是否已存在。
2. 收集战队基础资料。
3. 检查队长和队员信息完整性。
4. 检查重复战队或异常身份。
5. 确认战队是否接受行为准则。
6. 标记战队状态。
7. 同步给赛事或社群负责人。
8. 留存认证记录。

## Outputs
- 战队资料记录。
- 战队认证状态。
- 异常资料处理记录。

## Exceptions
- 队员信息缺失：退回补充。
- 重复战队：合并或升级人工判断。
- 违规记录未处理：暂停认证。
- 队长身份不清：要求重新确认。

## Related Playbooks
- 城市赛事启动：[../18-playbooks/city-event-launch-playbook.md](../18-playbooks/city-event-launch-playbook.md)
- 社群增长：[../18-playbooks/community-growth-playbook.md](../18-playbooks/community-growth-playbook.md)

## 后续待完成内容
- L3 阶段确认产品如何支持战队认证。
- L5 阶段补充战队认证指标口径。
