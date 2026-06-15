# vllm-project/vllm#11929: [Bug]: Loading model from S3 using RunAI Model Streamer excludes too many files

| 字段 | 值 |
| --- | --- |
| Issue | [#11929](https://github.com/vllm-project/vllm/issues/11929) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Loading model from S3 using RunAI Model Streamer excludes too many files

### Issue 正文摘录

### Your current environment N/A ### Model Input Dumps N/A ### 🐛 Describe the bug Loading models from S3 with the RunAI model streamer excludes potentially required files in the bucket. For the model, only files matching `*config.json` [are pulled](https://github.com/vllm-project/vllm/blob/2339d59f9260499599d60599f83978fad1827999/vllm/config.py#L378). For the tokenizer, [all files that _aren't_ weight files are pulled](https://github.com/vllm-project/vllm/blob/2339d59f9260499599d60599f83978fad1827999/vllm/config.py#L384) (`.pt`, `.safetensors`, `.bin`) - the tokenizer is pulled to a different temporary directory though so this doesn't help if there are files required by the _model_ that don't match `*config.json`. This leads to problems when initializing models with files that don't match the `*config.json` pattern. For example, models that requires remote code (*.py) or chat templates. My suggestion would be to use the same ignore_pattern when pulling model files as when pulling tokenizer files - i.e. only exclude weight files. In other words, changing ```python self.s3_model.pull_files(model, allow_pattern=["*config.json"]) ``` to ```python self.s3_model.pull_files(model, ignore...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Loading model from S3 using RunAI Model Streamer excludes too many files bug;stale ### Your current environment N/A ### Model Input Dumps N/A ### 🐛 Describe the bug Loading models from S3 with the RunAI model str...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: l_files(model, ignore_pattern=["*.pt", "*.safetensors", "*.bin"]) ``` Incidentally, I think there might be another bug here in loading _the tokenizer from S3_ resulting from copy-pasting. ```python self.s3_tokenizer.pul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .** ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ing model from S3 using RunAI Model Streamer excludes too many files bug;stale ### Your current environment N/A ### Model Input Dumps N/A ### 🐛 Describe the bug Loading models from S3 with the RunAI model streamer exclu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
