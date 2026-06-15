# vllm-project/vllm#24560: [Bug]: No truncation of input exceeding the maximum input length when using the embedding model

| 字段 | 值 |
| --- | --- |
| Issue | [#24560](https://github.com/vllm-project/vllm/issues/24560) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: No truncation of input exceeding the maximum input length when using the embedding model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In previous versions I was able to truncate overlong inputs via parameters, but now I can't find any available parameter configuration. ```python body = { "input": text, "truncate_prompt_tokens": 1, } res = requests.post(f"{config.EMBEDING_API}/embeddings", json=body) ``` response: ``` {"error":{"message":"This model's maximum context length is 8192 tokens. However, you requested 10288 tokens in the input for embedding generation. Please reduce the length of the input.","type":"BadRequestError","param":null,"code":400}} ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ion of input exceeding the maximum input length when using the embedding model bug ### Your current environment ### 🐛 Describe the bug In previous versions I was able to truncate overlong inputs via parameters, but now...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: bug ### Your current environment ### 🐛 Describe the bug In previous versions I was able to truncate overlong inputs via parameters, but now I can't find any available parameter configuration. ```python body = { "input":...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: hon body = { "input": text, "truncate_prompt_tokens": 1, } res = requests.post(f"{config.EMBEDING_API}/embeddings", json=body) ``` response: ``` {"error":{"message":"This model's maximum context length is 8192 tokens. H...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
