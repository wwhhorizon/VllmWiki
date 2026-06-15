# vllm-project/vllm#19729: [Bug]: tool_chat_template_deepseekr1 is no use

| 字段 | 值 |
| --- | --- |
| Issue | [#19729](https://github.com/vllm-project/vllm/issues/19729) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: tool_chat_template_deepseekr1 is no use

### Issue 正文摘录

My vllm version is 0.9.1, with startup parameters --enable-auto-tool-choice --tool-call-parser deepseek_v3 I am using the chat template you provided：'vllm/examples/tool_chat_template_deepseekr1.jinja' ,But I got an exception return： RuntimeError: DeepSeek-V3 Tool parser could not locate tool call start/end tokens in the tokenizer! **The model I deployed is DeepSeek-R1-0528-Qwen3-8B**

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ser could not locate tool call start/end tokens in the tokenizer! **The model I deployed is DeepSeek-R1-0528-Qwen3-8B**
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: tool_chat_template_deepseekr1 is no use bug;stale My vllm version is 0.9.1, with startup parameters --enable-auto-tool-choice --tool-call-parser deepseek_v3 I am using the chat template you provided：'vllm/example...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: tool_chat_template_deepseekr1 is no use bug;stale My vllm version is 0.9.1, with startup parameters --enable-auto-tool-choice --tool-call-parser deepseek_v3 I am using the chat template you provided：'vllm/example...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
