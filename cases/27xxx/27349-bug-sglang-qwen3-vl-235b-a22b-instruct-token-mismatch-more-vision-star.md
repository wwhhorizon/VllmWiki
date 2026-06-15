# vllm-project/vllm#27349: [Bug]: sglang Qwen3-VL-235B-A22B-Instruct 图片token占位符报错Mismatch: More '<|vision_start|><|image_pad|><|vision_end|>' tokens found than corresponding data items provided.

| 字段 | 值 |
| --- | --- |
| Issue | [#27349](https://github.com/vllm-project/vllm/issues/27349) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: sglang Qwen3-VL-235B-A22B-Instruct 图片token占位符报错Mismatch: More '<\|vision_start\|><\|image_pad\|><\|vision_end\|>' tokens found than corresponding data items provided.

### Issue 正文摘录

### Your current environment slang 环境 ### 🐛 Describe the bug from openai import OpenAI import base64 def encode_image(image_path): with open(image_path, "rb") as image_file: return base64.b64encode(image_file.read()).decode("utf-8") base64_image = encode_image("xxm_2.png") client = OpenAI( base_url="http://******/v1/", ) completion = client.chat.completions.create( model="default", messages=[ { "role": "system", "content": [{"type": "text", "text": "You are a helpful assistant."}], }, { "role": "user", "content": [ {"type": "text", "text": "q=小熊猫，图片= ，判断query和图片是否匹配"}, { "type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}, }, ], }, ], ) print(completion.choices[0].message.content) Traceback (most recent call last): File "/mnt/geminihzceph1/geminicephfs/mmsearch-luban-universal/hz/group_semantic/user_ivycui/data/astra/test.py", line 15, in completion = client.chat.completions.create( File "/root/conda/lib/python3.10/site-packages/openai/_utils/_utils.py", line 287, in wrapper return func(*args, **kwargs) File "/root/conda/lib/python3.10/site-packages/openai/resources/chat/completions/completions.py", line 925, in create return self._post( File "/root...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: sglang Qwen3-VL-235B-A22B-Instruct 图片token占位符报错Mismatch: More '<|vision_start|><|image_pad|><|vision_end|>' tokens found than corresponding data items provided. bug ### Your current environment slang 环境 ### 🐛 Des...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: sglang Qwen3-VL-235B-A22B-Instruct 图片token占位符报错Mismatch: More '<|vision_start|><|image_pad|><|vision_end|>' tokens found than corresponding data items provided. bug ### Your current environment slang 环境 ### 🐛 Des...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: "rb") as image_file: return base64.b64encode(image_file.read()).decode("utf-8") base64_image = encode_image("xxm_2.png") client = OpenAI( base_url="http://******/v1/", ) completion = client.chat.completions.create( mode...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: sglang Qwen3-VL-235B-A22B-Instruct 图片token占位符报错Mismatch: More '<|vision_start|><|image_pad|><|vision_end|>' tokens found than corresponding data items provided. bug ### Your current environment slang 环境 ### 🐛 Des...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Your current environment slang 环境 ### 🐛 Describe the bug from openai import OpenAI import base64 def encode_image(image_path): with open(image_path, "rb") as image_file: return base64.b64encode(image_file.read()).decode...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
