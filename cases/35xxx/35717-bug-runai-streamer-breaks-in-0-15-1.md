# vllm-project/vllm#35717: [Bug]: RunAI streamer breaks in 0.15.1

| 字段 | 值 |
| --- | --- |
| Issue | [#35717](https://github.com/vllm-project/vllm/issues/35717) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: RunAI streamer breaks in 0.15.1

### Issue 正文摘录

### Your current environment vLLM 0.15.1 ### 🐛 Describe the bug vLLM 0.15.1 + --load-format runai_streamer fails for S3 models (qwen-embedding-8b / qwen-tts): local cache path validated as HuggingFace repo_id When using Run:AI Model Streamer with vLLM 0.15.1 and models stored in S3 (e.g. qwen-embedding-8b, qwen-tts), vllm serve crashes during engine initialization with a Pydantic ValidationError. It appears that after streaming, the local cache path is being validated as a HuggingFace repo_id, which causes the failure. Start: ```python vllm serve s3://vllm-models/qwen-embedding --load-format runai_streamer ``` Logs: ``` python INFO 02-27 04:53:36 [utils.py:261] non-default args: {... 'model': 's3://vllm-models/qwen-embedding', 'load_format': 'runai_streamer', ...} ... INFO credentials.py:1252: Found credentials in environment variables. INFO configprovider.py:994: Found endpoint for s3 via: environment_global. INFO 02-27 04:53:43 [config.py:772] Found sentence-transformers modules configuration. Traceback (most recent call last): ... File "/usr/local/lib/python3.12/dist-packages/vllm/engine/arg_utils.py", line 1228, in create_model_config return ModelConfig( ... pydantic_core._pyd...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: t environment vLLM 0.15.1 ### 🐛 Describe the bug vLLM 0.15.1 + --load-format runai_streamer fails for S3 models (qwen-embedding-8b / qwen-tts): local cache path validated as HuggingFace repo_id When using Run:AI Model S...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
