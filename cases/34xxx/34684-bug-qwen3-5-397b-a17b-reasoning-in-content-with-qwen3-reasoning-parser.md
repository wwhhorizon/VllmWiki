# vllm-project/vllm#34684: [Bug]: Qwen3.5-397B-A17B - reasoning in content with qwen3 reasoning parser

| 字段 | 值 |
| --- | --- |
| Issue | [#34684](https://github.com/vllm-project/vllm/issues/34684) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-397B-A17B - reasoning in content with qwen3 reasoning parser

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The reasoning of the model leaks into the model response `content` when using reasoning_parser `qwen3`. Start vLLM with: ``` CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve \ /mnt/models/Qwen_Qwen3.5-397B-A17B\ --served-model-name Qwen3.5-397B-A17B \ --tensor-parallel-size 8 \ --mm-encoder-tp-mode data \ --mm-processor-cache-type shm \ --host 0.0.0.0 \ --port 8019 \ --api-key test \ --gpu-memory-utilization 0.95 \ --reasoning-parser qwen3 ``` The following request: ``` curl http://localhost:8019/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer test" -d '{ "model": "Qwen3.5-397B-A17B", "messages": [ { "role": "user", "content": "Hello! How are you?" } ] }' ``` Results in the whole reasoning chain and the ` ` token being part of the `content` field: ``` {"id":"chatcmpl-b66a2df8c0719552","object":"chat.completion","created":1771321720,"model":"Qwen3.5-397B-A17B","choices":[{"index":0,"message":{"role":"assistant","content":"Thinking Process:\n\n1. **Analyze the Request:**\n * Input: \"Hello! How are you?\"\n * Intent: Greeting and checking on the AI's status/well-being.\n * Tone: Friendly, casual, po...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: I can express readiness).\n * Offer assistance.\n * Keep it concise and friendly.\n\n3. **Drafting options:**\n * *Option 1:* Hello! I'm good. How about you?\n * *Option 2:* Hi there! I'm doing well, thank you. How can...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: -memory-utilization 0.95 \ --reasoning-parser qwen3 ``` The following request: ``` curl http://localhost:8019/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer test" -d '{ "model": "Qwen3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: se `content` when using reasoning_parser `qwen3`. Start vLLM with: ``` CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 vllm serve \ /mnt/models/Qwen_Qwen3.5-397B-A17B\ --served-model-name Qwen3.5-397B-A17B \ --tensor-parallel-size...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3.5-397B-A17B - reasoning in content with qwen3 reasoning parser bug ### Your current environment ### 🐛 Describe the bug The reasoning of the model leaks into the model response `content` when using reasoning...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
