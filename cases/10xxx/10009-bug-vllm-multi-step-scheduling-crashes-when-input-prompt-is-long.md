# vllm-project/vllm#10009: [Bug]: vLLM multi-step scheduling crashes when input prompt is long

| 字段 | 值 |
| --- | --- |
| Issue | [#10009](https://github.com/vllm-project/vllm/issues/10009) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM multi-step scheduling crashes when input prompt is long

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Command to start vllm server: `python -m vllm.entrypoints.openai.api_server --disable-log-requests --trust-remote-code --model meta-llama/Meta-Llama-3.1-8B-Instruct --tokenizer meta-llama/Meta-Llama-3.1-8B-Instruct --num-scheduler-steps 8` Query the vllm server using the following piece of code ``` def _get_payload(prompt: str): return { 'messages': [{ 'role': 'user', 'content': prompt }], 'model': 'meta-llama/Meta-Llama-3.1-8B-Instruct', 'n': 1, 'best_of': 1, 'use_beam_search': False, 'temperature': 0.0, 'top_p': 1.0, 'max_tokens': 50, 'ignore_eos': True, 'stream': False, } # Generate a really long input prompt of length 10K prompt = generate_long_prompt(length=10K) payload = _get_payload(prompt) session = aiohttp.ClientSession() async with session.post('http://localhost:8000/v1/chat/completions', headers=headers, json=payload) as response: data = await response.text() print(response.ok) await session.close() ``` The vllm server crashes with the following error ``` CRITICAL 11-04 23:40:27 launcher.py:72] AsyncLLMEngine has failed, terminating server process INFO: 127.0.0.1:33322 - "POST /v1/ch...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: vLLM multi-step scheduling crashes when input prompt is long bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Command to start vllm server: `python -m vllm.entrypo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t be incor rect.\nFor debugging consider passing CUDA_LAUNCH_BLOCKING=1\nCompile with `TORCH_USE_CUDA_DSA` to enable dev ice-side assertions.\n') ERROR 11-04 23:40:27 engine.py:158] Traceback (most recent cal
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: -8B-Instruct', 'n': 1, 'best_of': 1, 'use_beam_search': False, 'temperature': 0.0, 'top_p': 1.0, 'max_tokens': 50, 'ignore_eos': True, 'stream': False, } # Generate a really long input prompt of length 10K prompt = gene...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: uct', 'n': 1, 'best_of': 1, 'use_beam_search': False, 'temperature': 0.0, 'top_p': 1.0, 'max_tokens': 50, 'ignore_eos': True, 'stream': False, } # Generate a really long input prompt of length 10K prompt = generate_long...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: when input prompt is long bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Command to start vllm server: `python -m vllm.entrypoints.openai.api_server --disable-log-reque...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
