# vllm-project/vllm#18953: [RFC]: vLLM configuration  refactoring and modularization

| 字段 | 值 |
| --- | --- |
| Issue | [#18953](https://github.com/vllm-project/vllm/issues/18953) |
| 状态 | closed |
| 标签 | help wanted;RFC |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: vLLM configuration  refactoring and modularization

### Issue 正文摘录

### Motivation. Currently, the vLLM configuration is concentrated in a single large [config.py](https://github.com/vllm-project/vllm/blob/v0.9.0/vllm/config.py) containing over 5000 lines of code with multiple interconnected dataclasses. This monolithic structure has poor maintainability and readability, making it difficult for developers to locate, understand, and modify specific configurations. ### Proposed Change. I plan to split [config.py](https://github.com/vllm-project/vllm/blob/v0.9.0/vllm/config.py) into focused, domain-specific modules to improve code organization and developer experience (as shown below). ``` python vllm/config/ ├── __init__.py # Main exports and global functions to maintain backward compatibility. ├── cache_config.py # KV cache configuration ├── compilation_config.py # torch.compile configuration ├── decoding_config.py # Guided decoding configuration ├── device_config.py # Device and platform configuration ├── kvevents_config.py # KV cache event publishing ├── kvtransformer_config.py # Distributed KV cache transfer ├── load_config.py # Model loading configuration ├── lora_config.py # LoRA adapter configuration ├── model_config.py # Core model configura...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [RFC]: vLLM configuration refactoring and modularization help wanted;RFC ### Motivation. Currently, the vLLM configuration is concentrated in a single large [config.py](https://github.com/vllm-project/vllm/blob/v0.9.0/v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tion ├── promptadapter_config.py # Prompt adapter configuration ├── scheduler_config.py # Request scheduling configuration ├── speculative_config.py # Speculative decoding configuration ├── tokenizerpool_config.py # Dep...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: making it difficult for developers to locate, understand, and modify specific configurations. ### Proposed Change. I plan to split [config.py](https://github.com/vllm-project/vllm/blob/v0.9.0/vllm/config.py) into focuse...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: to maintain backward compatibility. ├── cache_config.py # KV cache configuration ├── compilation_config.py # torch.compile configuration ├── decoding_config.py # Guided decoding configuration ├── device_config.py # Devi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
