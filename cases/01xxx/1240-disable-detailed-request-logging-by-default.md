# vllm-project/vllm#1240: Disable detailed request logging by default

| 字段 | 值 |
| --- | --- |
| Issue | [#1240](https://github.com/vllm-project/vllm/issues/1240) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Disable detailed request logging by default

### Issue 正文摘录

vLLM 0.2.0 logs all requests in detail by default, which produces excessive log output. While it is useful for bug investigation (if a full log is provided) this is a pain for regular use. Currently the way to turn this off is to pass the `--disable-log-requests` command line argument. I would suggest the following: - Disable logging of detailed request information by default - Deprecate the `--disable-log-requests` flag and change it to do nothing - Introduce a `--log-requests` flag to enable this feature on demand

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: I would suggest the following: - Disable logging of detailed request information by default - Deprecate the `--disable-log-requests` flag and change it to do nothing - Introduce a `--log-requests` flag to enable this fe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Disable detailed request logging by default vLLM 0.2.0 logs all requests in detail by default, which produces excessive log output. While it is useful for bug investigation (if a full log is provided) this is a pain for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
