# vllm-project/vllm#41257: [Bug]: vLLM + FlexAttention crashes with torch._dynamo.exc.InternalTorchDynamoError: AcceleratorError: CUDA error: misaligned address

| 字段 | 值 |
| --- | --- |
| Issue | [#41257](https://github.com/vllm-project/vllm/issues/41257) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM + FlexAttention crashes with torch._dynamo.exc.InternalTorchDynamoError: AcceleratorError: CUDA error: misaligned address

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Reproducer Using vllm `v0.20.0`, the following python code results in a `torch._dynamo.exc.InternalTorchDynamoError: AcceleratorError: CUDA error: misaligned address` error. ```python import vllm from vllm.config import AttentionConfig from vllm.v1.attention.backends.registry import AttentionBackendEnum llm = vllm.LLM( "inferno-project/vllm-mixtral-2", max_num_seqs=2, attention_config=AttentionConfig( backend=AttentionBackendEnum.FLEX_ATTENTION ) ) llm.generate("token_175") ``` # Full traceback [traceback.txt](https://github.com/user-attachments/files/27207619/traceback.txt) Here are all the logged errors: ``` (EngineCore pid=22349) ERROR 04-29 16:04:08 [logging_utils/dump_input.py:72] Dumping input data for V1 LLM engine (v0.20.0) with config: model='inferno-project/vllm-mixtral-2', speculative_config=None, tokenizer='inferno-project/vllm-mixtral-2', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, decode_context_pa...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ror: AcceleratorError: CUDA error: misaligned address` error. ```python import vllm from vllm.config import AttentionConfig from vllm.v1.attention.backends.registry import AttentionBackendEnum llm = vllm.LLM( "inferno-p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: LM engine (v0.20.0) with config: model='inferno-project/vllm-mixtral-2', speculative_config=None, tokenizer='inferno-project/vllm-mixtral-2', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: port vllm from vllm.config import AttentionConfig from vllm.v1.attention.backends.registry import AttentionBackendEnum llm = vllm.LLM( "inferno-project/vllm-mixtral-2", max_num_seqs=2, attention_config=AttentionConfig(...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: lignment_asserts': True, 'scalar_asserts': True, 'combo_kernels': True, 'benchmark_combo_kernel': True}, 'inductor_passes': {}, 'cudagraph_mode': , 'cudagraph_num_of_warmups': 1, 'cudagraph_capture_sizes': [1, 2, 4], 'c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
