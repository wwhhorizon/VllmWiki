# vllm-project/vllm#37709: [CI Failure]:  mi325_2: Distributed Tests (2 GPUs)(H100-MI325)

| 字段 | 值 |
| --- | --- |
| Issue | [#37709](https://github.com/vllm-project/vllm/issues/37709) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe |
| 子分类 | debug |
| Operator 关键词 | moe |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_2: Distributed Tests (2 GPUs)(H100-MI325)

### Issue 正文摘录

### Name of failing test `pytest -v -s tests/distributed/test_context_parallel.py && VLLM_LOGGING_LEVEL=DEBUG python3 examples/offline_inference/data_parallel.py --model=Qwen/Qwen1.5-MoE-A2.7B -tp=1 -dp=2 --max-model-len=2048 --all2all-backend=deepep_high_throughput && pytest -v -s tests/v1/distributed/test_dbo.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There is a DeepEP issue in this TG. ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/6721/steps/canvas?sid=019d09d4-710f-4752-845d-a402e44ef028&tab=output

## 现有链接修复摘要

#38396 [AMD][CI] Update DeepEP branch

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: OGGING_LEVEL=DEBUG python3 examples/offline_inference/data_parallel.py --model=Qwen/Qwen1.5-MoE-A2.7B -tp=1 -dp=2 --max-model-len=2048 --all2all-backend=deepep_high_throughput && pytest -v -s tests/v1/distributed/test_d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_2: Distributed Tests (2 GPUs)(H100-MI325) rocm;ci-failure ### Name of failing test `pytest -v -s tests/distributed/test_context_parallel.py && VLLM_LOGGING_LEVEL=DEBUG python3 examples/offline_infere
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: mi325_2: Distributed Tests (2 GPUs)(H100-MI325) rocm;ci-failure ### Name of failing test `pytest -v -s tests/distributed/test_context_parallel.py && VLLM_LOGGING_LEVEL=DEBUG python3 examples/offline_infere...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: mi325_2: Distributed Tests (2 GPUs)(H100-MI325) rocm;ci-failure ### Name of failing test `pytest -v -s tests/distributed/test_context_parallel.py && VLLM_LOGGING_LEVEL=DEBUG python3 examples/offline_infere...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: -model=Qwen/Qwen1.5-MoE-A2.7B -tp=1 -dp=2 --max-model-len=2048 --all2all-backend=deepep_high_throughput && pytest -v -s tests/v1/distributed/test_dbo.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locall...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38396](https://github.com/vllm-project/vllm/pull/38396) | mentioned | 0.6 | [AMD][CI] Update DeepEP branch | head-of-time compiles for gfx942 and gfx950. This partially addresses #37709 Also, move the testcase to MI325 in order to verify the change, since there are currently no MI355 age… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
