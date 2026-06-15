# vllm-project/vllm#31700: [Bug]: CUDA error: "provided PTX was compiled with an unsupported toolchain" on vLLM 0.11.2

| 字段 | 值 |
| --- | --- |
| Issue | [#31700](https://github.com/vllm-project/vllm/issues/31700) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA error: "provided PTX was compiled with an unsupported toolchain" on vLLM 0.11.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am observing inconsistent behavior on vLLM 0.11.2 with NVIDIA Driver 550.144.03 (CUDA 12.4). Success: I can successfully serve and run Qwen-VL models (e.g., Qwen3VL) without any issues. Failure: When I try to serve InternVL (e.g., InternVL3_5-GPT-OSS-20B-A4B-Preview, InternVL3-14B), it crashes immediately upon initialization with a cudaErrorUnsupportedPtxVersion error. The error occurs when running: ```bash vllm serve /root/Models/InternVL3-14B \ --port 9875 \ --dtype bfloat16 \ --served-model-name "InternVL3-14B" \ --trust-remote-code \ --gpu-memory-utilization 0.9 \ --enable-prefix-caching \ --max-model-len 8192 ``` How can the vllm environment be successfully configured to run InternVL without affecting the operation of qwen3vl? Is there a flag to force InternVL to use a different attention backend? Or maybe there's another solution. Thanks a lot for your reply. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: river 550.144.03 (CUDA 12.4). Success: I can successfully serve and run Qwen-VL models (e.g., Qwen3VL) without any issues. Failure: When I try to serve InternVL (e.g., InternVL3_5-GPT-OSS-20B-A4B-Preview, InternVL3-14B)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: CUDA error: "provided PTX was compiled with an unsupported toolchain" on vLLM 0.11.2 bug ### Your current environment ### 🐛 Describe the bug I am observing inconsistent behavior on vLLM 0.11.2 with NVIDIA Driver...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: g: ```bash vllm serve /root/Models/InternVL3-14B \ --port 9875 \ --dtype bfloat16 \ --served-model-name "InternVL3-14B" \ --trust-remote-code \ --gpu-memory-utilization 0.9 \ --enable-prefix-caching \ --max-model-len 81...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA error: "provided PTX was compiled with an unsupported toolchain" on vLLM 0.11.2 bug ### Your current environment ### 🐛 Describe the bug I am observing inconsistent behavior on vLLM 0.11.2 with NVIDIA Driver...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: qwen3vl? Is there a flag to force InternVL to use a different attention backend? Or maybe there's another solution. Thanks a lot for your reply. ### Before submitting a new issue... - [x] Make sure you already searched...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
