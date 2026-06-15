# vllm-project/vllm#28396: [Bug]: Sporadic out.is_contiguous assert crashes with Kimi-K2-Thinking

| 字段 | 值 |
| --- | --- |
| Issue | [#28396](https://github.com/vllm-project/vllm/issues/28396) |
| 状态 | closed |
| 标签 | bug;stale;deepseek |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Sporadic out.is_contiguous assert crashes with Kimi-K2-Thinking

### Issue 正文摘录

### Your current environment Docker image: `hanseware/vllm-nightly:20251109` (also `20251107` was crashing) ### 🐛 Describe the bug Running on 4xB200 with the following params: ``` non-default args: { 'enable_auto_tool_choice': True, 'tool_call_parser': 'kimi_k2', 'trust_remote_code': True, 'served_model_name': ['moonshotai/Kimi-K2-Thinking'], 'load_format': 'runai_streamer', 'reasoning_parser': 'kimi_k2', 'tensor_parallel_size': 4, 'decode_context_parallel_size': 4, 'gpu_memory_utilization': 0.95, 'enable_prefix_caching': True} ``` Sporadic crashes with the following crashlog. [crash.log](https://github.com/user-attachments/files/23455622/crash.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 09` (also `20251107` was crashing) ### 🐛 Describe the bug Running on 4xB200 with the following params: ``` non-default args: { 'enable_auto_tool_choice': True, 'tool_call_parser': 'kimi_k2', 'trust_remote_code': True, '...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: True, 'tool_call_parser': 'kimi_k2', 'trust_remote_code': True, 'served_model_name': ['moonshotai/Kimi-K2-Thinking'], 'load_format': 'runai_streamer', 'reasoning_parser': 'kimi_k2', 'tensor_parallel_size': 4, 'decode_co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: Sporadic out.is_contiguous assert crashes with Kimi-K2-Thinking bug;stale;deepseek ### Your current environment Docker image: `hanseware/vllm-nightly:20251109` (also `20251107` was crashing) ### 🐛 Describe the bug...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s with Kimi-K2-Thinking bug;stale;deepseek ### Your current environment Docker image: `hanseware/vllm-nightly:20251109` (also `20251107` was crashing) ### 🐛 Describe the bug Running on 4xB200 with the following params:...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: Sporadic out.is_contiguous assert crashes with Kimi-K2-Thinking bug;stale;deepseek ### Your current environment Docker image: `hanseware/vllm-nightly:20251109` (also `20251107` was crashing) ### 🐛 Describe the bu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
