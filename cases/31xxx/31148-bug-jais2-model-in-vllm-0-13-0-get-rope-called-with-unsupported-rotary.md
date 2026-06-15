# vllm-project/vllm#31148: [Bug]: Jais2 model in vLLM 0.13.0: get_rope() called with unsupported rotary_dim kwarg (TypeError during model init)

| 字段 | 值 |
| --- | --- |
| Issue | [#31148](https://github.com/vllm-project/vllm/issues/31148) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Jais2 model in vLLM 0.13.0: get_rope() called with unsupported rotary_dim kwarg (TypeError during model init)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Title:** Jais2 model in vLLM 0.13.0: `get_rope()` called with unsupported `rotary_dim` kwarg (TypeError during model init) --- **Environment** - vLLM: `0.13.0` (wheel: `vllm-0.13.0-cp38-abi3-linux_x86_64.whl`) - Python: `3.12` - PyTorch: `2.9.0+cu129` - CUDA: `12.9` - GPUs: NVIDIA A40 (Compute Capability 8.6) - OS / container: Ubuntu-based Docker image (Python 3.12, vLLM 0.13.0 installed via wheel) --- **Summary** When serving the model `inceptionai/Jais-2-70B-Chat` (Jais2 architecture) with vLLM 0.13.0, engine initialization fails with: ```text TypeError: get_rope() got an unexpected keyword argument 'rotary_dim' ``` The error occurs during `Jais2Attention` initialization: the `jais2.py` model implementation calls `get_rope()` with a `rotary_dim` keyword argument, but the `get_rope` function exposed by `vllm.model_executor.layers.rotary_embedding` in this release does not accept that parameter. This appears to be an API mismatch between the Jais2 model integration and the RoPE helper in vLLM 0.13.0. --- **Steps to Reproduce** 1. Install vLLM 0.13.0: ```bash pip install vllm==0.13.0 ``` 2. Ensure CUDA is working (A40, CUDA 12.9...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: g (TypeError during model init) --- **Environment** - vLLM: `0.13.0` (wheel: `vllm-0.13.0-cp38-abi3-linux_x86_64.whl`) - Python: `3.12` - PyTorch: `2.9.0+cu129` - CUDA: `12.9` - GPUs: NVIDIA A40 (Compute Capability 8.6)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: cp38-abi3-linux_x86_64.whl`) - Python: `3.12` - PyTorch: `2.9.0+cu129` - CUDA: `12.9` - GPUs: NVIDIA A40 (Compute Capability 8.6) - OS / container: Ubuntu-based Docker image (Python 3.12, vLLM 0.13.0 installed via wheel...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: this release does not accept that parameter. This appears to be an API mismatch between the Jais2 model integration and the RoPE helper in vLLM 0.13.0. --- **Steps to Reproduce** 1. Install vLLM 0.13.0: ```bash pip inst...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Jais2 model in vLLM 0.13.0: get_rope() called with unsupported rotary_dim kwarg (TypeError during model init) bug ### Your current environment ### 🐛 Describe the bug **Title:** Jais2 model in vLLM 0.13.0: `get_ro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eter (or to encode the same effect via `partial_rotary_factor`). --- **Request** - Could you confirm the intended `get_rope` API for vLLM 0.13.x and the Jais2 integration? - If Jais2 is officially supported in 0.13.x, c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
