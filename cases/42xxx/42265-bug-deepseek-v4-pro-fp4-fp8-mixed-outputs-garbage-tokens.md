# vllm-project/vllm#42265: [Bug]:  DeepSeek-V4-Pro (fp4+fp8 mixed) outputs garbage tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#42265](https://github.com/vllm-project/vllm/issues/42265) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  DeepSeek-V4-Pro (fp4+fp8 mixed) outputs garbage tokens

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Frequently outputting garbage tokens that do not meet expectations, especially in front of numbers in the code, as shown in the following figure: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: DeepSeek-V4-Pro (fp4+fp8 mixed) outputs garbage tokens bug ### Your current environment ### 🐛 Describe the bug Frequently outputting garbage tokens that do not meet expectations, especially in front of numbers in...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Frequently outputting garbage tokens that do not meet expectations, especially in front of numbers in the code, as shown in the following figure: ### Before submitting a new issue... - [x] Make sure you already searched...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: questions. performance attention_kv_cache;ci_build;distributed_parallel;model_support;quantization fp8 dtype Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;model_support;quantizati...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
