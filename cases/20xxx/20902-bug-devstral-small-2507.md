# vllm-project/vllm#20902: [Bug]: Devstral-Small-2507

| 字段 | 值 |
| --- | --- |
| Issue | [#20902](https://github.com/vllm-project/vllm/issues/20902) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Devstral-Small-2507

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Tested to start Devstral-Small-2507 with v0.9.1 and v.0.9.2 Container and getting the same error: ValueError: Unknown version: v13 in /root/.cache/huggingface/hub/models--mistralai--Devstral-Small-2507/snapshots/3178e9e2d8880880098af656c1fe223927ce74f8/tekken.json. Make sure to use a valid version string: ['v1', 'v2', 'v3', 'v7', 'v11'] ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Devstral-Small-2507 bug ### Your current environment ### 🐛 Describe the bug Tested to start Devstral-Small-2507 with v0.9.1 and v.0.9.2 Container and getting the same error: ValueError: Unknown version: v13 in /r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 1 and v.0.9.2 Container and getting the same error: ValueError: Unknown version: v13 in /root/.cache/huggingface/hub/models--mistralai--Devstral-Small-2507/snapshots/3178e9e2d8880880098af656c1fe223927ce74f8/tekken.json....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: etting the same error: ValueError: Unknown version: v13 in /root/.cache/huggingface/hub/models--mistralai--Devstral-Small-2507/snapshots/3178e9e2d8880880098af656c1fe223927ce74f8/tekken.json. Make sure to use a valid ver...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: -Small-2507 bug ### Your current environment ### 🐛 Describe the bug Tested to start Devstral-Small-2507 with v0.9.1 and v.0.9.2 Container and getting the same error: ValueError: Unknown version: v13 in /root/.cache/hugg...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
