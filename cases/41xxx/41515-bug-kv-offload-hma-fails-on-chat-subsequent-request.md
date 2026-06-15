# vllm-project/vllm#41515: [Bug]:  [kv_offload+HMA] Fails on chat subsequent request

| 字段 | 值 |
| --- | --- |
| Issue | [#41515](https://github.com/vllm-project/vllm/issues/41515) |
| 状态 | open |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  [kv_offload+HMA] Fails on chat subsequent request

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I did test Qwen 3.6 27B FP8 and kv offload. command line: `VLLM_SKIP_P2P_CHECK=1 CUDA_VISIBLE_DEVICES=0,1 VLLM_NCCL_SO_PATH=/home/nicolas/nccl/build/lib/libnccl.so.2.30.3 NCCL_P2P_LEVEL=SYS vllm serve Qwen/Qwen3.6-27B-FP8 -tp 2 --reasoning-parser qwen3 --enable-prefix-caching --speculative-config '{"method": "mtp", "num_speculative_tokens": 3}' --enable-auto-tool-choice --tool-call-parser qwen3_coder --prefix-caching-hash-algo xxhash --kv-offloading-size 16 --max_num_batched_tokens 16384` It was NOT possible before this pull request [https://github.com/vllm-project/vllm/pull/41445](https://github.com/vllm-project/vllm/pull/41445). Now it works but issue arise when i continue the chat. First chat completion is fine, second one fails I compile VLLM (`TORCH_CUDA_ARCH_LIST="12.0+PTX" pip install -e .`) from sources every day, and do lots of testing. This issue do only happen with **`--kv-offloading-size`** (as it was not possible before) ``` (APIServer pid=3518) INFO 05-02 19:33:30 [loggers.py:271] Engine 000: Avg prompt throughput: 144.7 tokens/s, Avg generation throughput: 151.9 tokens/s, Running: 1 reqs, Waiting: 0 reqs, GPU KV ca...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: [kv_offload+HMA] Fails on chat subsequent request bug ### Your current environment ### 🐛 Describe the bug I did test Qwen 3.6 27B FP8 and kv offload. command line: `VLLM_SKIP_P2P_CHECK=1 CUDA_VISIBLE_DEVICES=0,1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: P_CHECK=1 CUDA_VISIBLE_DEVICES=0,1 VLLM_NCCL_SO_PATH=/home/nicolas/nccl/build/lib/libnccl.so.2.30.3 NCCL_P2P_LEVEL=SYS vllm serve Qwen/Qwen3.6-27B-FP8 -tp 2 --reasoning-parser qwen3 --enable-prefix-caching --speculative...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: bug ### Your current environment ### 🐛 Describe the bug I did test Qwen 3.6 27B FP8 and kv offload. command line: `VLLM_SKIP_P2P_CHECK=1 CUDA_VISIBLE_DEVICES=0,1 VLLM_NCCL_SO_PATH=/home/nicolas/nccl/build/lib/libnccl.so...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: current environment ### 🐛 Describe the bug I did test Qwen 3.6 27B FP8 and kv offload. command line: `VLLM_SKIP_P2P_CHECK=1 CUDA_VISIBLE_DEVICES=0,1 VLLM_NCCL_SO_PATH=/home/nicolas/nccl/build/lib/libnccl.so.2.30.3 NCCL_...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: [kv_offload+HMA] Fails on chat subsequent request bug ### Your current environment ### 🐛 Describe the bug I did test Qwen 3.6 27B FP8 and kv offload. command line: `VLLM_SKIP_P2P_CHECK=1 CUDA_VISIBLE_DEVICES=0,1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
