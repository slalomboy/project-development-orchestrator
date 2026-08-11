# Project Development Orchestrator

[English](README_EN.md) · [成品能力地图](docs/productization-map.md)

把一个软件项目从模糊需求推进到可验证、可追溯、可恢复的交付状态。它维护项目事实、规格、计划、测试证据、版本和回滚边界，并把专业实现交给对应能力。

> 当前状态：公开 Alpha · 固定源码版本：[`v0.5.0-alpha.1`](https://github.com/slalomboy/project-development-orchestrator/tree/v0.5.0-alpha.1) · Apache-2.0 · Python 3.10+ · 不自动部署、发布、推送或改权限

## 它解决什么问题

代码写完不等于项目交付。需求、实现、安装、Tag、Release 和用户侧结果经常被混成一个“完成”。本 Skill 用一套可恢复生命周期把这些真相面分开，并要求每次状态推进都有证据。

适合：新建、接手、修改、调试、测试、打包、部署准备和技术文档等项目型任务。

不适合：纯问答、一次性文案；也不替代前端、数据库、视频等专业 Skill。

## 你会得到什么

- `FIN-PM-000`：从需求到验证、版本、回滚与复盘的完整项目控制面；
- `FIN-PM-001`：六字段需求 Brief、规格、验收条件与变更边界；
- `FIN-PM-002`：带依赖、负责人、验收和测试映射的任务计划；
- `FIN-PM-003`：区分源码、候选包、安装、平台信任、Git/Release 和用户侧结果的验收报告；
- `FIN-PM-004`：版本、Tag、产物、兼容性和回滚一致的交付记录。

详细输入输出、免费领取物与升级路径见[成品能力地图](docs/productization-map.md)。

## 安装

    git clone --branch v0.5.0-alpha.1 --depth 1 https://github.com/slalomboy/project-development-orchestrator.git
    cp -R project-development-orchestrator "$HOME/.codex/skills/project-development-orchestrator"
    python3 -m unittest discover -s project-development-orchestrator/tests -p 'test_*.py'

复制前先确认目标目录不存在；本仓库不提供覆盖现有安装的自动安装器。

## 第一次使用

对 Agent 说：

> 使用 `project-development-orchestrator` 接手这个项目。先只读核对仓库、版本、测试和当前状态，输出目标、范围、排除项、风险、验收和下一步；不要部署或推送。

第一份可用结果应是项目事实、当前阶段、缺口、验证证据与一个明确下一步，而不是“代码看起来没问题”。

## Skill 与工作流

1. 建立六字段 intake，选择最小风险档位；
2. 把需求、验收、架构、任务和测试用稳定 ID 关联；
3. 实现前确认范围与授权，按任务执行专业 Skill；
4. 用真实行为证据推进验证；
5. 分开报告源码、候选、安装、平台信任、Git/Release 和用户侧结果；
6. 记录版本、风险、回滚和下一步。

[快速开始](docs/quickstart.md) · [使用说明](docs/usage.md) · [限制](docs/limitations.md)

## 已验证结果

- 安装包内 15/15 自动测试通过；
- `project-state.json` 合法/非法状态和证据缺口可确定性复现；
- 模板、引用、状态验证器和 Skill 路径在公开候选中完整；
- 当前验证证明源代码候选可用，不等于部署、Release、安装后行为或用户侧分发已验证。

## 限制、隐私与公开边界

公开包不包含私有角色、客户资料、账号、凭据、内部项目记录或机器路径。外部写入、依赖安装、迁移、部署、发布、推送、权限和破坏性操作仍需明确授权。它不能替用户决定会实质改变成本、架构或安全的关键选择。

需求是否被市场验证：**尚未验证**。本仓库只声明测试和实际项目回放支持其行为，不宣传已验证市场需求或业务收益。

## 许可证与来源

原创代码和文档采用 [Apache License 2.0](LICENSE)。维护者：大林·AI开物（Dalin AI Works）。第三方工具、平台和项目代码保持各自许可证；本仓库不重新授权它们。固定 Tag 只代表可追溯源码，本版本没有 GitHub Release。
