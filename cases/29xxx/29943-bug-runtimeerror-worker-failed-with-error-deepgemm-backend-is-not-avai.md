# vllm-project/vllm#29943: [Bug]: RuntimeError: Worker failed with error 'DeepGEMM backend is not available or outdated.' When deploy DeepSeek-V3.2

| 字段 | 值 |
| --- | --- |
| Issue | [#29943](https://github.com/vllm-project/vllm/issues/29943) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Worker failed with error 'DeepGEMM backend is not available or outdated.' When deploy DeepSeek-V3.2

### Issue 正文摘录

### Your current environment vllm v0.11.2, but add customized DeepSeekV32Tokenizer (like https://github.com/vllm-project/vllm/pull/29837, but with some modifications try to get work on v0.11.2). ### 🐛 Describe the bug I am trying to deploy DeepSeek-V3.2. But without a default chat template, I have to customized a tokenizer based on vllm==v0.11.2，like https://github.com/vllm-project/vllm/pull/29837 did. The porting of DeepSeekV32Tokenizer was completed quickly, and the model and tokenizer loaded successfully using the startup command below: ``` CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 VLLM_USE_V1=1 VLLM_WORKER_MULTIPROC_METHOD=spawn python -m vllm.entrypoints.openai.api_server \ --served-model-name DeepSeek-V3.2 \ --model /nvme0/ai_models/LLM/DeepSeek-V3.2 \ --tokenizer-mode deepseek_v32 \ --gpu-memory-utilization 0.95 \ --tensor-parallel-size 8 \ --host 0.0.0.0 \ --port 37001 \ --dtype auto \ --api-key sk-abc2dd6275a9187c77faccfdc730d352 \ --max-model-len 131072 \ --max-num-batched-tokens 32768 \ --trust-remote-code \ --reasoning-parser deepseek_r1 \ --enable-auto-tool-choice \ --tool-call-parser deepseek_v31 \ --enable-log-requests \ --enable-log-outputs > /nvme2/logs/vllm_log_format...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: lib/python3.12/site-packages/vllm/v1/worker/gpu_worker.py", line 429, in compile_or_warm_up_model (Worker_TP0 pid=3392998) ERROR 12-03 06:51:53 [v1/executor/multiproc_executor.py:815] cuda_graph_memory_bytes = self.mode...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --tensor-parallel-size 8 \ --host 0.0.0.0 \ --port 37001 \ --dtype auto \ --api-key sk-abc2dd6275a9187c77faccfdc730d352 \ --max-model-len 131072 \ --max-num-batched-tokens 32768 \ --trust-remote-code \ --reasoning-parse...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: id. The porting of DeepSeekV32Tokenizer was completed quickly, and the model and tokenizer loaded successfully using the startup command below: ``` CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 VLLM_USE_V1=1 VLLM_WORKER_MULTIPRO...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: uto-tool-choice \ --tool-call-parser deepseek_v31 \ --enable-log-requests \ --enable-log-outputs > /nvme2/logs/vllm_log_format/DeepSeek-V3.2_20251203_37001.log 2>&1 & ``` However, the following error eventually occurred...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: RuntimeError: Worker failed with error 'DeepGEMM backend is not available or outdated.' When deploy DeepSeek-V3.2 bug ### Your current environment vllm v0.11.2, but add customized DeepSeekV32Tokenizer (like https...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
