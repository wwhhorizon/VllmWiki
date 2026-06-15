# vllm-project/vllm#21513: [Bug]: Aborted without reason,timeout after three retries

| 字段 | 值 |
| --- | --- |
| Issue | [#21513](https://github.com/vllm-project/vllm/issues/21513) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Aborted without reason,timeout after three retries

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug > **code:** import fitz from PIL import Image import io import os from openai import OpenAI import base64 def pdf_to_png(file_path, output_dir=None, dpi=200): if output_dir is None: output_dir = os.path.dirname(file_path) try: doc = fitz.open(file_path) images = [] for page_num in range(len(doc)): page = doc.load_page(page_num) mat = fitz.Matrix(dpi / 72, dpi / 72) pix = page.get_pixmap(matrix=mat) img_data = pix.tobytes("png") img = Image.open(io.BytesIO(img_data)) images.append(img) doc.close() total_height = sum(img.height for img in images) max_width = max(img.width for img in images) combined_image = Image.new('RGB', (max_width, total_height)) y_offset =0 for img in images: combined_image.paste(img, (0, y_offset)) y_offset += img.height base_name = os.path.splitext(os.path.basename(file_path))[0] output_path = os.path.join(output_dir, f"{base_name}_combined.png") combined_image.save(output_path, format="PNG") return output_path except Exception as e: return None def encode_image(image_path): with open(image_path, "rb") as image_file: return base64.b64encode(image_file.read()).decode('utf-8') def rec_single_im(client: OpenAI,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e ### Your current environment ### 🐛 Describe the bug > **code:** import fitz from PIL import Image import io import os from openai import OpenAI import base64 def pdf_to_png(file_path, output_dir=None, dpi=200): if out...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: r, f"{base_name}_combined.png") combined_image.save(output_path, format="PNG") return output_path except Exception as e: return None def encode_image(image_path): with open(image_path, "rb") as image_file: return base64...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Aborted without reason,timeout after three retries bug;stale ### Your current environment ### 🐛 Describe the bug > **code:** import fitz from PIL import Image import io import os from openai import OpenAI import...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: QS} --tensor-parallel-size ${TENSOR_PARALLEL_SIZE} --cpu-offload-gb=200 restart: unless-stopped .env: MODEL_32=/models/Qwen2.5-VL-32B-Instruct SERVED_MODEL_NAME_32=Qwen2.5-VL-7B-Instruct TASK=transcription GPU_MEMORY_UT...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
