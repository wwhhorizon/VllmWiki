# vllm-project/vllm#39204: [Installation]: New 0.19.0 docker build to run gemma4: transformers outdated.

| 字段 | 值 |
| --- | --- |
| Issue | [#39204](https://github.com/vllm-project/vllm/issues/39204) |
| 状态 | open |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: New 0.19.0 docker build to run gemma4: transformers outdated.

### Issue 正文摘录

### Your current environment Hi, I just built the 0.19.0 version of the docker vllm for XPU and I am trying to run the gemma4-E4B model. After serving the model I receive the message that my transformers is outdated. Updating transformers kind of works, but only with errors: ``` Installing collected packages: huggingface-hub, transformers Attempting uninstall: huggingface-hub Found existing installation: huggingface_hub 0.36.2 Uninstalling huggingface_hub-0.36.2: Successfully uninstalled huggingface_hub-0.36.2 Attempting uninstall: transformers Found existing installation: transformers 4.57.6 Uninstalling transformers-4.57.6: Successfully uninstalled transformers-4.57.6 ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts. xgrammar 0.1.33 requires triton; platform_system == "Linux" and platform_machine == "x86_64", which is not installed. vllm 0.19.0+xpu requires transformers =4.56.0, but you have transformers 5.5.0 which is incompatible. compressed-tensors 0.14.0.1 requires transformers<5.0.0, but you have transformers 5.5.0 which is incompatible. Successfully...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: New 0.19.0 docker build to run gemma4: transformers outdated. installation ### Your current environment Hi, I just built the 0.19.0 version of the docker vllm for XPU and I am trying to run the gemma4-E4B
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Installation]: New 0.19.0 docker build to run gemma4: transformers outdated. installation ### Your current environment Hi, I just built the 0.19.0 version of the docker vllm for XPU and I am trying to run the gemma4-E4...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e source of the following dependency conflicts. xgrammar 0.1.33 requires triton; platform_system == "Linux" and platform_machine == "x86_64", which is not installed. vllm 0.19.0+xpu requires transformers =4.56.0, but yo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Installation]: New 0.19.0 docker build to run gemma4: transformers outdated. installation ### Your current environment Hi, I just built the 0.19.0 version of the docker vllm for XPU and I am trying to run the gemma4-E4...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
