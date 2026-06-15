# vllm-project/vllm#4430: [Bug]: Engine iteration timed out. This should never happen!

| 字段 | 值 |
| --- | --- |
| Issue | [#4430](https://github.com/vllm-project/vllm/issues/4430) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 31; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;oom;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Engine iteration timed out. This should never happen!

### Issue 正文摘录

### UPDATE on 2024-05-23 Workaround: Use the `--disable-custom-all-reduce` flag when starting the vLLM instance. Thanks @ywang96 ! ## Following is the original post ### 🐛 Describe the bug ### Summary A model execution thread hangs at [`_random_sample (vllm/model_executor/layers/sampler.py:292)`](https://github.com/vllm-project/vllm/blob/468d761b32e3b3c5d64eeaa797e54ab809b7e50c/vllm/model_executor/layers/sampler.py#L292) mysteriously during inference, and the corresponding code at that line is `random_samples = random_samples.cpu()` ### What happened We upgraded vLLM from `v0.3.3` to `0.4.x`, but found vLLM occasionally got stuck and refused to serve requests. From the vLLM log, we saw that a request never got finished. After we dug deeper, we found that it was because a thread got stuck during execution. #### Your current environment vLLM was running inside a docker container. The following was collected from inside the container. ```text Collecting environment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang ver...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ng execution. #### Your current environment vLLM was running inside a docker container. The following was collected from inside the container. ```text Collecting environment information... PyTorch version: 2.2.1+cu121 I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.2.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ## Following is the original post ### 🐛 Describe the bug ### Summary A model execution thread hangs at [`_random_sample (vllm/model_executor/layers/sampler.py:292)`](https://github.com/vllm-project/vllm/blob/468d761b32e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.19.3 [pip3] torch==2.2.1 [pip3] triton==2.2.0 [pip3] vllm-nccl-cu12==2.18.1.0.3.0 [conda] Could not collectROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ut: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0% INFO 04-28 16:24:40 metrics.py:229] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput:...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | sr/lib/x86_64-linux-gnu/libc.so.6) (rayworkerwrapper pid=7156) frame #4: clone + 0x44 (0x7f7fd7b90a04 in /usr/lib/x86_64-linux-gnu/libc.so.6) (rayworkerwrapper pid=7156) (rayworke |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | sr/lib/x86_64-linux-gnu/libc.so.6) (rayworkerwrapper pid=7156) frame #6: clone + 0x44 (0x7f7fd7b90a04 in /usr/lib/x86_64-linux-gnu/libc.so.6) (rayworkerwrapper pid=7156) (rayworke |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
