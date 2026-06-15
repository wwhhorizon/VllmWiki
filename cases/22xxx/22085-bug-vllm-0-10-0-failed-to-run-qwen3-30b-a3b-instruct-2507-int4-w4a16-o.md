# vllm-project/vllm#22085: [Bug]: vllm 0.10.0 failed to run Qwen3-30B-A3B-Instruct-2507-Int4-W4A16 on 4 L20 GPUs，but success on 2 L20 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#22085](https://github.com/vllm-project/vllm/issues/22085) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.10.0 failed to run Qwen3-30B-A3B-Instruct-2507-Int4-W4A16 on 4 L20 GPUs，but success on 2 L20 GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits cuda;operator;quantization;sampling;triton build_error;n...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: vllm 0.10.0 failed to run Qwen3-30B-A3B-Instruct-2507-Int4-W4A16 on 4 L20 GPUs，but success on 2 L20 GPUs bug;stale ### Your current environment ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm 0.10.0 failed to run Qwen3-30B-A3B-Instruct-2507-Int4-W4A16 on 4 L20 GPUs，but success on 2 L20 GPUs bug;stale ### Your current environment ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Ma...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;quantization;sampling_logits cuda;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
