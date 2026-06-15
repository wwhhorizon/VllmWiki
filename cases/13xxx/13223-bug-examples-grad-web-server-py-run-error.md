# vllm-project/vllm#13223: [Bug]: examples/grad_web_server.py run error

| 字段 | 值 |
| --- | --- |
| Issue | [#13223](https://github.com/vllm-project/vllm/issues/13223) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: examples/grad_web_server.py run error

### Issue 正文摘录

### Your current environment vllm 0.7.2 pytorch 2.4 cuda 12.1 ### 🐛 Describe the bug when chat with deepsek -r1-disill-qwen-7B when execte this funtion raise error def http_bot(prompt): headers = {"User-Agent": "vLLM Client"} pload = { "prompt": prompt, "stream": True, "max_tokens": 128, } response = requests.post(args.model_url, headers=headers, json=pload, stream=True) for chunk in response.iter_lines(chunk_size=8192, decode_unicode=False, delimiter=b"\0"): if chunk: s_data = chunk.decode("utf-8") print("str:",s_data) data = json.loads(s_data) output = data["text"][0] yield output the errors is as follows whatever i input, the results of chunk using json.loads is always wrong: {"text": ["himoon( 981215 ) \n\n is needed... \n\nI need to make a function that, given a number, returns a string indicating whether the number is prime, composite, or neither (i.e., neither prime nor composite). But I have to include \"hi-1\" in the string as a substring.\n \n\nSure! Here's a function that meets your requirements:\n\n```python\ndef check_number(n):\n if n is needed... \n\nI need to make a function that, given a number, returns a string indicating whether the number is prime, composite, o...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: examples/grad_web_server.py run error bug;stale ### Your current environment vllm 0.7.2 pytorch 2.4 cuda 12.1 ### 🐛 Describe the bug when chat with deepsek -r1-disill-qwen-7B when execte this funtion raise error...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ^^^^^^^^^^^^ File " /lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 2461, in run_sync_in_worker_thread return await future ^^^^^^^^^^^^ File " /lib/python3.11/site-packages/anyio/_backends/_asyncio.py",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: run error bug;stale ### Your current environment vllm 0.7.2 pytorch 2.4 cuda 12.1 ### 🐛 Describe the bug when chat with deepsek -r1-disill-qwen-7B when execte this funtion raise error def http_bot(prompt): headers = {"U...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: decode_unicode=False, delimiter=b"\0"): if chunk: s_data = chunk.decode("utf-8")
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 2.4 cuda 12.1 ### 🐛 Describe the bug when chat with deepsek -r1-disill-qwen-7B when execte this funtion raise error def http_bot(prompt): headers = {"User-Agent": "vLLM Client"} pload = { "promp

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
