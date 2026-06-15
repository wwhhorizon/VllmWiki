# vllm-project/vllm#43587: [Bug]: Prefix caching fails for incremental multimodal requests on Mamba-Attention hybrid models (Qwen3.5)

| 字段 | 值 |
| --- | --- |
| Issue | [#43587](https://github.com/vllm-project/vllm/issues/43587) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefix caching fails for incremental multimodal requests on Mamba-Attention hybrid models (Qwen3.5)

### Issue 正文摘录

### Your current environment vLLM version: 0.19.0 (V1 engine) Model: Qwen3.5-4B (Qwen3_5ForConditionalGeneration, Mamba-Attention hybrid / GDN + Attention) GPU: NVIDIA RTX A6000 OS: Linux (CentOS 8) ### 🐛 Describe the bug In a multi-turn agentic evaluation setting, each turn sends a prompt with one more image than the previous turn (incremental multimodal). Despite the shared prefix blocks having identical block hashes, num_cached_tokens is always 0. This issue is specific to the Mamba-Attention hybrid architecture. The same test with a pure-Attention model (Qwen3-VL-4B) works correctly. Details in document. [vllm_prefix_cache_issue.md](https://github.com/user-attachments/files/28214891/vllm_prefix_cache_issue.md) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#43628 [V1][Mamba] Opt-in granular prefill to fix align-mode prefix-cache misses on incremental requests (#43587)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Prefix caching fails for incremental multimodal requests on Mamba-Attention hybrid models (Qwen3.5) bug ### Your current environment vLLM version: 0.19.0 (V1 engine) Model: Qwen3.5-4B (Qwen3_5ForConditionalGenera...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Attention hybrid models (Qwen3.5) bug ### Your current environment vLLM version: 0.19.0 (V1 engine) Model: Qwen3.5-4B (Qwen3_5ForConditionalGeneration, Mamba-Attention hybrid / GDN + Attention) GPU: NVIDIA RTX A6000 OS:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: itionalGeneration, Mamba-Attention hybrid / GDN + Attention) GPU: NVIDIA RTX A6000 OS: Linux (CentOS 8) ### 🐛 Describe the bug In a multi-turn agentic evaluation setting, each turn sends a prompt with one more image tha...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: an the previous turn (incremental multimodal). Despite the shared prefix blocks having identical block hashes, num_cached_tokens is always 0. This issue is specific to the Mamba-Attention hybrid architecture. The same t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Prefix caching fails for incremental multimodal requests on Mamba-Attention hybrid models (Qwen3.5) bug ### Your current environment vLLM version: 0.19.0 (V1 engine) Model: Qwen3.5-4B (Qwen3_5ForConditionalGenera...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43628](https://github.com/vllm-project/vllm/pull/43628) | closes_keyword | 0.95 | [V1][Mamba] Opt-in granular prefill to fix align-mode prefix-cache misses on incremental requests (#43587) | Fixes #43587. In `mamba_cache_mode="align"` (the only prefix-caching mode Qwen3.5 supports), incremental multimodal / agentic multi-turn requests get `num_cached_tokens == 0` even |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
