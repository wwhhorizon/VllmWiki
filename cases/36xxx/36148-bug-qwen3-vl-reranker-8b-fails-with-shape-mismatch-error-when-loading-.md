# vllm-project/vllm#36148: [Bug]: Qwen3-VL-Reranker-8B fails with shape mismatch error when loading with --quantization bitsandbytes

| 字段 | 值 |
| --- | --- |
| Issue | [#36148](https://github.com/vllm-project/vllm/issues/36148) |
| 状态 | open |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-Reranker-8B fails with shape mismatch error when loading with --quantization bitsandbytes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Description: When attempting to load the model in quantized mode, the loading process fails at the final stage with the following error: AssertionError: Tried to load weights of size torch.Size([1, 4096]) to a parameter of size torch.Size([1024, 1]) Does this indicate that VLLM has not yet implemented quantization support for Qwen3-VL-Reranker-8B? Launch parameters: CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \ --model /home/kongkong/.cache/modelscope/hub/models/Qwen/Qwen3-VL-Reranker-8B \ --runner pooling \ --port 8001 \ --host 0.0.0.0 \ --dtype float16 \ --max-model-len 4096 \ --gpu-memory-utilization 0.9 \ --max-num-seqs 32 \ --max-num-batched-tokens 2048 \ --hf-overrides '{"architectures": ["Qwen3VLForSequenceClassification"], "classifier_from_token": ["no", "yes"], "is_original_qwen3_reranker": true}' \ --allowed-local-media-path /home/kongkong/下载/测试 \ --chat-template /home/kongkong/下载/qwen3_vl_reranker.jinja \ --quantization bitsandbytes \ --load-format bitsandbytes ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the botto...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-VL-Reranker-8B fails with shape mismatch error when loading with --quantization bitsandbytes bug ### Your current environment ### 🐛 Describe the bug Description: When attempting to load the model in quantiz...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Qwen3-VL-Reranker-8B fails with shape mismatch error when loading with --quantization bitsandbytes bug ### Your current environment ### 🐛 Describe the bug Description: When attempting to load the model in quantized mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen3-VL-Reranker-8B fails with shape mismatch error when loading with --quantization bitsandbytes bug ### Your current environment ### 🐛 Describe the bug Description: When attempting to load the model in quantiz...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Qwen3-VL-Reranker-8B fails with shape mismatch error when loading with --quantization bitsandbytes bug ### Your current environment ### 🐛 Describe the bug Description: When attempting to load the model in quantiz...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
