# vllm-project/vllm#8853: [Bug]: 0.6.2 OpenAI server outofmem for a previously stable setup

| 字段 | 值 |
| --- | --- |
| Issue | [#8853](https://github.com/vllm-project/vllm/issues/8853) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.6.2 OpenAI server outofmem for a previously stable setup

### Issue 正文摘录

### Your current environment ### Model Input Dumps [err_execute_model_input_20240926-130209.zip](https://github.com/user-attachments/files/17149205/err_execute_model_input_20240926-130209.zip) [err_execute_model_input_20240926-133238.zip](https://github.com/user-attachments/files/17149359/err_execute_model_input_20240926-133238.zip) ### 🐛 Describe the bug Running (on RunPod L40S PyTorch image 2.1.1 CUDA 12.1) `vllm serve "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4" --port 8093 --gpu-memory-utilization 0.97 --max-model-len 8192 --dtype "auto" --trust-remote-code` used to work in a stable way for my pipeline of batched request completions up to the previous VLLM version. Now, under heavy load (batch 100 with 500-1k tokens per prompt) the server crashes with CUDA outofmem error. Setting `--max-num-seqs 64` seems to stabilize things but it was not necessary before. Not sure if this is due to the new engine? Would be happy to know what's going on. Thanks! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can an...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: y for my pipeline of batched request completions up to the previous VLLM version. Now, under heavy load (batch 100 with 500-1k tokens per prompt) the server crashes with CUDA outofmem error. Setting `--max-num-seqs 64`...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ning (on RunPod L40S PyTorch image 2.1.1 CUDA 12.1) `vllm serve "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4" --port 8093 --gpu-memory-utilization 0.97 --max-model-len 8192 --dtype "auto" --trust-remote-code` us...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: 0.6.2 OpenAI server outofmem for a previously stable setup bug;stale ### Your current environment ### Model Input Dumps [err_execute_model_input_20240926-130209.zip](https://github.com/user-attachments/files/1714...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ip) ### 🐛 Describe the bug Running (on RunPod L40S PyTorch image 2.1.1 CUDA 12.1) `vllm serve "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4" --port 8093 --gpu-memory-utilization 0.97 --max-model-len 8192 --dtype...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: a previously stable setup bug;stale ### Your current environment ### Model Input Dumps [err_execute_model_input_20240926-130209.zip](https://github.com/user-attachments/files/17149205/err_execute_model_input_20240926-13...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
