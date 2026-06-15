# vllm-project/vllm#17468: [Bug]: `v0.8.5`: Special tokens (`<think>`, `</think>`) are split during streaming with Qwen3-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#17468](https://github.com/vllm-project/vllm/issues/17468) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `v0.8.5`: Special tokens (`<think>`, `</think>`) are split during streaming with Qwen3-FP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving the Qwen3-FP8 model using vLLM v0.8.5 and enabling streaming output, special tokens like and (used for reasoning steps) are not treated as atomic units. Instead, they are often split across multiple streamed chunks. This issue occurs both when running the server with the basic command: ``` vllm serve Qwen/Qwen3-8B-FP8 ``` ``` vllm serve Qwen/Qwen3-8B-FP8 --enable-reasoning --reasoning-parser deepseek_r1 ``` ### Steps to Reproduce: 1. Install vLLM `v0.8.5`. 2. Start the vLLM server using either of the commands mentioned above. 3. Send a request to the server's generation endpoint (e.g., `/v1/chat/completions` or `/generate`) with stream=True. Use a prompt that is likely to cause the Qwen/Qwen3-8B model to output ` `...` ` blocks. ### Expected Behavior: Special tokens like and should be treated as atomic units by the tokenizer/detokenizer during streaming. Each special token should be contained entirely within a single streamed chunk. Example of expected chunk sequence: Chunk 1: ` ` Chunk 2: \n Chunk 3: Okay Chunk 4: \n Chunk 5: ` ` Chunk 6: ...final answer... ### Actual Behavior: The special tokens are split across ch...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: `v0.8.5`: Special tokens (`<think>`, `</think>`) are split during streaming with Qwen3-FP8 bug ### Your current environment ### 🐛 Describe the bug When serving the Qwen3-FP8 model using vLLM v0.8.5 and enabling s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: : Special tokens (`<think>`, `</think>`) are split during streaming with Qwen3-FP8 bug ### Your current environment ### 🐛 Describe the bug When serving the Qwen3-FP8 model using vLLM v0.8.5 and enabling streaming output...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: -FP8 --enable-reasoning --reasoning-parser deepseek_r1 ``` ### Steps to Reproduce: 1. Install vLLM `v0.8.5`. 2. Start the vLLM server using either of the commands mentioned above. 3. Send a request to the server's gener...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ial tokens (`<think>`, `</think>`) are split during streaming with Qwen3-FP8 bug ### Your current environment ### 🐛 Describe the bug When serving the Qwen3-FP8 model using vLLM v0.8.5 and enabling streaming output, spec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ... ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
