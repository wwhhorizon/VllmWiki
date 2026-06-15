# vllm-project/vllm#28091: [Bug]: Aeala/ShareGPT_Vicuna_unfiltered should not be marked as multimodal in benchmarks/datasets.py

| 字段 | 值 |
| --- | --- |
| Issue | [#28091](https://github.com/vllm-project/vllm/issues/28091) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Aeala/ShareGPT_Vicuna_unfiltered should not be marked as multimodal in benchmarks/datasets.py

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/18b39828d90413d05d770dfd2e2f48304f4ca0eb/vllm/benchmarks/datasets.py#L2276-L2280 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;ope...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Aeala/ShareGPT_Vicuna_unfiltered should not be marked as multimodal in benchmarks/datasets.py bug ### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/18b39828d90413d05d77...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 280 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: : Aeala/ShareGPT_Vicuna_unfiltered should not be marked as multimodal in benchmarks/datasets.py bug ### Your current environment ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/18b39828d90413d05d770dfd2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
