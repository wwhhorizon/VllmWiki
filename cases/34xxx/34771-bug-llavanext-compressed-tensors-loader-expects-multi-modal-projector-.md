# vllm-project/vllm#34771: [Bug]: LlavaNext + compressed-tensors: loader expects multi_modal_projector.linear_1.weight_packed but model only has linear_1weight/linear_1bias

| 字段 | 值 |
| --- | --- |
| Issue | [#34771](https://github.com/vllm-project/vllm/issues/34771) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: LlavaNext + compressed-tensors: loader expects multi_modal_projector.linear_1.weight_packed but model only has linear_1weight/linear_1bias

### Issue 正文摘录

### Your current environment ## Environment - vLLM version: 0.15.1 (docker image vllm/vllm-openai:latest) - Model: LlavaNext-style VLM, quantized with llmcompressor (W4A16, compressed-tensors format) ### 🐛 Describe the bug ## Problem When loading the quantized model with vLLM, the engine exits with: ``` ValueError: There is no module or parameter named 'multi_modal_projector.linear_1.weight_packed' in LlavaNextForConditionalGeneration. The available parameters belonging to multi_modal_projector.linear_1 (ColumnParallelLinear) are: {'multi_modal_projector.linear_1weight', 'multi_modal_projector.linear_1bias'} ``` ## Checkpoint verification The saved safetensors **do contain** the expected keys: - `multi_modal_projector.linear_1.weight_packed` - `multi_modal_projector.linear_1.weight_scale` - `multi_modal_projector.linear_1.bias` (and similarly for linear_2). So the issue is not missing keys in the checkpoint. ## Expected vs actual - Loader asks for a **model parameter** named `multi_modal_projector.linear_1.weight_packed`. - The LlavaNext model only has `multi_modal_projector.linear_1weight` and `multi_modal_projector.linear_1bias`. So the loader's expectation (weight_packed parame...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ght/linear_1bias bug ### Your current environment ## Environment - vLLM version: 0.15.1 (docker image vllm/vllm-openai:latest) - Model: LlavaNext-style VLM, quantized with llmcompressor (W4A16, compressed-tensors format...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tensors: loader expects multi_modal_projector.linear_1.weight_packed but model only has linear_1weight/linear_1bias bug ### Your current environment ## Environment - vLLM version: 0.15.1 (docker image vllm/vllm-openai:l...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 5.1 (docker image vllm/vllm-openai:latest) - Model: LlavaNext-style VLM, quantized with llmcompressor (W4A16, compressed-tensors format) ### 🐛 Describe the bug ## Problem When loading the quantized model with vLLM, the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ## Environment - vLLM version: 0.15.1 (docker image vllm/vllm-openai:latest) - Model: LlavaNext-style VLM, quantized with llmcompressor (W4A16, compressed-tensors format) ### 🐛 Describe the bug ## Problem When loading t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
