# vllm-project/vllm#3858: [Bug] PyNCCL errors at termination

| 字段 | 值 |
| --- | --- |
| Issue | [#3858](https://github.com/vllm-project/vllm/issues/3858) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] PyNCCL errors at termination

### Issue 正文摘录

> > The model executes correctly but gives this error at the end. Does any one know what might be the issue? > > ``` > > Exception ignored in: > > Traceback (most recent call last): > > File "/workspace/vllm/vllm/model_executor/parallel_utils/pynccl.py", line 264, in __del__ > > TypeError: 'NoneType' object is not callable > > ``` > > Is this error related this PR? If not, you can submit a new issue with detail env and error info. Yup, it's related to the changes I've made. _Originally posted by @saurabhdash2512 in https://github.com/vllm-project/vllm/issues/3829#issuecomment-2037224229_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug] PyNCCL errors at termination > > The model executes correctly but gives this error at the end. Does any one know what might be the issue? > > ``` > > Exception ignored in: > > Traceback (most recent call last): >...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
