# vllm-project/vllm#6623: [Performance]: Llava runs with small batch size and # of GPU blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#6623](https://github.com/vllm-project/vllm/issues/6623) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support;multimodal_vlm |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Llava runs with small batch size and # of GPU blocks

### Issue 正文摘录

### Misc discussion on performance I was running `llava-hf/llava-1.5-7b-hf` vs. `meta-llama/Meta-Llama-3-8B-Instruct` on vLLM 0.5.2 and noticed that Llava 7B runs with a significantly smaller batch size overall -- Llama 3 8B would hit the maximum batch size 256, whereas Llava 7B would remain in the 70~80 range. I do notice that Llava 7B begins with much less GPU blocks allocated (# GPU blocks: 3631, # CPU blocks: 512) compared to LLama 3 8B (# GPU blocks: 13078, # CPU blocks: 2048), which probably explains the batch size. I wanted to understand whether this difference (existence and magnitude) is expected and the causes. I can think of some reasons that contribute to this: - Parameters of the vision tower and multimodal projector - Less than half a billion parameters - Activations of the vision tower and multimodal projector - They can't be *that* big, can they? I believe they can also be deallocated after generating the image embeddings. - Image tokens inserted into the prompt - I attempted to read the source code and it seems like it's 576 image tokens? If so I suppose that's a fair amount. But does this get reflected in the number of GPU blocks? Thanks. ### Your current environ...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: cks performance ### Misc discussion on performance I was running `llava-hf/llava-1.5-7b-hf` vs. `meta-llama/Meta-Llama-3-8B-Instruct` on vLLM 0.5.2 and noticed that Llava 7B runs with a significantly smaller batch size...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: s. ### Your current environment (if you think it is necessary) PyTorch version: 2.3.1+cu121 CUDA used to build PyTorch: 12.1 Single NVIDIA A40 GPU with 46068 MiB VRAM. performance ci_build;model_support;multimodal_vlm c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Performance]: Llava runs with small batch size and # of GPU blocks performance ### Misc discussion on performance I was running `llava-hf/llava-1.5-7b-hf` vs. `meta-llama/Meta-Llama-3-8B-Instruct` on vLLM 0.5.2 and not...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Performance]: Llava runs with small batch size and # of GPU blocks performance ### Misc discussion on performance I was running `llava-hf/llava-1.5-7b-hf` vs. `meta-llama/Meta-Llama-3-8B-Instruct` on vLLM 0.5.2 and not...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
