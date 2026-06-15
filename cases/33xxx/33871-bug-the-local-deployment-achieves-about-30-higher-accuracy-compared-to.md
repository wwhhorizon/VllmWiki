# vllm-project/vllm#33871: [Bug]: The local deployment achieves about 30% higher accuracy compared to the server deployment.

| 字段 | 值 |
| --- | --- |
| Issue | [#33871](https://github.com/vllm-project/vllm/issues/33871) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The local deployment achieves about 30% higher accuracy compared to the server deployment.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I’m currently using vllm 0.15.0 to run the 4B version of Qwen3VL on a 2080Ti. I noticed a significant performance gap between two deployment methods: Local deployment with vllm.LLM​ – I followed the official Qwen3VL preprocessing approach, using qwen-vl-utilsand process_vision_info to handle image data. Server deployment via vllm serve​ – I’m uncertain if the same preprocessing is required when sending image data via API requests. When testing the same image-text prompts, the local deployment achieves about 30% higher accuracy compared to the server deployment. This suggests that the image preprocessing may not be applied correctly (or at all) in the vllm servescenario. Could you clarify: 1. Does vllm serveautomatically apply the same vision preprocessing as the official Qwen3VL implementation, or should we manually preprocess images with process_vision_infobefore sending them to the server? 2. If preprocessing is required, is there a recommended way to integrate it with the vllm serving workflow? Any guidance on ensuring consistent performance between local and server deployments would be greatly appreciated. Thanks! ### Before...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### 🐛 Describe the bug I’m currently using vllm 0.15.0 to run the 4B version of Qwen3VL on a 2080Ti. I noticed a significant performance gap between two deployment methods: Local deployment with vllm.LLM​ – I followed t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: scribe the bug I’m currently using vllm 0.15.0 to run the 4B version of Qwen3VL on a 2080Ti. I noticed a significant performance gap between two deployment methods: Local deployment with vllm.LLM​ – I followed the offic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: chieves about 30% higher accuracy compared to the server deployment. bug;stale ### Your current environment ### 🐛 Describe the bug I’m currently using vllm 0.15.0 to run the 4B version of Qwen3VL on a 2080Ti. I noticed...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: The local deployment achieves about 30% higher accuracy compared to the server deployment. bug;stale ### Your current environment ### 🐛 Describe the bug I’m currently using vllm 0.15.0 to run the 4B version of Qw...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
