# vllm-project/vllm#36455: [Bug]: Unable to run Qwen3.5 on RTX5090

| 字段 | 值 |
| --- | --- |
| Issue | [#36455](https://github.com/vllm-project/vllm/issues/36455) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to run Qwen3.5 on RTX5090

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running log: `(EngineCore_DP0 pid=384010) ERROR 03-09 13:22:08 [core.py:1100] torch.AcceleratorError: CUDA error: the provided PTX was compiled with an unsupported toolchain. (EngineCore_DP0 pid=384010) ERROR 03-09 13:22:08 [core.py:1100] Search for cudaErrorUnsupportedPtxVersion in https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__TYPES.html for more information. (EngineCore_DP0 pid=384010) ERROR 03-09 13:22:08 [core.py:1100] CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. (EngineCore_DP0 pid=384010) ERROR 03-09 13:22:08 [core.py:1100] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 (EngineCore_DP0 pid=384010) ERROR 03-09 13:22:08 [core.py:1100] Compile with TORCH_USE_CUDA_DSA to enable device-side assertions. (EngineCore_DP0 pid=384010) ERROR 03-09 13:22:08 [core.py:1100] ` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [core.py:1100] torch.AcceleratorError: CUDA error: the provided PTX was compiled with an unsupported toolchain. (EngineCore_DP0 pid=384010) ERROR 03-09 13:22:08 [core.py:1100] Search for cudaErrorUnsupportedPtxVersion i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Unable to run Qwen3.5 on RTX5090 bug ### Your current environment ### 🐛 Describe the bug Running log: `(EngineCore_DP0 pid=384010) ERROR 03-09 13:22:08 [core.py:1100] torch.AcceleratorError: CUDA error: the provi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Unable to run Qwen3.5 on RTX5090 bug ### Your current environment ### 🐛 Describe the bug Running log: `(EngineCore_DP0 pid=384010) ERROR 03-09 13:22:08 [core.py:1100] torch.AcceleratorError: CUDA error: the provi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ked questions. correctness ci_build;frontend_api cuda;kernel build_error;mismatch env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 03-09 13:22:08 [core.py:1100] For debugging consider passing CUDA_LAUNCH_BLOCKING=1 (EngineCore_DP0 pid=384010) ERROR 03-09 13:22:08 [core.py:1100] Compile with TORCH_USE_CUDA_DSA to enable device-side assertions. (Engi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
