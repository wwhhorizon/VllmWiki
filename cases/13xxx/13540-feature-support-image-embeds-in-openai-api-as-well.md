# vllm-project/vllm#13540: [Feature]: support image_embeds in openai api as well

| 字段 | 值 |
| --- | --- |
| Issue | [#13540](https://github.com/vllm-project/vllm/issues/13540) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support image_embeds in openai api as well

### Issue 正文摘录

### 🚀 The feature, motivation and pitch would it be possible to support `image_embeds` in openai protocol api as well? And prefix-caching shall be supported via following proposal. thanks. So users can pass ``` { "type": "image_url", "image_url": { "image_url": {"url": f"data:image/embeds;base64,{base64_image}"}, } } ``` use base64 or other more efficient compression method? ```py import base64 import numpy as np def encode_base64(arr): return base64.b64encode(arr.astype(np.float32).tobytes()).decode('utf-8') def decode_base64(encoded_str, shape): decoded = base64.b64decode(encoded_str) return np.frombuffer(decoded, dtype=np.float32).reshape(shape) ``` cc @youkaichao ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: /embeds;base64,{base64_image}"}, } } ``` use base64 or other more efficient compression method? ```py import base64 import numpy as np def encode_base64(arr): return base64.b64encode(arr.astype(np.float32).tobytes()).de...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: as np def encode_base64(arr): return base64.b64encode(arr.astype(np.float32).tobytes()).decode('utf-8') def decode_base64(encoded_str, shape): decoded = base64.b64decode(encoded_str) return np.frombuffer(decoded, dtype=...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support image_embeds in openai api as well feature request ### 🚀 The feature, motivation and pitch would it be possible to support `image_embeds` in openai protocol api as well? And prefix-caching shall be su...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
