# vllm-project/vllm#30644: [Feature]: FLASHMLA_SPARSE (SM90/SM100 only) fallback to TILELANG reference kernel (supports ALL)

| 字段 | 值 |
| --- | --- |
| Issue | [#30644](https://github.com/vllm-project/vllm/issues/30644) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;model_support |
| 子分类 |  |
| Operator 关键词 | attention;cuda;kernel;triton |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: FLASHMLA_SPARSE (SM90/SM100 only) fallback to TILELANG reference kernel (supports ALL)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Based on your investigation and the search results, SGLang and vLLM handle the problematic DeepSeek-V3.2 sparse attention (**DSA**) kernels very differently. SGLang has a more flexible architecture that allows it to bypass the unsupported `FLASHMLA_SPARSE` kernel, while vLLM's structure forces its use and fails. Here is a breakdown of why vLLM is stuck and how SGLang works around the issue. ### 🔍 Why vLLM Fails: A Rigid Backend Chain The vLLM logs show the core problem: once `index_topk` is detected, the framework's attention backend selection is forced down a specific path. * **Monolithic FlashMLA Backend**: In vLLM, when a model uses **DeepSeek Sparse Attention (DSA)**, the only backend equipped to handle it is `FLASHMLA_SPARSE` . This backend relies on the high-performance, low-level CUDA kernels from the official `FlashMLA` library . * **Hardware Lock-In**: The official `FlashMLA` kernels are built **only for enterprise GPUs with SM90 (Hopper) and SM100 (Blackwell)** architectures . They do not support the consumer-grade **SM120 (RTX Blackwell)** architecture of your GPU, which is a known hardware support gap . * **No Fallback**: vLLM's...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Feature]: FLASHMLA_SPARSE (SM90/SM100 only) fallback to TILELANG reference kernel (supports ALL) feature request;stale ### 🚀 The feature, motivation and pitch Based on your investigation and the search results, SGLang...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Feature]: FLASHMLA_SPARSE (SM90/SM100 only) fallback to TILELANG reference kernel (supports ALL) feature request;stale ### 🚀 The feature, motivation and pitch Based on your investigation and the search results, SGLang...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: SM100 only) fallback to TILELANG reference kernel (supports ALL) feature request;stale ### 🚀 The feature, motivation and pitch Based on your investigation and the search results, SGLang and vLLM handle the problematic D...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: etected, the framework's attention backend selection is forced down a specific path. * **Monolithic FlashMLA Backend**: In vLLM, when a model uses **DeepSeek Sparse Attention (DSA)**, the only backend equipped to handle...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n a specific path. * **Monolithic FlashMLA Backend**: In vLLM, when a model uses **DeepSeek Sparse Attention (DSA)**, the only backend equipped to handle it is `FLASHMLA_SPARSE` . This backend relies on the high-perform...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
