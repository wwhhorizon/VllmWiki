# vllm-project/vllm#20176: [Performance]: supports of fused moe kernel implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#20176](https://github.com/vllm-project/vllm/issues/20176) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;gemm;kernel;moe;quantization;triton |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: supports of fused moe kernel implementation

### Issue 正文摘录

### Proposal to improve performance By reading relative parts of source code and running some test, we find that when launching a MoE model like Qwen3, vLLM seems to use Triton-based fused moe kernel. While other implementations like cutlass or deep gemm is only supported by specific GPU arch like Hopper, or specific quantization method like Compressed Tensor. Is there a way to specify a type of fused moe kernel to use? For example I might want to compare the performance of Triten-based and Cutlass-based implementation on my A100 GPUs. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: lementations like cutlass or deep gemm is only supported by specific GPU arch like Hopper, or specific quantization method like Compressed Tensor. Is there a way to specify a type of fused moe kernel to use? For example...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: t, we find that when launching a MoE model like Qwen3, vLLM seems to use Triton-based fused moe kernel. While other implementations like cutlass or deep gemm is only supported by specific GPU arch like Hopper, or specif...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: other implementations like cutlass or deep gemm is only supported by specific GPU arch like Hopper, or specific quantization method like Compressed Tensor. Is there a way to specify a type of fused moe kernel to use? Fo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: of source code and running some test, we find that when launching a MoE model like Qwen3, vLLM seems to use Triton-based fused moe kernel. While other implementations like cutlass or deep gemm is only supported by speci...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Performance]: supports of fused moe kernel implementation performance;stale ### Proposal to improve performance By reading relative parts of source code and running some test, we find that when launching a MoE model li...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
