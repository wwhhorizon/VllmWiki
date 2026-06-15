# vllm-project/vllm#14500: [Bug]:  ValueError: Expected a torch.device with a specified index or an integer, but got:cuda

| 字段 | 值 |
| --- | --- |
| Issue | [#14500](https://github.com/vllm-project/vllm/issues/14500) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  ValueError: Expected a torch.device with a specified index or an integer, but got:cuda

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug https://github.com/ROCm/ROCm/issues/3914#issuecomment-2530568375，I installed vllm on wsl2 according to this method, but I encountered problems when I wanted to use vllm to perform "microsoft/Phi-4-mini-instruct" model inference ```>>> from vllm import LLM, SamplingParams INFO 03-09 01:21:09 [__init__.py:264] Automatically detected platform rocm. WARNING 03-09 01:21:09 [rocm.py:25] Failed to import from amdsmi with ModuleNotFoundError("No module named 'amdsmi'") >>> prompts = ["The capital of France is"] >>> sampling_params = SamplingParams(temperature=0.8, top_p=0.95) >>> llm = LLM(model="microsoft/Phi-4-mini-instruct") INFO 03-09 01:21:36 [config.py:208] Replacing legacy 'type' key with 'rope_type' INFO 03-09 01:21:42 [config.py:576] This model supports multiple tasks: {'score', 'generate', 'reward', 'embed', 'classify'}. Defaulting to 'generate'. INFO 03-09 01:21:42 [config.py:1521] Disabled the custom all-reduce kernel because it is not supported on AMD GPUs. WARNING 03-09 01:21:42 [arg_utils.py:1276] The model has a long context length (131072). This may cause OOM errors during the initial memory profiling phase, or result in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: ValueError: Expected a torch.device with a specified index or an integer, but got:cuda bug;stale ### Your current environment ### 🐛 Describe the bug https://github.com/ROCm/ROCm/issues/3914#issuecomment-253056837...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_al...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: r: Expected a torch.device with a specified index or an integer, but got:cuda bug;stale ### Your current environment ### 🐛 Describe the bug https://github.com/ROCm/ROCm/issues/3914#issuecomment-2530568375，I installed vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ed a torch.device with a specified index or an integer, but got:cuda bug;stale ### Your current environment ### 🐛 Describe the bug https://github.com/ROCm/ROCm/issues/3914#issuecomment-2530568375，I installed vllm on wsl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
