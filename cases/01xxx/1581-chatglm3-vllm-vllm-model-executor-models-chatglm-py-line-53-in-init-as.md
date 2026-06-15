# vllm-project/vllm#1581: chatglm3 vllm/vllm/model_executor/models/chatglm.py", line 53, in __init__     assert self.total_num_kv_heads % tp_size == 0 AssertionError

| 字段 | 值 |
| --- | --- |
| Issue | [#1581](https://github.com/vllm-project/vllm/issues/1581) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> chatglm3 vllm/vllm/model_executor/models/chatglm.py", line 53, in __init__     assert self.total_num_kv_heads % tp_size == 0 AssertionError

### Issue 正文摘录

vllm/vllm/model_executor/models/chatglm.py", line 53, in __init__ assert self.total_num_kv_heads % tp_size == 0 AssertionError 拉了最新main分支

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: chatglm3 vllm/vllm/model_executor/models/chatglm.py", line 53, in __init__ assert self.total_num_kv_heads % tp_size == 0 AssertionError vllm/vllm/model_executor/models/chatglm.py", line 53, in __init__ assert self.total...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
