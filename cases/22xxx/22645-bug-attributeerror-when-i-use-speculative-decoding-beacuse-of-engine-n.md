# vllm-project/vllm#22645: [Bug]: AttributeError when I use speculative decoding beacuse of engine not available

| 字段 | 值 |
| --- | --- |
| Issue | [#22645](https://github.com/vllm-project/vllm/issues/22645) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError when I use speculative decoding beacuse of engine not available

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I still meet the AttributeError , because the post_init method of the dataclass is called before all necessary configuration from the engine is available. The CLI is vllm serve \ /workspace/models/Qwen2.5-VL-7B-Instruct \ --port 5580 --host 0.0.0.0 \ --max-num-seqs 128 --dtype bfloat16 --max-model-len=2048 \ --no-enable-prefix-caching --trust-remote-code\ --speculative-config '{"method": "eagle", "model": "/workspace/models/qwen2.5-vl-7b-eagle-sgl", "prefill_token_shift": false, "num_speculative_tokens": 5, "max_model_len": 2048}' \ --num-lookahead-slots=3 \ --max_num-batched_tokens=2048 \ --enforce-eager \ --gpu-memory-utilization=0.93 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -7B-Instruct \ --port 5580 --host 0.0.0.0 \ --max-num-seqs 128 --dtype bfloat16 --max-model-len=2048 \ --no-enable-prefix-caching --trust-remote-code\ --speculative-config '{"method": "eagle", "model": "/workspace/model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: use the post_init method of the dataclass is called before all necessary configuration from the engine is available. The CLI is vllm serve \ /workspace/models/Qwen2.5-VL-7B-Instruct \ --port 5580 --host 0.0.0.0 \ --max-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ": "/workspace/models/qwen2.5-vl-7b-eagle-sgl", "prefill_token_shift": false, "num_speculative_tokens": 5, "max_model_len": 2048}' \ --num-lookahead-slots=3 \ --max_num-batched_tokens=2048 \ --enforce-eager \ --gpu-memo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: AttributeError when I use speculative decoding beacuse of engine not available bug ### Your current environment ### 🐛 Describe the bug I still meet the AttributeError , because the post_init method of the datacla...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
