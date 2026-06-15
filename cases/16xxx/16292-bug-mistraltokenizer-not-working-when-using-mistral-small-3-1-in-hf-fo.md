# vllm-project/vllm#16292: [Bug]: MistralTokenizer not working when using Mistral Small 3.1 in HF format

| 字段 | 值 |
| --- | --- |
| Issue | [#16292](https://github.com/vllm-project/vllm/issues/16292) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 |  |
| Operator 关键词 | fp8 |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MistralTokenizer not working when using Mistral Small 3.1 in HF format

### Issue 正文摘录

### Your current environment vLLM v0.8.3 ### 🐛 Describe the bug vLLM v0.8.3 fails on start when using Mistral Small 3.1 in HF format and the mistral tokenizer (required for proper function calling parsing) Launch command : `docker run --runtime nvidia --gpus all -v /path/models:/models -e HF_CACHE=/models --ipc=host vllm/vllm-openai:v0.8.3 --model /models/Mistral-Small-3.1-24B-Instruct-2503-FP8-KV --download-dir /models --kv-cache-dtype fp8 --limit_mm_per_prompt 'image=10' --max-model-len 65536 --enable-auto-tool-choice --tool-call-parser mistral --tokenizer-mode mistral` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: MistralTokenizer not working when using Mistral Small 3.1 in HF format bug ### Your current environment vLLM v0.8.3 ### 🐛 Describe the bug vLLM v0.8.3 fails on start when using Mistral Small 3.1 in HF format and...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nizer (required for proper function calling parsing) Launch command : `docker run --runtime nvidia --gpus all -v /path/models:/models -e HF_CACHE=/models --ipc=host vllm/vllm-openai:v0.8.3 --model /models/Mistral-Small-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: m/vllm-openai:v0.8.3 --model /models/Mistral-Small-3.1-24B-Instruct-2503-FP8-KV --download-dir /models --kv-cache-dtype fp8 --limit_mm_per_prompt 'image=10' --max-model-len 65536 --enable-auto-tool-choice --tool-call-pa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: MistralTokenizer not working when using Mistral Small 3.1 in HF format bug ### Your current environment vLLM v0.8.3 ### 🐛 Describe the bug vLLM v0.8.3 fails on start when using Mistral Small 3.1 in HF format and...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: dels/Mistral-Small-3.1-24B-Instruct-2503-FP8-KV --download-dir /models --kv-cache-dtype fp8 --limit_mm_per_prompt 'image=10' --max-model-len 65536 --enable-auto-tool-choice --tool-call-parser mistral --tokenizer-mode mi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
