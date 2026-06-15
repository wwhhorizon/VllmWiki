# vllm-project/vllm#32222: [CI Failure]:  DP EP NixlConnector PD accuracy tests (Distributed)

| 字段 | 值 |
| --- | --- |
| Issue | [#32222](https://github.com/vllm-project/vllm/issues/32222) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  DP EP NixlConnector PD accuracy tests (Distributed)

### Issue 正文摘录

### Name of failing test `uv pip install --system -r /vllm-workspace/requirements/kv_connectors_rocm.txt && VLLM_ATTENTION_BACKEND=ROCM_ATTN DP_EP=1 bash v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a regression in this test group: ```log (EngineCore_DP1 pid=754) ERROR 01-12 17:11:19 [core.py:936] raise RuntimeError("NIXL is not available") 2026-01-12 17:11:19 UTC (EngineCore_DP1 pid=754) ERROR 01-12 17:11:19 [core.py:936] RuntimeError: NIXL is not available ... 2026-01-12 17:11:19 UTC (EngineCore_DP1 pid=754) File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py", line 2374, in shutdown 2026-01-12 17:11:19 UTC (EngineCore_DP1 pid=754) self._handshake_initiation_executor.shutdown(wait=False) 2026-01-12 17:11:19 UTC (EngineCore_DP1 pid=754) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 2026-01-12 17:11:19 UTC (EngineCore_DP1 pid=754) AttributeError: 'NixlConnectorWorker' object has no attribute '_handshake_initiation_executor' ``` ### 📝 History of f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: DP EP NixlConnector PD accuracy tests (Distributed) ci-failure ### Name of failing test `uv pip install --system -r /vllm-workspace/requirements/kv_connectors_rocm.txt && VLLM_ATTENTION_BACKEND=ROCM_ATTN D
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure]: DP EP NixlConnector PD accuracy tests (Distributed) ci-failure ### Name of failing test `uv pip install --system -r /vllm-workspace/requirements/kv_connectors_rocm.txt && VLLM_ATTENTION_BACKEND=ROCM_ATTN D...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: -r /vllm-workspace/requirements/kv_connectors_rocm.txt && VLLM_ATTENTION_BACKEND=ROCM_ATTN DP_EP=1 bash v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh` ### Basic information - [ ] Flaky test - [x] Can re...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [CI Failure]: DP EP NixlConnector PD accuracy tests (Distributed) ci-failure ### Name of failing test `uv pip install --system -r /vllm-workspace/requirements/kv_connectors_rocm.txt && VLLM_ATTENTION_BACKEND=ROCM_ATTN D...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: TTENTION_BACKEND=ROCM_ATTN DP_EP=1 bash v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
