# vllm-project/vllm#13822: [Usage]:  MLA disable prefix cache

| 字段 | 值 |
| --- | --- |
| Issue | [#13822](https://github.com/vllm-project/vllm/issues/13822) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  MLA disable prefix cache

### Issue 正文摘录

### Your current environment When using MLA, the prefix cache will be automatically disabled(https://github.com/vllm-project/vllm/blob/v0.7.3/vllm/config.py#L3328). However, when this content is commented out, the prefix cache will work normally. What is the reason for disabling the prefix cache here? My startup command is as follows： `python3 -m vllm.entrypoints.openai.api_server --model /data00/models/DeepSeek-R1 --port 8000 --enable-prefix-caching --gpu-memory-utilization 0.98 --max-model-len 1024 -tp 8`

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: matically disabled(https://github.com/vllm-project/vllm/blob/v0.7.3/vllm/config.py#L3328). However, when this content is commented out, the prefix cache will work normally. What is the reason for disabling the prefix ca...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: MLA disable prefix cache usage ### Your current environment When using MLA, the prefix cache will be automatically disabled(https://github.com/vllm-project/vllm/blob/v0.7.3/vllm/config.py#L3328). However, when...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
