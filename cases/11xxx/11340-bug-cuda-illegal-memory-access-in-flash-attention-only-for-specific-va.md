# vllm-project/vllm#11340: [Bug]: CUDA illegal memory access in flash attention only for specific values of --max-num-seqs (with AWQ model )

| 字段 | 值 |
| --- | --- |
| Issue | [#11340](https://github.com/vllm-project/vllm/issues/11340) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA illegal memory access in flash attention only for specific values of --max-num-seqs (with AWQ model )

### Issue 正文摘录

### Your current environment ### Model Input Dumps Failed to dump the input in pickle: ``` bash INFO 12-19 07:19:24 model_runner_base.py:120] Writing input of failed execution to /tmp/err_execute_model_input_20241219-071924.pkl... WARNING 12-19 07:19:24 model_runner_base.py:143] Failed to pickle inputs of failed execution ``` ### 🐛 Describe the bug Using `vllm/vllm-openai:v0.6.3` docker image, with entrypoint `openai.run_batch`, I encounter errors of CUDA illegal memory access that seemed related to flash attention kernels only with some specific values of `--max-num-seqs`. **Some power of 2 for `--max-num-seqs`, such as `256`, cause this failure, but not `255`. I monitored the sequence count running in parallel and it effectively use the max value as inputs are small.** The model used is an AWQ model: `casperhansen/llama-3-70b-instruct-awq`. ## Steps to reproduce ``` python3 -m vllm.entrypoints.openai.run_batch \ -i -o \ --max-model-len 8192 \ --max-num-batched-tokens 8192 \ --max-num-seqs 256 \ --tensor-parallel-size 1 \ --model casperhansen/llama-3-70b-instruct-awq \ --enforce-eager \ --gpu-memory-utilization 0.9 ``` You can try with the provided `test_inputs.jsonl`: [test_inpu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: CUDA illegal memory access in flash attention only for specific values of --max-num-seqs (with AWQ model ) bug ### Your current environment ### Model Input Dumps Failed to dump the input in pickle: ``` bash INFO...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: CUDA illegal memory access in flash attention only for specific values of --max-num-seqs (with AWQ model ) bug ### Your current environment ### Model Input Dumps Failed to dump the input in pickle: ``` bash INFO...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA illegal memory access in flash attention only for specific values of --max-num-seqs (with AWQ model ) bug ### Your current environment ### Model Input Dumps Failed to dump the input in pickle: ``` bash INFO...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: unified_flash_attention ERROR 12-19 07:19:24 async_llm_engine.py:66] decode_output = flash_attn_with_kvcache( ERROR 12-19 07:19:24 async_llm_engine.py:66] ^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 12-19 07:19:24 async_llm_engine.p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nc_llm_engine.py:66] attn_output = self.attn(q, k, v, kv_cache, attn_metadata) ERROR 12-19 07:19:24 async_llm_engine.py:66] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 12-19 07:19:24 async_llm_engine.py:66] File "...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
