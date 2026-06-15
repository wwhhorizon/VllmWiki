# vllm-project/vllm#17098: [Bug]: [0.7.2+] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#17098](https://github.com/vllm-project/vllm/issues/17098) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: [0.7.2+] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using vllm 0.7.2 (with https://github.com/vllm-project/vllm/pull/13693 cherry-picked) to deploy Deepseek-R1, it has running normally for some days, but occasionally shutdown with the following exception: ``` INFO 04-15 00:31:10 metrics.py:455] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 204.9 tokens/s, Running: 30 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 43.5%, CPU KV cache usage: 0.0%. bj4-ml-g8h20-k8s-slave471-20250326:808:21232 [0] NCCL INFO Using non-device net plugin version 0 bj4-ml-g8h20-k8s-slave471-20250326:808:21232 [0] NCCL INFO Using network IB bj4-ml-g8h20-k8s-slave471-20250326:808:21232 [0] NCCL INFO DMA-BUF is available on GPU device 0 bj4-ml-g8h20-k8s-slave471-20250326:808:21232 [0] NCCL INFO ncclCommInitRank comm 0x7f4600184e60 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId e000 commId 0x3ce46418f810614b - Init START bj4-ml-g8h20-k8s-slave471-20250326:808:21232 [0] NCCL INFO MNNVL busId 0xe000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0 bj4-ml-g8h20-k8s-slave471-20250326:808:21232 [0] NCCL INFO Setting affinity for GPU 0 to ffff,ffffffff,00000000,0000ffff,ffffffff bj4-ml-...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 8s-slave471-20250326:808:21232 [0] NCCL INFO Using non-device net plugin version 0 bj4-ml-g8h20-k8s-slave471-20250326:808:21232 [0] NCCL INFO Using network IB bj4-ml-g8h20-k8s-slave471-20250326:808:21232 [0] NCCL INFO D...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 8, in forward ERROR 04-15 00:31:11 worker_base.py:574] output = self.quant_method.apply(self, x, bias) ERROR 04-15 00:31:11 worker_base.py:574] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-15 00:31:11 worker_base.py:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: with exception: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug Using vllm 0.7.2 (with https://github.com/vllm-project/vllm/pull/13693 cherry-picked) to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 1:11 worker_base.py:574] File "/usr/local/lib/python3.12/dist-packages/triton/runtime/jit.py", line 345, in ERROR 04-15 00:31:11 worker_base.py:574] return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: [0.7.2+] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug Using vllm 0.7.2 (with https://...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 0x94ac3 (0x7f8f956d9ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #4: <unknown function> + 0x126a40 (0x7f8f9576ba40 in /usr/lib/x86_64-linux-gnu/libc.so.6) error 04-15 00:31:11 |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x14d (0x7f8f4aa2c61d in /usr/local/lib/python3.12/dist-pack… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | /local/lib/python3.12/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0x145c0 (0x7f8f94f9c5c0 in /usr/local/lib/python3.12/dist-packages/torch/lib/libtorc… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
