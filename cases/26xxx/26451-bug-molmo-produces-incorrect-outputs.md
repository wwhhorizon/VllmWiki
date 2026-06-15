# vllm-project/vllm#26451: [Bug]: Molmo produces incorrect outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#26451](https://github.com/vllm-project/vllm/issues/26451) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Molmo produces incorrect outputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Molmo produces incorrect outputs for vLLM >= 0.7.3. The issue is most obvious when using it for pointing, for example: ``` from vllm import LLM from vllm.sampling_params import SamplingParams import requests from PIL import Image model = LLM( model="allenai/Molmo-7B-D-0924", trust_remote_code=True, dtype='bfloat16', gpu_memory_utilization=0.95, ) sampling_params = SamplingParams( max_tokens=64, temperature=0, ) image_url = "https://www.visitscotland.com/binaries/content/gallery/visitscotland/cms-images/2022/06/24/clashnessie-bay-car-road" image = Image.open(requests.get(image_url, stream=True).raw) inputs = [ { "prompt": "Point to the car.", "multi_modal_data": {"image": image}, } ] outputs = model.generate(inputs, sampling_params=sampling_params) print(outputs[0].outputs[0].text) ``` - The transformer model without vLLM produces ` car ` for this query - vllm==0.7.2 produces ` car `, which is close - vllm==0.7.3 produces ` car `, which is way off In general, in vLLM 0.7.3 Molmo returns near-random points for almost all queries on images with the height or width > 336px. I believe the issue is changes in the image preprocessor. In...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: is most obvious when using it for pointing, for example: ``` from vllm import LLM from vllm.sampling_params import SamplingParams import requests from PIL import Image model = LLM( model="allenai/Molmo-7B-D-0924", trust...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ling_params import SamplingParams import requests from PIL import Image model = LLM( model="allenai/Molmo-7B-D-0924", trust_remote_code=True, dtype='bfloat16', gpu_memory_utilization=0.95, ) sampling_params = SamplingPa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: LM( model="allenai/Molmo-7B-D-0924", trust_remote_code=True, dtype='bfloat16', gpu_memory_utilization=0.95, ) sampling_params = SamplingParams( max_tokens=64, temperature=0, ) image_url = "https://www.visitscotland.com/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ge. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: m vllm import LLM from vllm.sampling_params import SamplingParams import requests from PIL import Image model = LLM( model="allenai/Molmo-7B-D-0924", trust_remote_code=True, dtype='bfloat16', gpu_memory_utilization=0.95...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
