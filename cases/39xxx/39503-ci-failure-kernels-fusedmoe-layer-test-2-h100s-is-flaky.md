# vllm-project/vllm#39503: [CI Failure]: Kernels FusedMoE Layer Test (2 H100s) is flaky

| 字段 | 值 |
| --- | --- |
| Issue | [#39503](https://github.com/vllm-project/vllm/issues/39503) |
| 状态 | open |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;distributed_parallel;moe;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;kernel;moe;operator |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Kernels FusedMoE Layer Test (2 H100s) is flaky

### Issue 正文摘录

### Name of failing test tests/kernels/moe/test_moe_layer.py::test_moe_layer[False-deepep_low_latency-2-1-True] ### Basic information - [x] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The `tests/kernels/moe/test_moe_layer.py::test_moe_layer[False-deepep_low_latency-2-1-True]` is occasionally failing in CI. Here's the run from the latest nightly (https://buildkite.com/vllm/ci/builds/60760#019d75fb-1530-448f-a743-a9270a55bc04) where the failure occurs. The test group passed when I reran it. I was able to reproduce the failure locally but only on my first run. It failed the first time I ran the test and has passed every time since. The full output is pasted below. It's unclear if these DeepEP timeouts are caused by a hang or just some first-run slowdown. Output snippet from my local repro. These same timeouts are in the nightly run's output as well. ``` DeepEP timeout check failed: rank = 1, thread = 0, value = 1024) DeepEP timeout check failed: rank = 1, thread = 1, value = 0) DeepEP timeout check failed: rank = 0, thread = 0, value = 0) DeepEP timeout check failed: rank = 0, thread = 1, value...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [CI Failure]: Kernels FusedMoE Layer Test (2 H100s) is flaky ci-failure ### Name of failing test tests/kernels/moe/test_moe_layer.py::test_moe_layer[False-deepep_low_latency-2-1-True] ### Basic information - [x] Flaky
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: # VLLM_USE_FLASHINFER_MOE_FP16=1 # VLLM_USE_FLASHINFER_MOE_FP8 # VLLM_USE_FLASHINFER_MOE_FP4 # VLLM_USE_FLASHINFER_MOE_INT4 parallel_config = ParallelConfig( pipeline_parallel_size=1, data_parallel_size=dp_size, tensor
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [CI Failure]: Kernels FusedMoE Layer Test (2 H100s) is flaky ci-failure ### Name of failing test tests/kernels/moe/test_moe_layer.py::test_moe_layer[False-deepep_low_latency-2-1-True] ### Basic information - [x] Flaky t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: layer.py::test_moe_layer[False-deepep_low_latency-2-1-True] ### Basic information - [x] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: timeout (float): Wait this long (in seconds) before giving up on waiting. grace_period (float): When any processes fail, wait this long (in seconds) for others to shutdown gracefully before terminating them. If they sti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
