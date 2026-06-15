# vllm-project/vllm#20427: [Bug]: Error decoding Tensors via ImageEmbeddingMediaIO

| 字段 | 值 |
| --- | --- |
| Issue | [#20427](https://github.com/vllm-project/vllm/issues/20427) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error decoding Tensors via ImageEmbeddingMediaIO

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using `ImageEmbeddingMediaIO` to encode and later decode a tensor fails raising a `pickle.UnpicklingError` exception. Sample code: ```python from vllm.multimodal.image import ImageEmbeddingMediaIO import torch tensor_sample= torch.full((6, 512, 512), 1.0,dtype=torch.float16) image_embeds_media_io = ImageEmbeddingMediaIO() encoded_tensor = image_embeds_media_io.encode_base64(tensor_sample) decoded_tensor = image_embeds_media_io.load_base64("",encoded_tensor) ``` Error: ``` (vllm) mgazz@mgazz-vllm-devpod-6c47989df9-hstsz:~/vllm$ python test.py Traceback (most recent call last): File "/workspace/vllm/test.py", line 10, in decoded_tensor = image_embeds_media_io.load_base64("",encoded_tensor) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/workspace/vllm/vllm/multimodal/image.py", line 97, in load_base64 return self.load_bytes(pybase64.b64decode(data, validate=True)) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/workspace/vllm/vllm/multimodal/image.py", line 94, in load_bytes return torch.load(buffer, weights_only=True) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/workspace/vllm/.venv/lib/python3.12/site-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lingError` exception. Sample code: ```python from vllm.multimodal.image import ImageEmbeddingMediaIO import torch tensor_sample= torch.full((6, 512, 512), 1.0,dtype=torch.float16) image_embeds_media_io = ImageEmbeddingM...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: eddingMediaIO import torch tensor_sample= torch.full((6, 512, 512), 1.0,dtype=torch.float16) image_embeds_media_io = ImageEmbeddingMediaIO() encoded_tensor = image_embeds_media_io.encode_base64(tensor_sample) decoded_te...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: a `pickle.UnpicklingError` exception. Sample code: ```python from vllm.multimodal.image import ImageEmbeddingMediaIO import torch tensor_sample= torch.full((6, 512, 512), 1.0,dtype=torch.float16) image_embeds_media_io =...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Error decoding Tensors via ImageEmbeddingMediaIO bug;stale ### Your current environment ### 🐛 Describe the bug Using `ImageEmbeddingMediaIO` to encode and later decode a tensor fails raising a `pickle.UnpicklingE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
