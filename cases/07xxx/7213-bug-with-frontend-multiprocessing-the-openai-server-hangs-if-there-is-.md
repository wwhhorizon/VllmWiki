# vllm-project/vllm#7213: [Bug]: With frontend multiprocessing the openai server hangs if there is an initialization error

| 字段 | 值 |
| --- | --- |
| Issue | [#7213](https://github.com/vllm-project/vllm/issues/7213) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: With frontend multiprocessing the openai server hangs if there is an initialization error

### Issue 正文摘录

### Your current environment The environment is not relevant for this issue. ### 🐛 Describe the bug With frontend multiprocessing, if there is an error in the initialization if the LLMEngine, the server prints the stack trace and then hangs and has to be killed. The expected behavior is that the server would exit, ideally with a non-zero status. Reproducing this error is pretty simple. Just add `raise Exception("foo")` at the first line of `AsyncLLEngine.from_engine_args()`. Passing `--disable-frontend-multiprocessing` makes this problem go away.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: r is that the server would exit, ideally with a non-zero status. Reproducing this error is pretty simple. Just add `raise Exception("foo")` at the first line of `AsyncLLEngine.from_engine_args()`. Passing `--disable-fro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
