# vllm-project/vllm#39867: [Bug]: When function_call is used in the request and tool_choice is set to required,the system performs schema formatting in advance before the request is sent to the model for inference.

| 字段 | 值 |
| --- | --- |
| Issue | [#39867](https://github.com/vllm-project/vllm/issues/39867) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When function_call is used in the request and tool_choice is set to required,the system performs schema formatting in advance before the request is sent to the model for inference.

### Issue 正文摘录

### Your current environment ```text model: Qwen3-8B serve cmd: vllm serve /home/data/Qwen3-8B \ --served-model-name Qwen3-8B \ --trust-remote-code \ --async-scheduling \ --no-enable-prefix-caching \ --distributed-executor-backend mp \ --tensor-parallel-size 1 \ --max-model-len 40000 \ --max-num-batched-tokens 40960 \ --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \ --additional-config '{"pa_shape_list":[48,64,72,80], "weight_prefetch_config":{"enabled":true}}' \ --port 20269 \ --block-size 128 \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --gpu-memory-utilization 0.9 ``` ### 🐛 Describe the bug - As a result, for the same input prompt: 1. Without formatting: the model outputs fewer tokens, with normal accuracy. 2. With formatting: inference performance is roughly halved (about 2x slower) - the code path: vllm/tool_parsers/utils.py ```python tool_choice: "required" if tool_choice == "required": return _get_json_schema_from_tools(tools) ``` - The output 1. With formating: ```txt e2e: 1.499s tokens: 48 [9640, 262, 341, 286, 330, 606, 788, 330, 1836, 69364, 756, 286, 330, 13786, 788, 341, 310, 330, 1074, 788, 330, 99407, 99683, 39426, 23836, 756, 310, 330, 1...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: he request and tool_choice is set to required,the system performs schema formatting in advance before the request is sent to the model for inference. bug ### Your current environment ```text model: Qwen3-8B serve cmd: v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --max-num-batched-tokens 40960 \ --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \ --additional-config '{"pa_shape_list":[48,64,72,80], "weight_prefetch_config":{"enabled":true}}' \ --port 20269 \ --block-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: When function_call is used in the request and tool_choice is set to required,the system performs schema formatting in advance before the request is sent to the model for inference. bug ### Your current environmen...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ompt: 1. Without formatting: the model outputs fewer tokens, with normal accuracy. 2. With formatting: inference performance is roughly halved (about 2x slower) - the code path: vllm/tool_parsers/utils.py ```python tool...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: --no-enable-prefix-caching \ --distributed-executor-backend mp \ --tensor-parallel-size 1 \ --max-model-len 40000 \ --max-num-batched-tokens 40960 \ --compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}' \

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
