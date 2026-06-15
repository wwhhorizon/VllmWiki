# vllm-project/vllm#37917: [Bug]: Qwen3.5 27b WorkerProc hit an exception ; CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#37917](https://github.com/vllm-project/vllm/issues/37917) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 27b WorkerProc hit an exception ; CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This is a vLLM crash : The observed error is in the join file: [qwen35-27berror.log](https://github.com/user-attachments/files/26192854/qwen35-27berror.log) The error doesn't occur immediately but under load. We start 16 simulated conversations with the model. About 15 minutes after the start, the error occurs, and vLLM crashes. Crash occur when conversations are around 50K to 100K tokens. Here is the running command : ``` exec vllm serve Qwen/Qwen3.5-27B-GPTQ-Int4 \ --host 127.0.0.1 \ --max-model-len 1000000 \ --tensor-parallel-size 2\ --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":3}' \ --max-num-seqs 256 \ --gpu-memory-utilization 0.93 \ --reasoning-parser qwen3 \ --disable-log-stats \ --tool-call-parser qwen3_coder \ --enable-auto-tool-choice \ --download-dir "/mnt/models" ``` Find here all scripts and data used to run query vllm until it crash. [crash_vllm_qwen3.tar.gz](https://github.com/user-attachments/files/26193740/crash_vllm_qwen3.tar.gz) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;opera...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Here is the running command : ``` exec vllm serve Qwen/Qwen3.5-27B-GPTQ-Int4 \ --host 127.0.0.1 \ --max-model-len 1000000 \ --tensor-parallel-size 2\ --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tok...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5 27b WorkerProc hit an exception ; CUDA error: an illegal memory access was encountered bug ### Your current environment ### 🐛 Describe the bug This is a vLLM crash : The observed error is in the join file:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Qwen3.5 27b WorkerProc hit an exception ; CUDA error: an illegal memory access was encountered bug ### Your current environment ### 🐛 Describe the bug This is a vLLM crash : The observed error is in the join file...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
