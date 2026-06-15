# vllm-project/vllm#28348: [Usage]: Does vllm support max_pixels in prompt on Qwen3-VL reasoning?

| 字段 | 值 |
| --- | --- |
| Issue | [#28348](https://github.com/vllm-project/vllm/issues/28348) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does vllm support max_pixels in prompt on Qwen3-VL reasoning?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of Qwen3-VL-A3B-Instruct, I tried to set max_pixels but it doesn't work. import json import base64 import requests img_path = r".\images\MMMU\735_1.jpg" base64_str = base64.b64encode(open(img_path, 'rb').read()).decode() url = "http://71.10.29.136:8000/v1/chat/completions" payload = json.dumps( { "model": "qwen3-vl-30b", "messages": [ { "role": "system", "content": "" }, { "role": "user", "content": [ { "type": "text", "text": "Question: " }, { "type": "image_url", "image_url": { "url": f"data:image/jpg;base64,{base64_str}" }, "max_pixels": 192 * 96 ## this is not work.... ## }, { "type": "text", "text": " How does the green and photosynthesising mistletoe impact the tree it is hosting? Options:\\nA. It will grow down into the roots and kill the tree.\\nB. Mistletoe is beneficial and increases the growth of the plant.\\nC. It just uses the tree for support and does not damage it.\\nD. I don't know and don't want to guess.\\nE. It has a very damaging impact on the health of the plant but localised to the place of infection.\\n Please select the c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Does vllm support max_pixels in prompt on Qwen3-VL reasoning? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inferenc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ge]: Does vllm support max_pixels in prompt on Qwen3-VL reasoning? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: f Qwen3-VL-A3B-Instruct, I tried to set max_pixels but it doesn't work. import json import base64 import requests img_path = r".\images\MMMU\735_1.jpg" base64_str = base64.b64encode(open(img_path, 'rb').read()).decode()...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: xt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
