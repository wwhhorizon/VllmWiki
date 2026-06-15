# vllm-project/vllm#1861: 01-ai/Yi-34B-Chat never stops

| 字段 | 值 |
| --- | --- |
| Issue | [#1861](https://github.com/vllm-project/vllm/issues/1861) |
| 状态 | closed |
| 标签 |  |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 01-ai/Yi-34B-Chat never stops

### Issue 正文摘录

Using latest 0.2.2 ``` stop_sequences = [' ', ' \n assistant\n'] base_model = 01-ai/Yi-34B-Chat openai_client.Completion.create( model=base_model, prompt=""" system You are a helpful assistant user Say exactly one word assistant """, max_tokens=200, stop=stop_sequences, stream=False, ) ``` gives: ``` Excellent! How may I assist you today? 造句机器 If you believe in yourself, you can achieve anything. 相信自己，你就能实现任何事情。 考研句子 The optimism of the youth is a powerful force that can drive societal change and personal growth. 年轻一代的乐观精神是一种强大的力量，可以推动社会变革和个人成长。 高考作文 The hero in the story displayed great courage and wisdom, serving as an inspiration to all. 故事中的英雄展现了极大的勇气和智慧，为所有人树立了榜样。 考研 During the interview, the candidate demonstrated excellent communication skills, readily answering all questions with confidence. 面试过程中，候选人表现出优秀的沟通技巧，自信地回答了所有问题。 高考 The students were filled with excitement as they prepared for the upcoming field trip, eagerly anticipating the new ``` It acts like chat model, but never stops until finish_reason "length" Is anybody seeing that too? No matter how I vary the prompt (in case I made mistake) always same issue. What's printed never shows the tokens between text, as if l...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s Using latest 0.2.2 ``` stop_sequences = [' ', ' \n assistant\n'] base_model = 01-ai/Yi-34B-Chat openai_client.Completion.create( model=base_model, prompt=""" system You are a helpful assistant user Say exactly one wor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 事情。 考研句子 The optimism of the youth is a powerful force that can drive societal change and personal growth. 年轻一代的乐观精神是一种强大的力量，可以推动社会变革和个人成长。 高考作文 The hero in the story displayed great courage and wisdom, serving as an in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: in yourself, you can achieve anything. 相信自己，你就能实现任何事情。 考研句子 The optimism of the youth is a powerful force that can drive societal change and personal growth. 年轻一代的乐观精神是一种强大的力量，可以推动社会变革和个人成长。 高考作文 The hero in the story d...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0, stop=stop_sequences, stream=False, ) ``` gives: ``` Excellent! How may I assist you today? 造句机器 If you believe in yourself, you can achieve anything. 相信自己，你就能实现任何事情。 考研句子 The optimism of the youth is a powerful force...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 01-ai/Yi-34B-Chat never stops Using latest 0.2.2 ``` stop_sequences = [' ', ' \n assistant\n'] base_model = 01-ai/Yi-34B-Chat openai_client.Completion.create( model=base_model, prompt=""" system You are a helpful as

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
