# vllm-project/vllm#13156: [Bug]: The service request for vllm064post1 was prematurely terminated, and it could not output a fixed number of tokens.”

| 字段 | 值 |
| --- | --- |
| Issue | [#13156](https://github.com/vllm-project/vllm/issues/13156) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The service request for vllm064post1 was prematurely terminated, and it could not output a fixed number of tokens.”

### Issue 正文摘录

### Your current environment Using vllm064 post1 and running a benchmark test, with the ignore_eos setting set to 1, for fixed-length input and output testing (input 20000, output 256, qps=2). I found that regardless of which ASYNC_REQUEST_FUNCS ("vllm": async_request_openai_completions, or "openai-chat": async_request_openai_chat_completions) is used, the actual output token count, which is the length of the output.itl list, does not match the preset value (max_tokens). Especially when the endpoint is /v1/completions, the length of len(output.itl) is often quite low. Please let me know how to resolve this. Is it an issue with my settings? For example: Using the /v1/chat/completions endpoint ![Image](https://github.com/user-attachments/assets/b7b03752-587d-41cd-9bc4-de72a58f903c) Using the /v1/completions endpoint ![Image](https://github.com/user-attachments/assets/447a1042-f834-431f-ba70-69c76f11a1de) I printed the data structure in “backend_request_func.py” below. ![Image](https://github.com/user-attachments/assets/c839af99-7516-4214-920f-572205607870) My startup command is ``` Model: Llama-3.1-70B-Instruct Startup command: CUDA_VISIBLE_DEVICES="0,1,2,3" python3 -u -m vllm.entry...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tartup command is ``` Model: Llama-3.1-70B-Instruct Startup command: CUDA_VISIBLE_DEVICES="0,1,2,3" python3 -u -m vllm.entrypoints.openai.api_server --model /models/Llama-3.1-70B-Instruct --served-model-name Llama-3.1-7...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ssets/c839af99-7516-4214-920f-572205607870) My startup command is ``` Model: Llama-3.1-70B-Instruct Startup command: CUDA_VISIBLE_DEVICES="0,1,2,3" python3 -u -m vllm.entrypoints.openai.api_server --model /models/Llama-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: The service request for vllm064post1 was prematurely terminated, and it could not output a fixed number of tokens.” usage;stale ### Your current environment Using vllm064 post1 and running a benchmark test, with...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ge;stale ### Your current environment Using vllm064 post1 and running a benchmark test, with the ignore_eos setting set to 1, for fixed-length input and output testing (input 20000, output 256, qps=2). I found that rega...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: /447a1042-f834-431f-ba70-69c76f11a1de) I printed the data structure in “backend_request_func.py” below. ![Image](https://github.com/user-attachments/assets/c839af99-7516-4214-920f-572205607870) My startup command is ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
