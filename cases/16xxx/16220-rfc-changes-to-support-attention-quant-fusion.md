# vllm-project/vllm#16220: [RFC]: Changes to support attention + quant fusion

| 字段 | 值 |
| --- | --- |
| Issue | [#16220](https://github.com/vllm-project/vllm/issues/16220) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Changes to support attention + quant fusion

### Issue 正文摘录

### Motivation. I am working on fusing FP8 quantization onto (V0) attention with a new `torch.compile` pass. However, this pass will require some other changes to core vLLM code so I just wanted to collect people's opinions before proceeding. AMD saw manually fusing quantization into the attention op lead to a major improvement in performance in the ROCm fork. Basically, when fused, the attention output is quantized inside the attention Triton kernel before being written out, saving data movement by avoiding a full roundtrip to global memory at 16-bit precision. To avoid modifying the model definitions (approach used in ROCm fork), we are planning to do the fusion using a `torch.compile` pass. Apart from the pass implementation, there are two obstacles in the Python integration code: 1. Attention is wrapped into a `unified_attention` custom op 1. In V1, piecewise compilation means that the ops we want to fuse appear in different graphs ### Proposed Change. #### 1. Extend `unified_attention` **EDIT:** @youkaichao has suggested to directly store `output_scale` on the attention object, which will also help more easily figure out if the attention backend supports fusing the op. So the...

## 现有链接修复摘要

#16756 [torch.compile][ROCm] Fuse quantization onto attention using a torch.compile pass

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: working on fusing FP8 quantization onto (V0) attention with a new `torch.compile` pass. However, this pass will require some other changes to core vLLM code so I just wanted to collect people's opinions before proceedin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [RFC]: Changes to support attention + quant fusion RFC ### Motivation. I am working on fusing FP8 quantization onto (V0) attention with a new `torch.compile` pass. However, this pass will require some other changes to c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: into the attention op lead to a major improvement in performance in the ROCm fork. Basically, when fused, the attention output is quantized inside the attention Triton kernel before being written out, saving data moveme...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ally, when fused, the attention output is quantized inside the attention Triton kernel before being written out, saving data movement by avoiding a full roundtrip to global memory at 16-bit precision. To avoid modifying...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: roundtrip to global memory at 16-bit precision. To avoid modifying the model definitions (approach used in ROCm fork), we are planning to do the fusion using a `torch.compile` pass. Apart from the pass implementation, t...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#16756](https://github.com/vllm-project/vllm/pull/16756) | mentioned | 0.6 | [torch.compile][ROCm] Fuse quantization onto attention using a torch.compile pass | use full cudagraphs or address the piecewise problem as described in #16220. Additionally, support for other quantization schemes can be added as well with minor additions to the… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
