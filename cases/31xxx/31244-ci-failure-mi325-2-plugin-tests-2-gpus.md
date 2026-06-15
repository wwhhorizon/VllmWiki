# vllm-project/vllm#31244: [CI Failure]:  mi325_2: Plugin Tests (2 GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#31244](https://github.com/vllm-project/vllm/issues/31244) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;gemm |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_2: Plugin Tests (2 GPUs)

### Issue 正文摘录

### Name of failing test `pip install -e ./plugins/vllm_add_dummy_platform && pytest -v -s plugins_tests/test_platform_plugins.py && pip uninstall vllm_add_dummy_platform -y && pip install -e ./plugins/prithvi_io_processor_plugin && pytest -v -s plugins_tests/test_io_processor_plugins.py && pip uninstall prithvi_io_processor_plugin -y && pip install -e ./plugins/vllm_add_dummy_stat_logger && pytest -v -s plugins_tests/test_stats_logger_plugins.py && pip uninstall dummy_stat_logger -y && pytest -v -s plugins_tests/test_scheduler_plugins.py && pip install -e ./plugins/vllm_add_dummy_model && pytest -v -s distributed/test_distributed_oot.py && pytest -v -s entrypoints/openai/test_oot_registration.py && pytest -v -s models/test_oot_registration.py && pytest -v -s plugins/lora_resolvers"` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There is a terratorch-related error: ``` RuntimeError: PyTorch is checking whether allow_tf32_new is enabled for cuBlas matmul,Current status indicate that you have used mix of the legacy and new APIs to set the TF32 status for cublas matmul...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_2: Plugin Tests (2 GPUs) ci-failure ### Name of failing test `pip install -e ./plugins/vllm_add_dummy_platform && pytest -v -s plugins_tests/test_platform_plugins.py && pip uninstall vllm_add_dummy_p
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: API to set the TF32 flag. See also: https://pytorch.org/docs/main/notes/cuda.html#tensorfloat-32-tf32-on-ampere-and-later-devices ``` ### 📝 History of failing test Passing: https://buildkite.com/vllm/amd-ci/builds/1867...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sts/test_scheduler_plugins.py && pip install -e ./plugins/vllm_add_dummy_model && pytest -v -s distributed/test_distributed_oot.py && pytest -v -s entrypoints/openai/test_oot_registration.py && pytest -v -s models/test_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: gins/lora_resolvers"` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There is a terratorch-related erro...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: t. _No response_ development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting cuda;gemm Name of failing test

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
