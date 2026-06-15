# vllm-project/vllm#41323: [CI Failure]:  mi300_1: V1 Core + KV + Metrics

| 字段 | 值 |
| --- | --- |
| Issue | [#41323](https://github.com/vllm-project/vllm/issues/41323) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi300_1: V1 Core + KV + Metrics

### Issue 正文摘录

### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-v1-core---kv---metrics && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd /vllm-workspace/tests && uv pip install --system -r /vllm-workspace/requirements/kv_connectors_rocm.txt && pytest -v -s -m 'not cpu_test' v1/core && pytest -v -s v1/executor && pytest -v -s v1/kv_offload && pytest -v -s v1/worker && pytest -v -s -m 'not cpu_test' v1/kv_connector/unit && pytest -v -s -m 'not cpu_test' v1/metrics && pip install -U git+https://github.com/robertgshaw2-redhat/lm-evaluation-harness.git@streaming-api && pytest -v -s entrypoints/openai/correctness/test_lmeval.py::test_lm_eval_accuracy_v1_engine` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` ERROR 04-29 07:29:19 [worker.py:2112] Traceback (most recent call last): ERROR 04-29 07:29:19 [worker.py:2112] File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/kv_transfer/kv_connector/v1/nixl/worker.py", line 2096, in _read_blocks ERROR 04-29 07:29:19 [worker.py:2112] handle = self.nixl_wrapper.make_prepped_xfer( ERROR 04...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [CI Failure]: mi300_1: V1 Core + KV + Metrics ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-v1-core---kv---metrics && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 &...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi300_1: V1 Core + KV + Metrics ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-v1-core---kv---metrics && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 &
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ailure]: mi300_1: V1 Core + KV + Metrics ci-failure ### Name of failing test `(command rocm-smi || true) && export VLLM_TEST_GROUP_NAME=mi300_1-v1-core---kv---metrics && export VLLM_ALLOW_DEPRECATED_BEAM_SEARCH=1 && cd...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: pytest -v -s entrypoints/openai/correctness/test_lmeval.py::test_lm_eval_accuracy_v1_engine` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transforme...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: 'not cpu_test' v1/core && pytest -v -s v1/executor && pytest -v -s v1/kv_offload && pytest -v -s v1/worker && pytest -v -s -m 'not cpu_test' v1/kv_connector/unit && pytest -v -s -m 'not cpu_test' v1/metrics && pip insta...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
