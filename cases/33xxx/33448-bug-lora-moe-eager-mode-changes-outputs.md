# vllm-project/vllm#33448: [Bug]: LoRA MoE Eager Mode Changes Outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#33448](https://github.com/vllm-project/vllm/issues/33448) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LoRA MoE Eager Mode Changes Outputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I launch a server with a LoRA MoE adapter in eager mode and non-eager mode, I get different outputs for the prompts. First configuration with CUDA graph capture disable: ```json { "version": "0.2.0", "configurations": [ { "name": "Launch vLLM Server (LoRA MoE)", "type": "debugpy", "request": "launch", "program": "-m", "args": [ "vllm.entrypoints.openai.api_server", "--model", "Qwen/Qwen1.5-MoE-A2.7B", "--enable-lora", "--lora-modules", "squad_adapter=sai-lakkshmii/Qwen1.5-MoE-A2.7B-squad-lora-latest", "--trust-remote-code", "--gpu-memory-utilization", "0.90", "--async-scheduling", "false", "--compilation-config", "{\"cudagraph_mode\": \"NONE\"}" ], "console": "integratedTerminal", "justMyCode": false, "env": { "CUDA_VISIBLE_DEVICES": "2", "TORCH_COMPILE_DISABLE": "1", "TRITON_PTXAS_PATH": "/usr/local/cuda/bin/ptxas" }, "cwd": "${workspaceFolder}", "presentation": { "echo": true, "reveal": "always", "focus": false, "panel": "shared" } } ] } ``` This is the output with the above server configuration: ```bash curl -X POST http://localhost:8000/v1/completions \1/completions \ -H "Content-Type: application/json" \ -d '{ "model":...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: . First configuration with CUDA graph capture disable: ```json { "version": "0.2.0", "configurations": [ { "name": "Launch vLLM Server (LoRA MoE)", "type": "debugpy", "request": "launch", "program": "-m", "args": [
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: LoRA MoE Eager Mode Changes Outputs bug;stale ### Your current environment ### 🐛 Describe the bug When I launch a server with a LoRA MoE adapter in eager mode and non-eager mode, I get different outputs for the p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ode, I get different outputs for the prompts. First configuration with CUDA graph capture disable: ```json { "version": "0.2.0", "configurations": [ { "name": "Launch vLLM Server (LoRA MoE)", "type": "debugpy", "request...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ode and non-eager mode, I get different outputs for the prompts. First configuration with CUDA graph capture disable: ```json { "version": "0.2.0", "configurations": [ { "name": "Launch vLLM Server (LoRA MoE)", "type":...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: LoRA MoE Eager Mode Changes Outputs bug;stale ### Your current environment ### 🐛 Describe the bug When I launch a server with a LoRA MoE adapter in eager mode and non-eager mode, I get different outputs for the p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
