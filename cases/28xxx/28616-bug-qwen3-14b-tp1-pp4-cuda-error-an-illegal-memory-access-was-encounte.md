# vllm-project/vllm#28616: [Bug]: Qwen3-14B TP1 PP4 CUDA error an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#28616](https://github.com/vllm-project/vllm/issues/28616) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Qwen3-14B TP1 PP4 CUDA error an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```shell CUDA_VISIBLE_DEVICES=0,1,2,3 \ python -m vllm.entrypoints.openai.api_server \ --model Qwen/Qwen3-14B \ --tensor-parallel-size 1 \ --pipeline-parallel-size 4 \ --port 8080 \ --max-model-len 8120 ``` Subsequently, I generate requests (i.e., calls to v1/chat/completions) following a Poisson arrival process with an average rate of 7 req/s and a fixed input length of 512 tokens. The corresponding logs are presented below. ``` INFO 11-13 05:41:21 [async_llm.py:270] Added request chatcmpl-70390ef6e604447ca3594c97fcb118e4. [rank2]:[E1113 05:41:21.214937724 ProcessGroupNCCL.cpp:1896] [PG ID 3 PG GUID 11 Rank 2] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at /pytorch/c10/cuda/CUDAException.cpp:43 (most recent call first): frame #0: c10::Error::Error(c10::SourceLocation, std::__...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: wen3-14B TP1 PP4 CUDA error an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug ```shell CUDA_VISIBLE_DEVICES=0,1,2,3 \ python -m vllm.entrypoints.openai.api_server \ -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ight be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at /pytorch/c10/cuda/CUDAE...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-14B TP1 PP4 CUDA error an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug ```shell CUDA_VISIBLE_DEVICES=0,1,2,3 \ python -m vllm.entrypoints.openai.api_se...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: INFO 11-13 05:41:21 [async_llm.py:345] Request chatcmpl-8f88c7ce5fd949f09fa3767be290b774 failed (engine dead). INFO 11-13 05:41:21 [async_llm.py:345] Request chatcmpl-82d35b7c43a440ada1bf54c83aea4c28 failed (engine dead...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen3-14B TP1 PP4 CUDA error an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug ```shell CUDA_VISIBLE_DEVICES=0,1,2,3 \ python -m vllm.entrypoints.openai.api_se...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | e/venv/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #4: c10d::processgroupnccl::worknccl::iscompleted() + 0x70 (0x78cd79052710 in /measure/venv/lib/python3.12/si… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | e/venv/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x14d (0x78cd79055ead in /measure/venv/lib/python3.12/site-p… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | e/venv/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdbbf4 (0x78cd68fefbf4 in /opt/conda/envs/py312/bin/../lib/libstdc++.so.6) frame #8… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
