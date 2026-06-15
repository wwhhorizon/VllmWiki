# vllm-project/vllm#17894: [Bug]: Engine crash when using large integer "maximum" in JSON schema (guided decoding)

| 字段 | 值 |
| --- | --- |
| Issue | [#17894](https://github.com/vllm-project/vllm/issues/17894) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine crash when using large integer "maximum" in JSON schema (guided decoding)

### Issue 正文摘录

### Your current environment **Environment:** • vLLM Version: v0.8.5 (Docker image vllm/vllm-openai:v0.8.5) • Model: Qwen3-32B • GPU: A100 40G x2 • Tensor parallelism: 2 • Host OS: Docker (Ubuntu 22.04 base) • Python Client: openai==1.13.3 • Trigger: large le= value in conint() → JSON Schema → grammar → C++ compile error ### 🐛 Describe the bug 🐛 Bug Report Describe the issue Using vllm/vllm-openai:v0.8.5 to serve Qwen3-32B with structured JSON output (guided decoding via response_format={"type": "json_schema", ...}), the model server crashes when the Pydantic schema allows a large upper bound for an integer field (population: conint(ge=0, le=20_000_000_000)). This causes a fatal error during the JSON Schema → Grammar compilation step. The service shuts down with RuntimeError: maximum must be an integer. --- **To Reproduce** 1. Docker Compose service config (partial): ``` image: vllm/vllm-openai:v0.8.5 command: --model /data/share/models/Qwen3-32B --host 0.0.0.0 --port 30000 --tensor-parallel-size 2 --trust-remote-code --served-model-name Qwen3-32B --gpu-memory-utilization 0.93 --max-model-len 25000 --enable-reasoning --reasoning-parser deepseek_r1 ``` 2. Python code to trigger cra...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ecoding) bug ### Your current environment **Environment:** • vLLM Version: v0.8.5 (Docker image vllm/vllm-openai:v0.8.5) • Model: Qwen3-32B • GPU: A100 40G x2 • Tensor parallelism: 2 • Host OS: Docker (Ubuntu 22.04 base...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ker image vllm/vllm-openai:v0.8.5) • Model: Qwen3-32B • GPU: A100 40G x2 • Tensor parallelism: 2 • Host OS: Docker (Ubuntu 22.04 base) • Python Client: openai==1.13.3 • Trigger: large le= value in conint() → JSON Schema...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: • vLLM Version: v0.8.5 (Docker image vllm/vllm-openai:v0.8.5) • Model: Qwen3-32B • GPU: A100 40G x2 • Tensor parallelism: 2 • Host OS: Docker (Ubuntu 22.04 base) • Python Client: openai==1.13.3 • Trigger: large le= valu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: json_schema( ``` Then the engine crashes with: ``` torch.distributed.DistBackendError: NCCL error ... Cuda failure 'out of memory' ``` --- **Environment:** • vLLM Version: v0.8.5 (Docker image vllm/vllm-openai:v0.8.5) •...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ice shuts down with RuntimeError: maximum must be an integer. --- **To Reproduce** 1. Docker Compose service config (partial): ``` image: vllm/vllm-openai:v0.8.5 command: --model /data/share/models/Qwen3-32B --host 0.0....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
