# vllm-project/vllm#29523: [CI Failure]: mi325_4: Distributed Tests (4 GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#29523](https://github.com/vllm-project/vllm/issues/29523) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_4: Distributed Tests (4 GPUs)

### Issue 正文摘录

### Name of failing test `torchrun --nproc-per-node=4 distributed/test_torchrun_example.py && PP_SIZE=2 torchrun --nproc-per-node=4 distributed/test_torchrun_example.py && TP_SIZE=4 torchrun --nproc-per-node=4 distributed/test_torchrun_example_moe.py && PP_SIZE=2 TP_SIZE=2 torchrun --nproc-per-node=4 distributed/test_torchrun_example_moe.py && DP_SIZE=4 ENABLE_EP=1 torchrun --nproc-per-node=4 distributed/test_torchrun_example_moe.py && TP_SIZE=2 DP_SIZE=2 ENABLE_EP=1 torchrun --nproc-per-node=4 distributed/test_torchrun_example_moe.py && python3 ../examples/offline_inference/data_parallel.py --enforce-eager && TP_SIZE=2 DP_SIZE=2 pytest -v -s v1/distributed/test_async_llm_dp.py && TP_SIZE=2 DP_SIZE=2 pytest -v -s v1/distributed/test_external_lb_dp.py && TP_SIZE=1 DP_SIZE=4 pytest -v -s v1/distributed/test_internal_lb_dp.py && TP_SIZE=1 DP_SIZE=4 pytest -v -s v1/distributed/test_hybrid_lb_dp.py && pytest -v -s v1/engine/test_engine_core_client.py::test_kv_cache_events_dp && pytest -v -s distributed/test_utils.py && pytest -v -s compile/fullgraph/test_basic_correctness.py && pytest -v -s distributed/test_pynccl.py && pytest -v -s distributed/test_events.py && pytest -v -s distribute...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: **Failing Test:** `data_parallel.py` example script Tests data parallelism with multiprocessing by spawning worker processes to handle distributed inference across multiple DP ranks. **Failure:** RuntimeError during mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: mi325_4: Distributed Tests (4 GPUs) ci-failure ### Name of failing test `torchrun --nproc-per-node=4 distributed/test_torchrun_example.py && PP_SIZE=2 torchrun --nproc-per-node=4 distributed/test_torchrun_e
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: mples/offline_inference && VLLM_ALLOW_INSECURE_SERIALIZATION=1 python3 rlhf.py && VLLM_ALLOW_INSECURE_SERIALIZATION=1 RAY_DEDUP_LOGS=0 python3 rlhf_colocate.py && popd` ### Basic information - [ ] Flaky test - [ ] Can r...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _colocate.py && popd` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Test:** `data_parallel.p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: in the parent, violating subprocess restrictions. The code path through quantization utils triggers device capability checks during import, which fails in forked contexts. Unlike the test suite which explicitly sets spa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
