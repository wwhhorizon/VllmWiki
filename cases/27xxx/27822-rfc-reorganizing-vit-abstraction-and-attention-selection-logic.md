# vllm-project/vllm#27822: [RFC]: Reorganizing ViT Abstraction and Attention Selection Logic

| 字段 | 值 |
| --- | --- |
| Issue | [#27822](https://github.com/vllm-project/vllm/issues/27822) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;multimodal_vlm |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;gemm;kernel;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Reorganizing ViT Abstraction and Attention Selection Logic

### Issue 正文摘录

### Motivation. This RFC is aimed to address the following issues: 1. The ViT right now is still pretty coupled with Text backbone attention. This RFC will further the effort to decouple the ViT and the text backbone attention. 2. Another pain point is that the overriding of the ViT logic is scattered all around the places. We should avoid doing ViT logic overriding in model definition classes. The platform class should define the logic of what ViT is supported and how it should be overwritten. 3. Since the introduction of `torch.compile` into the ViT, currently only starting with qwen vl model in PR https://github.com/vllm-project/vllm/pull/23207 , the AMD ViT Code path are broken. New approach will try to accommodate this new feature. `torch.compile` has brought a lot of performance improvement and we can now consider to replace triton kernels with pytorch native implementation as there are possibilities that `torch.compile` code is faster than custom `triton kernel` code. 4. Ensure ViT changes take into account the other model definition files `model.py` files, as current changes only involves `qwen_2_5_vl.py` which potentially affecting all other `models.py` files. - `vllm/mod...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: d and how it should be overwritten. 3. Since the introduction of `torch.compile` into the ViT, currently only starting with qwen vl model in PR https://github.com/vllm-project/vllm/pull/23207 , the AMD ViT Code path are...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: red all around the places. We should avoid doing ViT logic overriding in model definition classes. The platform class should define the logic of what ViT is supported and how it should be overwritten. 3. Since the intro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ught a lot of performance improvement and we can now consider to replace triton kernels with pytorch native implementation as there are possibilities that `torch.compile` code is faster than custom `triton kernel` code....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: at users know which `_MHA_Backend` is selected in the end. - Clean up cuda code path. Since `vllm.vllm_flash_attn` is just a wrapper for `flash_attn` library, on cuda, we always use `vllm.vllm_flash_attn` instead of `fl...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: he;ci_build;hardware_porting;model_support;multimodal_vlm attention;cuda;gemm;kernel;triton build_error env_dependency Motivation.

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
