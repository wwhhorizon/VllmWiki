# vllm-project/vllm#1100: gptq  Qwen-7B-Chat-Int4 load_error

| 字段 | 值 |
| --- | --- |
| Issue | [#1100](https://github.com/vllm-project/vllm/issues/1100) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> gptq  Qwen-7B-Chat-Int4 load_error

### Issue 正文摘录

qwen.py", line 303, in load_weights param = state_dict[name] KeyError: 'transformer.h.0.attn.c_attn.g_idx'

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: gptq Qwen-7B-Chat-Int4 load_error bug;stale qwen.py", line 303, in load_weights param = state_dict[name] KeyError: 'transformer.h.0.attn.c_attn.g_idx'
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: gptq Qwen-7B-Chat-Int4 load_error bug;stale qwen.py", line 303, in load_weights param = state_dict[name] KeyError: 'transformer.h.0.attn.c_attn.g_idx'
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: gptq Qwen-7B-Chat-Int4 load_error bug;stale qwen.py", line 303, in load_weights param = state_dict[name] KeyError: 'transformer.h.0.attn.c_attn.g_idx'

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
