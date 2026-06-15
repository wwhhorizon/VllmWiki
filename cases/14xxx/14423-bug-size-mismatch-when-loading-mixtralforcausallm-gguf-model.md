# vllm-project/vllm#14423: [Bug]: size mismatch when loading MixtralForCausalLM GGUF model

| 字段 | 值 |
| --- | --- |
| Issue | [#14423](https://github.com/vllm-project/vllm/issues/14423) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | wrong_output |
| Operator 关键词 | quantization |
| 症状 | mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: size mismatch when loading MixtralForCausalLM GGUF model

### Issue 正文摘录

### Your current environment GPU 0: NVIDIA GeForce RTX 3090 VLLM version: 0.7.3 ### 🐛 Describe the bug Hi, I downloaded the model locally from https://huggingface.co/piotrmaciejbednarski/PLLuM-8x7B-chat-GGUF, specifically the Q2_K quantization type. I try to start the server with the command: vllm serve ./PLLuM-8x7B-chat-gguf-q2_k.gguf --tokenizer CYFRAGOVPL/PLLuM-8x7B-chat I receive an error: RuntimeError: size mismatch, got input (32768), mat (32768x4096), vec (0) Modifying the max_model_len parameter does not help. I have already run other GGUF-type models, e.g. TheBloke/deepseek-coder-33B-instruct-GGUF, and the error did not appear. Has anyone encountered a similar problem and knows how to deal with it? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: size mismatch when loading MixtralForCausalLM GGUF model bug;stale ### Your current environment GPU 0: NVIDIA GeForce RTX 3090 VLLM version: 0.7.3 ### 🐛 Describe the bug Hi, I downloaded the model locally from ht...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: stale ### Your current environment GPU 0: NVIDIA GeForce RTX 3090 VLLM version: 0.7.3 ### 🐛 Describe the bug Hi, I downloaded the model locally from https://huggingface.co/piotrmaciejbednarski/PLLuM-8x7B-chat-GGUF, spec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: size mismatch when loading MixtralForCausalLM GGUF model bug;stale ### Your current environment GPU 0: NVIDIA GeForce RTX 3090 VLLM version: 0.7.3 ### 🐛 Describe the bug Hi, I downloaded the model locally from ht...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: size mismatch when loading MixtralForCausalLM GGUF model bug;stale ### Your current environment GPU 0: NVIDIA GeForce RTX 3090 VLLM version: 0.7.3 ### 🐛 Describe the bug Hi, I downloaded the model locally from ht...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: face.co/piotrmaciejbednarski/PLLuM-8x7B-chat-GGUF, specifically the Q2_K quantization type. I try to start the server with the command: vllm serve ./PLLuM-8x7B-chat-gguf-q2_k.gguf --tokenizer CYFRAGOVPL/PLLuM-8x7B-chat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
