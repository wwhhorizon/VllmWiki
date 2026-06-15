# vllm-project/vllm#35878: [Feature]: Support DeepGEMM MTP3 NV Kernel

| 字段 | 值 |
| --- | --- |
| Issue | [#35878](https://github.com/vllm-project/vllm/issues/35878) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api |
| 子分类 | latency_reg |
| Operator 关键词 | attention;kernel |
| 症状 | slowdown |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support DeepGEMM MTP3 NV Kernel

### Issue 正文摘录

### 🚀 The feature, motivation and pitch MTP3 is supported on NVIDIA's dev branch of DeepGEMM https://github.com/deepseek-ai/DeepGEMM/tree/nv_dev This would allow us to avoid batch expansion and get speedups for num_speculative_tokens=3, when deploying DeepSeek Sparse Attention in DeepSeek V3.2 and GLM5. TRTLLM already uses this branch for their DeepGEMM with MTP=3 using this kernel, and NVIDIA is committed to maintaining this branch as a first-class stable version with additional hardware and feature support beyond the DeepGEMM main branch. TRTLLM implementation reference: https://github.com/NVIDIA/TensorRT-LLM/blob/3d348ab32b0f063b99333c46587524e3bce84102/tensorrt_llm/_torch/attention_backend/sparse/dsa.py#L739 ### Alternatives Current implementation uses batch expansion, which may not be as efficient, especially for long sequences. Do not currently have benchmarking motivating this change, but MTP=3 performance is critical for low-latency and long-context decoding. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](h...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ot be as efficient, especially for long sequences. Do not currently have benchmarking motivating this change, but MTP=3 performance is critical for low-latency and long-context decoding. ### Additional context _No respo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: d NVIDIA is committed to maintaining this branch as a first-class stable version with additional hardware and feature support beyond the DeepGEMM main branch. TRTLLM implementation reference: https://github.com/NVIDIA/T...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support DeepGEMM MTP3 NV Kernel feature request ### 🚀 The feature, motivation and pitch MTP3 is supported on NVIDIA's dev branch of DeepGEMM https://github.com/deepseek-ai/DeepGEMM/tree/nv_dev This would allo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: b/3d348ab32b0f063b99333c46587524e3bce84102/tensorrt_llm/_torch/attention_backend/sparse/dsa.py#L739 ### Alternatives Current implementation uses batch expansion, which may not be as efficient, especially for long sequen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
