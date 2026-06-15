# vllm-project/vllm#13186: [Bug]: Concurrent streaming mode produces jumbled tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#13186](https://github.com/vllm-project/vllm/issues/13186) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Concurrent streaming mode produces jumbled tokens

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug If call any served model in stream mode (quant or not) in concurrency, vllm server returns strange characters: https://github.com/user-attachments/assets/0a8c2a52-03be-46a8-b4c1-700c5002be25 server: `vllm serve unsloth/Llama-3.2-1B-Instruct --max-model-len 4000 --port 8081` client(s): ```python from openai import OpenAI client = OpenAI( base_url="http://localhost:8081/v1", api_key="token-abc123", ) models = client.models.list() if models.data: first_model = models.data[0].id else: raise ValueError("Nenhum modelo disponível na API.") stream = client.chat.completions.create( model=first_model, messages=[{"role": "user", "content": "essay about life"}], stream=True, ) for chunk in stream: if chunk.choices and chunk.choices[0].delta.content: print(chunk.choices[0].delta.content, end="", flush=True) print() ``` And yes, I tested lots of models with differentes quants, same problem :( ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nts/assets/0a8c2a52-03be-46a8-b4c1-700c5002be25 server: `vllm serve unsloth/Llama-3.2-1B-Instruct --max-model-len 4000 --port 8081` client(s): ```python from openai import OpenAI client = OpenAI( base_url="http://localh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Your current environment ### 🐛 Describe the bug If call any served model in stream mode (quant or not) in concurrency, vllm server returns strange characters: https://github.com/user-attachments/assets/0a8c2a52-03be-46a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: uct --max-model-len 4000 --port 8081` client(s): ```python from openai import OpenAI client = OpenAI( base_url="http://localhost:8081/v1", api_key="token-abc123", ) models = client.models.list() if models.data: first_mo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ent ### 🐛 Describe the bug If call any served model in stream mode (quant or not) in concurrency, vllm server returns strange characters: https://github.com/user-attachments/assets/0a8c2a52-03be-46a8-b4c1-700c5002be25 s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: :( ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
