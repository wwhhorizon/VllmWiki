# vllm-project/vllm#19687: [Bug]: Async Beam Search Doesn't Pass Multimodal Data Correctly

| 字段 | 值 |
| --- | --- |
| Issue | [#19687](https://github.com/vllm-project/vllm/issues/19687) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Async Beam Search Doesn't Pass Multimodal Data Correctly

### Issue 正文摘录

### Your current environment The async implementation of beam search is not passing multimodal data correctly, somewhat similar to this bug I had previously fixed for the synchronous implementation: https://github.com/vllm-project/vllm/issues/16240. Will open a fix with more details shortly! ### 🐛 Describe the bug Start the server: ```bash python -m vllm.entrypoints.openai.api_server --device cuda --model microsoft/Phi-3.5-vision-instruct --api-key token-abc123 --enforce-eager --trust_remote_code --max-model-len 2048 ``` Then run inference: ```python from openai import OpenAI from vllm.multimodal.utils import encode_image_base64, fetch_image MODEL_NAME = "microsoft/Phi-3.5-vision-instruct" image_url = "https://upload.wikimedia.org/wikipedia/commons/0/0b/RGBA_comp.png" # Modify OpenAI's API key and API base to use vLLM's API server. openai_api_key = "token-abc123" openai_api_base = "http://localhost:8000/v1" client = OpenAI( # defaults to os.environ.get("OPENAI_API_KEY") api_key=openai_api_key, base_url=openai_api_base, ) messages = [{ "role": "user", "content": [ { "type": "image_url", "image_url": { "url": f"data:image/jpeg;base64,{encode_image_base64(fetch_image(image_url))}" }...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Async Beam Search Doesn't Pass Multimodal Data Correctly bug ### Your current environment The async implementation of beam search is not passing multimodal data correctly, somewhat similar to this bug I had previ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Async Beam Search Doesn't Pass Multimodal Data Correctly bug ### Your current environment The async implementation of beam search is not passing multimodal data correctly, somewhat similar to this bug I had previ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: --max-model-len 2048 ``` Then run inference: ```python from openai import OpenAI from vllm.multimodal.utils import encode_image_base64, fetch_image MODEL_NAME = "microsoft/Phi-3.5-vision-instruct" image_url = "https://u...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
