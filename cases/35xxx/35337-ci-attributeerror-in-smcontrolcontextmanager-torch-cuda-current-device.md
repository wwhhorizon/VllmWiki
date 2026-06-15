# vllm-project/vllm#35337: [CI] AttributeError in SMControlContextManager: torch.cuda.current_device() returns int, not device object

| 字段 | 值 |
| --- | --- |
| Issue | [#35337](https://github.com/vllm-project/vllm/issues/35337) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;model_support;moe;scheduler_memory |
| 子分类 | debug |
| Operator 关键词 | cuda;moe |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI] AttributeError in SMControlContextManager: torch.cuda.current_device() returns int, not device object

### Issue 正文摘录

## Name of failing test - `v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_low_latency]` - `v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_high_throughput]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Distributed Tests (2 GPUs)(H100) **Category:** test ## Describe the failing test During V1 engine initialization with data parallel and expert parallel enabled, the UBatchWrapper initialization fails in SMControlContextManager.__init__() when attempting to get GPU compute units. The code calls `torch.cuda.current_device().index`, but torch.cuda.current_device() returns an integer (the device index) directly, not a device object with an .index attribute. This causes an AttributeError: 'int' object has no attribute 'index'. The error occurs during model loading after weights are successfully loaded, when initializing the SM control context for micro-batch scheduling. ``` AttributeError: 'int' object has no attribute 'index' ``` ## Relevant builds - [Build #53087](https://buildkite.com/vllm/ci/builds/53087) (cd436736) - [Distributed Tests (2 GPUs)(H100)](https://buildkite.com/vllm/ci/builds/5308...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI] AttributeError in SMControlContextManager: torch.cuda.current_device() returns int, not device object ci-failure ## Name of failing test - `v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_low_latency]` - `v1
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [CI] AttributeError in SMControlContextManager: torch.cuda.current_device() returns int, not device object ci-failure ## Name of failing test - `v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_low_latency]` - `v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: nt_device() returns int, not device object ci-failure ## Name of failing test - `v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_low_latency]` - `v1/distributed/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_high_thro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: d/test_dbo.py::test_dbo_dp_ep_gsm8k[deepep_high_throughput]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Distributed Tests (2 GPUs)(H100) **Cat...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: the failing test During V1 engine initialization with data parallel and expert parallel enabled, the UBatchWrapper initialization fails in SMControlContextManager.__init__() when attempting to get GPU compute units. The...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
