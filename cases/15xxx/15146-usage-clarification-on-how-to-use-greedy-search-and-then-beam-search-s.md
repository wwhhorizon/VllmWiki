# vllm-project/vllm#15146: [Usage]: Clarification on how to use Greedy Search and then Beam search's Poor Performance in VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#15146](https://github.com/vllm-project/vllm/issues/15146) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error;nondeterministic |
| 根因提示 | env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Clarification on how to use Greedy Search and then Beam search's Poor Performance in VLLM

### Issue 正文摘录

### Your current environment ### ENVIRONMENT INFORMATION Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 12.3.0-17ubuntu1) 12.3.0 Clang version: Could not collect CMake version: version 3.31.6 Libc version: glibc-2.39 Python version: 3.12.2 | packaged by Anaconda, Inc. | (main, Feb 27 2024, 17:35:02) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.8.0-48-generic-x86_64-with-glibc2.39 Is CUDA available: False Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] pyzmq==26.3.0 [pip3] torch==2.5.1+cpu [pip3] torchaudio==2.5.1+cpu [pip3] torchvision==0.20.1+cpu [pip3] transformers==4.49.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] pyzmq 26.3.0 pypi_0 pypi [conda] torch 2.5.1+cpu pypi_0 pypi [conda] torchaudio 2.5.1+cpu pypi_0 pypi [conda] torchvision 0.20.1+cpu pypi_0 pypi [conda] transformers 4.49.0 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.7.4.dev341+g1253b157 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: Could not collect LD_LIBRARY_PATH=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: # ENVIRONMENT INFORMATION Collecting environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: Clarification on how to use Greedy Search and then Beam search's Poor Performance in VLLM usage;stale ### Your current environment ### ENVIRONMENT INFORMATION Collecting environment information... PyTorch versi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: and then calling **llm.beam_search().** Both methods seem to produce **deterministic outputs,** which is expected for greedy search. My questions are: 1. Which method is the correct way to implement greedy search in VLL...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: and then calling **llm.beam_search().** Both methods seem to produce **deterministic outputs,** which is expected for greedy search. My questions are: 1. Which method is the correct way to implement greedy search in VLL...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: environment information... PyTorch version: 2.5.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 24.04 LTS (x86_64) GCC version: (Ubuntu 12.3.0-17ubuntu1) 12.3.0 Cl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
