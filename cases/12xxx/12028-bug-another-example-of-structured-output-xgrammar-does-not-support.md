# vllm-project/vllm#12028: [Bug]: another example of structured output xgrammar does not support

| 字段 | 值 |
| --- | --- |
| Issue | [#12028](https://github.com/vllm-project/vllm/issues/12028) |
| 状态 | closed |
| 标签 | bug;structured-output |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: another example of structured output xgrammar does not support

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug It seems that xgrammar does not support some structured output. The test code is: ``` class Animals(BaseModel): location: str activity: str animals_seen: conint(ge=1, le=5) # type: ignore # Constrained integer type animals: list[str] user_input = "I saw a puppy, a cat and a raccoon during my bike ride in the park" messages = [ { "role": "system", "content": "You are a helpful which converts user input to JSON object. Respond in JSON format.", }, { "role": "user", "content": f"convert to JSON according to provided schema: '{user_input}'", }, ] logger.info(f"Sending Chat API request to {model_name}") completion = client.client.chat.completions.create( model=model_name, messages=messages, temperature=0.1, max_tokens=250, extra_body=dict(guided_json=json.dumps(Animals.model_json_schema()), guided_decoding_backend="lm-format-enforcer"), ) assert completion is not None logger.warning(f"{completion=}") # check that output JSON has keys according to the schema, assert for values is too brittle (e.g. "park" vs "the park") assert set(json.loads(completion.choices[0].message.content).keys()) == set( Anima...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s not support bug;structured-output ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug It seems that xgrammar does not support some structured output. The test code is: ``` class Ani...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ma: '{user_input}'", }, ] logger.info(f"Sending Chat API request to {model_name}") completion = client.client.chat.completions.create( model=model_name, messages=messages, temperature=0.1, max_tokens=250, extra_body=dic...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ict(guided_json=json.dumps(Animals.model_json_schema()), guided_decoding_backend="lm-format-enforcer"), ) assert completion is not None logger.warning(f"{completion=}") # check that output JSON has keys according to the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ls=None), prompt_logprobs=None) ``` I tested with llama3.1-8b-instruct, quantized using gpt-w8a8 using llm-compressor. The deployment arguments are: ``` - '--tensor-parallel-size=1' - '--max-num-batched-tokens=4096' - '...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
