# vllm-project/vllm#16068: [Bug]: v0.8.1 V1 with pipeline-parallel-size 4, weird responses

| 字段 | 值 |
| --- | --- |
| Issue | [#16068](https://github.com/vllm-project/vllm/issues/16068) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.8.1 V1 with pipeline-parallel-size 4, weird responses

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug First start a ray cluster with 4 nodes With v0.8.1 V0 pp=4 ```bash export VLLM_USE_V1=0 && vllm serve Qwen/Qwen1.5-MoE-A2.7B --pipeline-parallel-size 4 --distributed-executor-backend ray & ``` ```bash curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "Qwen/Qwen1.5-MoE-A2.7B", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?"} ] }' ``` Example correct response ``` {"id":"chatcmpl-30158d702c3b48c298f6f1a2bdfa5f15","object":"chat.completion","created":1743782147,"model":"Qwen/Qwen1.5-MoE-A2.7B","choices":[{"index":0,"message":{"role":"assistant","reasoning_content":null,"content":"In April, Natalia sold 48 clips. She sold half as many clips in May, so in May, she sold 48/2 = 24 clips. Altogether in April and May, Natalia sold 48 + 24 = 72 clips.","tool_calls":[]},"logprobs":null,"finish_reason":"stop","stop_reason":null}],"usage":{"prompt_tokens":58,"total_tokens":119,"com...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe cuda;moe build_error env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: read here and there encourage symmetry tell your friend People's capitalism on land\n Your friend's name$ We will go","tool_calls":[]},"logprobs":null,"finish_reason":"stop","stop_reason":null}],"usage":{"prompt_tokens"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 4 nodes With v0.8.1 V0 pp=4 ```bash export VLLM_USE_V1=0 && vllm serve Qwen/Qwen1.5-MoE-A2.7B --pipeline-parallel-size 4 --distributed-executor-backend ray & ``` ```bash curl http://localhost:8000/v1/chat/completions \...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: wen/Qwen1.5-MoE-A2.7B --pipeline-parallel-size 4 --distributed-executor-backend ray & ``` ```bash curl http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "Qwen/Qwen1.5-MoE-A...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: v0.8.1 V0 pp=4 ```bash export VLLM_USE_V1=0 && vllm serve Qwen/Qwen1.5-MoE-A2.7B --pipeline-parallel-size 4 --distributed-executor-backend ray & ``` ```bash curl http://localhost:8000/v1/chat/completions \ -H "Content-T...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
