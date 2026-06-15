# vllm-project/vllm#39199: [Security] Unpinned Third-Party GitHub Action in macOS Workflow

| 字段 | 值 |
| --- | --- |
| Issue | [#39199](https://github.com/vllm-project/vllm/issues/39199) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Security] Unpinned Third-Party GitHub Action in macOS Workflow

### Issue 正文摘录

### Your current environment Not applicable (CI configuration issue, not runtime environment related) ### 🐛 Describe the bug I identified CI/CD security issue related to an unpinned third-party GitHub Action. ### Finding The macOS workflow uses a third-party action pinned to a mutable tag: - File: `.github/workflows/macos-smoke-test.yml` - Line: 20 - Usage: ```yaml uses: astral-sh/setup-uv@v7 ``` Using mutable tags (e.g., `@v7`, `@main`, `@latest`) introduces a supply chain risk. These tags can be force-updated to point to different commits at any time. If the upstream repository is compromised, malicious code could be executed in CI without any visible changes in this repository. ### Scan Logs The issue was identified using Runner Guard: ``` Runner Guard v2.9.0 | Vigilant ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Fetching workflows from github.com/vllm-project/vllm... Scanning 6 workflow files... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ [LOW] RGS-007 — Unpinned Third-Party Action Using Mutable Tag File: macos-smoke-test.yml (line 20) Job: macos-m1-smoke-test Evidence: Third-party action pinned to mutable ref 'v7': astral-sh/setup-uv@v7 (job has...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -party action pinned to a mutable tag: - File: `.github/workflows/macos-smoke-test.yml` - Line: 20 - Usage: ```yaml uses: astral-sh/setup-uv@v7 ``` Using mutable tags (e.g., `@v7`, `@main`, `@latest`) introduces a suppl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tion in macOS Workflow bug ### Your current environment Not applicable (CI configuration issue, not runtime environment related) ### 🐛 Describe the bug I identified CI/CD security issue related to an unpinned third-part...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n in macOS Workflow bug ### Your current environment Not applicable (CI configuration issue, not runtime environment related) ### 🐛 Describe the bug I identified CI/CD security issue related to an unpinned third-party G...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: action pinned to a mutable tag: - File: `.github/workflows/macos-smoke-test.yml` - Line: 20 - Usage: ```yaml uses: astral-sh/setup-uv@v7 ``` Using mutable tags (e.g., `@v7`, `@main`, `@latest`) introduces a supply chain...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
