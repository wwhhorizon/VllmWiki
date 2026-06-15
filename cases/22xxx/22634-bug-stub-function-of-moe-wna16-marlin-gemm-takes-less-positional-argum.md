# vllm-project/vllm#22634: [Bug]: Stub function of moe_wna16_marlin_gemm takes less positional arguments than real implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#22634](https://github.com/vllm-project/vllm/issues/22634) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Stub function of moe_wna16_marlin_gemm takes less positional arguments than real implementation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Quantized MoE models default to using the Marlin backend for inference. When I use Dynamo to compile the model, the stub function appears to be missing an additional parameter named global_scale: Optional[torch.Tensor]. This causes a TypeError during fake tensor propagation in torch.compile: torch._dynamo.exc.Unsupported: TypeError when making fake tensor call Explanation: Developer debug context: TypeError _moe_C.moe_wna16_marlin_gemm: moe_wna16_marlin_gemm_fake() takes 24 positional arguments but 25 were given I'm not sure if other stub functions have similar issues, but I'd like to bring this to your attention and hope it can be addressed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: _gemm takes less positional arguments than real implementation bug;torch.compile ### Your current environment ### 🐛 Describe the bug Quantized MoE models default to using the Marlin backend for inference. When I use Dyn...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ### 🐛 Describe the bug Quantized MoE models default to using the Marlin backend for inference. When I use Dynamo to compile the model, the stub function appears to be missing an additional parameter named global_scale:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: g;torch.compile ### Your current environment ### 🐛 Describe the bug Quantized MoE models default to using the Marlin backend for inference. When I use Dynamo to compile the model, the stub function appears to be missing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Stub function of moe_wna16_marlin_gemm takes less positional arguments than real implementation bug;torch.compile ### Your current environment ### 🐛 Describe the bug Quantized MoE models default to using the Marl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
