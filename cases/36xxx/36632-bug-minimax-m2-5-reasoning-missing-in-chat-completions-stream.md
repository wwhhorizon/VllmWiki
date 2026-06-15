# vllm-project/vllm#36632: [Bug]: MiniMax-M2.5 reasoning missing in chat completions stream

| 字段 | 值 |
| --- | --- |
| Issue | [#36632](https://github.com/vllm-project/vllm/issues/36632) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MiniMax-M2.5 reasoning missing in chat completions stream

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when serving vllm using `vllm/vllm-openai:v0.17.0` + `lukealonso/MiniMax-M2.5-NVFP4 --reasoning-parser minimax_m2` reasoning is not present when calling /v1/chat/completions + stream=True it is working correctly with non-stream + /v1/responses bellow is script that reproduces the issue ```python from openai import OpenAI client = OpenAI(api_key=api_key, base_url=base_url) print("=== Non-Streaming ===") response = client.chat.completions.create( model=model, messages=[{"role": "user", "content": "hello"}], ) message = response.choices[0].message print(f"Reasoning: {getattr(message, 'reasoning_content', None)}") print(f"Content: {message.content}") print("\n=== Streaming ===") stream = client.chat.completions.create( model=model, messages=[{"role": "user", "content": "hello"}], stream=True, ) for chunk in stream: delta = chunk.choices[0].delta reasoning = getattr(delta, "reasoning_content", None) content = getattr(delta, "content", None) if reasoning: print(f"Reasoning: {reasoning}") if content: print(f"Content: {content}") ``` when running with same config on `vllm/vllm-openai:v0.15.1` reasoning is streamed properly ### Before sub...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: serving vllm using `vllm/vllm-openai:v0.17.0` + `lukealonso/MiniMax-M2.5-NVFP4 --reasoning-parser minimax_m2` reasoning is not present when calling /v1/chat/completions + stream=True it is working correctly with non-str...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ("=== Non-Streaming ===") response = client.chat.completions.create( model=model, messages=[{"role": "user", "content": "hello"}], ) message = response.choices[0].message print(f"Reasoning: {getattr(message, 'reasoning_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: working correctly with non-stream + /v1/responses bellow is script that reproduces the issue ```python from openai import OpenAI client = OpenAI(api_key=api_key, base_url=base_url) print("=== Non-Streaming ===") respons...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: onses bellow is script that reproduces the issue ```python from openai import OpenAI client = OpenAI(api_key=api_key, base_url=base_url) print("=== Non-Streaming ===") response = client.chat.completions.create( model=mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rly ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
