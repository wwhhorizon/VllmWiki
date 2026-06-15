# vllm-project/vllm#12864: [Bug]:  Extra fields still not working

| 字段 | 值 |
| --- | --- |
| Issue | [#12864](https://github.com/vllm-project/vllm/issues/12864) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  Extra fields still not working

### Issue 正文摘录

I have already reviewed the PR at https://github.com/vllm-project/vllm/pull/10463, but this issue still persists. docker：`vllm/vllm-openai:latest ` parameters：`--model /data/models/mistralai/Mistral-Large-Instruct-2411 --disable-log-requests --trust-remote-code --enforce-eager --enable-auto-tool-choice --tool-call-parser mistral --tokenizer-mode mistral --config-format mistral` code： ``` from openai import OpenAI client = OpenAI(base_url="http://xxx/v1", api_key="sk-xxx") response = client.chat.completions.create( model="/data/models/mistralai/Mistral-Large-Instruct-2411", messages=[{"role": "user", "content": "hello", "name": "bob"}], ) print(response.choices[0].message) ``` error: `openai.BadRequestError: Error code: 400 - {'error': {'message': "1 validation error for ChatCompletionRequest\nmessages.0.user.name\n Extra inputs are not permitted [type=extra_forbidden, input_value='bob', input_type=str]\n For further information visit https://errors.pydantic.dev/2.10/v/extra_forbidden (request id: 2025020619014024915328971379754)", 'type': 'upstream_error', 'param': '400', 'code': 'bad_response_status_code'}}`

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: issue still persists. docker：`vllm/vllm-openai:latest ` parameters：`--model /data/models/mistralai/Mistral-Large-Instruct-2411 --disable-log-requests --trust-remote-code --enforce-eager --enable-auto-tool-choice --tool-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: github.com/vllm-project/vllm/pull/10463, but this issue still persists. docker：`vllm/vllm-openai:latest ` parameters：`--model /data/models/mistralai/Mistral-Large-Instruct-2411 --disable-log-requests --trust-remote-code...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Extra fields still not working bug;stale I have already reviewed the PR at https://github.com/vllm-project/vllm/pull/10463, but this issue still persists. docker：`vllm/vllm-openai:latest ` parameters：`--model /da...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: m/pull/10463, but this issue still persists. docker：`vllm/vllm-openai:latest ` parameters：`--model /data/models/mistralai/Mistral-Large-Instruct-2411 --disable-log-requests --trust-remote-code --enforce-eager --enable-a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
