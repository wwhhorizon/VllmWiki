# vllm-project/vllm#1878: ChatGLM2-6B-32K使用vllm激素，外挂知识库后内容重复生成问题，如何解决

| 字段 | 值 |
| --- | --- |
| Issue | [#1878](https://github.com/vllm-project/vllm/issues/1878) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ChatGLM2-6B-32K使用vllm激素，外挂知识库后内容重复生成问题，如何解决

### Issue 正文摘录

我使用了vllm对ChatGLM2-6B-32K进行加速，然后外挂了milvus向量数据库。生成过程中，发现进行长文本交互过程中，出现了内容重复生成的问题。 ![vllm重复生成](https://github.com/vllm-project/vllm/assets/49576528/5834e3f2-c167-4c2c-ae57-8a93fda31dbb)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
