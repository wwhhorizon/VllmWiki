# vllm-project/vllm#40616: [Bug]:  `/v2/embed` with `input_type` returns misleading 400 on nemotron-embed-vl

| 字段 | 值 |
| --- | --- |
| Issue | [#40616](https://github.com/vllm-project/vllm/issues/40616) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  `/v2/embed` with `input_type` returns misleading 400 on nemotron-embed-vl

### Issue 正文摘录

### Your current environment n/a - not an env specifc issue ### 🐛 Describe the bug # [Bug] `/v2/embed` with `input_type` returns misleading 400 on nemotron-embed-vl ## Summary The Cohere `/v2/embed` path synthesizes `[system, user]` messages internally when `input_type` maps to a `task_instructions` prefix (#38362). Chat templates that guard against `messages | length > 1` then reject this 2-message input with an error that\ reads like a caller-side problem. Today this breaks `nvidia/llama-nemotron-embed-vl-1b-v2`. ## Reproducer ```bash vllm serve nvidia/llama-nemotron-embed-vl-1b-v2 \ --trust-remote-code --max-model-len 10240 \ --chat-template examples/pooling/embed/template/nemotron_embed_vl.jinja ``` ```bash curl -sS -X POST http://localhost:8000/v2/embed \ -H "Content-Type: application/json" \ -d '{ "model": "nvidia/llama-nemotron-embed-vl-1b-v2", "texts": ["machine learning", "the cat sat on the mat"], "input_type": "query", "embedding_types": ["float"] }' ``` ```json {"error":{"message":"Embedding models should only embed one message at a time","type":"BadRequestError","code":400}} ``` ## Root cause `EmbedIOProcessor._mixed_input_to_messages` (`vllm/entrypoints/pooling/embed...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: error that\ reads like a caller-side problem. Today this breaks `nvidia/llama-nemotron-embed-vl-1b-v2`. ## Reproducer ```bash vllm serve nvidia/llama-nemotron-embed-vl-1b-v2 \ --trust-remote-code --max-model-len 10240 \...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Future multimodal embedding models that declare `task_instructions` and ship with a guarded template will break on arrival. ## Proposed direction Move the multi-message policy out of jinja and into `EmbedIOProcessor`. D...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nemotron-embed-vl bug ### Your current environment n/a - not an env specifc issue ### 🐛 Describe the bug # [Bug] `/v2/embed` with `input_type` returns misleading 400 on nemotron-embed-vl ## Summary The Cohere `/v2/embed...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: e problem. Today this breaks `nvidia/llama-nemotron-embed-vl-1b-v2`. ## Reproducer ```bash vllm serve nvidia/llama-nemotron-embed-vl-1b-v2 \ --trust-remote-code --max-model-len 10240 \ --chat-template examples/pooling/e...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: a` silently concatenates multi-message input for CLIP/Siglip/ColPali/PaliGemma/Chameleon, which is a separate footgun that may deserve its own issue. ## Out of scope Changing the `/v1/embeddings` `messages` contract (si...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
