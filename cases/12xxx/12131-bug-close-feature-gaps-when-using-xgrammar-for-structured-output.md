# vllm-project/vllm#12131: [Bug]: Close feature gaps when using xgrammar for structured output

| 字段 | 值 |
| --- | --- |
| Issue | [#12131](https://github.com/vllm-project/vllm/issues/12131) |
| 状态 | open |
| 标签 | bug;structured-output;keep-open;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Close feature gaps when using xgrammar for structured output

### Issue 正文摘录

### 🐛 Describe the bug As of v0.6.5, we use xgrammar as the default backend for structured output. However, not all ways of expressing output requirements are supported. This issue is for tracking the list of known cases needed to be resolved for making xgrammar the default in all cases. Fallback cases can be found here: https://github.com/vllm-project/vllm/blob/d06e824006d1ba4b92871347738ce1b89f658499/vllm/model_executor/guided_decoding/__init__.py#L40-L76 - [ ] non-x86 architectures - [ ] regex - related: https://github.com/mlc-ai/xgrammar/pull/144 - https://github.com/mlc-ai/xgrammar/issues/175 - [ ] choice \ - https://github.com/vllm-project/vllm/pull/12632 - [ ] jsonschema support is incomplete - https://github.com/mlc-ai/xgrammar/issues/160 - [ ] lark grammars

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ale ### 🐛 Describe the bug As of v0.6.5, we use xgrammar as the default backend for structured output. However, not all ways of expressing output requirements are supported. This issue is for tracking the list of known...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 9/vllm/model_executor/guided_decoding/__init__.py#L40-L76 - [ ] non-x86 architectures - [ ] regex - related: https://github.com/mlc-ai/xgrammar/pull/144 - https://github.com/mlc-ai/xgrammar/issues/175 - [ ] choice \ - h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/d06e824006d1ba4b92871347738ce1b89f658499/vllm/model_executor/guided_decoding/__init__.py#L40-L76 - [ ] non-x86 architectures - [ ] regex - related: https://github.com/mlc-ai/xgrammar/pull/144...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: hen using xgrammar for structured output bug;structured-output;keep-open;stale ### 🐛 Describe the bug As of v0.6.5, we use xgrammar as the default backend for structured output. However, not all ways of expressing outpu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
