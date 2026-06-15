# vllm-project/vllm#25888: [Bug]: [llama4] Llama 4 vision understanding performance degrades significantly since #21126

| 字段 | 值 |
| --- | --- |
| Issue | [#25888](https://github.com/vllm-project/vllm/issues/25888) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [llama4] Llama 4 vision understanding performance degrades significantly since #21126

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Since #21126 got merged, the vision understanding performance of Llama 4 family (Llama 4 scout / maverick) has significantly dropped: ```python import httpx from openai import OpenAI client = OpenAI(base_url="http://localhost:8080/v1", api_key="a") # This is the 4 dice image used in the vllm multimodal test CI pipeline image_url = "https://raw.githubusercontent.com/vllm-project/vllm/refs/heads/main/tests/multimodal/assets/rgba.png" messages = [{"role": "user", "content": [{"type": "text", "text": "Explain the image."}, {"type": "image_url", "image_url": {"url": image_url}}]}] for t in client.chat.completions.create(model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8", messages=messages, stream=True): if t.choices: d = t.choices[0].delta print(getattr(d, "reasoning_content", "") or d.content or "", end="", flush=True) ``` - `vllm==0.10.2rc3.dev276+ge57fc1597.cu129` The model is perfectly normal, it correctly recognizes the four colored dice. ```text The image depicts four dice in mid-air, with one die prominently displayed in the foreground and three others blurred in the background. * The dice are colored: * Red * Blue * Gre...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: [llama4] Llama 4 vision understanding performance degrades significantly since #21126 bug ### Your current environment ### 🐛 Describe the bug Since #21126 got merged, the vision understanding performance of Llama...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: family (Llama 4 scout / maverick) has significantly dropped: ```python import httpx from openai import OpenAI client = OpenAI(base_url="http://localhost:8080/v1", api_key="a") # This is the 4 dice image used in the vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: enerated graphic, rather than a photograph. The level of detail and realism suggests that it may have been created for use in a game, advertisement, or other visual media. ``` - `vllm==0.10.2rc3.dev277+g48ecb4438.cu129`...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: .completions.create(model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8", messages=messages, stream=True): if t.choices: d = t.choices[0].delta print(getattr(d, "reasoning_content", "") or d.content or "", end="",...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 1", api_key="a") # This is the 4 dice image used in the vllm multimodal test CI pipeline image_url = "https://raw.githubusercontent.com/vllm-project/vllm/refs/heads/main/tests/multimodal/assets/rgba.png" messages = [{"r...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
