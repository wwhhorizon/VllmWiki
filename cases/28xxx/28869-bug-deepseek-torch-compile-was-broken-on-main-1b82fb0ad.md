# vllm-project/vllm#28869: [Bug]: deepseek + torch compile was broken on main (1b82fb0ad)

| 字段 | 值 |
| --- | --- |
| Issue | [#28869](https://github.com/vllm-project/vllm/issues/28869) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deepseek + torch compile was broken on main (1b82fb0ad)

### Issue 正文摘录

### Your current environment NGC 25.03 (torch 2.7.0 with cu128) on H20. ### 🐛 Describe the bug The main branch (tested with 1b82fb0ad3cea2e1a31da4fa20dd736a8a181089) seems to be broken with DeepSeek-R1 model (with TP8, on H20) when torch compile with on, with some correctness issue. The error can be reproduced by setting `--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}'`, and if `{"mode": 0}` is added to compilation config (cuda graph without torch compile), the error disappears. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: deepseek + torch compile was broken on main (1b82fb0ad) bug;torch.compile;stale ### Your current environment NGC 25.03 (torch 2.7.0 with cu128) on H20. ### 🐛 Describe the bug The main branch (tested with 1b82fb0a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: issue. The error can be reproduced by setting `--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}'`, and if `{"mode": 0}` is added to compilation config (cuda graph without torch compile), the error disappears...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: b0ad3cea2e1a31da4fa20dd736a8a181089) seems to be broken with DeepSeek-R1 model (with TP8, on H20) when torch compile with on, with some correctness issue. The error can be reproduced by setting `--compilation-config '{"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eepseek + torch compile was broken on main (1b82fb0ad) bug;torch.compile;stale ### Your current environment NGC 25.03 (torch 2.7.0 with cu128) on H20. ### 🐛 Describe the bug The main branch (tested with 1b82fb0ad3cea2e1...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: en torch compile with on, with some correctness issue. The error can be reproduced by setting `--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}'`, and if `{"mode": 0}` is added to compilation config (cuda gr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
