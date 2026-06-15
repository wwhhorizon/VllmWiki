# vllm-project/vllm#18916: [Bug]: VLLM Docker v0.9.0 produces Runtime Error: Cuda Error on Blackwell using Qwen0.6B

| 字段 | 值 |
| --- | --- |
| Issue | [#18916](https://github.com/vllm-project/vllm/issues/18916) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM Docker v0.9.0 produces Runtime Error: Cuda Error on Blackwell using Qwen0.6B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When queuing V1/chat/completions with qwen0.6b in b16, the VLLM instance crashes due to ```text RuntimeError: CUDA error: no kernel image is available for execution on the device ``` I've read other issues, and while there are other issues with the same error as this issue The error's in other issues are on a completely different system, with a different gpu topology, with a different traceback leading to that error. That is why im creating a independent issue. If this is problematic, please feel free to close it.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: VLLM Docker v0.9.0 produces Runtime Error: Cuda Error on Blackwell using Qwen0.6B bug ### Your current environment ### 🐛 Describe the bug When queuing V1/chat/completions with qwen0.6b in b16, the VLLM instance c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: VLLM Docker v0.9.0 produces Runtime Error: Cuda Error on Blackwell using Qwen0.6B bug ### Your current environment ### 🐛 Describe the bug When queuing V1/chat/completions with qwen0.6b in b16, the VLLM instance c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cache;cuda;kernel;operator;quantization;sampling;triton build_error;c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: VLLM Docker v0.9.0 produces Runtime Error: Cuda Error on Blackwell using Qwen0.6B bug ### Your current environment ### 🐛 Describe the bug When queuing V1/chat/completions with qwen0.6b in b16, the VLLM instance crashes...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cache;cuda;kernel;operator;quantization;sampling;triton build_error;crash;mismatch;nan_inf;slowdow...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
