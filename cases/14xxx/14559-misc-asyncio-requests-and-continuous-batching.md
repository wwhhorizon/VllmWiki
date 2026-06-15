# vllm-project/vllm#14559: [Misc]: asyncio requests and continuous batching

| 字段 | 值 |
| --- | --- |
| Issue | [#14559](https://github.com/vllm-project/vllm/issues/14559) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: asyncio requests and continuous batching

### Issue 正文摘录

I'm using asyncio methods to make concurrent requests to vllm server which in turn should batch these requests (continuous batching). however looking at the logs, vllm pass each request alone to the llm. note: I can't use multi threading requests, I'm limited to use single thread here is my code: ```python async def llm_call(prompt_template, engine,parser, kwg): raw_output = await (prompt_template | engine).invoke(kwg) output = parser.invoke(raw_output) return output async def llm_concurrent_requests(inputs,prompt_template, engine,parser): tasks = [] # 5 to test for record in (inputs[:5]): tasks.append(llm_call( prompt_template=prompt_template, engine=engine, parser=parser, kwg = record ) ) results = await asyncio.gather(*tasks) return results async def main(inputs): engine = ChatOpenAI(**CONFIG) prompt_template = ChatPromptTemplate.from_messages([("user", PROMPT)] ) parser = JsonOutputParser(pydantic_object=Response) responses = await llm_concurrent_requests(inputs = inputs,prompt_template = prompt_template, engine = engine,parser = parser) if __name__ == "__main__": #.... asyncio.run(main(inputs)) ``` ### Before submitting a new issue... - [x] Make sure you already searched for...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Misc]: asyncio requests and continuous batching stale I'm using asyncio methods to make concurrent requests to vllm server which in turn should batch these requests (continuous batching). however looking at the logs, v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Misc]: asyncio requests and continuous batching stale I'm using asyncio methods to make concurrent requests to vllm server which in turn should batch these requests (continuous batching). however looking at the logs, v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s) return results async def main(inputs): engine = ChatOpenAI(**CONFIG) prompt_template = ChatPromptTemplate.from_messages([("user", PROMPT)] ) parser = JsonOutputParser(pydantic_object=Response) responses = await llm_c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: quests(inputs,prompt_template, engine,parser): tasks = [] # 5 to test for record in (inputs[:5]): tasks.append(llm_call( prompt_template=prompt_template, engine=engine, parser=parser, kwg = record

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
