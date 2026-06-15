# vllm-project/vllm#9547: [Bug]: continue_final_message doesn't support strings that end with '\n', '\t', ' ' and so on, for Llama-3.1-8B-Instruct.

| 字段 | 值 |
| --- | --- |
| Issue | [#9547](https://github.com/vllm-project/vllm/issues/9547) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: continue_final_message doesn't support strings that end with '\n', '\t', ' ' and so on, for Llama-3.1-8B-Instruct.

### Issue 正文摘录

### Your current environment vllm 0.6.3.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I used the following code to call Llama-3.1-8B-Instruct. ```python import requests no_bug_messages = [ {'role': 'user', 'content': """Hello, tell me a joke."""}, {'role': 'assistant', 'content': """OK!"""}, ] bug_messages1 = [ {'role': 'user', 'content': """Hello, tell me a joke."""}, {'role': 'assistant', 'content': """OK!\n"""}, ] bug_messages2 = [ {'role': 'user', 'content': """Hello, tell me a joke."""}, {'role': 'assistant', 'content': """OK! """}, ] response = requests.post(url, headers=header, json={ "model": model, "messages": no_bug_messages, "continue_final_message": True, "add_generation_prompt": False}) print(response.json()) ``` When I used `no_bug_messages`, the response was OK. But when I used `bug_messages1`, the response was as follows: ``` {'object': 'error', 'message': 'substring not found', 'type': 'BadRequestError', 'param': None, 'code': 400} ``` The log is as follows: ``` ERROR 10-21 15:57:28 serving_chat.py:156] Error in applying chat template from request ERROR 10-21 15:57:28 serving_chat.py:156] Traceback (most recent call last): ERROR 10-21 15:57:28 s...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: age doesn't support strings that end with '\n', '\t', ' ' and so on, for Llama-3.1-8B-Instruct. bug ### Your current environment vllm 0.6.3.post1 ### Model Input Dumps _No response_ ### 🐛 Describe the bug I used the fol...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ug I used the following code to call Llama-3.1-8B-Instruct. ```python import requests no_bug_messages = [ {'role': 'user', 'content': """Hello, tell me a joke."""}, {'role': 'assistant', 'content': """OK!"""}, ] bug_mes...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: sage": True, "add_generation_prompt": False}) print(response.json()) ``` When I used `no_bug_messages`, the response was OK. But when I used `bug_messages1`, the response was as follows: ``` {'object': 'error', 'message...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: sed the following code to call Llama-3.1-8B-Instruct. ```python import requests no_bug_messages = [ {'role': 'user', 'content': """Hello, tell me a joke."""}, {'role': 'assistant', 'content': """OK!"""}, ] bug_messages1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
