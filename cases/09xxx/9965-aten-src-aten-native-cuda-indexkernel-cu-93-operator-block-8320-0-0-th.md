# vllm-project/vllm#9965: ../aten/src/ATen/native/cuda/IndexKernel.cu:93: operator(): block: [8320,0,0], thread: [64,0,0] Assertion `-sizes[i] <= index && in dex < sizes[i] && "index out of bounds"` failed.

| 字段 | 值 |
| --- | --- |
| Issue | [#9965](https://github.com/vllm-project/vllm/issues/9965) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error;mismatch |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ../aten/src/ATen/native/cuda/IndexKernel.cu:93: operator(): block: [8320,0,0], thread: [64,0,0] Assertion `-sizes[i] <= index && in dex < sizes[i] && "index out of bounds"` failed.

### Issue 正文摘录

Recently, I have encountered an issue while modifying the positional encoding in the **mrope_input_positions** section of the Qwen2-VL code, and I have tried but don't know how to resolve it. In short, I'm aiming to explore the model's performance when extrapolating to a 60k context on the Qwen2-VL 7B model, using video data for testing. I tried replacing this section (https://github.com/vllm-project/vllm/blob/3bb4befea7166850bdee3f72fe060c9c4044ba85/vllm/worker/model_runner.py#L672) with vanilla-ROPE（That is, placing image, video, and text tokens all on the main diagonal of the M-RoPE.）, which caused the max value of the mrope_input_positions up to approximately 59k, but it eventually led to an error. ```bash ../aten/src/ATen/native/cuda/IndexKernel.cu:93: operator(): block: [8320,0,0], thread: [64,0,0] Assertion `-sizes[i] <= index && in dex < sizes[i] && "index out of bounds"` failed. ../aten/src/ATen/native/cuda/IndexKernel.cu:93: operator(): block: [8320,0,0], thread: [65,0,0] Assertion `-sizes[i] <= index && in dex < sizes[i] && "index out of bounds"` failed. ../aten/src/ATen/native/cuda/IndexKernel.cu:93: operator(): block: [8320,0,0], thread: [66,0,0] Assertion `-sizes[i]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ext on the Qwen2-VL 7B model, using video data for testing. I tried replacing this section (https://github.com/vllm-project/vllm/blob/3bb4befea7166850bdee3f72fe060c9c4044ba85/vllm/worker/model_runner.py#L672) with vanil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ../aten/src/ATen/native/cuda/IndexKernel.cu:93: operator(): block: [8320,0,0], thread: [64,0,0] Assertion `-sizes[i] <= index && in dex < sizes[i] && "index out of bounds"` failed. Recently, I have encountered an issue...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ../aten/src/ATen/native/cuda/IndexKernel.cu:93: operator(): block: [8320,0,0], thread: [64,0,0] Assertion `-sizes[i] <= index && in dex < sizes[i] && "index out of bounds"` failed. Recently, I have encountered an issue...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: the positional encoding in the **mrope_input_positions** section of the Qwen2-VL code, and I have tried but don't know how to resolve it. In short, I'm aiming to explore the model's performance when extrapolating to a 6...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: polating to a 60k context on the Qwen2-VL 7B model, using video data for testing. I tried replacing this section (https://github.com/vllm-project/vllm/blob/3bb4befea7166850bdee3f72fe060c9c4044ba85/vllm/worker/model_runn...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
