# vllm-project/vllm#13889: [Bug]: ValueError: Unsupported config format: ConfigFormat.AUTO on macOS

| 字段 | 值 |
| --- | --- |
| Issue | [#13889](https://github.com/vllm-project/vllm/issues/13889) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Unsupported config format: ConfigFormat.AUTO on macOS

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm startup failed on macOS ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;hardware_porting;model_support cuda build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: ValueError: Unsupported config format: ConfigFormat.AUTO on macOS bug ### Your current environment ### 🐛 Describe the bug vllm startup failed on macOS ### Before submitting a new issue... - [x] Make sure you alre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: cOS ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;hardware_porting;model_support cuda build_error env_dependency Y...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
