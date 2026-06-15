# vllm-project/vllm#10746: [Bug]: RuntimeError: Error in model execution (GGUF; MOE; Q8_0; Salesforce/xLAM-8x22b-r)

| 字段 | 值 |
| --- | --- |
| Issue | [#10746](https://github.com/vllm-project/vllm/issues/10746) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Error in model execution (GGUF; MOE; Q8_0; Salesforce/xLAM-8x22b-r)

### Issue 正文摘录

### Your current environment ### Model Input Dumps [dump.zip](https://github.com/user-attachments/files/17947794/dump.zip) ### 🐛 Describe the bug When I try load gguf MOE model, I have an error ```python import os os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1, 2, 3' from vllm import SamplingParams, LLM llm = LLM( model="./models/xlam-8x22b-Q8_0.gguf", tokenizer="./hf_cache/models--Salesforce--xLAM-8x22b-r/snapshots/3b98fc677d97dc491f2a5243acb7b9ca4b9da2e1", quantization="gguf" ) ``` ### Traceback ```sh INFO 11-28 09:21:41 config.py:1861] Downcasting torch.float32 to torch.float16. INFO 11-28 09:21:45 config.py:350] This model supports multiple tasks: {'embedding', 'generate'}. Defaulting to 'generate'. WARNING 11-28 09:21:45 config.py:428] gguf quantization is not fully optimized yet. The speed can be slower than non-quantized models. WARNING 11-28 09:21:45 arg_utils.py:1013] Chunked prefill is enabled by default for models with max_model_len > 32K. Currently, chunked prefill might not work with some features or models. If you encounter any issues, please disable chunked prefill by setting --enable-chunked-prefill=False. INFO 11-28 09:21:45 config.py:1136] Chunked prefill is enabled...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ribe the bug When I try load gguf MOE model, I have an error ```python import os os.environ['CUDA_VISIBLE_DEVICES'] = '0, 1, 2, 3' from vllm import SamplingParams, LLM llm = LLM( model="./models/xlam-8x22b-Q8_0.gguf", t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e--xLAM-8x22b-r/snapshots/3b98fc677d97dc491f2a5243acb7b9ca4b9da2e1", quantization="gguf" ) ``` ### Traceback ```sh INFO 11-28 09:21:41 config.py:1861] Downcasting torch.float32 to torch.float16. INFO 11-28 09:21:45 conf...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: RuntimeError: Error in model execution (GGUF; MOE; Q8_0; Salesforce/xLAM-8x22b-r) bug ### Your current environment ### Model Input Dumps [dump.zip](https://github.com/user-attachments/files/17947794/dump.zip) ###...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: non-quantized models. WARNING 11-28 09:21:45 arg_utils.py:1013] Chunked prefill is enabled by default for models with max_model_len > 32K. Currently, chunked prefill might not work with some features or models. If you e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
