# vllm-project/vllm#11329: [Bug]: FP8 kvcache causes RuntimeError in v1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#11329](https://github.com/vllm-project/vllm/issues/11329) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FP8 kvcache causes RuntimeError in v1 engine

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I encountered an issue when using the v1 engine of vLLM with FP8 kvCache, It seems that the issue might be related to the flash attention kernel? **Steps to reproduce** ```bash VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server \ --model meta-llama/Llama-3.1-8B-Instruct --dtype auto \ --served-model-name llama3-8b --kv-cache-dtype fp8 --port 9314 \ --max-num-seqs 128 --gpu-memory-utilization 0.9 --max_num_batched_tokens 5048 --max-model-len 5048 ``` **Full traceback** ``` ERROR 12-19 09:04:11 core.py:270] query and key must have the same dtype ERROR 12-19 09:04:11 core.py:270] Traceback (most recent call last): ERROR 12-19 09:04:11 core.py:270] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 264, in run_engine_core ERROR 12-19 09:04:11 core.py:270] engine_core.run_busy_loop() ERROR 12-19 09:04:11 core.py:270] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 302, in run_busy_loop ERROR 12-19 09:04:11 core.py:270] outputs = self.step() ERROR 12-19 09:04:11 core.py:270] File "/usr/local/lib/python3.10/dist-packag...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: f vLLM with FP8 kvCache, It seems that the issue might be related to the flash attention kernel? **Steps to reproduce** ```bash VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server \ --model...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization attention;cuda;fp8;kernel;operator;triton build_error;crash...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: FP8 kvcache causes RuntimeError in v1 engine bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I encountered an issue when using the v1 engine of vLLM with FP8 kvCache, It
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: he flash attention kernel? **Steps to reproduce** ```bash VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server \ --model meta-llama/Llama-3.1-8B-Instruct --dtype auto \ --served-model-name l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: auses RuntimeError in v1 engine bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I encountered an issue when using the v1 engine of vLLM with FP8 kvCache, It seems that the iss...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
