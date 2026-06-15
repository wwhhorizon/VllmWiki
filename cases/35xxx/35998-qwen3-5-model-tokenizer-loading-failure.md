# vllm-project/vllm#35998: Qwen3.5 Model Tokenizer Loading Failure

| 字段 | 值 |
| --- | --- |
| Issue | [#35998](https://github.com/vllm-project/vllm/issues/35998) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Qwen3.5 Model Tokenizer Loading Failure

### Issue 正文摘录

**Environment** - vLLM version: 0.16.0rc2.dev376+gf4af642a6 (qwen3_5-cu130) and 0.16.1rc1.dev48+ga572baff5 (nightly) - Docker image: vllm/vllm-openai:qwen3_5-cu130 and vllm/vllm-openai:nightly - Host environment: Linux, CUDA 13.0 - Python version: 3.12 **Reproduction Steps** 1. Pull the Qwen3.5-4B model from HuggingFace: ```bash huggingface-cli download Qwen/Qwen3.5-4B --local-dir /data/models/Qwen3.5-4B ``` 2. Try to run with vLLM: ```bash docker run --gpus device=7 \ -v /data/models:/data/models \ -p 8000:8000 \ -e HF_TOKEN=xxx \ vllm/vllm-openai:qwen3_5-cu130 \ --model /data/models/Qwen3.5-4B \ --dtype bfloat16 \ --host 0.0.0.0 \ --port 8000 ``` **Expected Behavior** Model should load and start the API server. **Actual Error** ``` RuntimeError: Failed to load the tokenizer. If the tokenizer is a custom tokenizer not yet available in the HuggingFace transformers library, consider setting `trust_remote_code=True` in LLM or using the `--trust-remote-code` flag in the CLI. ``` Full stack trace: ``` ValueError: Tokenizer class TokenizersBackend does not exist or is not currently imported. ``` **Model Details** - Model: Qwen/Qwen3.5-4B (HuggingFace) - Config: model_type: qwen3_5 - Tr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Qwen3.5 Model Tokenizer Loading Failure **Environment** - vLLM version: 0.16.0rc2.dev376+gf4af642a6 (qwen3_5-cu130) and 0.16.1rc1.dev48+ga572baff5 (nightly) - Docker image: vllm/vllm-openai:qwen3_5-cu130 and vllm/vllm-o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Qwen3.5 Model Tokenizer Loading Failure **Environment** - vLLM version: 0.16.0rc2.dev376+gf4af642a6 (qwen3_5-cu130) and 0.16.1rc1.dev48+ga572baff5 (nightly) - Docker image: vllm/vllm-openai:qwen3_5-cu130 and vllm/vllm-op
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: vllm/vllm-openai:qwen3_5-cu130 \ --model /data/models/Qwen3.5-4B \ --dtype bfloat16 \ --host 0.0.0.0 \ --port 8000 ``` **Expected Behavior** Model should load and start the API server. **Actual Error** ``` RuntimeError:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: he CLI. ``` Full stack trace: ``` ValueError: Tokenizer class TokenizersBackend does not exist or is not currently imported. ``` **Model Details** - Model: Qwen/Qwen3.5-4B (HuggingFace) - Config: model_type: qwen3_5 - T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ai:qwen3_5-cu130 and vllm/vllm-openai:nightly - Host environment: Linux, CUDA 13.0 - Python version: 3.12 **Reproduction Steps** 1. Pull the Qwen3.5-4B model from HuggingFace: ```bash huggingface-cli download Qwen/Qwen3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
