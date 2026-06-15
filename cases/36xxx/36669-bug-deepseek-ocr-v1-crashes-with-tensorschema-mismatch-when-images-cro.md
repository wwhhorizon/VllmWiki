# vllm-project/vllm#36669: [Bug]: DeepSeek-OCR v1 crashes with TensorSchema mismatch when images_crop is empty (small images ≤640px)

| 字段 | 值 |
| --- | --- |
| Issue | [#36669](https://github.com/vllm-project/vllm/issues/36669) |
| 状态 | closed |
| 标签 | torch.compile |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-OCR v1 crashes with TensorSchema mismatch when images_crop is empty (small images ≤640px)

### Issue 正文摘录

### Your current environment - **vLLM version:** 0.17.0 (also current `main`) - **GPU:** NVIDIA A100 - **Python:** 3.12 - **CUDA:** 13.1 ### Model `deepseek-ai/DeepSeek-OCR` (`DeepseekOCRForCausalLM`) ### 🐛 Describe the bug `DeepseekOCRForCausalLM` crashes with a fatal `EngineDeadError` when processing images that do **not** require cropping (images ≤ 640×640 pixels). The V1 engine dies on the first such request and all subsequent requests fail. **Error:** ``` ValueError: images_crop dim[2] expected 1024, got 640. Expected shape: ('bnp', 3, 1024, 1024), but got torch.Size([0, 3, 640, 640]) ``` **Root cause:** In `_parse_and_validate_image_input` ([deepseek_ocr.py#L455](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/deepseek_ocr.py#L455)), when `images_crop.numel() == 0` (no crops needed for small images), the code sets `image_size = base_size = 1024`. But the empty tensor's shape is still `(0, 3, 640, 640)` — the `image_size` dimension carries 640 from the Gundam processor preset. `TensorSchema.validate()` then sees the mismatch: expected 1024, got 640. **The fix is trivial** — remove the `numel() > 0` guard since `shape[-1]` is valid on zero-element ten...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: sorSchema mismatch when images_crop is empty (small images ≤640px) torch.compile ### Your current environment - **vLLM version:** 0.17.0 (also current `main`) - **GPU:** NVIDIA A100 - **Python:** 3.12 - **CUDA:** 13.1 #...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: DeepSeek-OCR v1 crashes with TensorSchema mismatch when images_crop is empty (small images ≤640px) torch.compile ### Your current environment - **vLLM version:** 0.17.0 (also current `main`) - **GPU:** NVIDIA A10...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: CR", hf_overrides={"architectures": ["DeepseekOCRForCausalLM"]}, dtype="bfloat16", max_model_len=4096, ) # This will crash with EngineDeadError output = llm.generate( [{"prompt": " \nDescribe this image.", "multi_modal_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: DeepSeek-OCR v1 crashes with TensorSchema mismatch when images_crop is empty (small images ≤640px) torch.compile ### Your current environment - **vLLM version:** 0.17.0 (also current `main`) - **GPU:** NVIDIA A10...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `main`) - **GPU:** NVIDIA A100 - **Python:** 3.12 - **CUDA:** 13.1 ### Model `deepseek-ai/DeepSeek-OCR` (`DeepseekOCRForCausalLM`) ### 🐛 Describe the bug `DeepseekOCRForCausalLM` crashes with a fatal `EngineDeadError` w...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
