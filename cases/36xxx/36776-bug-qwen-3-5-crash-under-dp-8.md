# vllm-project/vllm#36776: [Bug]: qwen 3.5 crash under dp 8

| 字段 | 值 |
| --- | --- |
| Issue | [#36776](https://github.com/vllm-project/vllm/issues/36776) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;fp8 |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen 3.5 crash under dp 8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm will crash under dp 8. my commit is 66f927f20 ``` vllm serve Qwen/Qwen3.5-397B-A17B-FP8 --language-model-only -dp 8 --load-format fastsafetensors -ep vllm bench serve --model Qwen/Qwen3.5-397B-A17B-FP8 --endpoint /v1/completions --dataset-name random --max-concurrency 32 --random-output-len 1024 ``` error log ``` [rank0]:[W311 18:21:36.049434121 CUDAGuardImpl.h:122] Warning: CUDA warning: an illegal memory access was encountered (function destroyEvent) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: nder dp 8. my commit is 66f927f20 ``` vllm serve Qwen/Qwen3.5-397B-A17B-FP8 --language-model-only -dp 8 --load-format fastsafetensors -ep vllm bench serve --model Qwen/Qwen3.5-397B-A17B-FP8 --endpoint /v1/completions --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen 3.5 crash under dp 8 bug ### Your current environment ### 🐛 Describe the bug vllm will crash under dp 8. my commit is 66f927f20 ``` vllm serve Qwen/Qwen3.5-397B-A17B-FP8 --language-model-only -dp 8 --load-fo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ndom-output-len 1024 ``` error log ``` [rank0]:[W311 18:21:36.049434121 CUDAGuardImpl.h:122] Warning: CUDA warning: an illegal memory access was encountered (function destroyEvent) ``` ### Before submitting a new issue....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ons. performance model_support;moe;quantization cuda;fp8 crash dtype;env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: can answer lots of frequently asked questions. performance model_support;moe;quantization cuda;fp8 crash dtype;env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
