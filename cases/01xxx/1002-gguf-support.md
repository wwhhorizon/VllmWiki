# vllm-project/vllm#1002: GGUF support

| 字段 | 值 |
| --- | --- |
| Issue | [#1002](https://github.com/vllm-project/vllm/issues/1002) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 49; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> GGUF support

### Issue 正文摘录

### Motivation AWQ is nice, but if you want more control over the bit depth (thus VRAM usage), then GGUF may be a better option. A wide range of models are available from TheBloke at various bit depths, so everybody can use the biggest one which can fit into their GPUs. I cannot find a high-throughput batch inference engine which can load GGUF, maybe there is none. (vLLM cannot load it either.) ### Related resources https://github.com/ggerganov/llama.cpp https://huggingface.co/TheBloke

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: pth (thus VRAM usage), then GGUF may be a better option. A wide range of models are available from TheBloke at various bit depths, so everybody can use the biggest one which can fit into their GPUs. I cannot find a high...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: GGUF support feature request ### Motivation AWQ is nice, but if you want more control over the bit depth (thus VRAM usage), then GGUF may be a better option. A wide range of models are available from TheBloke at various...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: use the biggest one which can fit into their GPUs. I cannot find a high-throughput batch inference engine which can load GGUF, maybe there is none. (vLLM cannot load it either.) ### Related resources https://github.com/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
