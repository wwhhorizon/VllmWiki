# vllm-project/vllm#40279: [Bug]: Load Balancer doesn't work

| 字段 | 值 |
| --- | --- |
| Issue | [#40279](https://github.com/vllm-project/vllm/issues/40279) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;moe;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Load Balancer doesn't work

### Issue 正文摘录

### Your current environment torch==2.10.0 triton==3.6.0 cuda-nvcc==12.8.61 vLLM Version==0.19.0 ### 🐛 Describe the bug ### 🐛 Manual Load balancing using `AsyncLLMEngine` class ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: current environment torch==2.10.0 triton==3.6.0 cuda-nvcc==12.8.61 vLLM Version==0.19.0 ### 🐛 Describe the bug ### 🐛 Manual Load balancing using `AsyncLLMEngine` class ### Before submitting a new issue... - [x] Make sur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: esn't work bug ### Your current environment torch==2.10.0 triton==3.6.0 cuda-nvcc==12.8.61 vLLM Version==0.19.0 ### 🐛 Describe the bug ### 🐛 Manual Load balancing using `AsyncLLMEngine` class ### Before submitting a new...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ad Balancer doesn't work bug ### Your current environment torch==2.10.0 triton==3.6.0 cuda-nvcc==12.8.61 vLLM Version==0.19.0 ### 🐛 Describe the bug ### 🐛 Manual Load balancing using `AsyncLLMEngine` class ### Before su...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: t;moe;sampling_logits cache;cuda;moe;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: stions. correctness attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;sampling_logits cache;cuda;moe;sampling;triton build_error;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
