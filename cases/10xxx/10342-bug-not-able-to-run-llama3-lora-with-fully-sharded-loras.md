# vllm-project/vllm#10342: [Bug]: Not able to run LLama3 LoRA with --fully-sharded-loras

| 字段 | 值 |
| --- | --- |
| Issue | [#10342](https://github.com/vllm-project/vllm/issues/10342) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Not able to run LLama3 LoRA with --fully-sharded-loras

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I got the following error when running LoRA: `RuntimeError('Error in model execution: The size of tensor a (16) must match the size of tensor b (64) at non-singleton dimension 0')` Steps to reproduce: I followed the steps in https://github.com/vllm-project/vllm/blob/main/docs/source/models/lora.rst ``` from huggingface_hub import snapshot_download snapshot_download(repo_id="UnderstandLing/Llama-3-8B-Instruct-fr") ``` ``` vllm serve unsloth/llama-3-8b-Instruct \ --tensor-parallel-size 4 \ --enable-lora \ --lora-modules french=/tmp/.cache/huggingface/hub/models--UnderstandLing--Llama-3-8B-Instruct-fr/snapshots/0752aa9d84072112b0e59daac788bf9d8a942e50 \ --max-lora-rank 64 \ --fully-sharded-loras ``` Request: ``` curl http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "french", "prompt": "San Francisco is a", "max_tokens": 32, "temperature": 0 }' ``` Stacktrace: ``` ERROR 11-14 13:38:14 engine.py:158] Traceback (most recent call last): ERROR 11-14 13:38:14 engine.py:158] File "/usr/local/lib/python3.12/dist-packages/vllm/worker/model_runner_base.py", line 11...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ect/vllm/blob/main/docs/source/models/lora.rst ``` from huggingface_hub import snapshot_download snapshot_download(repo_id="UnderstandLing/Llama-3-8B-Instruct-fr") ``` ``` vllm serve unsloth/llama-3-8b-Instruct \ --tens...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Not able to run LLama3 LoRA with --fully-sharded-loras bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I got the following error when running LoRA: `RuntimeError('Error...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: d(repo_id="UnderstandLing/Llama-3-8B-Instruct-fr") ``` ``` vllm serve unsloth/llama-3-8b-Instruct \ --tensor-parallel-size 4 \ --enable-lora \ --lora-modules french=/tmp/.cache/huggingface/hub/models--UnderstandLing--Ll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 88bf9d8a942e50 \ --max-lora-rank 64 \ --fully-sharded-loras ``` Request: ``` curl http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "french", "prompt": "San Francisco is a", "ma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
