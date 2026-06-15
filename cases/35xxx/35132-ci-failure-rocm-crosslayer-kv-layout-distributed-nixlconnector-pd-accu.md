# vllm-project/vllm#35132: [CI Failure][ROCm]:  CrossLayer KV layout Distributed NixlConnector PD accuracy tests (4 GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#35132](https://github.com/vllm-project/vllm/issues/35132) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure][ROCm]:  CrossLayer KV layout Distributed NixlConnector PD accuracy tests (4 GPUs)

### Issue 正文摘录

### Name of failing test `CROSS_LAYERS_BLOCKS=True [ROCM_ATTN=1] bash v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test is not running yet on any AMD signal. It is failing: ```bash CROSS_LAYERS_BLOCKS=True ROCM_ATTN=1 bash v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh # or CROSS_LAYERS_BLOCKS=True bash v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh ``` ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/5157/steps/canvas?sid=019c7ec6-4d09-4be4-bbdc-fe7e23f36c80&tab=output This signal belongs in a custom branch to evaluate the feasibility of introducing this new TG.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure][ROCm]: CrossLayer KV layout Distributed NixlConnector PD accuracy tests (4 GPUs) rocm;ci-failure ### Name of failing test `CROSS_LAYERS_BLOCKS=True [ROCM_ATTN=1] bash v1/kv_connector/nixl_integration/config...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [CI Failure][ROCm]: CrossLayer KV layout Distributed NixlConnector PD accuracy tests (4 GPUs) rocm;ci-failure ### Name of failing test `CROSS_LAYERS_BLOCKS=True [ROCM_ATTN=1] bash v1/kv_connector/nixl_integration/config...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure][ROCm]: CrossLayer KV layout Distributed NixlConnector PD accuracy tests (4 GPUs) rocm;ci-failure ### Name of failing test `CROSS_LAYERS_BLOCKS=True [ROCM_ATTN=1] bash v1/kv_connector/nixl_integration/config
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [CI Failure][ROCm]: CrossLayer KV layout Distributed NixlConnector PD accuracy tests (4 GPUs) rocm;ci-failure ### Name of failing test `CROSS_LAYERS_BLOCKS=True [ROCM_ATTN=1] bash v1/kv_connector/nixl_integration/config...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: S_LAYERS_BLOCKS=True [ROCM_ATTN=1] bash v1/kv_connector/nixl_integration/config_sweep_accuracy_test.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
