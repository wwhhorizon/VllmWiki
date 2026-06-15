# vllm-project/vllm#5280: [Bug]: Regression in predictions in v0.4.3

| 字段 | 值 |
| --- | --- |
| Issue | [#5280](https://github.com/vllm-project/vllm/issues/5280) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Regression in predictions in v0.4.3

### Issue 正文摘录

### 🐛 Describe the bug The predictions changed between v0.4.2 and v0.4.3 - both the actual tokens at temperature 0 and also the logprobs. I'll show here how to reproduce the issue with a TinyLLama (I noticed it orignally with Llama-3-8B-Instruct). Running 2 vLLM servers with: ```bash python -m vllm.entrypoints.openai.api_server --model TinyLlama/TinyLlama-1.1B-Chat-v1.0 --gpu-memory-utilization 0.4 ``` for 0.4.2 adding `--port 8001` and for 0.4.3 `--port 8002`. Then running this client code: ```python def convert_logprobs_to_chat(legacy_logprobs: Logprobs) -> ChoiceLogprobs: top_logprobs = [] for top_token, top_logprob in legacy_logprobs.top_logprobs[0].items(): top_logprobs.append( TopLogprob(token=top_token, logprob=top_logprob) ) chat_logprobs = ChatCompletionTokenLogprob( token=legacy_logprobs.tokens[0], logprob=legacy_logprobs.token_logprobs[0], top_logprobs=top_logprobs ) return ChoiceLogprobs(content=[chat_logprobs]) vllms = { "0.4.2": "http://localhost:8001/v1", "0.4.3": "http://localhost:8002/v1", } for version, endpoint in vllms.items(): print(f"\nvLLM {version=}, {endpoint=}") client = openai.OpenAI( base_url=endpoint, api_key="foo" ) msgs = [{"role": "user", "content":...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: also the logprobs. I'll show here how to reproduce the issue with a TinyLLama (I noticed it orignally with Llama-3-8B-Instruct). Running 2 vLLM servers with: ```bash python -m vllm.entrypoints.openai.api_server --model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: tp://localhost:8001/v1", "0.4.3": "http://localhost:8002/v1", } for version, endpoint in vllms.items(): print(f"\nvLLM {version=}, {endpoint=}") client = openai.OpenAI( base_url=endpoint, api_key="foo" ) msgs = [{"role"...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: al tokens at temperature 0 and also the logprobs. I'll show here how to reproduce the issue with a TinyLLama (I noticed it orignally with Llama-3-8B-Instruct). Running 2 vLLM servers with: ```bash python -m vllm.entrypo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: bs=}") logprobs = convert_logprobs_to_chat(legacy_logprobs) else: logprobs = response.choices[0].logprobs top_logprobs = logprobs.content[0].top_logprobs print(f"top_logprobs:\t\t{top_logprobs}") sorted_top_logprobs = s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: Regression in predictions in v0.4.3 bug ### 🐛 Describe the bug The predictions changed between v0.4.2 and v0.4.3 - both the actual tokens at temperature 0 and also the logprobs. I'll show here how to reproduce th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
