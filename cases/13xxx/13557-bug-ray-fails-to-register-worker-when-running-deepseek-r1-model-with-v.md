# vllm-project/vllm#13557: [Bug]: Ray fails to register worker when running DeepSeek R1 model with vLLM and tensor parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#13557](https://github.com/vllm-project/vllm/issues/13557) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ray fails to register worker when running DeepSeek R1 model with vLLM and tensor parallelism

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am encountering an issue while running the DeepSeek R1 model using vLLM with tensor parallelism (tp=16) across two 8*H20 machines. The process hangs with the following message: ```code Connected to Ray cluster. View the dashboard at 127.0.0.1:8265 [2025-02-19 13:33:40,672 E 15244 15244] core_worker.cc:496: Failed to register worker to Raylet: IOError: [RayletClient] Unable to register worker with raylet. Failed to read data from the socket: End of file worker_id=01000000ffffffffffffffffffffffffffffffffffffffffffffffff ``` Steps to Reproduce: 1. Set up two machines, each with 8 H20 GPUs. 2.use vllm openai image. 3. Configure the environment for distributed tensor parallelism with tensor_parallel_size=16. 4. Run the DeepSeek R1 model using vLLM. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantiza...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ster worker when running DeepSeek R1 model with vLLM and tensor parallelism bug;ray ### Your current environment ### 🐛 Describe the bug I am encountering an issue while running the DeepSeek R1 model using vLLM with tens...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Ray fails to register worker when running DeepSeek R1 model with vLLM and tensor parallelism bug;ray ### Your current environment ### 🐛 Describe the bug I am encountering an issue while running the DeepSeek R1 mo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: d=01000000ffffffffffffffffffffffffffffffffffffffffffffffff ``` Steps to Reproduce: 1. Set up two machines, each with 8 H20 GPUs. 2.use vllm openai image. 3. Configure the environment for distributed tensor parallelism w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
