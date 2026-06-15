# vllm-project/vllm#32186: [Bug]: Unable to serve Qwen3-8B-FP8 with moriio kv connector

| 字段 | 值 |
| --- | --- |
| Issue | [#32186](https://github.com/vllm-project/vllm/issues/32186) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to serve Qwen3-8B-FP8 with moriio kv connector

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 🐛 Describe the bug Encountered error related to RDMA when serving model with moriio kv connector. ```python VLLM_ROCM_USE_AITER=1 CUDA_VISIBLE_DEVICES=0 vllm serve Qwen/Qwen3-8B-FP8 \ --port 20005 \ --max-num-batched-tokens 4096 \ --distributed-executor-backend mp \ --gpu_memory_utilization 0.85 \ --max-model-len 4096 \ --enforce-eager \ --max_num_seqs 64\ --no-enable-prefix-caching \ --kv-transfer-config '{"kv_connector":"MoRIIOConnector","kv_role":"kv_producer","kv_connector_extra_config":{"proxy_ip":"127.0.0.1","proxy_ping_port":"36367","http_port":"20005"}}' ``` (Worker pid=1945) INFO 01-12 13:57:09 [moriio_connector.py:573] Initializing MoRIIO worker 10.21.9.39:6301 (Worker pid=1945) INFO 01-12 13:57:09 [moriio_connector.py:641] Initializing MoRIIO Engine, engine = , role = producer libibverbs: Warning: Driver bnxt_re does not support the kernel ABI of 6 (supports 1 to 1) for device /sys/class/infiniband/rdma6 libibverbs: Warning: Driver bnxt_re does not support the kernel ABI of 6 (supports 1 to 1) for device /sys/class/infiniband/rdma6 libibverbs: Warning: Driver bnxt_re does not support the kernel ABI of 6 (supports 1 to...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: MA when serving model with moriio kv connector. ```python VLLM_ROCM_USE_AITER=1 CUDA_VISIBLE_DEVICES=0 vllm serve Qwen/Qwen3-8B-FP8 \ --port 20005 \ --max-num-batched-tokens 4096 \ --distributed-executor-backend mp \ --...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: loop/__init__.py", line 96, in run (APIServer pid=1769) return __asyncio.run( (APIServer pid=1769) ^^^^^^^^^^^^^^ (APIServer pid=1769) File "/usr/lib/python3.12/asyncio/runners.py", line 195, in run (APIServer pid=1769)...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Unable to serve Qwen3-8B-FP8 with moriio kv connector bug;rocm ### Your current environment ### 🐛 Describe the bug 🐛 Describe the bug Encountered error related to RDMA when serving model with moriio kv connector....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Unable to serve Qwen3-8B-FP8 with moriio kv connector bug;rocm ### Your current environment ### 🐛 Describe the bug 🐛 Describe the bug Encountered error related to RDMA when serving model with moriio kv connector....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Unable to serve Qwen3-8B-FP8 with moriio kv connector bug;rocm ### Your current environment ### 🐛 Describe the bug 🐛 Describe the bug Encountered error related to RDMA when serving model with moriio kv connector....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
