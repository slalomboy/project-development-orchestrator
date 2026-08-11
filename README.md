# 项目研发总控

面向需要可复用 Agent Skill 工作流的个人与团队。研发任务容易在需求、实现、测试、版本和交付之间失去可追溯关系。先核项目事实，再选择最小流程档位，维护范围、验证、版本与回滚证据。

**当前状态：**`v0.1.0-alpha.1` 首个固定源码版本；本仓库不提供 GitHub Release。**下一步：**按固定 Tag 安装并完成一次最小调用，所有外部动作继续服从人工授权。English: [README_EN.md](README_EN.md).

## 解决什么问题

- 识别新建、续做与接管场景
- 建立需求—验收—测试追溯
- 判断版本影响
- 输出交付与回滚状态

## 安装

使用固定 Tag：`git clone --branch v0.1.0-alpha.1 --depth 1 https://github.com/slalomboy/project-development-orchestrator.git`。将仓库根目录作为 Skill 安装目录。

## 第一次使用

调用：

> 使用 project-development-orchestrator 接手这个现有项目，先只读盘点事实并给出最小修复计划。

## 限制

- 不包含私有治理规则、账号、项目清单或交付数据
- 不自动部署、推送、付费或改权限
- 专业实现仍交给对应领域能力

## 版本、许可证与来源

- 版本：`v0.1.0-alpha.1`。
- 许可证：[`Apache-2.0`](LICENSE)，已由老板明确选择。
- 来源：大林·AI开物内部形成能力的公开轻量重写，不包含私有路径、账号、密钥、客户数据或内部控制面。
- 状态：`PUBLICATION_AUTHORIZED_PENDING_REMOTE_VERIFICATION`。

[English docs](docs/en/README.md) · [License record](LICENSE-DECISION.md)
