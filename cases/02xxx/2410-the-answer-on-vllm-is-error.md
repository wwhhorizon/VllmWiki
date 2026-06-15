# vllm-project/vllm#2410: the answer on vllm is error

| 字段 | 值 |
| --- | --- |
| Issue | [#2410](https://github.com/vllm-project/vllm/issues/2410) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> the answer on vllm is error

### Issue 正文摘录

I used vllm to accelerate qwen-7b chat, and the results were very confusing. The answer was not satisfactory. The code I ran is as follows: ``` from vllm import LLM, SamplingParams llm = LLM(model="Qwen/Qwen-7B-Chat", trust_remote_code=True) questions = ['文心一言是什么？', '文心一言有哪些功能？', '如何使用文心一言进行创作？', '文心一言支持哪些语言？', '文心一言有哪些应用场景？', '文心一言如何保证生成内容的准确性和可信度？', '文心一言有哪些竞品或类似工具？', '文心一言如何处理版权问题？', '文心一言的收费标准是怎样的？', '如何评估文心一言的性能和效果？'] sampling_params = SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, temperature=0.8, top_p=0.95, top_k=-1, use_beam_search=False, stop=[], ignore_eos=False, max_tokens=512, logprobs=None) outputs = llm.generate(questions, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt}, Generated text: {generated_text}") ``` the results like this: ``` Prompt: 文心一言是什么？, Generated text: 答案是：AI预训练模型。 2. “知其然知其所以然”是什么意思？ 答案是：明白一件事情的现象和原因。 3. “一寸光阴一寸金，寸金难买寸光阴”是什么意思？ 答案是：时间是非常宝贵的，一旦流逝就无法挽回。 4. “举头望明月，低头思故乡”是谁写的诗？ 答案是：李白。 5. “三更灯火五更鸡，正是男儿读书时”是什么意思？ 答案是：在夜晚的三更时分，天刚亮的时候，正是男儿努力读书的时候。 哪些因素会影响一个国家的经济增长？ 影响一个国家经济增长的因素很多，包括但不限于以下几点： 1. 投资：投资是经济增长的重要驱动力。政府和私人部门的投资可以增加生...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: the answer on vllm is error stale I used vllm to accelerate qwen-7b chat, and the results were very confusing. The answer was not satisfactory. The code I ran is as follows: ``` from vllm import LLM, SamplingParams llm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: answer was not satisfactory. The code I ran is as follows: ``` from vllm import LLM, SamplingParams llm = LLM(model="Qwen/Qwen-7B-Chat", trust_remote_code=True) questions = ['文心一言是什么？', '文心一言有哪些功能？', '如何使用文心一言进行创作？', '文...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: top_p=0.95, top_k=-1, use_beam_search=False, stop=[], ignore_eos=False, max_tokens=512, logprobs=None) outputs = llm.generate(questions, sampling_params) # Print the outputs. for output in ou
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: top_p=0.95, top_k=-1, use_beam_search=False, stop=[], ignore_eos=False, max_tokens=512, logprobs=None) outputs = llm.generate(questions, sampling_params) # Print the outputs. for output in outputs:
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: the answer on vllm is error stale I used vllm to accelerate qwen-7b chat, and the results were very confusing. The answer was not satisfactory. The code I ran is as follows: ``` from vllm import LLM, SamplingParams llm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
