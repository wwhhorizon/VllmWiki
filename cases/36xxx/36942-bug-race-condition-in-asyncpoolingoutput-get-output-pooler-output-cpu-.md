# vllm-project/vllm#36942: [Bug]: Race condition in AsyncPoolingOutput.get_output() — pooler_output_cpu accessed before copy_event.synchronize()

| 字段 | 值 |
| --- | --- |
| Issue | [#36942](https://github.com/vllm-project/vllm/issues/36942) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support |
| 子分类 | race_cond |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 | env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Race condition in AsyncPoolingOutput.get_output() — pooler_output_cpu accessed before copy_event.synchronize()

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug There is a race condition in AsyncPoolingOutput.get_output() in [vllm/v1/worker/gpu/async_utils.py](https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu/async_utils.py). The method accesses self.pooler_output_cpu (via .unbind()) before calling self.copy_event.synchronize(), meaning the asynchronous GPU→CPU copy may not yet be complete when the tensor data is consumed. **Current code (incorrect ordering):** ``` # vllm/v1/worker/gpu/async_utils.py — AsyncPoolingOutput.get_output() def get_output(self) -> ModelRunnerOutput: pooler_output = list(self.pooler_output_cpu.unbind(dim=0)) # ❌ accesses tensor BEFORE sync self.copy_event.synchronize() # sync happens too late if self.is_valid_cpu is not None: is_valid_cpu = self.is_valid_cpu.tolist() for i, is_valid in enumerate(is_valid_cpu): if not is_valid: pooler_output[i] = None self.model_runner_output.pooler_output = pooler_output return self.model_runner_output ``` The sibling class AsyncOutput.get_output() in the same file does this correctly - it calls self.copy_event.synchronize() first, then accesses the CPU tensors: ``` # vllm/v1/worker/gpu/async_utils.py — AsyncOutp...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: __init__, the GPU→CPU transfer is initiated non-blockingly on a separate CUDA stream and copy_event is recorded after it: ``` with stream(copy_stream, main_stream): copy_stream.wait_stream(main_stream) self.pooler_outpu...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ll means reading from a buffer that may be partially filled. **Steps to reproduce:** Use a pooling/embedding model with AsyncLLM. Set VLLM_USE_V2_MODEL_RUNNER=1. Call embed() with a batch of prompts under GPU load. Obse...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sked questions. correctness frontend_api;model_support cuda mismatch env_dependency;race_condition;shape Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ... ``` **Context**: In __init__, the GPU→CPU transfer is initiated non-blockingly on a separate CUDA stream and copy_event is recorded after it: ``` with stream(copy_stream, main_stream): copy_stream.wait_stream(main_s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sync_utils.py — AsyncPoolingOutput.get_output() def get_output(self) -> ModelRunnerOutput: pooler_output = list(self.pooler_output_cpu.unbind(dim=0)) # ❌ accesses tensor BEFORE sync self.copy_event.synchronize() # sync...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
