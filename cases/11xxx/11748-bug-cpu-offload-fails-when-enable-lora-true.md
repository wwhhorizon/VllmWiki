# vllm-project/vllm#11748: [Bug]: CPU Offload fails when `enable_lora=True`

| 字段 | 值 |
| --- | --- |
| Issue | [#11748](https://github.com/vllm-project/vllm/issues/11748) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPU Offload fails when `enable_lora=True`

### Issue 正文摘录

### Your current environment ### Model Input Dumps [err_execute_model_input_20250105-235132.zip](https://github.com/user-attachments/files/18310630/err_execute_model_input_20250105-235132.zip) ### 🐛 Describe the bug When I ran the following code, the `cpu_offload_gb=8` worked correctly. ```python import vllm llm = vllm.LLM( "princeton-nlp/gemma-2-9b-it-SimPO", tensor_parallel_size=1, # ref: https://docs.vllm.ai/en/latest/quantization/bnb.html#inflight-quantization-load-as-4bit-quantization # quantization="bitsandbytes", # load_format="bitsandbytes", # enable_lora=True, # ref: https://github.com/vllm-project/vllm/issues/2847#issuecomment-2009845554 # max_lora_rank=64, dtype="bfloat16", enforce_eager=True, max_model_len=3201, enable_prefix_caching=True, gpu_memory_utilization=0.9, cpu_offload_gb=8, swap_space=0, ) ``` ![vllm_without_cpu_offload](https://github.com/user-attachments/assets/6894aec7-368a-49f5-b3f0-4c74ed95e1ea) However, when I set `enable_lora` to True, the following error happened. I tried downgrading the version of vllm, but it didn't work. ``` --------------------------------------------------------------------------- ValueError Traceback (most recent call last) Fil...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: n the following code, the `cpu_offload_gb=8` worked correctly. ```python import vllm llm = vllm.LLM( "princeton-nlp/gemma-2-9b-it-SimPO", tensor_parallel_size=1, # ref: https://docs.vllm.ai/en/latest/quantization/bnb.ht...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: ", tensor_parallel_size=1, # ref: https://docs.vllm.ai/en/latest/quantization/bnb.html#inflight-quantization-load-as-4bit-quantization # quantization="bitsandbytes", # load_format="bitsandbytes", # enable_lora=True, # r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: d fails when `enable_lora=True` bug ### Your current environment ### Model Input Dumps [err_execute_model_input_20250105-235132.zip](https://github.com/user-attachments/files/18310630/err_execute_model_input_20250105-23...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: ensors, num_steps) 1689 with set_forward_context(model_input.attn_metadata, 1690 self.vllm_config): -> 1691 hidden_or_intermediate_states = model_executable( 1692 input_ids=model_input.input_tokens, 1693 positions=mo
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: hon3.11/site-packages/vllm/model_executor/models/gemma2.py:233, in Gemma2DecoderLayer.forward(self, positions, hidden_states, kv_cache, attn_metadata, residual) 231 hidden_states, residual = self.input_layernorm( 232 hi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
