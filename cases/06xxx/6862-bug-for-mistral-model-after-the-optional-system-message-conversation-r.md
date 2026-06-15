# vllm-project/vllm#6862: [Bug]: for mistral model, After the optional system message, conversation roles must  alternate user/assistant/user/assistant/

| 字段 | 值 |
| --- | --- |
| Issue | [#6862](https://github.com/vllm-project/vllm/issues/6862) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: for mistral model, After the optional system message, conversation roles must  alternate user/assistant/user/assistant/

### Issue 正文摘录

### Your current environment vllm version: v0.5.3.post1 ### 🐛 Describe the bug launch the vllm: ```CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.openai.api_server --model mistralai/Mistral-7B-Instruct-v0.3 --api-key "yyy" --port 1703 ``` call the mistral model via python : ``` import openai client = openai.OpenAI( api_key="yyy", base_url="http://localhost:1704/v1/", ) response = client.chat.completions.create(model="mistralai/Mistral-7B-Instruct-v0.3", messages=[{'role':'system', 'content':'you are wikipedia agent.'}, {'role':'user', 'content':'whta is the capital city of ontario ?'}, {'role':'user', 'content':'and tell me about its history.'}], max_tokens=128, temperature=0) ``` error message: ``` BadRequestError: Error code: 400 - {'object': 'error', 'message': 'After the optional system message, conversation roles must alternate user/assistant/user/assistant/...', 'type': 'BadRequestError', 'param': None, 'code': 400} ``` This error does not appear in other model series other than mistral. Any hint ?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: r/assistant/user/assistant/ bug;stale ### Your current environment vllm version: v0.5.3.post1 ### 🐛 Describe the bug launch the vllm: ```CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.openai.api_server --model mistra...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e, conversation roles must alternate user/assistant/user/assistant/ bug;stale ### Your current environment vllm version: v0.5.3.post1 ### 🐛 Describe the bug launch the vllm: ```CUDA_VISIBLE_DEVICES=7 python -m vllm.entr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: vllm version: v0.5.3.post1 ### 🐛 Describe the bug launch the vllm: ```CUDA_VISIBLE_DEVICES=7 python -m vllm.entrypoints.openai.api_server --model mistralai/Mistral-7B-Instruct-v0.3 --api-key "yyy" --port 1703 ``` call t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: for mistral model, After the optional system message, conversation roles must alternate user/assistant/user/assistant/ bug;stale ### Your current environment vllm version: v0.5.3.post1 ### 🐛 Describe the bug laun...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
