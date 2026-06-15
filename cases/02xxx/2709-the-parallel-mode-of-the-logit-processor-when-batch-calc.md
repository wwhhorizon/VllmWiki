# vllm-project/vllm#2709: The parallel mode of the logit processor when batch calc 

| 字段 | 值 |
| --- | --- |
| Issue | [#2709](https://github.com/vllm-project/vllm/issues/2709) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The parallel mode of the logit processor when batch calc 

### Issue 正文摘录

I encountered performance issues when conducting batch calculations because my logit processor involves CPU-intensive computing, and the logit processor is called serially for elements within the batch. For instance, for a single call to the generate method, which generates 300 output tokens (meaning the logit processor is invoked 300 times) ，my logit processor takes about 0.7 seconds. However, when I perform batch operations, such as with a batch size of 50, the time taken jumps from 0.7 to 0.7*50=35 seconds, which is extremely excessive. Therefore, I attempted to convert the for loop here into parallel processing by using ProcessPoolExecutor, but I found that multiprocessing is ineffective during the execution of llm.generate, as the logit processor still executes serially. I'm not sure what restrictions might exist during the execution of llm.generate that prevent multiprocessing within the _apply_logits_processors method. Of course, if the author could help modify this to make it parallel, that would be great. _Please note that using ThreadPoolExecutor will not improve efficiency, because it involves CPU-intensive tasks. Therefore, I can only attempt to use ProcessPoolExecutor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: great. _Please note that using ThreadPoolExecutor will not improve efficiency, because it involves CPU-intensive tasks. Therefore, I can only attempt to use ProcessPoolExecutor in Python._ ![image](https://github.com/vl...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
