# vllm-project/vllm#23448: [Bug]: VLLM_ALL2ALL_BACKEND=naive hangs/crashes on multi nodes when serving DeepSeekV3

| 字段 | 值 |
| --- | --- |
| Issue | [#23448](https://github.com/vllm-project/vllm/issues/23448) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: VLLM_ALL2ALL_BACKEND=naive hangs/crashes on multi nodes when serving DeepSeekV3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM_ALL2ALL_BACKEND=naive (the default) hangs/crashes on multi nodes when serving DeepSeekV3 We are aware that PPLX and DeepEP kernels can be used. However, these kernels cannot be used if IB is not available for multinode. To reproduce: ``` # Node 0 (with ip address 10.96.94.252) vllm serve /mnt/.cache/huggingface/hub/models--deepseek-ai--DeepSeek-V3-0324/snapshots/e9b33add76883f293d6bf61f6bd89b497e80e335 --data-parallel-size 16 --data-parallel-size-local 8 --data-parallel-address 10.96.94.252 --data-parallel-rpc-port 13345 --enable-expert-parallel # Node 1 vllm serve /mnt/.cache/huggingface/hub/models--deepseek-ai--DeepSeek-V3-0324/snapshots/e9b33add76883f293d6bf61f6bd89b497e80e335 --headless --data-parallel-size 16 --data-parallel-size-local 8 --data-parallel-start-rank 8 --data-parallel-address 10.96.94.252 --data-parallel-rpc-port 13345 --enable-expert-parallel ``` Execution hangs and the node dies (possibly due to OOM, see analysis with ray below) during CUDA graph capture. And the following errors are logged: If testing with --distributed-executor-backend ray, hanging would also cause CPU memory OOM, and ray OOM killer wo...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: VLLM_ALL2ALL_BACKEND=naive hangs/crashes on multi nodes when serving DeepSeekV3 bug;stale ### Your current environment ### 🐛 Describe the bug VLLM_ALL2ALL_BACKEND=naive (the default) hangs/crashes on multi nodes...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding cuda;kernel;mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: the node dies (possibly due to OOM, see analysis with ray below) during CUDA graph capture. And the following errors are logged: If testing with --distributed-executor-backend ray, hanging would also cause CPU memory OO...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ce: ``` # Node 0 (with ip address 10.96.94.252) vllm serve /mnt/.cache/huggingface/hub/models--deepseek-ai--DeepSeek-V3-0324/snapshots/e9b33add76883f293d6bf61f6bd89b497e80e335 --data-parallel-size 16 --data-parallel-siz...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: L_BACKEND=naive hangs/crashes on multi nodes when serving DeepSeekV3 bug;stale ### Your current environment ### 🐛 Describe the bug VLLM_ALL2ALL_BACKEND=naive (the default) hangs/crashes on multi nodes when serving DeepS...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | x7f90e0786198 in /home/ray/anaconda3/bin/../lib/libstdc++.so.6) frame #4: <unknown function> + 0x94ac3 (0x7f90e092fac3 in /lib/x86_64-linux-gnu/libc.so.6) frame #5: <unknown funct… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | > + 0x94ac3 (0x7f90e092fac3 in /lib/x86_64-linux-gnu/libc.so.6) frame #6: <unknown function> + 0x126850 (0x7f90e09c1850 in /lib/x86_64-linux-gnu/libc.so.6) exception raised from n… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
