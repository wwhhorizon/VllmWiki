# vllm-project/vllm#30342: [Bug]: HunyuanOCR batching problem with variable sized images in a batch.

| 字段 | 值 |
| --- | --- |
| Issue | [#30342](https://github.com/vllm-project/vllm/issues/30342) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: HunyuanOCR batching problem with variable sized images in a batch.

### Issue 正文摘录

### Your current environment Running on the latest nightly docker vllm-openai image using the following paramters: ``` command: "--model tencent/HunyuanOCR --trust-remote-code --dtype bfloat16 --max-model-len 6144 --limit-mm-per-prompt '{\"image\": 1}' --max-num-seqs 256 --max-num-batched-tokens 16384 --gpu-memory-utilization 0.9 --swap-space 32 --enforce-eager" ``` ### 🐛 Describe the bug When running the [tencent/HunyuanOCR](https://huggingface.co/tencent/HunyuanOCR) model under load, another problem in the batching logic mixes different images / inputs. The problem appears to be inside the model executor code and seems to happen when differently sized pictures are present in the same batch. The behavior has been produced and described in this Issue over at the model's repository: https://github.com/Tencent-Hunyuan/HunyuanOCR/issues/60#issuecomment-3620922425 I have reliably reproduced the issue in my pipeline, however was not able to generate a minimal example that i can share since my dataset that encountered the issue is confidential. However, I have built a fix that seems to sidestep the issue by processing the images independently and will open a PR. Additional Information:...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: aramters: ``` command: "--model tencent/HunyuanOCR --trust-remote-code --dtype bfloat16 --max-model-len 6144 --limit-mm-per-prompt '{\"image\": 1}' --max-num-seqs 256 --max-num-batched-tokens 16384 --gpu-memory-utilizat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: docker vllm-openai image using the following paramters: ``` command: "--model tencent/HunyuanOCR --trust-remote-code --dtype bfloat16 --max-model-len 6144 --limit-mm-per-prompt '{\"image\": 1}' --max-num-seqs 256 --max-...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nt-Hunyuan/HunyuanOCR/issues/60#issuecomment-3620922425 I have reliably reproduced the issue in my pipeline, however was not able to generate a minimal example that i can share since my dataset that encountered the issu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: a batch. bug ### Your current environment Running on the latest nightly docker vllm-openai image using the following paramters: ``` command: "--model tencent/HunyuanOCR --trust-remote-code --dtype bfloat16 --max-model-l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: st. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
