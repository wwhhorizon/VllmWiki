# vllm-project/vllm#22250: [Bug]: I got an `torch._scaled_mm` error using async tp with Ampere GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#22250](https://github.com/vllm-project/vllm/issues/22250) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: I got an `torch._scaled_mm` error using async tp with Ampere GPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug INFO 08-05 19:37:30 [__init__.py:241] Automatically detected platform cuda. WARNING 08-05 19:37:32 [config.py:535] The global random seed is set to 0. Since VLLM_ENABLE_V1_MULTIPROCESSING is set to False, this may affect the random state of the Python process that launched vLLM. INFO 08-05 19:37:42 [config.py:726] Resolved architecture: Qwen3MoeForCausalLM INFO 08-05 19:37:42 [config.py:1765] Using max model len 10000 INFO 08-05 19:37:42 [arg_utils.py:1188] Using mp-based distributed executor backend for async scheduling. INFO 08-05 19:37:42 [config.py:2594] Chunked prefill is enabled with max_num_batched_tokens=2048. WARNING 08-05 19:37:42 [config.py:4914] Batch sizes [1] are removed because they are not multiple of tp_size 2 when sequence parallelism is enabled INFO 08-05 19:37:51 [__init__.py:241] Automatically detected platform cuda. (EngineCore_0 pid=776130) INFO 08-05 19:37:53 [core.py:619] Waiting for init message from front-end. (EngineCore_0 pid=776130) INFO 08-05 19:37:53 [core.py:71] Initializing a V1 LLM engine (v0.10.1.dev371+g74333ae2f) with config: model='/data/pretrained_models/Qwen3-30B-A3B-Thinking-2507-FP8', sp...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: I got an `torch._scaled_mm` error using async tp with Ampere GPU bug;torch.compile ### Your current environment ### 🐛 Describe the bug INFO 08-05 19:37:30 [__init__.py:241] Automatically detected platform cuda. W...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: I got an `torch._scaled_mm` error using async tp with Ampere GPU bug;torch.compile ### Your current environment ### 🐛 Describe the bug INFO 08-05 19:37:30 [__init__.py:241] Automatically detected platform cuda. W...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: O 08-05 19:37:42 [arg_utils.py:1188] Using mp-based distributed executor backend for async scheduling. INFO 08-05 19:37:42 [config.py:2594] Chunked prefill is enabled with max_num_batched_tokens=2048. WARNING 08-05 19:3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: got an `torch._scaled_mm` error using async tp with Ampere GPU bug;torch.compile ### Your current environment ### 🐛 Describe the bug INFO 08-05 19:37:30 [__init__.py:241] Automatically detected platform cuda. WARNING 08...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ckend for async scheduling. INFO 08-05 19:37:42 [config.py:2594] Chunked prefill is enabled with max_num_batched_tokens=2048. WARNING 08-05 19:37:42 [config.py:4914] Batch sizes [1] are removed because they are not mult...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
