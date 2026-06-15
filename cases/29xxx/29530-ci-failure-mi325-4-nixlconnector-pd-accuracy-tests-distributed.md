# vllm-project/vllm#29530: [CI Failure]: mi325_4: NixlConnector PD accuracy tests (Distributed)

| 字段 | 值 |
| --- | --- |
| Issue | [#29530](https://github.com/vllm-project/vllm/issues/29530) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;moe |
| 子分类 |  |
| Operator 关键词 | attention;cache |
| 症状 | build_error;crash |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_4: NixlConnector PD accuracy tests (Distributed)

### Issue 正文摘录

### Name of failing test `uv pip install --system -r /vllm-workspace/requirements/kv_connectors.txt && bash v1/kv_connector/nixl_integration/tp_config_sweep_accuracy_test.sh` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Test:** `tp_config_sweep_accuracy_test.sh` - KV connector NIXL integration tests with tensor parallelism **Configuration:** - Script: `run_accuracy_test.sh` with TP configuration sweep - Configs tested: TP1/TP2 for prefiller/decoder, including MLA models and DP-EP modes - Environment: `UCX_NET_DEVICES=all`, NIXL side channel enabled - KV transfer: NixlConnector for disaggregated prefill/decode **Failure:** `RuntimeError: Worker failed with error ''UCX''` during engine initialization **Error location:** `multiproc_executor.py:344` in `collective_rpc()` → worker process crash **Call stack:** - `EngineCore.__init__()` → `_initialize_kv_caches()` → `model_executor.initialize_from_config()` → `collective_rpc("initialize_from_config")` → worker death **Symptoms:** - Worker process `VllmWorker-1` dies unexpectedly during KV cache initialization -...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_4: NixlConnector PD accuracy tests (Distributed) ci-failure ### Name of failing test `uv pip install --system -r /vllm-workspace/requirements/kv_connectors.txt && bash v1/kv_connector/nixl_integration
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: quirements/kv_connectors.txt && bash v1/kv_connector/nixl_integration/tp_config_sweep_accuracy_test.sh` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [CI Failure]: mi325_4: NixlConnector PD accuracy tests (Distributed) ci-failure ### Name of failing test `uv pip install --system -r /vllm-workspace/requirements/kv_connectors.txt && bash v1/kv_connector/nixl_integratio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: racy_test.sh` - KV connector NIXL integration tests with tensor parallelism **Configuration:** - Script: `run_accuracy_test.sh` with TP configuration sweep - Configs tested: TP1/TP2 for prefiller/decoder, including MLA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: uracy_test.sh` with TP configuration sweep - Configs tested: TP1/TP2 for prefiller/decoder, including MLA models and DP-EP modes - Environment: `UCX_NET_DEVICES=all`, NIXL side channel enabled - KV transfer: NixlConnect...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
