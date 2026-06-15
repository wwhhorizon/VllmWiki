# vllm-project/vllm#28861: [Bug]: bad_words ineffective for n > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#28861](https://github.com/vllm-project/vllm/issues/28861) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: bad_words ineffective for n > 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I found that another user reported back in May that bad_words is ineffective for n > 1. https://github.com/vllm-project/vllm/issues/18767#event-19955388050 Running model Qwen3 235B A22B Instruct 2507, I run a VLLM request to v1/chat/completions as: `{ "n": 3, "bad_words": [ "Mmm" ], "seed": 1588207426, "model": "Big-Q", "return_token_ids": true, "top_k": 20, "messages": [ { "role": "system", "content": " " } ], "temperature": 0.7, "presence_penalty": 0, "frequency_penalty": 0, "repetition_penalty": 1, "add_prefix_space": true, "add_special_tokens": false }` However, the generated response, also contains "Mmm". Initially I suspected the tokenizer finding a different way to come up with the word "Mmm", however I verified with: ""return_token_ids": true," in my request, Tokens returned were: "44", "3821", "11", Then I did a call to /tokenizer with "Mmm", which also returns "44", "3821", "11", ruling out the suspected tokenizer issue. Since I have had a different but similar problem with high n count on an old version of VLLM before, my instinct was to try n = 1, and then bad_words worked right away: "Mmm" disappeared and was replace...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ty": 0, "repetition_penalty": 1, "add_prefix_space": true, "add_special_tokens": false }` However, the generated response, also contains "Mmm". Initially I suspected the tokenizer finding a different way to come up with...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s://github.com/vllm-project/vllm/issues/18767#event-19955388050 Running model Qwen3 235B A22B Instruct 2507, I run a VLLM request to v1/chat/completions as: `{ "n": 3, "bad_words": [ "Mmm" ], "seed": 1588207426, "model"...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 1. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ition_penalty": 1, "add_prefix_space": true, "add_special_tokens": false }` However, the generated response, also contains "Mmm". Initially I suspected the tokenizer finding a different way to come up with the word "Mmm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t-19955388050 Running model Qwen3 235B A22B Instruct 2507, I run a VLLM request to v1/chat/completions as: `{ "n": 3, "bad_words": [ "Mmm" ], "seed": 1588207426, "model": "Big-Q", "return_token_ids": true, "top_k": 20,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
