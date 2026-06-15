# vllm-project/vllm#7421: [Bug]: Triton assert/crash in tests/samplers/test_logprobs.py

| 字段 | 值 |
| --- | --- |
| Issue | [#7421](https://github.com/vllm-project/vllm/issues/7421) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Triton assert/crash in tests/samplers/test_logprobs.py

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Got an assert/crash in triton when running: ``` pytest -s tests/samplers/test_logprobs.py::test_get_prompt_logprobs[True-0-1-float-facebook/opt-125m] ``` There are some other logprobs tests that also trigger the same assert. Stack trace: ``` INFO 08-12 14:41:41 model_runner.py:1397] Graph capturing finished in 1 secs. ^MProcessed prompts: 0%| | 0/8 [00:00 , llvm::SmallVector > mlir::triton::getCvtOrder(mlir::Attribute, mlir::Attribute): Assertion `!(srcMmaLayout && dstMmaLayout && !srcMmaLayout.isAmpere()) && "mma -> mma layout conversion is only supported on Ampere"' failed. Fatal Python error: Aborted Thread 0x00007dd1e1fff640 (most recent call first): File "/home/bnell/.local/lib/python3.10/site-packages/torch/_inductor/compile_worker/subproc_pool.py", line 57 in _recv_msg File "/home/bnell/.local/lib/python3.10/site-packages/torch/_inductor/compile_worker/subproc_pool.py", line 123 in _read_thread File "/usr/lib/python3.10/threading.py", line 953 in run File "/usr/lib/python3.10/threading.py", line 1016 in _bootstrap_inner File "/usr/lib/python3.10/threading.py", line 973 in _bootstrap Thread 0x00007dd3fccdf640 (most recent c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ut && dstMmaLayout && !srcMmaLayout.isAmpere()) && "mma -> mma layout conversion is only supported on Ampere"' failed. Fatal Python error: Aborted Thread 0x00007dd1e1fff640 (most recent call first): File "/home/bnell/.l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Triton assert/crash in tests/samplers/test_logprobs.py bug;stale ### Your current environment ### 🐛 Describe the bug Got an assert/crash in triton when running: ``` pytest -s tests/samplers/test_logprobs.py::test...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Triton assert/crash in tests/samplers/test_logprobs.py bug;stale ### Your current environment ### 🐛 Describe the bug Got an assert/crash in triton when running: ``` pytest -s tests/samplers/test_logprobs.py::test...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: shed in 1 secs. ^MProcessed prompts: 0%| | 0/8 [00:00 , llvm::SmallVector > mlir::triton::getCvtOrder(mlir::Attribute, mlir::Attribute): Assertion `!(srcMmaLayout && dstMmaLayout && !srcMmaLayout.isAmpere()) && "mma ->...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: that also trigger the same assert. Stack trace: ``` INFO 08-12 14:41:41 model_runner.py:1397] Graph capturing finished in 1 secs. ^MProcessed prompts: 0%| | 0/8 [00:00 , llvm::SmallVector > mlir::triton::getCvtOrder(mli...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
