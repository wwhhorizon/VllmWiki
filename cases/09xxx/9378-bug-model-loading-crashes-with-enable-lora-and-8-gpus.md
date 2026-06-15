# vllm-project/vllm#9378: [Bug]: Model loading crashes with enable_lora and 8 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#9378](https://github.com/vllm-project/vllm/issues/9378) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model loading crashes with enable_lora and 8 GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While loading the model with LLM using 8 GPUs on a single node with enable_lora=true, vllm crashes without any error messages (even with all trace options enabled). Error: ``` (VllmWorkerProcess pid=397111) INFO 10-15 15:30:32 model_runner.py:1329] Capturing the model for CUDA graphs. This may lead to unexpected consequences if the model is not static. To run the model in eager mode, set 'enforce_eager=True' or use '--enforce-eager' in the CLI. (VllmWorkerProcess pid=397111) INFO 10-15 15:30:32 model_runner.py:1333] CUDA graphs can take additional 1~3 GiB memory per GPU. If you are running out of memory, consider decreasing `gpu_memory_utilization` or enforcing eager mode. You can also reduce the `max_num_seqs` as needed to decrease memory usage. (VllmWorkerProcess pid=397117) INFO 10-15 15:31:13 model_runner.py:1456] Graph capturing finished in 42 secs. (VllmWorkerProcess pid=397110) INFO 10-15 15:31:13 model_runner.py:1456] Graph capturing finished in 42 secs. (VllmWorkerProcess pid=397113) INFO 10-15 15:31:13 model_runner.py:1456] Graph capturing finished in 41 secs. (VllmWorkerProcess pid=397108) INFO 10-15 15:31:13 model_run...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ning out of memory, consider decreasing `gpu_memory_utilization` or enforcing eager mode. You can also reduce the `max_num_seqs` as needed to decrease memory usage. (VllmWorkerProcess pid=397117) INFO 10-15 15:31:13 mod...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: enable_lora=True, max_lora_rank=128, dtype=torch.float16, max_model_len=1024, gpu_memory_utilization=0.75, tensor_parallel_size=8) ```` What is strange is that it works if I use 4 GPUs (tensor_parallel_size=4). An eas
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Model loading crashes with enable_lora and 8 GPUs bug ### Your current environment ### 🐛 Describe the bug While loading the model with LLM using 8 GPUs on a single node with enable_lora=true, vllm crashes without...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ogits;speculative_decoding attention;cuda;operator;quantization;sampling;triton build_error;crash;nan_inf;oom dtype;env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ngs.warn('resource_tracker: There appear to be %d ' Killed ```` Code to reproduce: ````python from vllm import LLM, SamplingParams llm = LLM(model="meta-llama/Meta-Llama-3.1-8B-Instruct", enable_lora=True, max_lora_rank...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
