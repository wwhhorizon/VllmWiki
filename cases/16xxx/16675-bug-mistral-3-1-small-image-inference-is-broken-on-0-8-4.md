# vllm-project/vllm#16675: [Bug]: Mistral 3.1 Small Image inference is broken on 0.8.4

| 字段 | 值 |
| --- | --- |
| Issue | [#16675](https://github.com/vllm-project/vllm/issues/16675) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Mistral 3.1 Small Image inference is broken on 0.8.4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tested that `vllm==0.8.3` works fine and `vllm==0.8.4` fails Server: ``` vllm serve nm-testing/Mistral-Small-3.1-24B-Instruct-2503-FP8-dynamic --disable-log-requests ``` Client: ```python from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI(api_key=openai_api_key, base_url=openai_api_base) model_id = client.models.list().data[0].id # Text inference chat_response = client.chat.completions.create( model=model_id, messages=[{ "role": "user", "content": [ {"type": "text", "text": "Who are you?"}, ], }], ) print("Text Chat completion output:", chat_response.choices[0].message.content) # Single-image input inference image_url = [ "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg", ] prompt = "What's in this image?" for img in image_url: messages=[{ "role": "user", "content": [ {"type": "text", "text": prompt}, {"type": "image_url", "image_url": {"url": img}}, ], }] chat_response = client.chat.completions.create(model=model_id, messages=messages) print("Single image Ch...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Mistral 3.1 Small Image inference is broken on 0.8.4 bug ### Your current environment ### 🐛 Describe the bug I tested that `vllm==0.8.3` works fine and `vllm==0.8.4` fails Server: ``` vllm serve nm-testing/Mistra...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nm-testing/Mistral-Small-3.1-24B-Instruct-2503-FP8-dynamic --disable-log-requests ``` Client: ```python from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI(api...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ~~~~~~~^^^^^^^^^^ ERROR 04-15 17:28:02 [core.py:387] RuntimeError: shape mismatch: value tensor of shape [1980, 5120] cannot be broadcast to indexing result of shape [7920, 5120] ``` ### Before submitting a new issue......
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 03-FP8-dynamic --disable-log-requests ``` Client: ```python from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:8000/v1" client = OpenAI(api_key=openai_api_key, base_url=openai_api_bas...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: s Server: ``` vllm serve nm-testing/Mistral-Small-3.1-24B-Instruct-2503-FP8-dynamic --disable-log-requests ``` Client: ```python from openai import OpenAI openai_api_key = "EMPTY" openai_api_base = "http://localhost:800...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
