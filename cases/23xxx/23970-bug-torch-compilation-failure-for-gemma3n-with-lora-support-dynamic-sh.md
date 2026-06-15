# vllm-project/vllm#23970: [Bug]: Torch Compilation Failure for Gemma3n with LoRA Support - Dynamic Shape Constraints Violated

| 字段 | 值 |
| --- | --- |
| Issue | [#23970](https://github.com/vllm-project/vllm/issues/23970) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Torch Compilation Failure for Gemma3n with LoRA Support - Dynamic Shape Constraints Violated

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Description I'm attempting to enable LoRA support for the `Gemma3nForConditionalGeneration` model by implementing the `SupportsLoRA` interface. While the model functions correctly with torch compilation disabled (`level=0`) and without CUDA graphs, it fails during torch compilation when using `PIECEWISE` mode due to dynamic shape constraint violations in the embedding and position encoding components. ## Environment - **OS**: Ubuntu 22.04.5 LTS (Kernel: 6.8.0-1017-aws) - **Python Version**: 3.11.13 - **vLLM Version**: 0.10.1rc2.dev213+ga406a0e36.d20250828 (development build) - **PyTorch Version**: 2.7.1+cu126 - **CUDA Runtime**: 12.6 - **CUDA Compiler**: 12.4 (V12.4.131) - **GPU**: NVIDIA A10G (23GB VRAM) - **NVIDIA Driver**: 550.127.05 - **Key Dependencies**: - transformers: 4.55.4 - torchvision: 0.22.1 - torchaudio: 2.7.1 - numpy: 2.2.6 - safetensors: 0.6.2 - tokenizers: 0.21.4 - triton: 3.3.1 - scipy: 1.16.1 ## Base Commit Changes made from main branch commit: `[Docs] [V1] [Hybrid] Add new documentation re: contributing mamba-based models` (#23824 ) ## Expected Behavior The Gemma3n model with LoRA support should compile suc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Gemma3n with LoRA Support - Dynamic Shape Constraints Violated bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug ## Description I'm attempting to enable LoRA support for the `Gemma3nForConditio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Torch Compilation Failure for Gemma3n with LoRA Support - Dynamic Shape Constraints Violated bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug ## Description I'm attempting to enable LoR...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ctions correctly with torch compilation disabled (`level=0`) and without CUDA graphs, it fails during torch compilation when using `PIECEWISE` mode due to dynamic shape constraint violations in the embedding and positio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: with LoRA Support - Dynamic Shape Constraints Violated bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug ## Description I'm attempting to enable LoRA support for the `Gemma3nForConditionalGener...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: mpt to start the vLLM server 4. Observe compilation failure during model profiling ## Workaround The model works correctly with: - `--compilation-level=0` (disables torch.compile) - `--disable-cuda-graph` ## Logs ### Be...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
