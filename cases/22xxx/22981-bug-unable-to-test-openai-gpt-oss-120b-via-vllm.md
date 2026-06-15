# vllm-project/vllm#22981: [Bug]: Unable to test openai/gpt-oss-120b via vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#22981](https://github.com/vllm-project/vllm/issues/22981) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unable to test openai/gpt-oss-120b via vllm

### Issue 正文摘录

### Your current environment without environment variables, as I'm running the service on a rented server. I don't have access to the console ### 🐛 Describe the bug **Describe the bug** `KeyError: 'content'` **To Reproduce** Exact steps to reproduce the behavior: 1. Run vllm on H100 `vastai create instance --image vllm/vllm-openai:gptoss --env '-p 8000:8000 --ipc=host --gpus all' --disk 8 --args --model "openai/gpt-oss-120b" --tensor-parallel-size 1` 2. Run guidellm **Errors** ``` > export GUIDELLM__PREFERRED_ROUTE="chat_completions" && export GUIDELLM__OPENAI__MAX_OUTPUT_TOKENS=512 && export GUIDELLM__MAX_CONCURRENCY=233 && export GUIDELLM__REQUEST_TIMEOUT=300 && export GUIDELLM__PREFERRED_PROMPT_TOKENS_SOURCE=local && export GUIDELLM__PREFERRED_OUTPUT_TOKENS_SOURCE=local && guidellm benchmark --target http://....:11509 --rate-type sweep --rate 5 --model openai/gpt-oss-120b --processor openai/gpt-oss-120b --random-seed 2025 --max-requests=100 --data "prompt_tokens=4096,output_tokens=512" --backend-args '{"extra_body":{"chat_template_kwargs":{"enable_thinking":false}}}' --output-path "data/benchmarks.json" Creating backend... 2025-08-15T09:46:20.216941+0000 | chat_completions | ER...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: **To Reproduce** Exact steps to reproduce the behavior: 1. Run vllm on H100 `vastai create instance --image vllm/vllm-openai:gptoss --env '-p 8000:8000 --ipc=host --gpus all' --disk 8 --args --model "openai/gpt-oss-120b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Unable to test openai/gpt-oss-120b via vllm bug;stale ### Your current environment without environment variables, as I'm running the service on a rented server. I don't have access to the console ### 🐛 Describe t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Unable to test openai/gpt-oss-120b via vllm bug;stale ### Your current environment without environment variables, as I'm running the service on a rented server. I don't have access to the console ### 🐛 Describe t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Unable to test openai/gpt-oss-120b via vllm bug;stale ### Your current environment without environment variables, as I'm running the service on a rented server. I don't have access to the console ### 🐛 Describe t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2025 --max-requests=100 --data "prompt_tokens=4096,output_tokens=512" --backend-args '{"extra_body":{"chat_template_kwargs":{"enable_thinking":false}}}' --output-path "data/benchmarks.json" Creating backend... 2025-08-1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
