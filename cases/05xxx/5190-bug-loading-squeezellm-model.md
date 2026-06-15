# vllm-project/vllm#5190: [Bug]: loading squeezellm model

| 字段 | 值 |
| --- | --- |
| Issue | [#5190](https://github.com/vllm-project/vllm/issues/5190) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;operator |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: loading squeezellm model

### Issue 正文摘录

### Your current environment I used 0.4.3 version, pip install, cuda vsesion 12.0, A100 GPU RuntimeError: t == DeviceType::CUDA INTERNAL ASSERT FAILED ### 🐛 Describe the bug ``` INFO 06-02 03:21:56 model_runner.py:173] Loading model weights took 12.1389 GB Traceback (most recent call last): File "/export/aiops-data/yuhui/wanda/benchmark_throughput_xgen.py", line 402, in main(args) File "/export/aiops-data/yuhui/wanda/benchmark_throughput_xgen.py", line 221, in main elapsed_time = run_vllm( File "/export/aiops-data/yuhui/wanda/benchmark_throughput_xgen.py", line 85, in run_vllm llm = LLM( File "/miniconda/envs/sqllm/lib/python3.9/site-packages/vllm/entrypoints/llm.py", line 118, in __init__ self.llm_engine = LLMEngine.from_engine_args( File "/miniconda/envs/sqllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 277, in from_engine_args engine = cls( File "/miniconda/envs/sqllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 160, in __init__ self._initialize_kv_caches() File "/miniconda/envs/sqllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 236, in _initialize_kv_caches self.model_executor.determine_num_available_blocks()) File "/miniconda/e...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #21 Add ninja to dependency | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ing squeezellm model bug;stale ### Your current environment I used 0.4.3 version, pip install, cuda vsesion 12.0, A100 GPU RuntimeError: t == DeviceType::CUDA INTERNAL ASSERT FAILED ### 🐛 Describe the bug ``` INFO 06-02...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ug;stale ### Your current environment I used 0.4.3 version, pip install, cuda vsesion 12.0, A100 GPU RuntimeError: t == DeviceType::CUDA INTERNAL ASSERT FAILED ### 🐛 Describe the bug ``` INFO 06-02 03:21:56 model_runner...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: raceback (most recent call last): File "/export/aiops-data/yuhui/wanda/benchmark_throughput_xgen.py", line 402, in main(args) File "/export/aiops-data/yuhui/wanda/benchmark_throughput_xgen.py", line 221, in main elapsed...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: lopment ci_build;model_support cuda;operator crash env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: loading squeezellm model bug;stale ### Your current environment I used 0.4.3 version, pip install, cuda vsesion 12.0, A100 GPU RuntimeError: t == DeviceType::CUDA INTERNAL ASSERT FAILED ### 🐛 Describe the bug ```...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | ython3.9/site-packages/vllm/_c.cpython-39-x86_64-linux-gnu.so) frame #4: <unknown function> + 0x98263 (0x7d837cd58263 in /miniconda/envs/sqllm/lib/python3.9/site-packages/vllm/_c.… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | frame #8: python() [0x4f80b3] frame #10: python() [0x4e69da] frame #12: python() [0x505131] frame #14: python() [0x4e69da] frame #16: python() [0x505131] frame #18: python() [0x |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | frame #12: python() [0x505131] frame #14: python() [0x4e69da] frame #16: python() [0x505131] frame #18: python() [0x4e69da] frame #21: python() [0x5cb113] frame #24: python() [0x |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | frame #16: python() [0x505131] frame #18: python() [0x4e69da] frame #21: python() [0x5cb113] frame #24: python() [0x4e69da] frame #25: python() [0x50509d] frame #28: python() [0x |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | frame #25: python() [0x50509d] frame #28: python() [0x4e69da] frame #29: python() [0x50509d] frame #32: python() [0x4e69da] frame #36: python() [0x5cb113] frame #39: python() [0x |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | frame #28: python() [0x4e69da] frame #29: python() [0x50509d] frame #32: python() [0x4e69da] frame #36: python() [0x5cb113] frame #39: python() [0x4f80b3] frame #40: python() [0x |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
