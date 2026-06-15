# vllm-project/vllm#20118: [Bug]: Model initialization failed

| 字段 | 值 |
| --- | --- |
| Issue | [#20118](https://github.com/vllm-project/vllm/issues/20118) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model initialization failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Engine core initialization failed. Code example: ```python from vllm import LLM llm = LLM(model="facebook/opt-125m") ``` Error: ```text DEBUG 06-26 08:13:27 [__init__.py:31] No plugins for group vllm.platform_plugins found. DEBUG 06-26 08:13:27 [__init__.py:35] Checking if TPU platform is available. DEBUG 06-26 08:13:27 [__init__.py:45] TPU platform is not available because: No module named 'libtpu' DEBUG 06-26 08:13:27 [__init__.py:52] Checking if CUDA platform is available. DEBUG 06-26 08:13:27 [__init__.py:72] Confirmed CUDA platform is available. DEBUG 06-26 08:13:27 [__init__.py:100] Checking if ROCm platform is available. DEBUG 06-26 08:13:27 [__init__.py:114] ROCm platform is not available because: No module named 'amdsmi' DEBUG 06-26 08:13:27 [__init__.py:121] Checking if HPU platform is available. DEBUG 06-26 08:13:27 [__init__.py:128] HPU platform is not available because habana_frameworks is not found. DEBUG 06-26 08:13:27 [__init__.py:138] Checking if XPU platform is available. DEBUG 06-26 08:13:27 [__init__.py:148] XPU platform is not available because: No module named 'intel_extension_for_pytorch' DEBUG 06-26 08:13:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Engine core initialization failed. Code example: ```python from vllm import LLM llm = LLM(model="facebook/opt-125m") ``` Error: ```text DEBUG 06-26 08:13:27 [__init__.py:31] No plugins for group vllm.platform_plugins fo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Model initialization failed bug;stale ### Your current environment ### 🐛 Describe the bug Engine core initialization failed. Code example: ```python from vllm import LLM llm = LLM(model="facebook/opt-125m") ``` E...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: module named 'libtpu' DEBUG 06-26 08:13:27 [__init__.py:52] Checking if CUDA platform is available. DEBUG 06-26 08:13:27 [__init__.py:72] Confirmed CUDA platform is available. DEBUG 06-26 08:13:27 [__init__.py:100] Chec...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: ed as DP rank 0, PP rank 0, TP rank 0, EP rank 0 WARNING 06-26 08:13:57 [topk_topp_sampler.py:59] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best pe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
