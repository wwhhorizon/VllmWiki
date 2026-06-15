# vllm-project/vllm#27819: [Bug]: Google Storage broken in Run:ai model streamer

| 字段 | 值 |
| --- | --- |
| Issue | [#27819](https://github.com/vllm-project/vllm/issues/27819) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Google Storage broken in Run:ai model streamer

### Issue 正文摘录

### Your current environment vllm/vllm-openai/[nightly-8bff831f0aa239006f34b721e63e1340e3472067](https://hub.docker.com/layers/vllm/vllm-openai/nightly-8bff831f0aa239006f34b721e63e1340e3472067/images/sha256-ef112680ed30e4b9d7bf794dcda4abd829e9405a73e013f9e046658cf22d0577) ### 🐛 Describe the bug PR #27308 introduced a bug that breaks the Google cloud storage integration when using the Run:ai model streamer. The bug is because of method[ is_s3](https://github.com/vllm-project/vllm/blob/33a0ea5f3264b5b2f571b8a53357e10efcc94670/vllm/transformers_utils/utils.py#L18) which is used [here](https://github.com/vllm-project/vllm/blob/60f76baa6688ce265a4205f183bd42a62d8f7179/vllm/engine/arg_utils.py#L1303C8-L1312C14) It is only checking S3:// path when gs:// is also a valid path

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lm-openai/[nightly-8bff831f0aa239006f34b721e63e1340e3472067](https://hub.docker.com/layers/vllm/vllm-openai/nightly-8bff831f0aa239006f34b721e63e1340e3472067/images/sha256-ef112680ed30e4b9d7bf794dcda4abd829e9405a73e013f9...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Google Storage broken in Run:ai model streamer bug ### Your current environment vllm/vllm-openai/[nightly-8bff831f0aa239006f34b721e63e1340e3472067](https://hub.docker.com/layers/vllm/vllm-openai/nightly-8bff831f0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
