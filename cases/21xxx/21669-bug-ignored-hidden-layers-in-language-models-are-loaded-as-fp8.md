# vllm-project/vllm#21669: [Bug]: Ignored Hidden Layers in Language Models Are Loaded as FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#21669](https://github.com/vllm-project/vllm/issues/21669) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;quantization;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ignored Hidden Layers in Language Models Are Loaded as FP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I used the following code to quantize the qwen25vl model. Please note that I kept the linear parts in model.layers.0 as bf16. ```python import argparse import dataclasses import os import shutil from pathlib import Path from llmcompressor.transformers import oneshot from llmcompressor.modifiers.quantization import QuantizationModifier from transformers import Qwen2_5_VLForConditionalGeneration, Qwen2_5_VLProcessor from llmcompressor.utils import dispatch_for_generation import base64 from qwen_vl_utils import process_vision_info question = '''What can be seen in the picture?''' MIN_PIXELS = 4 * 28 * 28 max_pixels = 262144 parser = argparse.ArgumentParser() parser.add_argument("--output", "-o", required=True, type=str, help="path to output checkpoint") parser.add_argument("--model-path", "-m", required=True, type=str, help="path to input checkpoint") def read_image(path): with open(path, 'rb') as f: return base64.b64encode(f.read()).decode('utf-8') def main(args): # Create LLM instance from arguments model = Qwen2_5_VLForConditionalGeneration.from_pretrained(args.model_path, device_map="auto", torch_dtype="auto") processor = Qwen2_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e note that I kept the linear parts in model.layers.0 as bf16. ```python import argparse import dataclasses import os import shutil from pathlib import Path from llmcompressor.transformers import oneshot from llmcompres...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Ignored Hidden Layers in Language Models Are Loaded as FP8 bug;stale ### Your current environment ### 🐛 Describe the bug I used the following code to quantize the qwen25vl model. Please note that I kept the linea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: mage_data, padding=False, return_tensors="pt", ).to("cuda") output = model.generate(**inputs, temperature = 1e-8, max_new_tokens = 100) print(processor.decode(output[0], skip_special_tokens=True)) print("===============...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Ignored Hidden Layers in Language Models Are Loaded as FP8 bug;stale ### Your current environment ### 🐛 Describe the bug I used the following code to quantize the qwen25vl model. Please note that I kept the linea...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Ignored Hidden Layers in Language Models Are Loaded as FP8 bug;stale ### Your current environment ### 🐛 Describe the bug I used the following code to quantize the qwen25vl model. Please note that I kept the linea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
