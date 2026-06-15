# vllm-project/vllm#13485: [Bug]: HFValidation

| 字段 | 值 |
| --- | --- |
| Issue | [#13485](https://github.com/vllm-project/vllm/issues/13485) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: HFValidation

### Issue 正文摘录

### Your current environment Hi, I'm trying to run vllm while loading the model from a s3 compatible storage. Using the official image tag v0.6.6 I have defined following env vars: AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_ENDPOINT_URL AWS_EC2_METADATA_DISABLED=true RUNAI_STREAMER_S3_ENDPOINT RUNAI_STREAMER_S3_USE_VIRTUAL_ADDRESSING=0 ### 🐛 Describe the bug I'm running the following command: `vllm serve s3://vllm-phi35 --load-format runai_streamer` And I get the following error: ``` huggingface_hub.errors/HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/tmp/tmp8px3pe24' . Use `repo_type` argument if needed. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: HFValidation bug;stale ### Your current environment Hi, I'm trying to run vllm while loading the model from a s3 compatible storage. Using the official image tag v0.6.6 I have defined following env vars: AWS_ACCE...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: llm while loading the model from a s3 compatible storage. Using the official image tag v0.6.6 I have defined following env vars: AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_ENDPOINT_URL AWS_EC2_METADATA_DISABLED=true RU...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: vars: AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_ENDPOINT_URL AWS_EC2_METADATA_DISABLED=true RUNAI_STREAMER_S3_ENDPOINT RUNAI_STREAMER_S3_USE_VIRTUAL_ADDRESSING=0 ### 🐛 Describe the bug I'm running the following comman...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: HFValidation bug;stale ### Your current environment Hi, I'm trying to run vllm while loading the model from a s3 compatible storage. Using the official image tag v0.6.6 I have defined following env vars: AWS_ACCE...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
