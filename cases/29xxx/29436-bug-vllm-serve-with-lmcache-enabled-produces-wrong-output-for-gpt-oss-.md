# vllm-project/vllm#29436: [Bug]: vLLM Serve with LMCache enabled produces wrong output for GPT-OSS-20B

| 字段 | 值 |
| --- | --- |
| Issue | [#29436](https://github.com/vllm-project/vllm/issues/29436) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM Serve with LMCache enabled produces wrong output for GPT-OSS-20B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM serve command with LMCache enabled produces wrong output with GPT OSS 20B for subsequent invocations with the same prompt Steps to reproduce: Command to start the server: ``` LMCACHE_CONFIG_FILE=lmcache_cpu.yaml vllm serve openai/gpt-oss-20b --port 8000 --kv-transfer-config '{"kv_connector":"LMCacheConnectorV1", "kv_role":"kv_both"}' ``` Invocation: ``` curl 127.0.0.1:8000/v1/chat/completions -H "Content-Type: application/json" -d '{"model": "openai/gpt-oss-20b", "messages": [ {"role": "user", "content": "What is Amazon SageMaker?"}]}' ``` First invocation: ``` { "id":"chatcmpl-951ca7178b1e4226b0343cb070033487", "object":"chat.completion", "created":1764098087, "model":"openai/gpt-oss-20b", "choices":[ {"index":0,"message":{"role":"assistant","content":"**Amazon SageMaker** is Amazon Web Services’ fully‑managed platform that lets you build, train, tune, and deploy machine‑learning models fast—without managing the underlying infrastructure.\n\nKey capabilities\n\n| Feature | What it does |\n|--------|--------------|\n| **SageMaker Studio** | A web‑based IDE that bundles notebooks, visual debugging, model monitoring, and colla...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vLLM Serve with LMCache enabled produces wrong output for GPT-OSS-20B bug;stale ### Your current environment ### 🐛 Describe the bug vLLM serve command with LMCache enabled produces wrong output with GPT OSS 20B f...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: th GPT OSS 20B for subsequent invocations with the same prompt Steps to reproduce: Command to start the server: ``` LMCACHE_CONFIG_FILE=lmcache_cpu.yaml vllm serve openai/gpt-oss-20b --port 8000 --kv-transfer-config '{"...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: SageMaker** is Amazon Web Services’ fully‑managed platform that lets you build, train, tune, and deploy machine‑learning models fast—without managing the underlying infrastructure.\n\nKey capabilities\n\n| Feature | Wha...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: \n| **Managed training** | Spot, distributed, and GPU training jobs that scale to the required compute. |\n| **Model deployment** | One‑click production endpoints, batch transform, edge inference (SageMaker Edge), and r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Auto‑ML & automated model tuning** | SageMaker Autopilot automatically searches model architectures and hyper‑parameters. |\n| **Managed training** | Spot, distributed, and GPU training jobs that scale to the required c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
