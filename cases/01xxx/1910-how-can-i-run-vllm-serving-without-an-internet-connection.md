# vllm-project/vllm#1910: How can I run VLLM serving without an internet connection?

| 字段 | 值 |
| --- | --- |
| Issue | [#1910](https://github.com/vllm-project/vllm/issues/1910) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How can I run VLLM serving without an internet connection?

### Issue 正文摘录

### Discussed in https://github.com/vllm-project/vllm/discussions/1405 Originally posted by **ZPerling** October 18, 2023 I cloned the model repository on Hugging Face to my local machine and used the `--download-dir` parameter to specify the directory. However, when running VLLM, it still tries to connect to Hugging Face, which doesn't work without an internet connection. Even after setting `export HF_HUB_OFFLINE=1`, offline mode doesn't seem to be working. Is it possible to run VLLM offline and if so, how can I achieve this?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 05 Originally posted by **ZPerling** October 18, 2023 I cloned the model repository on Hugging Face to my local machine and used the `--download-dir` parameter to specify the directory. However, when running VLLM, it st...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: g Face to my local machine and used the `--download-dir` parameter to specify the directory. However, when running VLLM, it still tries to connect to Hugging Face, which doesn't work without an internet connection. Even...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
