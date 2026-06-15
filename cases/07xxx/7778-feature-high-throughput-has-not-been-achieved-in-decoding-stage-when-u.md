# vllm-project/vllm#7778: [Feature]: High throughput has not been achieved in decoding stage when using json format output  

| 字段 | 值 |
| --- | --- |
| Issue | [#7778](https://github.com/vllm-project/vllm/issues/7778) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: High throughput has not been achieved in decoding stage when using json format output  

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I launched a LLM service by vllm, and I use AsyncOpenAI function for high throughput output. like this: ` async def async_llm_infer_sampling(prompt, api_key, base_url, model_name, response_json): client = AsyncOpenAI(api_key=api_key, base_url=base_url) try: chat_response = await client.chat.completions.create( model=model_name, messages=[ {"role": "user", "content": prompt}, ], temperature=0.5, ) return chat_response.choices[0].message.content except: return json.dumps({"analysis": "无法分析", "score": -1}, ensure_ascii=False) ` and I success to speed up inference with high prompt throughput and generation throughput . However, when I add **guided_json** like this ` chat_response = await client.chat.completions.create( model=model_name, messages=[ {"role": "user", "content": prompt}, ], extra_body={ "guided_json": response_json, "response_format": {"type": "json_object"}, }, temperature=0.5, ) ` the prompt throughput is also high, but generation throughput is as low as one request sent. I guess this problem caused by **outlines**, and how to solve it. BTW, asynchronous inference with json mode is very imporant, I need help. ### Alternatives _No...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: High throughput has not been achieved in decoding stage when using json format output feature request;stale ### 🚀 The feature, motivation and pitch I launched a LLM service by vllm, and I use AsyncOpenAI function for hi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: been achieved in decoding stage when using json format output feature request;stale ### 🚀 The feature, motivation and pitch I launched a LLM service by vllm, and I use AsyncOpenAI function for high throughput output. li...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: : return json.dumps({"analysis": "无法分析", "score": -1}, ensure_ascii=False) ` and I success to speed up inference with high prompt throughput and generation throughput . However, when I add **guided_json** like this ` ch...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: return json.dumps({"analysis": "无法分析", "score": -1}, ensure_ascii=False) ` and I success to speed up inference with high prompt throughput and generation throughput . However, when I add **guided_json** like this ` chat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: High throughput has not been achieved in decoding stage when using json format output feature request;stale ### 🚀 The feature, motivation and pitch I launched a LLM service by vllm, and I use AsyncOpenAI func...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
