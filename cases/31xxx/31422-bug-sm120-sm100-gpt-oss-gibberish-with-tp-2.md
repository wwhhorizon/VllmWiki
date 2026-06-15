# vllm-project/vllm#31422: [Bug]: SM120/SM100: gpt-oss gibberish with tp=2

| 字段 | 值 |
| --- | --- |
| Issue | [#31422](https://github.com/vllm-project/vllm/issues/31422) |
| 状态 | open |
| 标签 | bug;stale;gpt-oss;nvidia |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SM120/SM100: gpt-oss gibberish with tp=2

### Issue 正文摘录

### Environment Docker Container: nvcr.io/nvidia/vllm:25.12-py3 vLLM Version: 0.11.1+9114fd76 (also reproduced on 0.13.0) CUDA: 13.1 GPU: 2x NVIDIA RTX 6000 Blackwell (SM120) Model: openai/gpt-oss-120b ```bash python3 -m vllm.entrypoints.openai.api_server \ --model "/huggingface_hub/models/openai/gpt_oss_120b" \ --host 0.0.0.0 \ --port 8355 \ --tensor-parallel-size 2 \ --max-model-len 32768 \ --max-num-seqs 4 \ --gpu-memory-utilization 0.95 \ --kv-cache-dtype=auto \ --async-scheduling ``` ### 🐛 Describe the bug ## Bug Description **Summary:** When running gpt-oss-120b with `--tensor-parallel-size 2` on Blackwell GPUs, the first request returns correct output, but all subsequent requests return empty `content: None` with `reasoning_content: ''` despite usage stats showing tokens were generated. **Steps to Reproduce:** 1. Start vLLM server with above command 2. Send a chat completion request → Works correctly 3. Send another chat completion request (same or different prompt) → Fails **Actual Behavior:** First request succeeds. All subsequent requests return: ```python { 'choices': [{ 'message': { 'role': 'assistant', 'content': None, # <-- Should contain generated text 'tool_calls':...

## 现有链接修复摘要

#31607 [Bugfix] Add SM 12.1 support + Fix GPT-OSS Harmony garbled reasoning and HarmonyError crashes

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 0: gpt-oss gibberish with tp=2 bug;stale;gpt-oss;nvidia ### Environment Docker Container: nvcr.io/nvidia/vllm:25.12-py3 vLLM Version: 0.11.1+9114fd76 (also reproduced on 0.13.0) CUDA: 13.1 GPU: 2x NVIDIA RTX 6000 Blackw...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: SM120/SM100: gpt-oss gibberish with tp=2 bug;stale;gpt-oss;nvidia ### Environment Docker Container: nvcr.io/nvidia/vllm:25.12-py3 vLLM Version: 0.11.1+9114fd76 (also reproduced on 0.13.0) CUDA: 13.1 GPU: 2x NVIDI...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: SM120/SM100: gpt-oss gibberish with tp=2 bug;stale;gpt-oss;nvidia ### Environment Docker Container: nvcr.io/nvidia/vllm:25.12-py3 vLLM Version: 0.11.1+9114fd76 (also reproduced on 0.13.0) CUDA: 13.1 GPU: 2x NVIDI...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: SM120/SM100: gpt-oss gibberish with tp=2 bug;stale;gpt-oss;nvidia ### Environment Docker Container: nvcr.io/nvidia/vllm:25.12-py3 vLLM Version: 0.11.1+9114fd76 (also reproduced on 0.13.0) CUDA: 13.1 GPU: 2x NVIDI...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ainer: nvcr.io/nvidia/vllm:25.12-py3 vLLM Version: 0.11.1+9114fd76 (also reproduced on 0.13.0) CUDA: 13.1 GPU: 2x NVIDIA RTX 6000 Blackwell (SM120) Model: openai/gpt-oss-120b ```bash python3 -m vllm.entrypoints.openai.a...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31607](https://github.com/vllm-project/vllm/pull/31607) | closes_keyword | 0.95 | [Bugfix] Add SM 12.1 support + Fix GPT-OSS Harmony garbled reasoning and HarmonyError crashes | fix) - Related: #31422 (SM120 gibberish with tp=2 — different root cause: prefix caching + TP) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
