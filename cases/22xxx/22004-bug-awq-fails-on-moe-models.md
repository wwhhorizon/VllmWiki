# vllm-project/vllm#22004: [Bug]: AWQ fails on MoE models

| 字段 | 值 |
| --- | --- |
| Issue | [#22004](https://github.com/vllm-project/vllm/issues/22004) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AWQ fails on MoE models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to start a model with vllm, but it fails. Model: tclf90/Qwen3-30B-A3B-Thinking-2507-AWQ (modelscope) logs: root@GPUServer-1:/opt/vllm# docker compose up -d [+] Running 1/1 ✔ Container vllm-vllm-server-1 Started 4.3s root@GPUServer-1:/opt/vllm# docker logs -f vllm-vllm-server-1 DEBUG 07-31 02:22:59 [__init__.py:30] No plugins for group vllm.platform_plugins found. DEBUG 07-31 02:22:59 [__init__.py:35] Checking if TPU platform is available. DEBUG 07-31 02:22:59 [__init__.py:45] TPU platform is not available because: No module named 'libtpu' DEBUG 07-31 02:22:59 [__init__.py:52] Checking if CUDA platform is available. DEBUG 07-31 02:22:59 [__init__.py:72] Confirmed CUDA platform is available. DEBUG 07-31 02:22:59 [__init__.py:100] Checking if ROCm platform is available. DEBUG 07-31 02:22:59 [__init__.py:114] ROCm platform is not available because: No module named 'amdsmi' DEBUG 07-31 02:22:59 [__init__.py:121] Checking if XPU platform is available. DEBUG 07-31 02:22:59 [__init__.py:140] XPU platform is not available because: No module named 'intel_extension_for_pytorch' DEBUG 07-31 02:22:59 [__init__.py:147] Checking if CPU...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: [Bug]: AWQ fails on MoE models bug;stale ### Your current environment ### 🐛 Describe the bug I tried to start a model with vllm, but it fails. Model: tclf90/Qwen3-30B-A3B-Thinking-2507-AWQ (modelscope) logs: root@GPUSer...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: B-A3B-Thinking-2507-AWQ (modelscope) logs: root@GPUServer-1:/opt/vllm# docker compose up -d [+] Running 1/1 ✔ Container vllm-vllm-server-1 Started 4.3s root@GPUServer-1:/opt/vll
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: module named 'libtpu' DEBUG 07-31 02:22:59 [__init__.py:52] Checking if CUDA platform is available. DEBUG 07-31 02:22:59 [__init__.py:72] Confirmed CUDA platform is available. DEBUG 07-31 02:22:59 [__init__.py:100] Chec...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: -Thinking-2507-AWQ', 'trust_remote_code': True, 'max_model_len': 65536, 'quantization': 'awq', 'served_model_name': ['Qwen3-30B-A3B-Thinking-2507-AWQ'], 'tensor_parallel_size': 2, 'enable_expert_parallel': True, 'gpu_me...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
