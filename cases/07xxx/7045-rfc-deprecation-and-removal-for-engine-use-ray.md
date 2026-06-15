# vllm-project/vllm#7045: [RFC]: Deprecation and removal for `--engine-use-ray`

| 字段 | 值 |
| --- | --- |
| Issue | [#7045](https://github.com/vllm-project/vllm/issues/7045) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Deprecation and removal for `--engine-use-ray`

### Issue 正文摘录

### Motivation. In the `async_engine` code path, we have an option to launch the engine in a separate process using Ray ```python parser.add_argument('--engine-use-ray', action='store_true', help='Use Ray to start the LLM engine in a ' 'separate process as the server process ``` Originally, the option make it possible to separate the server's Python overhead with the engine's main scheduler loop. However, few factors made this unused/less popular * Ray is an optional component, and typically not used in single node environment. * The serialization and rpc typically offset the theoretical performance gain * There are typically other ways to isolate server and engine (through multiprocessing, threading, etc). * Recently, we are separating this in server using lower overhead approaches #6883 ### Proposed Change. Deprecation of the flag with warning for one release. Removal of the flag given no major pushbacks. ### Feedback Period. 1wk ### CC List. _No response_ ### Any Other Things. _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: possible to separate the server's Python overhead with the engine's main scheduler loop. However, few factors made this unused/less popular * Ray is an optional component, and typically not used in single node environme...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
