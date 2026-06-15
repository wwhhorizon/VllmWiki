# vllm-project/vllm#607: AttributeError: 'ChatGLMConfig' object has no attribute 'num_hidden_layers' 

| 字段 | 值 |
| --- | --- |
| Issue | [#607](https://github.com/vllm-project/vllm/issues/607) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AttributeError: 'ChatGLMConfig' object has no attribute 'num_hidden_layers' 

### Issue 正文摘录

Seems chatglm2 is not supported. is there a plan to support it? Seems vllm relies on model config or implementation in transformers. ``` -07-28 07:40:21 | ERROR | stderr | │ │ 1736 2023-07-28 07:40:21 | ERROR | stderr | │ 108 │ │ self.scheduler = Scheduler(scheduler_config, cache_config, log │ 1737 2023-07-28 07:40:21 | ERROR | stderr | │ 109 │ │ 1738 2023-07-28 07:40:21 | ERROR | stderr | │ 110 │ def _verify_args(self) -> None: │ 1739 2023-07-28 07:40:21 | ERROR | stderr | │ ❱ 111 │ │ self.model_config.verify_with_parallel_config(self.parallel_co │ 1740 2023-07-28 07:40:21 | ERROR | stderr | │ 112 │ │ self.cache_config.verify_with_parallel_config(self.parallel_co │ 1741 2023-07-28 07:40:21 | ERROR | stderr | │ 113 │ │ 1742 2023-07-28 07:40:21 | ERROR | stderr | │ 114 │ def _init_cache(self) -> None: │ 1743 2023-07-28 07:40:21 | ERROR | stderr | │ │ 1744 2023-07-28 07:40:21 | ERROR | stderr | │ /usr/local/lib/python3.10/site-packages/vllm/config.py:77 in │ 1745 2023-07-28 07:40:21 | ERROR | stderr | │ verify_with_parallel_config │ 1746 2023-07-28 07:40:21 | ERROR | stderr | │ │ 1747 2023-07-28 07:40:21 | ERROR | stderr | │ 74 │ │ │ │ " must be divisible by tensor parallel size " │...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: AttributeError: 'ChatGLMConfig' object has no attribute 'num_hidden_layers' new-model Seems chatglm2 is not supported. is there a plan to support it? Seems vllm relies on model config or implementation in transformers....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: │ 1736 2023-07-28 07:40:21 | ERROR | stderr | │ 108 │ │ self.scheduler = Scheduler(scheduler_config, cache_config, log │ 1737 2023-07-28 07:40:21 | ERROR | stderr | │ 109 │ │ 1738 2023-07-28 07:40:21 | ERROR |

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
