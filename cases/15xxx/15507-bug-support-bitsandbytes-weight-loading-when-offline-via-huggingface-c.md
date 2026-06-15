# vllm-project/vllm#15507: [Bug]: Support Bitsandbytes weight loading when offline (via huggingface cache)

| 字段 | 值 |
| --- | --- |
| Issue | [#15507](https://github.com/vllm-project/vllm/issues/15507) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Support Bitsandbytes weight loading when offline (via huggingface cache)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Bitsandbytes quantized models use a different model loader than normal models. For prequantized models (e.g. unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit) this fails to load when operating in a restricted environment (HF_HUB_OFFLINE=1). In these cases model weights may already be available via the huggingface cache mechanism (e.g. loading meta-llama/Meta-Llama-3.1-8B-Instruct in the same environment works fine). Tracing the code path shows a custom HfApi call when loading bitsandbytes that isnt present for normal huggingface reference resolution (huggingface download methods are cache aware and will attempt to load locally when offline, but the api call will fail with an offline error) https://github.com/vllm-project/vllm/blob/ebcebeeb6b632c7e0f25fbf9ebc42f458b594fe1/vllm/model_executor/model_loader/loader.py#L796 code: ```python # download to cache to simulate offline behavior from huggingface_hub import snapshot_download for model_id in ("unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit", "meta-llama/Meta-Llama-3.1-8B-Instruct"): snapshot_download(repo_id=model_id, revision="main", ignore_patterns="original/*") ``` ```python # simula...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Support Bitsandbytes weight loading when offline (via huggingface cache) bug;stale ### Your current environment ### 🐛 Describe the bug Bitsandbytes quantized models use a different model loader than normal models...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: lama/Meta-Llama-3.1-8B-Instruct in the same environment works fine). Tracing the code path shows a custom HfApi call when loading bitsandbytes that isnt present for normal huggingface reference resolution (huggingface d...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: model weights may already be available via the huggingface cache mechanism (e.g. loading meta-llama/Meta-Llama-3.1-8B-Instruct in the same environment works fine). Tracing the code path shows a custom HfApi call when lo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: le ### Your current environment ### 🐛 Describe the bug Bitsandbytes quantized models use a different model loader than normal models. For prequantized models (e.g. unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit) this fails...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: fferent model loader than normal models. For prequantized models (e.g. unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit) this fails to load when operating in a restricted environment (HF_HUB_OFFLINE=1). In these cases model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
