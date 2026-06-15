# vllm-project/vllm#1127: vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. 

| 字段 | 值 |
| --- | --- |
| Issue | [#1127](https://github.com/vllm-project/vllm/issues/1127) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. 

### Issue 正文摘录

I am receiving this error: vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. This should never happen! Please open an issue on Github. See stack trace above for the actual cause. with simple quickstart guide: `python3 -m vllm.entrypoints.openai.api_server --model facebook/opt-125m`

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: quickstart guide: `python3 -m vllm.entrypoints.openai.api_server --model facebook/opt-125m`

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
