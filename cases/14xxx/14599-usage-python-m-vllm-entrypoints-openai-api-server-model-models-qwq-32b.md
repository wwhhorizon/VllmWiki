# vllm-project/vllm#14599: [Usage]: python -m vllm.entrypoints.openai.api_server --model models/QwQ-32B  --served-model-name QwQ-32B --max-model-len=2048 --dtype=bflo at16 --quantization=bitsandbytes --load_format=bitsandbytes

| 字段 | 值 |
| --- | --- |
| Issue | [#14599](https://github.com/vllm-project/vllm/issues/14599) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: python -m vllm.entrypoints.openai.api_server --model models/QwQ-32B  --served-model-name QwQ-32B --max-model-len=2048 --dtype=bflo at16 --quantization=bitsandbytes --load_format=bitsandbytes

### Issue 正文摘录

### Your current environment 我想在模型加载时量化部署，我用了这条命令启服务：python -m vllm.entrypoints.openai.api_server --model models/QwQ-32B --served-model-name QwQ-32B --max-model-len=2048 --dtype=bflo at16 --quantization=bitsandbytes --load_format=bitsandbytes 是成功的，但我不知道是都为INT4的量化 ### How would you like to use vllm 我想在模型加载时量化部署，我用了这条命令启服务：python -m vllm.entrypoints.openai.api_server --model models/QwQ-32B --served-model-name QwQ-32B --max-model-len=2048 --dtype=bflo at16 --quantization=bitsandbytes --load_format=bitsandbytes 是成功的，但我不知道是都为INT4的量化 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: model models/QwQ-32B --served-model-name QwQ-32B --max-model-len=2048 --dtype=bflo at16 --quantization=bitsandbytes --load_format=bitsandbytes usage ### Your current environment 我想在模型加载时量化部署，我用了这条命令启服务：python -m vllm.en...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: python -m vllm.entrypoints.openai.api_server --model models/QwQ-32B --served-model-name QwQ-32B --max-model-len=2048 --dtype=bflo at16 --quantization=bitsandbytes --load_format=bitsandbytes usage ### Your curre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 的量化 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
