# vllm-project/vllm#28965: [Bug]: Some compilation tests can not run in the same process due to "Cannot re-initialize CUDA in forked subprocess"

| 字段 | 值 |
| --- | --- |
| Issue | [#28965](https://github.com/vllm-project/vllm/issues/28965) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Some compilation tests can not run in the same process due to "Cannot re-initialize CUDA in forked subprocess"

### Issue 正文摘录

### Your current environment vLLM build from source at: d8874c61a PyTorch build from source at: cda7604434c ### 🐛 Describe the bug When running some compiler tests together in the same process, they would fail with ``` RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method ``` However, running these tests individually in separate processes would work. This issue persists even if I force 'spawn' start method with Repro: ``` pytest -s -v tests/compile/test_aot_compile.py tests/compile/test_config.py ``` Mitigations I have tried (and failed): - setting environment variable VLLM_WORKER_MULTIPROC_METHOD=spawn - Force pytorch start method to be `spawn`: `torch.multiprocessing.set_start_method('spawn')` - Decorate affected tests with `@create_new_process_for_each_test()` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: CUDA in forked subprocess" bug;stale ### Your current environment vLLM build from source at: d8874c61a PyTorch build from source at: cda7604434c ### 🐛 Describe the bug When running some compiler tests together in the sa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ation tests can not run in the same process due to "Cannot re-initialize CUDA in forked subprocess" bug;stale ### Your current environment vLLM build from source at: d8874c61a PyTorch build from source at: cda7604434c #...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: o: ``` pytest -s -v tests/compile/test_aot_compile.py tests/compile/test_config.py ``` Mitigations I have tried (and failed): - setting environment variable VLLM_WORKER_MULTIPROC_METHOD=spawn - Force pytorch start metho...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: same process due to "Cannot re-initialize CUDA in forked subprocess" bug;stale ### Your current environment vLLM build from source at: d8874c61a PyTorch build from source at: cda7604434c ### 🐛 Describe the bug When runn...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: Some compilation tests can not run in the same process due to "Cannot re-initialize CUDA in forked subprocess" bug;stale ### Your current environment vLLM build from source at: d8874c61a PyTorch build from source...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
