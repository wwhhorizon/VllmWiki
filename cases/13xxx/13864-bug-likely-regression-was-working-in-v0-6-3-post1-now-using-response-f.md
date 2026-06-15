# vllm-project/vllm#13864: [Bug]: Likely Regression - Was working in v0.6.3.post1, now using response_format parameter with "type": "bool" in v0.7.3: BadRequestError: Error code 400 - {'object': 'error', 'message': 'json_schema_converter.cc:595 Unsupported type bool in schema {type":"bool"}\n, 'type': 'BadRequestError', 'param': None, 'code': 400}

| 字段 | 值 |
| --- | --- |
| Issue | [#13864](https://github.com/vllm-project/vllm/issues/13864) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Likely Regression - Was working in v0.6.3.post1, now using response_format parameter with "type": "bool" in v0.7.3: BadRequestError: Error code 400 - {'object': 'error', 'message': 'json_schema_converter.cc:595 Unsupported type bool in schema {type":"bool"}\n, 'type': 'BadRequestError', 'param': None, 'code': 400}

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Note code might have minor typos, could not copy paste. ``` from openai import OpenAI client = OpenAI( api_key="API_KEY_HERE" base_url="vllm_hostname_or_IP_here:8000/v1" ) messages = [ {"role": "system", "content": "is there a number in the following text?\n"}, {"role": "user", "content": "lets do a math problem 2 + 2 is equal to what?"} ] model = llama3.3 #(any llama 3.3 model) completion = client.chat.completions.create( model=model, messages=messages, stream=False, seed=1234, response_format={ "type": "json_schema", "json_schema": { "name":"format_response", "schema": { "contains_number": {"type":"bool"} } } } } ) print(completetion.choices[0].message.content) ``` Results in following error: `BadRequestError: Error code 400 - {'object': 'error', 'message': 'json_schema_converter.cc:595 Unsupported type bool in schema {type":"bool"}\n, 'type': 'BadRequestError', 'param': None, 'code': 400}` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of fre...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ug]: Likely Regression - Was working in v0.6.3.post1, now using response_format parameter with "type": "bool" in v0.7.3: BadRequestError: Error code 400 - {'object': 'error', 'message': 'json_schema_converter.cc:595 Uns...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 1, now using response_format parameter with "type": "bool" in v0.7.3: BadRequestError: Error code 400 - {'object': 'error', 'message': 'json_schema_converter.cc:595 Unsupported type bool in schema {type":"bool"}\n, 'typ...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Likely Regression - Was working in v0.6.3.post1, now using response_format parameter with "type": "bool" in v0.7.3: BadRequestError: Error code 400 - {'object': 'error', 'message': 'json_schema_converter.cc:595 U...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Note code might have minor typos, could not copy paste. ``` from openai import OpenAI client = OpenAI( api_key="API_KEY_HERE" base_url="vllm_hostname_or_IP_here:8000/v1" ) messages = [ {"role": "system", "content": "is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0}` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
