# vllm-project/vllm#28400: [CI Failure]: Nightly Failure B200 (Context Parallel)

| 字段 | 值 |
| --- | --- |
| Issue | [#28400](https://github.com/vllm-project/vllm/issues/28400) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Nightly Failure B200 (Context Parallel)

### Issue 正文摘录

### Name of failing test FAILED tests/distributed/test_context_parallel.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```bash FAILED tests/distributed/test_context_parallel.py::test_cp_generation[deepseek-ai/DeepSeek-V2-Lite-Chat-parallel_setup3-mp-auto-test_options3] - AssertionError: function test_cp_generation failed when called with args () and kwargs {'model_id': 'deepseek-ai/DeepSeek-V2-Lite-Chat', 'parallel_setup': ParallelSetup(tp_size=2, pp_size=1, dcp_size=2, dcp_kv_cache_interleave_size=1, eager_mode=False, chunked_prefill=True), 'distributed_backend': 'mp', 'runner': 'auto', 'test_options': CPTestOptions(multi_node_only=False, load_format=None), 'num_gpus_available': 2} (exit code: 256) | FAILED tests/distributed/test_context_parallel.py::test_cp_generation[deepseek-ai/DeepSeek-V2-Lite-Chat-parallel_setup5-mp-auto-test_options5] - AssertionError: function test_cp_generation failed when called with args () and kwargs {'model_id': 'deepseek-ai/DeepSeek-V2-Lite-Chat', 'parallel_setup': ParallelSetup(tp_size=2, pp_size=1, dcp_size=2, dcp_kv_cache_interlea...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Nightly Failure B200 (Context Parallel) ci-failure ### Name of failing test FAILED tests/distributed/test_context_parallel.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Cause
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ing test FAILED tests/distributed/test_context_parallel.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: interleave_size=1, eager_mode=False, chunked_prefill=True), 'distributed_backend': 'mp', 'runner': 'auto', 'test_options': CPTestOptions(multi_node_only=False, load_format=None), 'num_gpus_available': 2} (exit code: 256...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t_context_parallel.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ```bash FAILED tests/distributed/t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: Nightly Failure B200 (Context Parallel) ci-failure ### Name of failing test FAILED tests/distributed/test_context_parallel.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
