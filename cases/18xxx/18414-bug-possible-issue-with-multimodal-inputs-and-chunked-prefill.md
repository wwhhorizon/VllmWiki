# vllm-project/vllm#18414: [Bug]: Possible issue with multimodal inputs and chunked prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#18414](https://github.com/vllm-project/vllm/issues/18414) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Possible issue with multimodal inputs and chunked prefill

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm running https://huggingface.co/stelterlab/Mistral-Small-24B-Instruct-2501-AWQ on vLLM v0 (serve) with FP8 KV-cache, enforce-eager and chunked prefill enabled. Occasionally, I'm seeing this error when working with image inputs in chats: ``` May 20 14:20:23 ip-172-26-1-54 vllm[32308]: ERROR 05-20 14:20:23 [engine.py:160] ValueError('Attempted to assign 1705 = 1705 multimodal tokens to 0 placeholders') May 20 14:20:23 ip-172-26-1-54 vllm[32308]: ERROR 05-20 14:20:23 [engine.py:160] Traceback (most recent call last): May 20 14:20:23 ip-172-26-1-54 vllm[32308]: ERROR 05-20 14:20:23 [engine.py:160] File "/home/ubuntu/.local/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 158, in start May 20 14:20:23 ip-172-26-1-54 vllm[32308]: ERROR 05-20 14:20:23 [engine.py:160] self.run_engine_loop() May 20 14:20:23 ip-172-26-1-54 vllm[32308]: ERROR 05-20 14:20:23 [engine.py:160] File "/home/ubuntu/.local/lib/python3.12/site-packages/vllm/engine/multiprocessing/engine.py", line 221, in run_engine_loop May 20 14:20:23 ip-172-26-1-54 vllm[32308]: ERROR 05-20 14:20:23 [engine.py:160] request_outputs = self.engine_step() Ma...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Possible issue with multimodal inputs and chunked prefill bug ### Your current environment ### 🐛 Describe the bug I'm running https://huggingface.co/stelterlab/Mistral-Small-24B-Instruct-2501-AWQ on vLLM v0 (serv...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;qu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: o/stelterlab/Mistral-Small-24B-Instruct-2501-AWQ on vLLM v0 (serve) with FP8 KV-cache, enforce-eager and chunked prefill enabled. Occasionally, I'm seeing this error when working with image inputs in chats: ``` May 20 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Describe the bug I'm running https://huggingface.co/stelterlab/Mistral-Small-24B-Instruct-2501-AWQ on vLLM v0 (serve) with FP8 KV-cache, enforce-eager and chunked prefill enabled. Occasionally, I'm seeing this error whe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Possible issue with multimodal inputs and chunked prefill bug ### Your current environment ### 🐛 Describe the bug I'm running https://huggingface.co/stelterlab/Mistral-Small-24B-Instruct-2501-AWQ on vLLM v0 (serv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
