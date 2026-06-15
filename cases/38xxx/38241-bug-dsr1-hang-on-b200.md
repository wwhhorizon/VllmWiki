# vllm-project/vllm#38241: [Bug]: DSR1 hang on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#38241](https://github.com/vllm-project/vllm/issues/38241) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DSR1 hang on B200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Deepseek R1 hangs on B200. Tried the following commands, all hung before warmup run: ``` vllm serve deepseek-ai/DeepSeek-R1 -dp=8 -ep vllm serve deepseek-ai/DeepSeek-R1 -tp=8 vllm serve deepseek-ai/DeepSeek-R1 --load-format=dummy -dp=8 -ep vllm serve deepseek-ai/DeepSeek-R1 --load-format=dummy -dp=8 -ep --kernel-config.enable_flashinfer_autotune=False vllm serve deepseek-ai/DeepSeek-R1 --load-format=dummy -tp=8 vllm serve deepseek-ai/DeepSeek-R1 --load-format=dummy -tp=8 -cc.fuse_allreduce_rms=False vllm serve deepseek-ai/DeepSeek-R1 --load-format=dummy -dp=8 -ep --enforce-eager # seems that 3.1 has the same issue vllm serve deepseek-ai/DeepSeek-V3.1 --load-format=dummy -dp=8 -ep ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: deepseek-ai/DeepSeek-R1 -tp=8 vllm serve deepseek-ai/DeepSeek-R1 --load-format=dummy -dp=8 -ep vllm serve deepseek-ai/DeepSeek-R1 --load-format=dummy -dp=8 -ep --kernel-config.enable_flashinfer_autotune=False vllm serve...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: DSR1 hang on B200 bug ### Your current environment ### 🐛 Describe the bug Deepseek R1 hangs on B200. Tried the following commands, all hung before warmup run: ``` vllm serve deepseek-ai/DeepSeek-R1 -dp=8 -ep vllm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: seek-ai/DeepSeek-R1 --load-format=dummy -dp=8 -ep --kernel-config.enable_flashinfer_autotune=False vllm serve deepseek-ai/DeepSeek-R1 --load-format=dummy -tp=8 vllm serve deepseek-ai/DeepSeek-R1 --load-format=dummy -tp=...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding cuda;kernel;operator;quantization;s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
