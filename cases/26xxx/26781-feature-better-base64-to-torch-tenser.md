# vllm-project/vllm#26781: [Feature]: Better base64 to torch tenser

| 字段 | 值 |
| --- | --- |
| Issue | [#26781](https://github.com/vllm-project/vllm/issues/26781) |
| 状态 | closed |
| 标签 | good first issue;feature request;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Better base64 to torch tenser

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Support float32, float16, bfloat16, fp8_e4m3, fp8_e5m2 embed dtype in #26414 The following line of code will raise annoying UserWarning ``` torch.frombuffer( base64.b64decode(data["embedding"]), dtype=torch_dtype ).to(torch.float32) ``` UserWarning: ``` examples/online_serving/pooling/embedding_embed_dtype_client.py:49: UserWarning: The given buffer is not writable, and PyTorch does not support non-writable tensors. This means you can write to the underlying (supposedly non-writable) buffer using the tensor. You may want to copy the buffer to protect its data or make it writable before converting it to a tensor. This type of warning will be suppressed for the rest of this program. (Triggered internally at /pytorch/torch/csrc/utils/tensor_new.cpp:1578.) torch.frombuffer( ``` Cannot use numpy to load data['embedding'] because numpy does not support bfloat16, fp8_e4m3, fp8_e5m2 Welcome to contribute. If you know an efficient method that does not trigger this UserWarning (It's best to use a zero-copy method here.) This issue involves the following files - examples/online_serving/pooling/embedding_embed_dtype_client.py - tests/entrypoints/pooling...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e;feature request;stale ### 🚀 The feature, motivation and pitch Support float32, float16, bfloat16, fp8_e4m3, fp8_e5m2 embed dtype in #26414 The following line of code will raise annoying UserWarning ``` torch.frombuffe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Better base64 to torch tenser good first issue;feature request;stale ### 🚀 The feature, motivation and pitch Support float32, float16, bfloat16, fp8_e4m3, fp8_e5m2 embed dtype in #26414 The following line of...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: bfloat16, fp8_e4m3, fp8_e5m2 Welcome to contribute. If you know an efficient method that does not trigger this UserWarning (It's best to use a zero-copy method here.) This issue involves the following files - examples/o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: iles - examples/online_serving/pooling/embedding_embed_dtype_client.py - tests/entrypoints/pooling/openai/test_pooling.py - tests/entrypoints/pooling/openai/test_embedding.py ### Alternatives _No response_ ### Additiona...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
