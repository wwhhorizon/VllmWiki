# vllm-project/vllm#6890: [Bug]: Vllm api server does not receive supported parameter `truncate_prompt_tokens`

| 字段 | 值 |
| --- | --- |
| Issue | [#6890](https://github.com/vllm-project/vllm/issues/6890) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Vllm api server does not receive supported parameter `truncate_prompt_tokens`

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I used the openai compatible server deployed with vllm: ```bash python -m vllm.entrypoints.openai.api_server --model meta-llama/Meta-Llama-3-8B-Instruct--host 127.0.0.1 --port 8077 --enforce-eager --gpu-memory-utilization 0.8 --swap-space 32 ``` When I send a request with the following snippet (openai client): ```python openai_api_key="EMPTY" openai_api_base="http://localhost:8077/v1" from openai import OpenAI client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) models = client.models.list() model = models.data[0].id client.chat.completions.create( messages=[ { "role": "user", "content": "How are you today?" }, ], model=model, max_tokens=128, temperature=0.0, seed=42, extra_body=dict( truncate_prompt_tokens=1792, ) ) ``` I got the error: ``` in _request raise self._make_status_error_from_response(err.response) from None openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': "[{'type': 'extra_forbidden', 'loc': ('body', 'truncate_prompt_tokens'), 'msg': 'Extra inputs are not permitted', 'input': 1792}]", 'type': 'BadRequestError', 'param': None, 'c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ployed with vllm: ```bash python -m vllm.entrypoints.openai.api_server --model meta-llama/Meta-Llama-3-8B-Instruct--host 127.0.0.1 --port 8077 --enforce-eager --gpu-memory-utilization 0.8 --swap-space 32 ``` When I send...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: server does not receive supported parameter `truncate_prompt_tokens` bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I used the openai compatible server de...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: i_api_key="EMPTY" openai_api_base="http://localhost:8077/v1" from openai import OpenAI client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) models = client.models.list() model = models.data[0].id client....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: parameter ) ) ``` I wonder why in https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#extra-parameters, `truncate_prompt_tokens` is supported but I am getting the error here ?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
