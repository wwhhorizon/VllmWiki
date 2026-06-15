# vllm-project/vllm#1862: integration with langchain and streaming

| 字段 | 值 |
| --- | --- |
| Issue | [#1862](https://github.com/vllm-project/vllm/issues/1862) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> integration with langchain and streaming

### Issue 正文摘录

HI I'm loading llama2 chat Vllm with langchain and streamlit the problem isI can't manage to stream the data. I get the response as one "chunk". I aslo check if there is "stream" argument that I can use in vllm_kwargs but couldn't find one any idea how to solve this and make it work in a streaming fashion with langchain? ` llm = VLLM( model=model_path, trust_remote_code=True, max_new_tokens=3000, top_k=10, top_p=0.95, temperature=0.8, callback_manager=callback_manager, verbose=True, token=hf_auth) ` for resp in llm.stream(some_prompt): print(resp)`

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: integration with langchain and streaming HI I'm loading llama2 chat Vllm with langchain and streamlit the problem isI can't manage to stream the data. I get the response as one "chunk". I aslo check if there is "stream"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
