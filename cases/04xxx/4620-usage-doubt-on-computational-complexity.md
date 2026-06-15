# vllm-project/vllm#4620: [Usage]: doubt on computational complexity

| 字段 | 值 |
| --- | --- |
| Issue | [#4620](https://github.com/vllm-project/vllm/issues/4620) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: doubt on computational complexity

### Issue 正文摘录

TODO: The current hashing function is O(L^2). We should optimize this in the future. return hash((tuple(self.data.get_token_ids()[0:num_tokens]), self.lora_int_id)) May I ask why is O(L^2) here?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
