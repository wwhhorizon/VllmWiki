# vllm-project/vllm#29176: [CI Failure]: [AMD] Nixl PD tests

| 字段 | 值 |
| --- | --- |
| Issue | [#29176](https://github.com/vllm-project/vllm/issues/29176) |
| 状态 | open |
| 标签 | rocm;unstale;ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: [AMD] Nixl PD tests

### Issue 正文摘录

### Name of failing test bash v1/kv_connector/nixl_integration/tp_config_sweep_accuracy_test.sh ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test I think there may be some issues with the nixl package being installed on the amd CI, as it appears to be missing UCX, which possibly would need to be built from source? ``` (Worker_TP0 pid=1295) ERROR 11-20 07:10:15 [multiproc_executor.py:822] self.model_runner.initialize_kv_cache(kv_cache_config) -- (Worker_TP0 pid=1295) ERROR 11-20 07:10:15 [multiproc_executor.py:822] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_model_runner.py", line 5020, in initialize_kv_cache (Worker_TP0 pid=1295) ERROR 11-20 07:10:15 [multiproc_executor.py:822] kv_transfer_group.register_kv_caches(kv_caches) (Worker_TP0 pid=1295) ERROR 11-20 07:10:15 [multiproc_executor.py:822] File "/usr/local/lib/python3.12/dist-packages/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py", line 256, in register_kv_caches (Worker_TP0 pid=1295) ERROR 11-20 07:10:15 [multiproc_executor.py:822] self.connector_worker.register_kv_caches(kv_c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: [AMD] Nixl PD tests rocm;unstale;ci-failure ### Name of failing test bash v1/kv_connector/nixl_integration/tp_config_sweep_accuracy_test.sh ### Basic information - [ ] Flaky test - [ ] Can reproduce local
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ilure ### Name of failing test bash v1/kv_connector/nixl_integration/tp_config_sweep_accuracy_test.sh ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: e of failing test bash v1/kv_connector/nixl_integration/tp_config_sweep_accuracy_test.sh ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: [AMD] Nixl PD tests rocm;unstale;ci-failure ### Name of failing test bash v1/kv_connector/nixl_integration/tp_config_sweep_accuracy_test.sh ### Basic information - [ ] Flaky test - [ ] Can reproduce locall...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [multiproc_executor.py:822] self.nixl_wrapper.register_memory(descs, backends=self.nixl_backends) (Worker_TP0 pid=1295) ERROR 11-20 07:10:15 [multiproc_executor.py:822] File "/usr/local/lib/python3.12/dist-packages/nixl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
