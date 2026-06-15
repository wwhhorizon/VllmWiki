# vllm-project/vllm#12769: [Bug]:  crash when receive a request

| 字段 | 值 |
| --- | --- |
| Issue | [#12769](https://github.com/vllm-project/vllm/issues/12769) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  crash when receive a request

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve /root/.cache/huggingface/DeepSeek-R1/ \ --host 0.0.0.0 --port 6006 --tensor-parallel-size 8 --pipeline-parallel-size 5 --max_model_len 8192 \ --trust-remote-code --quantization="fp8" --enforce-eager then request api v1/chat/completions, the engine will crash void cutlass::arch::Mma , 32, cutlass::float_e4m3_t, cutlass::layout::RowMajor, cutlass::float_e4m3_t, cutlass::layout::ColumnMajor, float, cutlass::layout::RowMajor, Operator_>::operator()(cutlass::Array &, const cutlass::Array &, const cutlass::Array &, const cutlass::Array &) const [with Operator_ = cutlass::arch::OpMultiplyAddFastAccum] not implemented INFO 02-04 23:28:20 model_runner_base.py:120] Writing input of failed execution to /tmp/err_execute_model_input_20250204-232820.pkl... WARNING 02-04 23:28:20 model_runner_base.py:143] Failed to pickle inputs of failed execution: CUDA error: unspecified launch failure WARNING 02-04 23:28:20 model_runner_base.py:143] CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. WARNING 02-04 23:28:20 model_runner_base.py:143] For debugging consider passing C...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: se.py:143] Failed to pickle inputs of failed execution: CUDA error: unspecified launch failure WARNING 02-04 23:28:20 model_runner_base.py:143] CUDA kernel errors might be asynchronously reported at some other API call,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: -eager then request api v1/chat/completions, the engine will crash void cutlass::arch::Mma , 32, cutlass::float_e4m3_t, cutlass::layout::RowMajor, cutlass::float_e4m3_t, cutlass::layout::ColumnMajor, float, cutlass::lay...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --pipeline-parallel-size 5 --max_model_len 8192 \ --trust-remote-code --quantization="fp8" --enforce-eager then request api v1/chat/completions, the engine will crash void cutlass::arch::Mma , 32, cutlass::float_e4m3_t,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: hen request api v1/chat/completions, the engine will crash void cutlass::arch::Mma , 32, cutlass::float_e4m3_t, cutlass::layout::RowMajor, cutlass::float_e4m3_t, cutlass::layout::ColumnMajor, float, cutlass::layout::Row...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: will crash void cutlass::arch::Mma , 32, cutlass::float_e4m3_t, cutlass::layout::RowMajor, cutlass::float_e4m3_t, cutlass::layout::ColumnMajor, float, cutlass::layout::RowMajor, Operator_>::operator()(cutlass::Array &,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
