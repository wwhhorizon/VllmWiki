# vllm-project/vllm#29529: [CI Failure]: mi325_2: Distributed Tests (2 GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#29529](https://github.com/vllm-project/vllm/issues/29529) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: mi325_2: Distributed Tests (2 GPUs)

### Issue 正文摘录

### Name of failing test `TP_SIZE=1 DP_SIZE=2 pytest -v -s v1/distributed/test_async_llm_dp.py && TP_SIZE=1 DP_SIZE=2 pytest -v -s v1/distributed/test_external_lb_dp.py && DP_SIZE=2 pytest -v -s v1/entrypoints/openai/test_multi_api_servers.py && pytest -v -s entrypoints/llm/test_collective_rpc.py && pytest -v -s ./compile/fullgraph/test_basic_correctness.py && pytest -v -s ./compile/test_wrapper.py && VLLM_TEST_SAME_HOST=1 torchrun --nproc-per-node=4 distributed/test_same_node.py | grep 'Same node test passed' && VLLM_TEST_SAME_HOST=1 VLLM_TEST_WITH_DEFAULT_DEVICE_SET=1 torchrun --nproc-per-node=4 distributed/test_same_node.py | grep 'Same node test passed' && pytest -v -s distributed/test_sequence_parallel.py && CUDA_VISIBLE_DEVICES=0,1 pytest -v -s v1/shutdown && pytest -v -s v1/worker/test_worker_memory_snapshot.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Test:** `test_async_llm_dp.py::test_load` - V1 async data parallel engine testing **Configuration:** - Models: `ibm-research/PowerMoE-3b`, `hmellor/tiny-random-LlamaForCausalLM` - Data parallel b...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: n && pytest -v -s v1/worker/test_worker_memory_snapshot.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_2: Distributed Tests (2 GPUs) rocm;ci-failure ### Name of failing test `TP_SIZE=1 DP_SIZE=2 pytest -v -s v1/distributed/test_async_llm_dp.py && TP_SIZE=1 DP_SIZE=2 pytest -v -s v1/distributed/test_ext
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [CI Failure]: mi325_2: Distributed Tests (2 GPUs) rocm;ci-failure ### Name of failing test `TP_SIZE=1 DP_SIZE=2 pytest -v -s v1/distributed/test_async_llm_dp.py && TP_SIZE=1 DP_SIZE=2 pytest -v -s v1/distributed/test_ex...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rch/PowerMoE-3b`, `hmellor/tiny-random-LlamaForCausalLM` - Data parallel backend: `ray` (fails) vs `mp` (passes) - Output kinds: `DELTA`, `FINAL_ONLY` - DP_SIZE=2 **Failure 1 (4 tests):** `RuntimeError: NCCL error: inva...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: r_memory_snapshot.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Test:** `test_async_llm_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
