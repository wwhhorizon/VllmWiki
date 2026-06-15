# vllm-project/vllm#14353: [Bug]: Memory leak due to LLMEngine.seq_id_to_seq_group

| 字段 | 值 |
| --- | --- |
| Issue | [#14353](https://github.com/vllm-project/vllm/issues/14353) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Memory leak due to LLMEngine.seq_id_to_seq_group

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM does not release the `LLMEngine.seq_id_to_seq_group`, so the requests are always stored in memory, eventually leading to excessive memory usage and Out-of-Memory (OOM) errors. Code to reproduce: ```python import torch from torch.distributed import breakpoint from vllm import LLM, SamplingParams from PIL import Image import resource import math from datetime import datetime MODEL_PATH = "Qwen/Qwen2.5-VL-3B-Instruct" TEST_IMG_PATH = "test.jpeg" VISION_PROMPT_TEMPLATE = ( " system\nYou are a helpful assistant. \n" " user\nQuestion No.{idx:08} " "Conclude this image in 10 words. \n assistant\n " ) def construct_query(idx: int, max_pixels: int = 2048 * 2048, min_pixels: int = 512 * 512): prompt = VISION_PROMPT_TEMPLATE.format(idx=idx) image = Image.open(TEST_IMG_PATH) if (image.width * image.height) > max_pixels: resize_factor = math.sqrt(max_pixels / (image.width * image.height)) width, height = int(image.width * resize_factor), int(image.height * resize_factor) image = image.resize((width, height)) if (image.width * image.height) 0: breakpoint() print("===========================================") data = [construct_query(idx) f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ory usage and Out-of-Memory (OOM) errors. Code to reproduce: ```python import torch from torch.distributed import breakpoint from vllm import LLM, SamplingParams from PIL import Image import resource import math from da...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: import Image import resource import math from datetime import datetime MODEL_PATH = "Qwen/Qwen2.5-VL-3B-Instruct" TEST_IMG_PATH = "test.jpeg" VISION_PROMPT_TEMPLATE = ( " system\nYou are a helpful assistant. \n" " user\...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: age](https://github.com/user-attachments/assets/6842cb1f-11f8-4e79-8a19-dfa33bf51578) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 78) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ading to excessive memory usage and Out-of-Memory (OOM) errors. Code to reproduce: ```python import torch from torch.distributed import breakpoint from vllm import LLM, SamplingParams from PIL import Image import resour...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
