# vllm-project/vllm#13673: [Bug]: [V1][SpecDec] RuntimeError: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#13673](https://github.com/vllm-project/vllm/issues/13673) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cache;cuda;kernel;quantization;sampling |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [V1][SpecDec] RuntimeError: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment I'm using the `vllm/vllm-openai:v0.7.3` docker image. ### 🐛 Describe the bug I'm trying to run `[ngram]` speculative decoding on `vllm` `v1` using the following parameters on a fine-tuned [Llama-3.2-3B](https://huggingface.co/meta-llama/Llama-3.2-3B): ``` args: ["--model", "/models", "--disable-log-requests", "--max-model-len", "350", "--tensor-parallel-size", "1", "--port", "8080", "--speculative-model", "[ngram]", "--num-speculative-tokens", "3", "--ngram-prompt-lookup-max", "4", "--ngram-prompt-lookup-min", "3"] ``` The server starts up correctly, but after sending a few concurrent requests (~5 RPS), I receive ``` ERROR 02-21 06:30:25 core.py:291] EngineCore hit an exception: Traceback (most recent call last): ERROR 02-21 06:30:25 core.py:291] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 284, in run_engine_core ERROR 02-21 06:30:25 core.py:291] engine_core.run_busy_loop() ERROR 02-21 06:30:25 core.py:291] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 327, in run_busy_loop ERROR 02-21 06:30:25 core.py:291] outputs = step_fn() ERROR 02-21 06:30:25 core.py:291] ^^^^^^^^^ ERROR 02-21 06:30:25...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ug ### Your current environment I'm using the `vllm/vllm-openai:v0.7.3` docker image. ### 🐛 Describe the bug I'm trying to run `[ngram]` speculative decoding on `vllm` `v1` using the following parameters on a fine-tuned...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: decoding on `vllm` `v1` using the following parameters on a fine-tuned [Llama-3.2-3B](https://huggingface.co/meta-llama/Llama-3.2-3B): ``` args: ["--model", "/models", "--disable-log-requests", "--max-model-len", "350",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: .7.3` docker image. ### 🐛 Describe the bug I'm trying to run `[ngram]` speculative decoding on `vllm` `v1` using the following parameters on a fine-tuned [Llama-3.2-3B](https://huggingface.co/meta-llama/Llama-3.2-3B): `...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: media_path=None, download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', max_model_len=350, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', dist...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: dtype='auto', kv_cache_dtype='auto', max_model_len=350, guided_decoding_backend='xgrammar', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
