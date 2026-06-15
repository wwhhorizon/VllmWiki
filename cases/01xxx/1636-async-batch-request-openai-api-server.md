# vllm-project/vllm#1636: (Async) Batch request, OpenAI API server

| 字段 | 值 |
| --- | --- |
| Issue | [#1636](https://github.com/vllm-project/vllm/issues/1636) |
| 状态 | closed |
| 标签 |  |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> (Async) Batch request, OpenAI API server

### Issue 正文摘录

On the Langchain website, it states vLLMOpenAI supports both batching and async batching. But I can't get it working. Can you help? Thank you. A minimal example: ``` from langchain.llms import VLLMOpenAI llm = VLLMOpenAI( openai_api_key="EMPTY", openai_api_base="http://localhost:8000/v1", model_name="TheBloke/Llama-2-7B-Chat-AWQ", ) results = await llm.abatch(["Write me three sentences about AI."] * 10) ``` What I get is "prompts in a list are not supported".

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nai_api_key="EMPTY", openai_api_base="http://localhost:8000/v1", model_name="TheBloke/Llama-2-7B-Chat-AWQ", ) results = await llm.abatch(["Write me three sentences about AI."] * 10) ``` What I get is "prompts in a list...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ng. Can you help? Thank you. A minimal example: ``` from langchain.llms import VLLMOpenAI llm = VLLMOpenAI( openai_api_key="EMPTY", openai_api_base="http://localhost:8000/v1", model_name="TheBloke/Llama-2-7B-Chat-AWQ",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: (Async) Batch request, OpenAI API server On the Langchain website, it states vLLMOpenAI supports both batching and async batching. But I can't get it working. Can you help? Thank you. A minimal example: ``` from langcha...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
