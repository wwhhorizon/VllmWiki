# vllm-project/vllm#9177: [Bug]: quantization does not work with dummy weight format

| 字段 | 值 |
| --- | --- |
| Issue | [#9177](https://github.com/vllm-project/vllm/issues/9177) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: quantization does not work with dummy weight format

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug found in ci, https://buildkite.com/vllm/ci-aws/builds/9653#01926d8d-2b87-4c7e-b5dd-bf56514236f0 , test_cpu_offload_gptq and test_cpu_offload_compressed_tensors do not work with dummy format. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ### Model Input Dumps _No response_ ### 🐛 Describe the bug found in ci, https://buildkite.com/vllm/ci-aws/builds/9653#01926d8d-2b87-4c7e-b5dd-bf56514236f0 , test_cpu_offload_gptq and test_cpu_offload_compressed_tensors...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: quantization does not work with dummy weight format bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug found in ci, https://buildkite.com/vllm/ci-aws/builds/9653#019...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: quantization does not work with dummy weight format bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug found in ci, https://buildkite.com/vllm/ci-aws/builds/9653#0192
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: at. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: /vllm/ci-aws/builds/9653#01926d8d-2b87-4c7e-b5dd-bf56514236f0 , test_cpu_offload_gptq and test_cpu_offload_compressed_tensors do not work with dummy format. ### Before submitting a new issue... - [X] Make sure you alrea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
