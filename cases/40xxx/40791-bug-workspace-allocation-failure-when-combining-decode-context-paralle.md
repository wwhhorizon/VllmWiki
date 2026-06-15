# vllm-project/vllm#40791: [Bug]: Workspace allocation failure when combining Decode Context Parallelism (DCP) with EAGLE3 speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#40791](https://github.com/vllm-project/vllm/issues/40791) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Workspace allocation failure when combining Decode Context Parallelism (DCP) with EAGLE3 speculative decoding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Describe the bug When running vLLM V1 with **both** `--decode-context-parallel-size > 1` and `--speculative-config '{"method": "eagle3", ...}'`, the engine crashes during the first request at the speculative decoding phase. The error indicates that the temporary workspace required by DCP attention (`_forward_with_dcp`) has a size of `0.00 MB` and is locked, preventing allocation. ### To Reproduce 1. Pull the image: ```bash docker pull vllm/vllm-openai:deepseekv4-cu130 ``` 2. Run the server with the following command (on an 8-GPU host): ```bash docker run --rm -it --name vllm-kimi-k2.6 \ --gpus all \ --ipc=host \ --ulimit memlock=-1 \ --ulimit stack=67108864 \ -e VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS=1 \ -p 8000:8000 \ -v /model_files:/model_files \ vllm/vllm-openai:deepseekv4-cu130 \ /model_files/kimi-k2.6 \ --tensor-parallel-size 8 \ --served-model-name /model_files/h20/Kimi-K2.5 \ --compilation-config '{"pass_config": {"fuse_allreduce_rms": true}}' \ --speculative-config '{"model": "/model_files/kimi-k2.6-eagle3", "method": "eagle3", "num_speculative_tokens": 3}' \ --gpu-memory-utilization 0.90 \ --max-num-batched-tokens...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Workspace allocation failure when combining Decode Context Parallelism (DCP) with EAGLE3 speculative decoding bug ### Your current environment ### 🐛 Describe the bug ### Describe the bug When running vLLM V1 with...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: eventing allocation. ### To Reproduce 1. Pull the image: ```bash docker pull vllm/vllm-openai:deepseekv4-cu130 ``` 2. Run the server with the following command (on an 8-GPU host): ```bash docker run --rm -it --name vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ug]: Workspace allocation failure when combining Decode Context Parallelism (DCP) with EAGLE3 speculative decoding bug ### Your current environment ### 🐛 Describe the bug ### Describe the bug When running vLLM V1 with *...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 576) ERROR ... [multiproc_executor.py:971] File ".../vllm/v1/attention/backends/flash_attn.py", line 903, in _forward_with_dcp (Worker_TP4_DCP4 pid=1576) ERROR ... [multiproc_executor.py:971] (dcp_context_out,) = curren...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: V1 with **both** `--decode-context-parallel-size > 1` and `--speculative-config '{"method": "eagle3", ...}'`, the engine crashes during the first request at the speculative decoding phase. The error indicates that the t...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
