# vllm-project/vllm#32903: [Bug]: FlashInfer error when running vLLM throughput bench on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#32903](https://github.com/vllm-project/vllm/issues/32903) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;model_support;moe;quantization |
| 子分类 | throughput |
| Operator 关键词 | attention;fp8;moe |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer error when running vLLM throughput bench on B200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug running ``` VLLM_WORKER_MULTIPROC_METHOD=spawn \ VLLM_USE_FLASHINFER_MOE_FP8=1 \ VLLM_FLASHINFER_MOE_BACKEND=throughput \ vllm bench throughput \ --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 \ -tp=2 --enable-expert-parallel \ --attention-backend=FLASHINFER ``` res: https://paste.ubuntu.com/p/FQq62qRVxs/ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: running ``` VLLM_WORKER_MULTIPROC_METHOD=spawn \ VLLM_USE_FLASHINFER_MOE_FP8=1 \ VLLM_FLASHINFER_MOE_BACKEND=throughput \ vllm bench throughput \ --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 \ -tp=2 --enable-expert...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: FlashInfer error when running vLLM throughput bench on B200 bug;stale ### Your current environment ### 🐛 Describe the bug running ``` VLLM_WORKER_MULTIPROC_METHOD=spawn \ VLLM_USE_FLASHINFER_MOE_FP8=1 \ VLLM_FLAS...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: FlashInfer error when running vLLM throughput bench on B200 bug;stale ### Your current environment ### 🐛 Describe the bug running ``` VLLM_WORKER_MULTIPROC_METHOD=spawn \ VLLM_USE_FLASHINFER_MOE_FP8=1 \ VLLM_FLAS...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 1 \ VLLM_FLASHINFER_MOE_BACKEND=throughput \ vllm bench throughput \ --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 \ -tp=2 --enable-expert-parallel \ --attention-backend=FLASHINFER ``` res: https://paste.ubuntu.com/...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ug running ``` VLLM_WORKER_MULTIPROC_METHOD=spawn \ VLLM_USE_FLASHINFER_MOE_FP8=1 \ VLLM_FLASHINFER_MOE_BACKEND=throughput \ vllm bench throughput \ --model=nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 \ -tp=2 --enable-exp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
