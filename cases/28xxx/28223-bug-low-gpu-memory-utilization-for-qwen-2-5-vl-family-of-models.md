# vllm-project/vllm#28223: [Bug]: Low GPU Memory Utilization for Qwen-2.5-VL family of models

| 字段 | 值 |
| --- | --- |
| Issue | [#28223](https://github.com/vllm-project/vllm/issues/28223) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Low GPU Memory Utilization for Qwen-2.5-VL family of models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There appears to be a bug in the torch peak memory calculation with **Qwen-2.5-VL family of** models (base model/quantized). This results in a lower overall GPU memory utilization resulting in very low supported concurrency (as a side effect of low KV Cache availability). On a 4xL20 (or L40) loading , we would see memory utilization along the lines of: - vLLM 0.10.2 - ~45 GB of 46 GB (per GPU) - vLLM 0.11.0 - ~35 GB of 45 GB (per GPU) Using --skip-mm-profile brings gpu memory utilization of vLLM 0.11.0 in line with 0.10.2. This appears to be specific to just the Qwen-2.5-VL (maybe Qwen-3-VL) family of models. I did not see the same issue with adept/fuyu-8b model. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: utilization of vLLM 0.11.0 in line with 0.10.2. This appears to be specific to just the Qwen-2.5-VL (maybe Qwen-3-VL) family of models. I did not see the same issue with adept/fuyu-8b model. ### Before submitting a new...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: Low GPU Memory Utilization for Qwen-2.5-VL family of models bug ### Your current environment ### 🐛 Describe the bug There appears to be a bug in the torch peak memory calculation with **Qwen-2.5-VL family of** mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Low GPU Memory Utilization for Qwen-2.5-VL family of models bug ### Your current environment ### 🐛 Describe the bug There appears to be a bug in the torch peak memory calculation with **Qwen-2.5-VL family of** mo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: GB (per GPU) - vLLM 0.11.0 - ~35 GB of 45 GB (per GPU) Using --skip-mm-profile brings gpu memory utilization of vLLM 0.11.0 in line with 0.10.2. This appears to be specific to just the Qwen-2.5-VL (maybe Qwen-3-VL) fami...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
