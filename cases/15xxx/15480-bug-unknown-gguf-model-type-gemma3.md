# vllm-project/vllm#15480: [Bug]: Unknown gguf model_type: gemma3

| 字段 | 值 |
| --- | --- |
| Issue | [#15480](https://github.com/vllm-project/vllm/issues/15480) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unknown gguf model_type: gemma3

### Issue 正文摘录

### Your current environment vLLM Version: 0.8.1 ### 🐛 Describe the bug RuntimeError: Unknown gguf model_type: gemma3 code: ```python llm = LLM(model="gemma-3-27b-it-GGUF/mmproj-model-f16.gguf",tokenizer="google-gemma-3-27b-it",tensor_parallel_size=2,dtype=torch.float16,hf_config_path="/google-gemma-3-27b-it") ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Unknown gguf model_type: gemma3 bug;stale ### Your current environment vLLM Version: 0.8.1 ### 🐛 Describe the bug RuntimeError: Unknown gguf model_type: gemma3 code: ```python llm = LLM(model="gemma-3-27b-it-GGUF...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: model-f16.gguf",tokenizer="google-gemma-3-27b-it",tensor_parallel_size=2,dtype=torch.float16,hf_config_path="/google-gemma-3-27b-it") ``` ### Before submitting a new issue... - [x] Make sure you already searched for rel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: own gguf model_type: gemma3 bug;stale ### Your current environment vLLM Version: 0.8.1 ### 🐛 Describe the bug RuntimeError: Unknown gguf model_type: gemma3 code: ```python llm = LLM(model="gemma-3-27b-it-GGUF/mmproj-mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Unknown gguf model_type: gemma3 bug;stale ### Your current environment vLLM Version: 0.8.1 ### 🐛 Describe the bug RuntimeError: Unknown gguf model_type: gemma3 code: ```python llm = LLM(model="gemma-3-27b-it-GGUF...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
