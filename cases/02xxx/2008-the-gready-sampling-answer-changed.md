# vllm-project/vllm#2008: The gready sampling answer changed？

| 字段 | 值 |
| --- | --- |
| Issue | [#2008](https://github.com/vllm-project/vllm/issues/2008) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The gready sampling answer changed？

### Issue 正文摘录

I use tp=4 with the llama-70b model, and the sampling is gready("temperature":0.0)， the answer is not stable when the Concurrency >=3. the answer changed. for example： 15035362-deb3-46e7-8fb1-f8edab919578--xx---{"id":"cmpl-efa9cb1a7f5943d8a0babaa1dd3b913d","object":"text_completion","created":1702265103,"model":"xx","choices":[{"index":0,"text":"\n\n### 回答\n台湾四大天王是指20世纪80年代至90年代初期，台湾乐坛最具代表性的四位男歌手，他们分别是：\n\n1. 张学友：香港歌手，但因其在台湾乐坛的巨大影响力而被称为“台湾四大天王”之一。\n\n2. 王杰：台湾歌手，以其独特的嗓音和深情的演唱风格著称。\n\n3. 周华健：台湾歌手，以其清新自然的演唱风格和多才多艺的表现力而受到广泛赞誉。\n\n4. 林志颖：台湾歌手、演员，以其青春阳光的形象和多才多艺的表现力而受到广泛喜爱。","logprobs":null,"finish_reason":"stop"}],"usage":{"prompt_tokens":7,"total_tokens":147,"completion_tokens":**140**}} 15035362-deb3-46e7-8fb1-f8edab919578--xx--- 请求耗时: 5524.03 ms a919e84e-4d21-4d6c-b034-98b406d51b0b--xx---{"id":"cmpl-cf68e3c280c1443c94f0b68a720b6a7f","object":"text_completion","created":1702265104,"model":"xx","choices":[{"index":0,"text":"\n\n### 回答\n台湾四大天王是指20世纪80年代至90年代初期，台湾乐坛最具代表性的四位男歌手，他们分别是：\n\n1. 张学友：香港歌手，但因其在台湾乐坛的巨大影响力而被称为“台湾四大天王”之一。\n\n2. 王杰：台湾歌手，以其独特的嗓音和深情的演唱风格著称。\n\n3. 周华健：台湾歌手，以其清新自然的演唱风格和多才多艺的表现力而受到广泛赞誉。\n\n4. 林志颖：台湾歌手、演员，以其青春阳光的形象和多才多艺的表现力而受到广泛喜爱。","logprobs":null,"finish_reason":"stop"}...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: The gready sampling answer changed？ I use tp=4 with the llama-70b model, and the sampling is gready("temperature":0.0)， the answer is not stable when the Concurrency >=3. the answer changed. for example： 15035362-deb3-4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: {"prompt_tokens":7,"total_tokens":144,"completion_tokens":**137**}} The version is vllm==0.2.1 or 0.1.4 when tp=2 or Concurrency <= 2, the answer is stable.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
