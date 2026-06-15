# vllm-project/vllm#27821: [RFC]: Reorganizing ViT Abstraction and Attention Selection Logic

| 字段 | 值 |
| --- | --- |
| Issue | [#27821](https://github.com/vllm-project/vllm/issues/27821) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;multimodal_vlm |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;gemm;kernel;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Reorganizing ViT Abstraction and Attention Selection Logic

### Issue 正文摘录

### Motivation. This RFC is aimed to address the following issues: 1. The ViT right now is still pretty coupled with Text backbone attention. This RFC will further the effort to decouple the ViT and the text backbone attention. 2. Another pain point is that the overriding of the ViT logic is scattered all around the places. We should avoid doing ViT logic overriding in model definition classes. The platform class should define the logic of what ViT is supported and how it should be overwritten. - The above logic is applied to general use case. As of the time of this RFC is proposed. This single logic is applied to all of the VL model below: - `vllm/model_executor/models/qwen2_5_vl.py` (this is shared by Qwen2.5 VL and Qwen3 VL) - `vllm/model_executor/models/dots_ocr.py` - `vllm/model_executor/models/ernie45_vl.py` - `vllm/model_executor/models/glm4_1v.py` - `vllm/model_executor/models/qwen2_vl.py` - `vllm/model_executor/models/siglip2navit.py` - If the model only supports a specific type of attention, the ViT overriding logic will be implemented explicitly in the model definition file (`model.py`). 3. Since the introduction of `torch.compile` into the ViT, currently only starting...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: model_executor/models/siglip2navit.py` - If the model only supports a specific type of attention, the ViT overriding logic will be implemented explicitly in the model definition file (`model.py`). 3. Since the introduct...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: thon class _MHA_Backend(enum.Enum): VLLM_FLASH_ATTN = enum.auto() # CUDA-only FLASH_ATTN = enum.auto() # CUDA/ROCm XFORMERS = enum.auto() # CUDA ROCM_AITER_FA = enum.auto() # ROCM-only TORCH_SDPA = enum.auto() # CUDA/RO...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: red all around the places. We should avoid doing ViT logic overriding in model definition classes. The platform class should define the logic of what ViT is supported and how it should be overwritten. - The above logic...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ught a lot of performance improvement and we can now consider to replace triton kernels with pytorch native implementation as there are possibilities that `torch.compile` code is faster than custom `triton kernel` code....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: def get_vit_attn_backend( cls, head_size: int, dtype: torch.dtype, backend: Optional["_MHA_Backend"] = None, ) -> "_MHA_Backend": # ViT Attention should be checked and override # in the platform-specific implementation....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
