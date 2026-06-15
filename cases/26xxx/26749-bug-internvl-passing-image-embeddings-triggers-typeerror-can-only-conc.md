# vllm-project/vllm#26749: [Bug]: InternVL: passing image embeddings triggers TypeError: can only concatenate tuple (not "Tensor") to tuple in get_multimodal_embeddings, and v1 sanity check then expects a sequence of 2D tensors

| 字段 | 值 |
| --- | --- |
| Issue | [#26749](https://github.com/vllm-project/vllm/issues/26749) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: InternVL: passing image embeddings triggers TypeError: can only concatenate tuple (not "Tensor") to tuple in get_multimodal_embeddings, and v1 sanity check then expects a sequence of 2D tensors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Title InternVL: passing image **embeddings** triggers `TypeError: can only concatenate tuple (not "Tensor") to tuple` in `get_multimodal_embeddings`, and v1 sanity check then expects a sequence of 2D tensors ## Environment - vLLM: 0.10.2 (also reproducible on 0.10.1) - Python: 3.11.x - Model: `InternVL3_5-1B` (HF, `trust_remote_code=True`) ## Minimal Repro (image **embeddings** input) ```python from vllm import LLM import torch llm = LLM(model="InternVL3_5-1B", trust_remote_code=True) prompt = "USER: \nWhat is this image?\nASSISTANT:" # 3D embeddings: [B, T, H] just to illustrate the bug (B=1 here) # H equals the LM hidden_size for the given weight; using 1024 to reproduce. image_embeds = torch.randn(1, 16, 1024) out = llm.generate({ "prompt": prompt, "multi_modal_data": {"image": image_embeds}, # or {"images": image_embeds} }) print(out[0].outputs[0].text) ``` ## Actual Behavior / Stack On 0.10.2: ``` File ".../vllm/model_executor/models/internvl.py", line 1328, in get_multimodal_embeddings multimodal_embeddings += vision_embeddings TypeError: can only concatenate tuple (not "Tensor") to tuple ``` If we monkey-patch around the...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: InternVL: passing image embeddings triggers TypeError: can only concatenate tuple (not "Tensor") to tuple in get_multimodal_embeddings, and v1 sanity check then expects a sequence of 2D tensors bug ### Your curre...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: cts a sequence of 2D tensors ## Environment - vLLM: 0.10.2 (also reproducible on 0.10.1) - Python: 3.11.x - Model: `InternVL3_5-1B` (HF, `trust_remote_code=True`) ## Minimal Repro (image **embeddings** input) ```python...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: en expects a sequence of 2D tensors ## Environment - vLLM: 0.10.2 (also reproducible on 0.10.1) - Python: 3.11.x - Model: `InternVL3_5-1B` (HF, `trust_remote_code=True`) ## Minimal Repro (image **embeddings** input) ```...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: in 0.10.1/0.10.2 this path is broken due to type/shape inconsistencies, blocking these use-cases. ## Proposed Fix (minimal) Normalize to a sequence of 2D tensors before concatenation. For example, in `vllm/model_executo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ecutor is safer. - Pixel input path works and can be used as a temporary fallback, but defeats the purpose of passing precomputed embeddings. ## Version Matrix - ✅ Pixel input: OK on 0.10.1 and 0.10.2 - ❌ Embedding inpu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
