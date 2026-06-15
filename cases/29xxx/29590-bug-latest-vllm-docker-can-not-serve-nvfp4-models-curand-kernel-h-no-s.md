# vllm-project/vllm#29590: [Bug]: Latest vllm docker can not serve nvfp4 models. `curand_kernel.h: No such file or directory`

| 字段 | 值 |
| --- | --- |
| Issue | [#29590](https://github.com/vllm-project/vllm/issues/29590) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Latest vllm docker can not serve nvfp4 models. `curand_kernel.h: No such file or directory`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Main problem seems to be following: ``` /usr/local/lib/python3.12/dist-packages/flashinfer/data/cutlass/tools/util/include/cutlass/util/reference/device/tensor_fill.h:52:10: fatal error: curand_kernel.h: No such file or directory ``` I can run the model via my local env, where the model is quantized by following the example https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a4_fp4/qwen3_vl_moe_w4a4_fp4.py Docker image is the latest one: `vllm/vllm-openai:nightly-11ea5ec1ff7afc5ba181cba41f0cc2e4053e27f3` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Latest vllm docker can not serve nvfp4 models. `curand_kernel.h: No such file or directory` bug ### Your current environment ### 🐛 Describe the bug Main problem seems to be following: ``` /usr/local/lib/python3.1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: oblem seems to be following: ``` /usr/local/lib/python3.12/dist-packages/flashinfer/data/cutlass/tools/util/include/cutlass/util/reference/device/tensor_fill.h:52:10: fatal error: curand_kernel.h: No such file or direct...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Latest vllm docker can not serve nvfp4 models. `curand_kernel.h: No such file or directory` bug ### Your current environment ### 🐛 Describe the bug Main problem seems to be following: ``` /usr/local/lib/python3.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Latest vllm docker can not serve nvfp4 models. `curand_kernel.h: No such file or directory` bug ### Your current environment ### 🐛 Describe the bug Main problem seems to be following: ``` /usr/local/lib/python3.1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
