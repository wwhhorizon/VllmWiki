# vllm-project/vllm#20214: [CI Failure]: Speculative decoding tests - spec_decode/e2e/test_eagle_correctness.py

| 字段 | 值 |
| --- | --- |
| Issue | [#20214](https://github.com/vllm-project/vllm/issues/20214) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Speculative decoding tests - spec_decode/e2e/test_eagle_correctness.py

### Issue 正文摘录

### Name of failing test `spec_decode/e2e/test_eagle_correctness.py::test_llama3_eagle_e2e_greedy_correctness[1-1-32-test_llm_kwargs0-baseline_llm_kwargs0-per_test_common_llm_kwargs0-common_llm_kwargs0]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test It doesn't fail locally but that might be because the OOM is specific to the L4 we use in CI https://buildkite.com/vllm/ci/builds/22853/steps/canvas?jid=0197b520-e1dc-4ace-bfdc-f483b4dee76f ``` [2025-06-28T09:19:58Z] FAILED spec_decode/e2e/test_eagle_correctness.py::test_llama3_eagle_e2e_greedy_correctness[1-1-32-test_llm_kwargs0-baseline_llm_kwargs0-per_test_common_llm_kwargs0-common_llm_kwargs0] - torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 116.00 MiB. GPU 0 has a total capacity of 22.05 GiB of which 112.12 MiB is free. Including non-PyTorch memory, this process has 21.92 GiB memory in use. Of the allocated memory 21.56 GiB is allocated by PyTorch, and 113.98 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: Speculative decoding tests - spec_decode/e2e/test_eagle_correctness.py ci-failure ### Name of failing test `spec_decode/e2e/test_eagle_correctness.py::test_llama3_eagle_e2e_greedy_correctness[1-1-32-test_ll
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: # Name of failing test `spec_decode/e2e/test_eagle_correctness.py::test_llama3_eagle_e2e_greedy_correctness[1-1-32-test_llm_kwargs0-baseline_llm_kwargs0-per_test_common_llm_kwargs0-common_llm_kwargs0]` ### Basic informa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [CI Failure]: Speculative decoding tests - spec_decode/e2e/test_eagle_correctness.py ci-failure ### Name of failing test `spec_decode/e2e/test_eagle_correctness.py::test_llama3_eagle_e2e_greedy_correctness[1-1-32-test_l...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: -common_llm_kwargs0]` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test It doesn't fail locally but that m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er_test_common_llm_kwargs0-common_llm_kwargs0] - torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 116.00 MiB. GPU 0 has a total capacity of 22.05 GiB of which 112.12 MiB is free. Including non-PyTorch memor...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
