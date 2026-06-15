# vllm-project/vllm#22911: [Bug]: Inference fails when there is space character in local file path

| 字段 | 值 |
| --- | --- |
| Issue | [#22911](https://github.com/vllm-project/vllm/issues/22911) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inference fails when there is space character in local file path

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When sending a local image file as `image_url` in form of `file:` uri, `vllm` crashes with the underlying error being file not found. ```python # offline_inference.py from pathlib import Path from vllm import LLM from vllm.assets.image import ImageAsset import numpy as np from PIL import Image image_path1 = Path(__file__).parent / "no_error.jpg" image_path2 = Path(__file__).parent / "this errors.jpg" # <-- DUE TO THIS!! Image.fromarray(np.random.randint(0, 256, (224, 224), dtype=np.uint8)).save(image_path1) Image.fromarray(np.random.randint(0, 256, (224, 224), dtype=np.uint8)).save(image_path2) assert image_path1.is_file() and image_path2.is_file() llm = LLM( model="hfl/Qwen2.5-VL-3B-Instruct-GPTQ-Int4", allowed_local_media_path=str(Path(__file__).parent), ) image_url1 = image_path1.as_uri() image_url2 = image_path2.as_uri() print(image_path1, image_url1) print(image_path2, image_url2) conversation = [ {"role": "system", "content": "You are a helpful assistant"}, {"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hello! How can I assist you today?"}, { "role": "user", "content": [ {"type": "image_url", "image...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ) assert image_path1.is_file() and image_path2.is_file() llm = LLM( model="hfl/Qwen2.5-VL-3B-Instruct-GPTQ-Int4", allowed_local_media_path=str(Path(__file__).parent), ) image_url1 = image_path1.as_uri() image_url2 = ima...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ror being file not found. ```python # offline_inference.py from pathlib import Path from vllm import LLM from vllm.assets.image import ImageAsset import numpy as np from PIL import Image image_path1 = Path(__file__).par...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: <-- DUE TO THIS!! Image.fromarray(np.random.randint(0, 256, (224, 224), dtype=np.uint8)).save(image_path1) Image.fromarray(np.random.randint(0, 256, (224, 224), dtype=np.uint8)).save(image_path2) assert image_path1.is_f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: it. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tive_decoding attention;cache;cuda;kernel;operator;quantization;sampling;triton build_error;crash;nan_inf;slowdown dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
