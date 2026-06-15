# vllm-project/vllm#6173: [Bug]: As V100 does not support FlashAttention, it is not possible to run the gemma model, hopefully it can support the xformers way to run it

| 字段 | 值 |
| --- | --- |
| Issue | [#6173](https://github.com/vllm-project/vllm/issues/6173) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | attention |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: As V100 does not support FlashAttention, it is not possible to run the gemma model, hopefully it can support the xformers way to run it

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug python3 -m vllm.entrypoints.openai.api_server --model /model/models/gemma-2-27b-it/ --dtype float16 --gpu-memory-utilization 0.98 --dtype float16 --port xxxxxx --tensor-parallel-size 8 --served-model-name gemma-2-27b --disable-custom-all-reduce --disable-sliding-window rank0]: Traceback (most recent call last): [rank0]: File " ", line 198, in _run_module_as_main [rank0]: File " ", line 88, in _run_code [rank0]: File "/model/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/entrypoints/openai/api_server.py", line 216, in [rank0]: engine = AsyncLLMEngine.from_engine_args( [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/model/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 431, in from_engine_args [rank0]: engine = cls( [rank0]: ^^^^ [rank0]: File "/model/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/engine/async_llm_engine.py", line 360, in __init__ [rank0]: self.engine = self._init_engine(*args, **kwargs) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/model/anaconda3/envs/vllm/lib/python3.11/site-packages/vl...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: As V100 does not support FlashAttention, it is not possible to run the gemma model, hopefully it can support the xformers way to run it bug;stale ### Your current environment ```text The output of `python collect...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: alize_kv_caches [rank0]: self.model_executor.determine_num_available_blocks()) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/model/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/ex...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: lm.entrypoints.openai.api_server --model /model/models/gemma-2-27b-it/ --dtype float16 --gpu-memory-utilization 0.98 --dtype float16 --port xxxxxx --tensor-parallel-size 8 --served-model-name gemma-2-27b --disable-custo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: out, q, k, v, out_padded, softmax_lse, S_dmask, rng_state = flash_attn_cuda.varlen_fwd( [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: RuntimeError: FlashAttention only supports Ampere GPUs or newer. ERROR 07-06 08:57:19...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: : As V100 does not support FlashAttention, it is not possible to run the gemma model, hopefully it can support the xformers way to run it bug;stale ### Your current environment ```text The output of `python collect_env....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
