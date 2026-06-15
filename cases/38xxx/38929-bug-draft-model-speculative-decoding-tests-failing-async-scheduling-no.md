# vllm-project/vllm#38929: [Bug]: Draft model speculative decoding tests failing: async_scheduling not enabled and engine core initialization errors

| 字段 | 值 |
| --- | --- |
| Issue | [#38929](https://github.com/vllm-project/vllm/issues/38929) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;scheduler_memory;speculative_decoding |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Draft model speculative decoding tests failing: async_scheduling not enabled and engine core initialization errors

### Issue 正文摘录

The tests that use `assert_draft_model_correctness` in `tests/v1/e2e/spec_decode/test_spec_decode.py` are failing with two types of errors: ### Error 1: async_scheduling not enabled ``` AssertionError: Expected async_scheduling=True for draft_model spec decode, got False. ``` This assertion is at line 1084-1086 of the test file. The draft_model spec decode expects async scheduling to be auto-enabled, but it's not happening. ### Error 2: Engine core initialization failure ``` RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} ``` This appears to be a more serious runtime error during engine initialization for some test cases. ## Failing Tests All tests that call `assert_draft_model_correctness`: - `test_draft_model_correctness` (line 850) - `test_draft_model_realistic_example` (line 856) - `test_draft_model_parallel_drafting` (line 871) - `test_draft_model_quantization` (line 897) - `test_draft_model_tensor_parallelism` (line 909) ## Steps to Reproduce ```bash CUDA_VISIBLE_DEVICES=0 pytest tests/v1/e2e/spec_decode/test_spec_decode.py::test_draft_model_correctness -v ``` ## Environment - vLLM version: 0.19.1rc1.dev17+ga5a623d96.d20260403.p...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Draft model speculative decoding tests failing: async_scheduling not enabled and engine core initialization errors bug The tests that use `assert_draft_model_correctness` in `tests/v1/e2e/spec_decode/test_spec_de...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ``` ## Environment - vLLM version: 0.19.1rc1.dev17+ga5a623d96.d20260403.precompiled - Installation: Built from source with VLLM_USE_PRECOMPILED=1 - Platform: Linux with CUDA 13.2 ## Expected Behavior Tests should pass w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: - `test_draft_model_tensor_parallelism` (line 909)
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ## Steps to Reproduce
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: - `test_draft_model_quantization` (line 897)

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
