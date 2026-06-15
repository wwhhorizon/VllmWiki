# vllm-project/vllm#32895: [Bug]: [ROCm] [MI355X] new 0.14 upstream gptoss hard error TP=1?

| 字段 | 值 |
| --- | --- |
| Issue | [#32895](https://github.com/vllm-project/vllm/issues/32895) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [ROCm] [MI355X] new 0.14 upstream gptoss hard error TP=1?

### Issue 正文摘录

### Your current environment Platform: AMD MI355X Docker Image: vllm/vllm-openai-rocm:v0.14.0 ### 🐛 Describe the bug hi @powderluv @chunfangamd Full logs of this bug available at: https://github.com/InferenceMAX/InferenceMAX/actions/runs/21260856946 Docker image: vllm/vllm-openai-rocm:v0.14.0 When running vLLM 0.14.0 on MI355X with TP=1 (single GPU), the server consistently fails with: ``` torch.AcceleratorError: HIP error: no kernel image is available for execution on the device Search for `hipErrorNoBinaryForGpu' in https://docs.nvidia.com/cuda/cuda-runtime-api/group__HIPRT__TYPES.html for more information. HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing AMD_SERIALIZE_KERNEL=3 Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions. ``` Key observations: The failure occurs after approximately 2 hours of CUDA graph capture and torch.compile warmup TP=1 consistently fails (100% failure rate across 17 jobs in our testing) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner o...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: error TP=1? bug;rocm ### Your current environment Platform: AMD MI355X Docker Image: vllm/vllm-openai-rocm:v0.14.0 ### 🐛 Describe the bug hi @powderluv @chunfangamd Full logs of this bug available at: https://github.com...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: [ROCm] [MI355X] new 0.14 upstream gptoss hard error TP=1? bug;rocm ### Your current environment Platform: AMD MI355X Docker Image: vllm/vllm-openai-rocm:v0.14.0 ### 🐛 Describe the bug hi @powderluv @chunfangamd F...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: stributed_parallel;frontend_api;hardware_porting cuda;kernel build_error;mismatch env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ocs.nvidia.com/cuda/cuda-runtime-api/group__HIPRT__TYPES.html for more information. HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: warmup TP=1 consistently fails (100% failure rate across 17 jobs in our testing) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
