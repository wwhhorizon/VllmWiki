# vllm-project/vllm#9143: [Bug]: vllm much slower on long context inputs when using --enable-lora even when lora is not used

| 字段 | 值 |
| --- | --- |
| Issue | [#9143](https://github.com/vllm-project/vllm/issues/9143) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | quantization |
| 症状 | slowdown |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm much slower on long context inputs when using --enable-lora even when lora is not used

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using `--enable-lora`, vllm output generation speed goes dramatically down. I've ran an experiment with the following parameters: ```bash --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --dtype half --max-model-len 48000 --gpu-memory-utilization 0.99 --block-size 16 --enable-prefix-caching --served-model-name gpt-3.5-turbo --enable-lora --max-loras 1 --max-lora-rank 64 --lora-modules test-module=/models/my-module ``` Using docker `vllm/vllm-openai:v0.6.2` Running this on an A100 80GB. When running without enabling lora with an input of 9k tokens, I get a generation speed of around 27 tokens/s. When enabling lora, not specifying any adapter and same input, the generation speed is 5 tokens/s. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: max-lora-rank 64 --lora-modules test-module=/models/my-module ``` Using docker `vllm/vllm-openai:v0.6.2` Running this on an A100 80GB. When running without enabling lora with an input of 9k tokens, I get a generation sp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: an an experiment with the following parameters: ```bash --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --dtype half --max-model-len 48000 --gpu-memory-utilization 0.99 --block-size 16 --enable-prefix-cachin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y-module ``` Using docker `vllm/vllm-openai:v0.6.2` Running this on an A100 80GB. When running without enabling lora with an input of 9k tokens, I get a generation speed of around 27 tokens/s. When enabling lora, not sp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: -INT4 --dtype half --max-model-len 48000 --gpu-memory-utilization 0.99 --block-size 16 --enable-prefix-caching --served-model-name gpt-3.5-turbo --enable-lora --max-loras 1 --max-lora-rank 64 --lora-modules test-module=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: lora even when lora is not used bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using `--enable-lora`, vllm output generation speed goes dramatically down. I've ran an ex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
