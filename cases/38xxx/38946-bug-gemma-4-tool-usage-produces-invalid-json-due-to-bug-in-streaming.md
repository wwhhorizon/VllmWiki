# vllm-project/vllm#38946: [Bug]: Gemma 4 tool usage produces invalid json due to bug in streaming

| 字段 | 值 |
| --- | --- |
| Issue | [#38946](https://github.com/vllm-project/vllm/issues/38946) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 tool usage produces invalid json due to bug in streaming

### Issue 正文摘录

### Summary Currently, the parsing logic while streaming does not consider the string delimiter. This leads to incorrect strings and somtimes even invalid json during tool usage in applications such as OpenCode. ### 🐛 Describe the bug When using tools like OpenCode connected to the [nvidia/Gemma-4-31B-IT-NVFP4](https://huggingface.co/nvidia/Gemma-4-31B-IT-NVFP4) model hosted with vllm on an H100, the model is mostly unable to use tools due to a bug in the parsing / streaming logic. #### Test Result **Before fix**: > try to write a simple todo using the tool > invalid [tool=todowrite, error=Invalid input for tool todowrite: JSON parsing failed: Text: {"todos": [{"content": " try to write a simple todo using the tool > Todos [•] Demonstrate todowrite tool usage ### Pull request [[Bugfix] Gemma 4: Fix bug around invalid JSON diffs during tool usage](https://github.com/vllm-project/vllm/pull/38945) I believe this is also related to #38910. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma 4 tool usage produces invalid json due to bug in streaming bug ### Summary Currently, the parsing logic while streaming does not consider the string delimiter. This leads to incorrect strings and somtimes e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: When using tools like OpenCode connected to the [nvidia/Gemma-4-31B-IT-NVFP4](https://huggingface.co/nvidia/Gemma-4-31B-IT-NVFP4) model hosted with vllm on an H100, the model is mostly unable to use tools due to a bug i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: huggingface.co/nvidia/Gemma-4-31B-IT-NVFP4) model hosted with vllm on an H100, the model is mostly unable to use tools due to a bug in the parsing / streaming logic. #### Test Result **Before fix**: > try to write a sim...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma 4 tool usage produces invalid json due to bug in streaming bug ### Summary Currently, the parsing logic while streaming does not consider the string delimiter. This leads to incorrect strings and somtimes e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [•] Demonstrate todowrite tool usage ### Pull request [[Bugfix] Gemma 4: Fix bug around invalid JSON diffs during tool usage](https://github.com/vllm-project/vllm/pull/38945) I believe this is also related to #38910. ##...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
