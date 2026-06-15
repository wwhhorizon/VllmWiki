# vllm-project/vllm#6154: [Feature]: expose the tqdm progress bar to enable logging the progress

| 字段 | 值 |
| --- | --- |
| Issue | [#6154](https://github.com/vllm-project/vllm/issues/6154) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: expose the tqdm progress bar to enable logging the progress

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am running vLLM on aws batch on large datasets and would like to see the progress of the jobs, this is currently not possible. however [tqdm-loggable](https://pypi.org/project/tqdm-loggable/) does enable this, but then I would need to swap the tqdm driver in the llm_engine, this is however not exposed. so my request would be either to move to tqdm-loggable since it automatically switches given a interactive vs non-interactive environment. Or expose tqdm such that the user can swap it themselves. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: re]: expose the tqdm progress bar to enable logging the progress feature request;stale ### 🚀 The feature, motivation and pitch I am running vLLM on aws batch on large datasets and would like to see the progress of the j...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
