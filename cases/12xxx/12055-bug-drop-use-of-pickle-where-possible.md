# vllm-project/vllm#12055: [Bug]: Drop use of pickle where possible

| 字段 | 值 |
| --- | --- |
| Issue | [#12055](https://github.com/vllm-project/vllm/issues/12055) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Drop use of pickle where possible

### Issue 正文摘录

### 🐛 Describe the bug vLLM uses pickle for serialization and sometimes also sends serialized objects over a local zeromq unix socket. Using pickle and any sort of network communication is a known dangerous combination, as it's an easy way to open a vulnerability to remote code execution on a host when a host deserializes pickled data. There have already been some changes to use [msgpack](https://github.com/msgpack/msgpack-python) instead. This issue is open to track the conversion away from using pickle where possible. Thank you to @avilum who responsibly reported this as a security report. We discussed it and concluded we did not see any path to exploit at this time. However, it is still an important weakness that should be addressed to improve vLLM security.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: .com/msgpack/msgpack-python) instead. This issue is open to track the conversion away from using pickle where possible. Thank you to @avilum who responsibly reported this as a security report. We discussed it and conclu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Drop use of pickle where possible bug;stale ### 🐛 Describe the bug vLLM uses pickle for serialization and sometimes also sends serialized objects over a local zeromq unix socket. Using pickle and any sort of netw...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
