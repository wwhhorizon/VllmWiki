# vllm-project/vllm#19002: [Bug]:  Engine core initialization failed. See root cause above. Failed core proc(s): {}

| 字段 | 值 |
| --- | --- |
| Issue | [#19002](https://github.com/vllm-project/vllm/issues/19002) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Engine core initialization failed. See root cause above. Failed core proc(s): {}

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I used the command: python3 -m vllm.entrypoints.openai.api_server --model alperenyildiz/vllm_test --port 8001 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits attention;cuda;operator;quantization;sampling crash dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 001 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ing_logits attention;cuda;operator;quantization;sampling crash dtype;env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: I used the command: python3 -m vllm.entrypoints.openai.api_server --model alperenyildiz/vllm_test --port 8001 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: mance attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits attention;cuda;operator;quantization;sampling crash dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
