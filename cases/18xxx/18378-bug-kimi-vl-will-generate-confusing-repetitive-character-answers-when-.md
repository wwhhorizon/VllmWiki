# vllm-project/vllm#18378: [Bug]: Kimi_VL will generate confusing/repetitive character answers when n > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#18378](https://github.com/vllm-project/vllm/issues/18378) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Kimi_VL will generate confusing/repetitive character answers when n > 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when SamplingParams.n > 1, the output result is some meaningless characters or keeps repeating.(See the comments below) But when SamplingParams.n = 1, the result is normal. I also tested not using the V1 engine, at this time, the results when n=1 or n>1 are all meaningless characters. data: hiyouga/geometry3k env: 8*A100-80G ```python from transformers import AutoProcessor from transformers import AutoTokenizer import re import datasets from io import BytesIO from typing import Union from PIL import Image from qwen_vl_utils import fetch_image from vllm import LLM, SamplingParams def _build_messages(example: dict): messages: list = example.pop("prompt") if "images" in example or "videos" in example: for message in messages: content = message["content"] content_list = [] for segment in re.split("( | )", content): if segment == " ": content_list.append({"type": "image"}) elif segment == " ": content_list.append({"type": "video"}) else: content_list.append({"type": "text", "text": segment}) message["content"] = content_list return messages def process_image(image: Union[dict, Image.Image]) -> Image.Image: if isinstance(image, Image.I...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: . data: hiyouga/geometry3k env: 8*A100-80G ```python from transformers import AutoProcessor from transformers import AutoTokenizer import re import datasets from io import BytesIO from typing import Union from PIL impor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: or n>1 are all meaningless characters. data: hiyouga/geometry3k env: 8*A100-80G ```python from transformers import AutoProcessor from transformers import AutoTokenizer import re import datasets from io import BytesIO fr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: i_VL will generate confusing/repetitive character answers when n > 1 bug;stale ### Your current environment ### 🐛 Describe the bug when SamplingParams.n > 1, the output result is some meaningless characters or keeps rep...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m io import BytesIO from typing import Union from PIL import Image from qwen_vl_utils import fetch_image from vllm import LLM, SamplingParams def _build_messages(example: dict): messages: list = example.pop("prompt") if...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
