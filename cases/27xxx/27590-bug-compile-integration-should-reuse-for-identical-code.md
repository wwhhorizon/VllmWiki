# vllm-project/vllm#27590: [Bug]: Compile Integration should reuse for identical code

| 字段 | 值 |
| --- | --- |
| Issue | [#27590](https://github.com/vllm-project/vllm/issues/27590) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Compile Integration should reuse for identical code

### Issue 正文摘录

### Your current environment ### Your current environment ### 🐛 Describe the bug While investigating torch.compile for ViT backbone in vLLM, I tried applying the `support_torch_compile` decorator on the VisionBlock for Qwen2_5_vl; however, this causes each unique definition of the `VisionBlock` to be compiled seperately Torch.compile should be able to reuse this compiled code for different instantiations of VisionBlock, but this is currently not the case due to the existing compile integration - this issue asks us to modify the logic so that we only compile once, cutting compile time when we use torch.compile on subblocks in vLLM To close this task, we would be able to modify the multimodal_compile unittest to see only 4 models as opposed to 35 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Compile Integration should reuse for identical code bug;torch.compile;stale ### Your current environment ### Your current environment ### 🐛 Describe the bug While investigating torch.compile for ViT backbone in v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ed applying the `support_torch_compile` decorator on the VisionBlock for Qwen2_5_vl; however, this causes each unique definition of the `VisionBlock` to be compiled seperately Torch.compile should be able to reuse this...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 35 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ting;model_support;multimodal_vlm;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: LLM, I tried applying the `support_torch_compile` decorator on the VisionBlock for Qwen2_5_vl; however, this causes each unique definition of the `VisionBlock` to be compiled seperately Torch.compile should be able to r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
