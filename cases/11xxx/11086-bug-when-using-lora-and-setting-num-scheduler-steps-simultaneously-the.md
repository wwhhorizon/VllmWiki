# vllm-project/vllm#11086: [Bug]: When using lora and setting num-scheduler-steps simultaneously, the output does not meet expectations.

| 字段 | 值 |
| --- | --- |
| Issue | [#11086](https://github.com/vllm-project/vllm/issues/11086) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When using lora and setting num-scheduler-steps simultaneously, the output does not meet expectations.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug VLLM version： 0.6.4.post1 I have trained a LoRA model based on Qwen2.5-7B-Instruct, and I have started the vllm service using pm2 with the following configuration: ```yaml apps: - name: "vllm" script: "/home/lucas/envs/nlp-vllm/bin/python" args: - "-m" - "vllm.entrypoints.openai.api_server" - "--port=18101" # 端口设置 # # Meta-Llama-3.1-8B-Instruct # - "--served-model-name=Meta-Llama-3.1-8B-Instruct" # - "--model=/data/llms/Meta-Llama-3.1-8B-Instruct" # - "--tokenizer=/data/llms/Meta-Llama-3.1-8B-Instruct" # qwen - "--served-model-name=Qwen2.5-7B-Instruct" - "--model=/data/llms/Qwen2.5-7B-Instruct" - "--tokenizer=/data/llms/Qwen2.5-7B-Instruct" # - "--max-model-len=8192" # 最大模型长度 - "--max-model-len=4096" - "--gpu-memory-utilization=0.9" # GPU内存利用率 # speedup # - "--enable-chunked-prefill" # NOTE: LoRA is not supported with chunked prefill yet - "--enable-prefix-caching" # - "--num-scheduler-steps=8" # NOTE: LoRA, will always use base model(BUG) - "--enable-lora" - "--max-lora-rank=64" - "--lora-modules" # - '{"name": "nl2filter", "path": "/home/lucas/workspace/github_project/LLaMA-Factory/saves/Meta...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: put does not meet expectations. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug VLLM version： 0.6.4.post1 I have trained a LoRA model based on Qwen2.5-7B-Instruct, and I have...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lter-all", "base_model_name": "Qwen2.5-7B-Instruct"}' env: CUDA_VISIBLE_DEVICES: "0" log_date_format: "YYYY-MM-DD HH:mm:ss" error_file: "/home/lucas/workspace/pm2_logs/error.log" out_file: "/home/lucas/workspace/pm2_log...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: When using lora and setting num-scheduler-steps simultaneously, the output does not meet expectations. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug VLLM version： 0.6...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t ### Model Input Dumps _No response_ ### 🐛 Describe the bug VLLM version： 0.6.4.post1 I have trained a LoRA model based on Qwen2.5-7B-Instruct, and I have started the vllm service using pm2 with the following configura...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
