# vllm-project/vllm#39112: [Bug]: HFValidationError when loading model from cloud storage (s3://) with `HF_HUB_OFFLINE=1`

| 字段 | 值 |
| --- | --- |
| Issue | [#39112](https://github.com/vllm-project/vllm/issues/39112) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: HFValidationError when loading model from cloud storage (s3://) with `HF_HUB_OFFLINE=1`

### Issue 正文摘录

### Your current environment - vLLM version: 0.19.x (and earlier) - `runai_model_streamer` installed ### 🐛 Describe the bug When `HF_HUB_OFFLINE=1` is set and the model path is a cloud storage URI (`s3://`), vLLM raises an `HFValidationError` immediately on startup before any model loading begins: ``` huggingface_hub.errors.HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': 's3://my-bucket/my-model' is not a valid repo ID. ``` ### 📋 Steps to reproduce ```bash export HF_HUB_OFFLINE=1 vllm serve s3://my-bucket/my-model ``` ### Root cause `EngineArgs.__post_init__` unconditionally calls `get_model_path()` for **all** model paths when `HF_HUB_OFFLINE=1`. `get_model_path()` forwards the path straight to `huggingface_hub.snapshot_download(repo_id=...)`, which validates the string as a HF repo ID before even touching the cache — causing the crash. This happens **before `ModelConfig` is ever constructed**, so vLLM's existing cloud-storage machinery (`maybe_pull_model_tokenizer_for_runai`) never gets a chance to run. ```python # vllm/engine/arg_utils.py ← crash site if huggingface_hub.constants.HF_HUB_OFFLINE: self.model = get_model_path(self.model, self.r...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: HFValidationError when loading model from cloud storage (s3://) with `HF_HUB_OFFLINE=1` bug ### Your current environment - vLLM version: 0.19.x (and earlier) - `runai_model_streamer` installed ### 🐛 Describe the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: (s3://) with `HF_HUB_OFFLINE=1` bug ### Your current environment - vLLM version: 0.19.x (and earlier) - `runai_model_streamer` installed ### 🐛 Describe the bug When `HF_HUB_OFFLINE=1` is set and the model path is a clou...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ': 's3://my-bucket/my-model' is not a valid repo ID. ``` ### 📋 Steps to reproduce ```bash export HF_HUB_OFFLINE=1 vllm serve s3://my-bucket/my-model ``` ### Root cause `EngineArgs.__post_init__` unconditionally calls `g...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rror when loading model from S3 - #23684 — `HF_HUB_OFFLINE` + local path regression (introduced `get_model_path` call) - #23236, #24313, #26600 — S3 / RunAI breakage across minor vLLM releases

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
