# vllm-project/vllm#27414: [Bug]: LongRoPE transition causes random outputs mid-sequence in Phi-3.5

| 字段 | 值 |
| --- | --- |
| Issue | [#27414](https://github.com/vllm-project/vllm/issues/27414) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: LongRoPE transition causes random outputs mid-sequence in Phi-3.5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While serving `microsoft/Phi-3.5-mini-instruct` (or any other model with LongRoPE), concurrent requests end up with random token outputs after the LongRoPE transition point from short factor to long factor, in this case, 4K tokens. When a prompt starts below the ~4K transition boundary and continues generating past it, the model switches from the short to long scaling factors mid-sequence. This causes the previous KV-cache to become invalid for the long-format scales, resulting in random tokens beyond that point, since it was encoded with different RoPE parameters. Synchronous requests aren’t affected because they use consistent scaling without shared cache states. The only current workaround is to modify the model’s config.json to either set the long factor scales equal to the short factor or set the short factor equal to the long factor. This removes the changing scales at the transition point, ensuring consistency throughout the generation. **Related issues:** - https://github.com/vllm-project/vllm/pull/8254 - https://github.com/vllm-project/vllm/issues/14058 - https://github.com/huggingface/transformers/pull/33129 **Reproduct...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: the bug While serving `microsoft/Phi-3.5-mini-instruct` (or any other model with LongRoPE), concurrent requests end up with random token outputs after the LongRoPE transition point from short factor to long factor, in t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: boundary: ```bash vllm serve microsoft/Phi-3.5-mini-instruct guidellm benchmark \ --target "http://localhost:8080" \ --rate-type concurrent \ --rate 16 \ --data "prompt_tokens=3900,output_tokens=500" \ --max-requests 10...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: /github.com/huggingface/transformers/pull/33129 **Reproduction:** Reproducible with any Phi-3.5 variant using the following workload designed to cross the 4K boundary: ```bash vllm serve microsoft/Phi-3.5-mini-instruct...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: .com/huggingface/transformers/pull/33129 **Reproduction:** Reproducible with any Phi-3.5 variant using the following workload designed to cross the 4K boundary: ```bash vllm serve microsoft/Phi-3.5-mini-instruct guidell...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: This causes the previous KV-cache to become invalid for the long-format scales, resulting in random tokens beyond that point, since it was encoded with different RoPE parameters. Synchronous requests aren’t affected bec...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
