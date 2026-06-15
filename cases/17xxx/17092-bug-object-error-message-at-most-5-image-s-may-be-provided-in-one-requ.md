# vllm-project/vllm#17092: [Bug]: {'object': 'error', 'message': 'At most 5 image(s) may be provided in one request.', 'type': 'BadRequestError', 'param': None, 'code': 400}......Can this issue be avoided by modifying the source code? If so, where should it be modified?

| 字段 | 值 |
| --- | --- |
| Issue | [#17092](https://github.com/vllm-project/vllm/issues/17092) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: {'object': 'error', 'message': 'At most 5 image(s) may be provided in one request.', 'type': 'BadRequestError', 'param': None, 'code': 400}......Can this issue be avoided by modifying the source code? If so, where should it be modified?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug File "/ssd_data/home/panyunfeng/project/EasyR1-main/z_tools_py/w_sft_json_creat.py", line 48, in check_semantic_similarity response = client.chat.completions.create( File "/home/allinrl/miniconda3/envs/easyr1/lib/python3.10/site-packages/openai/_utils/_utils.py", line 279, in wrapper return func(*args, **kwargs) File "/home/allinrl/miniconda3/envs/easyr1/lib/python3.10/site-packages/openai/resources/chat/completions/completions.py", line 914, in create return self._post( File "/home/allinrl/miniconda3/envs/easyr1/lib/python3.10/site-packages/openai/_base_client.py", line 1242, in post return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls)) File "/home/allinrl/miniconda3/envs/easyr1/lib/python3.10/site-packages/openai/_base_client.py", line 919, in request return self._request( File "/home/allinrl/miniconda3/envs/easyr1/lib/python3.10/site-packages/openai/_base_client.py", line 1023, in _request raise self._make_status_error_from_response(err.response) from None openai.BadRequestError: Error code: 400 - {'object': 'error', 'message': 'At most 5 image(s) may be provided in one request.', 'type': 'B...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 00} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 'object': 'error', 'message': 'At most 5 image(s) may be provided in one request.', 'type': 'BadRequestError', 'param': None, 'code': 400}......Can this issue be avoided by modifying the source code? If so, where should...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
