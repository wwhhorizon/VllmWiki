# vllm-project/vllm#43446: [Doc]: VLLM_USE_FASTOKENS=1

| 字段 | 值 |
| --- | --- |
| Issue | [#43446](https://github.com/vllm-project/vllm/issues/43446) |
| 状态 | open |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: VLLM_USE_FASTOKENS=1

### Issue 正文摘录

### 📚 The doc issue https://docs.vllm.ai/en/latest/configuration/optimization/#batch-level-dp-for-multi-modal-encoders states: _Input Processing¶ fastokens Backend¶ By default vLLM uses the standard Hugging Face tokenizers library to power the fast tokenizer. For BPE tokenizers (Qwen, Llama, DeepSeek, GPT-OSS, etc.) you can switch to the fastokens Rust backend, a drop-in replacement that's substantially faster on encode/decode and on streaming detokenization. Enable it by setting VLLM_USE_FASTOKENS=1:_ But there is no VLLM_USE_FASTOKENS in recent versions of vllm ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: KENS=1 documentation ### 📚 The doc issue https://docs.vllm.ai/en/latest/configuration/optimization/#batch-level-dp-for-multi-modal-encoders states: _Input Processing¶ fastokens Backend¶ By default vLLM uses the standard...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: h-level-dp-for-multi-modal-encoders states: _Input Processing¶ fastokens Backend¶ By default vLLM uses the standard Hugging Face tokenizers library to power the fast tokenizer. For BPE tokenizers (Qwen, Llama, DeepSeek,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ing VLLM_USE_FASTOKENS=1:_ But there is no VLLM_USE_FASTOKENS in recent versions of vllm ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched fo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ust backend, a drop-in replacement that's substantially faster on encode/decode and on streaming detokenization. Enable it by setting VLLM_USE_FASTOKENS=1:_ But there is no VLLM_USE_FASTOKENS in recent versions of vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
