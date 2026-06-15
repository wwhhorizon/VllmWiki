# vllm-project/vllm#18006: [Bug]: OpenAI Chat Completions API: NULL response

| 字段 | 值 |
| --- | --- |
| Issue | [#18006](https://github.com/vllm-project/vllm/issues/18006) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: OpenAI Chat Completions API: NULL response

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When invoking the OpenAI Chat API with model google/gemma-3-4b-it, the response is null, i.e., response.choices[0].message.content is empty. I tried increasing the max tokens but this did not change anything. But when I tried the same with the gemma-3-1b-it, it is able to give a response. Below is the code snippet: ```text payload = json.dumps(df, ensure_ascii=False) messages = [ { "role": "system", "content": (SYSTEM_PROMPT) }, { "role": "user", "content": (USER_TEMPLATE.format( uid=uid, day=day, start=window_start.strftime("%Y-%m-%d %H:%M"), end=(window_start + pd.Timedelta(hours=1)).strftime("%Y-%m-%d %H:%M"), payload=payload ) ) } ] response = client.chat.completions.create( model="google/gemma-3-4b-it", messages=messages, max_tokens=500, temperature=1.0, top_p=0.95, ) print("------------------Response:", response) raw = response.choices[0].message.content ``` I receive the following response: ```text ChatCompletion(id='chatcmpl-7c65dciojknknmjbg1f72e74f', choices=[Choice(finish_reason='length', index=0, logprobs=None, message=ChatCompletionMessage(content='', refusal=None, role='assistant', annotations=None, audio=None, func...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nment ### 🐛 Describe the bug When invoking the OpenAI Chat API with model google/gemma-3-4b-it, the response is null, i.e., response.choices[0].message.content is empty. I tried increasing the max tokens but this did no...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he code snippet: ```text payload = json.dumps(df, ensure_ascii=False) messages = [ { "role": "system", "content": (SYSTEM_PROMPT) }, { "role": "user",
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e snippet: ```text payload = json.dumps(df, ensure_ascii=False) messages = [ { "role": "system", "content": (SYSTEM_PROMPT) }, { "role": "user",
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: 🐛 Describe the bug When invoking the OpenAI Chat API with model google/gemma-3-4b-it, the response is null, i.e., response.choices[0].message.content is empty. I tried increasing the max tokens but this did not change a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
