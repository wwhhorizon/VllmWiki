# vllm-project/vllm#10931: [Bug]: vLLM (running HuggingFaceTB/SmolVLM-Instruct) crashes with a 500 when making concurrent requests through the OpenAI compatible HTTP server

| 字段 | 值 |
| --- | --- |
| Issue | [#10931](https://github.com/vllm-project/vllm/issues/10931) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM (running HuggingFaceTB/SmolVLM-Instruct) crashes with a 500 when making concurrent requests through the OpenAI compatible HTTP server

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Starting the vllm sever with the following command: ``` vllm serve HuggingFaceTB/SmolVLM-Instruct --dtype bfloat16 ``` Snippet used to fire requests to the OpenAI compatible server ``` curl -X POST \ 'http://localhost:8000/v1/chat/completions' \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer abc' \ -d '{ "model": "HuggingFaceTB/SmolVLM-Instruct", "max_tokens": 512, "temperature": 0.4, "top_p": 0.8, "frequency_penalty": 0.2, "messages": [ { "role": "user", "content": [ { "type": "image_url", "image_url": { "url": } }, { "type": "text", "text": "Please provide a detailed, flowing description that could have been used as a prompt to generate this image.\nYour description should naturally incorporate:\n- The main subjects, capturing their specific features, expressions, poses, and distinguishing characteristics\n- The complete setting and background elements, from foreground to distance\n- The color palette, quality of light, and atmospheric conditions\n- Any striking or unusual details that catch the eye\n- How different elements are positioned and interact spatially with each oth...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vLLM (running HuggingFaceTB/SmolVLM-Instruct) crashes with a 500 when making concurrent requests through the OpenAI compatible HTTP server bug ### Your current environment ### Model Input Dumps _No response_ ###...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: hon3.11/site-packages/aiohttp/streams.py", line 344, in _wait await waiter asyncio.exceptions.CancelledError The above exception was the direct cause of the following exception: Traceback (most recent call last): File "...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n should naturally incorporate:\n- The main subjects, capturing their specific features, expressions, poses, and distinguishing characteristics\n- The complete setting and background elements, from foreground to distanc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: the following command: ``` vllm serve HuggingFaceTB/SmolVLM-Instruct --dtype bfloat16 ``` Snippet used to fire requests to the OpenAI compatible server ``` curl -X POST \ 'http://localhost:8000/v1/chat/completions' \ -H...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: vLLM (running HuggingFaceTB/SmolVLM-Instruct) crashes with a 500 when making concurrent requests through the OpenAI compatible HTTP server bug ### Your current environment ### Model Input Dumps _No response_ ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
