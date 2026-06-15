# vllm-project/vllm#29778: [Bug]: Using image_embeds to input multimodal image embedding results causes array out-of-bounds during processing.

| 字段 | 值 |
| --- | --- |
| Issue | [#29778](https://github.com/vllm-project/vllm/issues/29778) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Using image_embeds to input multimodal image embedding results causes array out-of-bounds during processing.

### Issue 正文摘录

### Your current environment vllm version: 0.10.0rc2 ### 🐛 Describe the bug async def all_mm_data(self) -> Optional[MultiModalDataDict]: if not self._items_by_modality: return None mm_inputs = {} items_by_modality = { modality: await asyncio.gather(*items) for modality, items in self._items_by_modality.items() } if "image" in items_by_modality and "image_embeds" in items_by_modality: raise ValueError( "Mixing raw image and embedding inputs is not allowed" ) if "image_embeds" in items_by_modality: image_embeds_lst = items_by_modality["image_embeds"] if len(image_embeds_lst) > 1: raise ValueError( "Only one message can have {'type': 'image_embeds'}" ) mm_inputs["image"] = image_embeds_lst[0] if "image" in items_by_modality: mm_inputs["image"] = items_by_modality["image"] # A list of images if "audio" in items_by_modality: mm_inputs["audio"] = items_by_modality["audio"] # A list of audios if "video" in items_by_modality: mm_inputs["video"] = items_by_modality["video"] # A list of videos return mm_inputs -------------------------------------------------- The code here retrieves `mm_inputs["image"] = image_embeds_lst[0]`, which is a dictionary. In the following code, `for i, item in en...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Using image_embeds to input multimodal image embedding results causes array out-of-bounds during processing. bug ### Your current environment vllm version: 0.10.0rc2 ### 🐛 Describe the bug async def all_mm_data(s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: out-of-bounds during processing. bug ### Your current environment vllm version: 0.10.0rc2 ### 🐛 Describe the bug async def all_mm_data(self) -> Optional[MultiModalDataDict]: if not self._items_by_modality: return None m...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: , mm_items: MultiModalDataItems, hf_processor_mm_kwargs: Mapping[str, object], tokenization_kwargs: Mapping[str, object], *, mm_uuids: Optional[MultiModalUUIDDict] = None, ) -> MultiModalHashes: """Create MM hashes to b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ut? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
